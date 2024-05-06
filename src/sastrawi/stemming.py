"""
This module contains classes for stemming purpose.
"""

import re
import os
from sastrawi.rules import Dictionary, Context, SimplifiedContext
from typing import Optional


class Stemmer:
    """
    Indonesian sentence stemmer.

    Nazief & Adriani, CS Stemmer, ECS Stemmer, Improved ECS.
    @link https://github.com/sastrawi/sastrawi/wiki/Resources
    """

    def __init__(
        self,
        rootwords: Optional[Dictionary] = None,
        stopwords: Optional[Dictionary] = None,
    ):

        current_dir = os.path.dirname(os.path.realpath(__file__))
        err_msg = "{} is missing. It seems that your installation is corrupted"

        if rootwords is None:
            try:
                filepath = "/data/rootwords.txt"
                with open(current_dir + filepath, "r") as file:
                    words = file.read().split("\n")
                    self.rootwords = set(words)
            except FileNotFoundError:
                raise RuntimeError(err_msg.format(filepath)) from None
        else:
            self.rootwords = rootwords

        if stopwords is None:
            try:
                filepath = "/data/stopwords.txt"
                with open(current_dir + filepath, "r") as file:
                    words = file.read().split("\n")
                    self.stopwords = set(words)
            except FileNotFoundError:
                raise RuntimeError(err_msg.format(filepath)) from None
        else:
            self.stopwords = stopwords

        self._cache: dict[str, str] = dict()

    def stem(self, text: str) -> str:
        """
        Stem a text string to its common stem form.
        """

        if type(text) != str:
            raise TypeError("text must be a string!")

        # normalize_text
        result = text.lower()  # lower the text even unicode given
        result = re.sub(r"[^a-z0-9 -]", " ", result, flags=re.IGNORECASE | re.MULTILINE)
        result = re.sub(r"( +)", " ", result, flags=re.IGNORECASE | re.MULTILINE)
        words = result.strip().split(" ")

        stems = list()

        for word in words:
            if word not in self._cache:
                self._cache[word] = self.context(word)[0]
            stems.append(self._cache[word])

        return " ".join(stems)

    def remove_stopword(self, text: str) -> str:
        """
        Remove stop words from a text string.
        """

        if type(text) != str:
            raise TypeError("text must be a string!")

        words = text.lower().split(" ")
        stopped_words = [w for w in words if w not in self.stopwords]

        return " ".join(stopped_words)

    def _is_plural(self, word: str) -> bool:
        """
        Check if a word is in plural form.
        """

        # -ku|-mu|-nya
        # nikmat-Ku, etc
        matches = re.match(r"^(.*)-(ku|mu|nya|lah|kah|tah|pun)$", word)
        if matches:
            return matches.group(1).find("-") != -1
        return word.find("-") != -1

    def context(self, word: str) -> SimplifiedContext:
        """
        Return simplified Context of the word.
        """

        if type(word) != str:
            raise TypeError("word must be a string!")

        if self._is_plural(word):
            return self._plural_context(word)
        return self._singular_context(word)

    def _plural_context(self, word: str) -> SimplifiedContext:

        matches = re.match(r"^(.*)-(.*)$", word)
        words = [matches.group(1), matches.group(2)]

        # resolve:
        # malaikat-malaikat-nya -> malaikat malaikat-nya
        suffix = words[1]
        suffixes = ["ku", "mu", "nya", "lah", "kah", "tah", "pun"]
        matches = re.match(r"^(.*)-(.*)$", words[0])
        if suffix in suffixes and matches:
            words[0] = matches.group(1)
            words[1] = matches.group(2) + suffix

        # resolve:
        # berbalas-balasan -> balas
        word1, removals1 = self._singular_context(words[0])
        word2, removals2 = self._singular_context(words[1])

        # resolve:
        # meniru-nirukan -> tiru
        if not words[1] in self.rootwords and word2 == words[1]:
            word2, removals1 = self._singular_context("me" + words[1])

        # repeated word form?
        if word1 == word2:
            removals = list(set(removals1 + removals2))
            return word1, removals

        # can't be stemmed
        return word, list()

    def _singular_context(self, word: str) -> SimplifiedContext:
        t = Context(word, self.rootwords)
        removals = [(r.removedPart, r.affixType) for r in t.removals]
        return t.result, removals
