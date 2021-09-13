# Stemmer

Ini adalah kode Python sederhana yang memungkinkan anda untuk mengubah kata berimbuhan dalam Bahasa Indonesia ke bentuk kata dasar ([stem](http://en.wikipedia.org/wiki/Stemming)). Proyek ini adalah perapian kode dan beberapa perbaikan dari proyek [PySastrawi](https://github.com/har07/PySastrawi). Anda dapat mengecek demonstrasi program [di sini](https://stemmer.herokuapp.com/).


## Penggunaan

```python
from sastrawi import Stemmer

stemmer = Stemmer()

sentences = ['Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan',
             'Mereka meniru-nirukannya']

# proses stemming
for sentence in sentences:
    print(stemmer.stem(sentence))
# ekonomi indonesia sedang dalam tumbuh yang bangga
# mereka tiru

# hilangkan stopwords
for sentence in sentences:
    print(stemmer.remove_stopword(sentence))
# perekonomian indonesia pertumbuhan membanggakan
# meniru-nirukannya

# Klasifikasi affiks sebuah kata
res = stemmer.context('meniru-nirukannya'))
# ['tiru', [('me', 'DP'), ('nya', 'PP'), ('kan', 'DS')]]

```

## Lisensi

Lisensi stemmer adalah MIT License (MIT).
Lisensi PySastrawi adalah MIT License (MIT).
Proyek ini mengandung kamus kata dasar yang berasal dari Kateglo dengan lisensi
[CC-BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/).

## Referensi
- [Halaman Repo PySastrawi](https://github.com/har07/PySastrawi)
- [Halaman Repo Sastrawi PHP](https://github.com/sastrawi/sastrawi)
- Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". PhD thesis School of Computer Science and Information Technology RMIT University Australia
