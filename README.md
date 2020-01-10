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
[原始语料](https://github.com/QiaowenYoung/NLP_Debias_Word_Embedding/blob/master/professions.txt)共有 7569 个职业，
调用 [getFromPretrained.ipynb](https://github.com/QiaowenYoung/NLP_Debias_Word_Embedding/blob/master/getFromPretrained.ipynb)得到预处理语料中，和“他”&“她”余弦距离最近的十个职业词汇<br>
2. 使用[生语料](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles-multistream.xml.bz2)结合 word2vec 训练模型<br>
```
sudo pip3 install gensim
python3 xml2vec.py zhwiki-latest-pages-articles-multistream.xml.bz2 wiki.zh.txt
brew install opencc
opencc -i wiki.zh.txt -o wiki.zh.txt.jian -c t2s.json
```
之后调用 [wikiprocess.ipynb](https://github.com/QiaowenYoung/NLP_Debias_Word_Embedding/blob/master/wikiprocess.ipynb) 训练出模型并保存
3. 性别子空间<br>
利用 2 中得到的模型取出 10 对具有确定性别指向的词对（如：男->女，他->她，国王->王后），作为定义集。求出每个定义集中词向量的均值，再相加，得到一个矩阵。取其奇异值分解矩阵的前 k 行，得到维度为 k 的子空间<br>
奇异值分解的算法参考: https://www.cnblogs.com/Shinered/p/9206210.html <br>
4. 纠偏处理<br>
对每一个在 word2vec 词向量词典中的词，若其是职业词，则按照取其在子空间上的垂直分量的单位向量作为新的词向量。用此办法完成纠偏<br>
5. 性能评价<br>
