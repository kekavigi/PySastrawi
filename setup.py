import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "stemmer",
    version = "0.1.0",
    author = "Agapitus Keyka Vigiliant",
    author_email = "keka.vigi@gmail.com",
    description = ("Package for stemming Indonesian text sentences."),
    license = "MIT",
    keywords = "linguistic stemming indonesian language",
    url = "http://github.com/kekavigi/stemmer",
    packages=['src', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
    ],
 )
