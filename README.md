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
这一步的成果并不明显。<br>
2. 使用[生语料](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles-multistream.xml.bz2)结合 word2vec 训练模型<br>
```
sudo pip3 install gensim
python3 xml2vec.py zhwiki-latest-pages-articles-multistream.xml.bz2 wiki.zh.txt
brew install opencc
opencc -i wiki.zh.txt -o wiki.zh.txt.jian -c t2s.json
```
之后调用 [wikiprocess.ipynb](https://github.com/QiaowenYoung/NLP_Debias_Word_Embedding/blob/master/wikiprocess.ipynb) 训练出模型并保存<br>
训练的结果为：
```
他:
知识分子 0.37548497319221497
工人 0.3566417992115021
程序员 0.34266018867492676
飞行员 0.34135007858276367
法官 0.3393450677394867
农民 0.33123716711997986
政府 0.327675461769104
学生 0.3257449269294739
科学家 0.3218073844909668
理发师 0.31932613253593445
她:
经纪人 0.42258161306381226
学生 0.39186251163482666
模特 0.3902280330657959
理发师 0.36837172508239746
妓女 0.36631840467453003
医生 0.35447198152542114
家庭主妇 0.3534913659095764
老师 0.33671343326568604
飞行员 0.3289238214492798
药剂师 0.31823986768722534
```
不仅男性和女性的职业偏向有性别相关性，女性与其偏向职业的关联度也更强。较强地反映了 word2vec 在处理中文时的性别偏向。<br>
3. 性别子空间 <b>ongoing</b><br>
利用 2 中得到的模型取出 10 对具有确定性别指向的词对（如：男->女，他->她，国王->王后），作为定义集。求出每个定义集中词向量的均值，再相加，得到一个矩阵。取其奇异值分解矩阵的前 k 行，得到维度为 k 的子空间<br>
奇异值分解的算法参考: https://www.cnblogs.com/Shinered/p/9206210.html <br>
目前用子空间处理的方法并未显示出纠偏效果，而沿着单个性别方向的纠偏过度，反映为男性和女性的偏向职业全部一致。<br>
4. 纠偏处理 <b>ongoing</b><br>
对每一个在 word2vec 词向量词典中的词，若其是职业词，则按照取其在子空间上的垂直分量的单位向量作为新的词向量。用此办法完成纠偏<br>
5. 性能评价 <b>ongoing</b><br>
