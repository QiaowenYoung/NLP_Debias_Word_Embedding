# NLP_Debias_Word_Embedding
## corpus
### 英文
wikipedia corpus: https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz <br>
GloVe 的 wiki 预训练: http://nlp.stanford.edu/data/glove.6B.zip
### 中文
职业名称: https://github.com/imhuster/funNLP/blob/master/data/%E8%81%8C%E4%B8%9A%E8%AF%8D%E5%BA%93/professions.txt <br>
预处理词向量: https://github.com/Embedding/Chinese-Word-Vectors <br>
生语料: https://dumps.wikimedia.org/zhwiki/latest/ <br>
已确定用中文来做。<br>
## 实验步骤
1. 使用[预训练词向量](https://github.com/Embedding/Chinese-Word-Vectors)<br>
[原始语料](https://github.com/QiaowenYoung/NLP_Debias_Word_Embedding/blob/master/professions.txt)共有7569个职业，
调用 [getFromPretrained.ipynb] (https://github.com/QiaowenYoung/NLP_Debias_Word_Embedding/blob/master/getFromPretrained.ipynb)得到预处理语料中，和“他”&“她”余弦距离最近的十个职业词汇<br>
2. 使用[生语料](https://dumps.wikimedia.org/zhwiki/latest/)结合 word2vec 训练模型<br>
```
sudo pip3 install gensim
python3 xml2vec.py zhwiki-latest-pages-articles-multistream1.xml-p1p162886.bz2 wiki.zh.txt
brew install opencc
opencc -i wiki.zh.txt -o wiki.zh.txt.jian -c t2s.json
```
之后调用 [wikiprocess.ipynb](https://github.com/QiaowenYoung/NLP_Debias_Word_Embedding/blob/master/wikiprocess.ipynb) 训练出模型并保存
