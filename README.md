# NLP_Debias_Word_Embedding
## corpus
### 英文
wikipedia corpus: https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz <br>
GloVe 的 wiki 预训练: http://nlp.stanford.edu/data/glove.6B.zip
### 中文
职业名称: https://github.com/imhuster/funNLP/blob/master/data/%E8%81%8C%E4%B8%9A%E8%AF%8D%E5%BA%93/professions.txt <br>
预处理词向量: https://github.com/Embedding/Chinese-Word-Vectors <br>
已确定用中文来做。<br>
原始语料共有7569个职业。
将语料中的职业名称控制在 10 个字及以下后，剩余 6258 个职业。预处理代码在preprocess.ipynb<br>
如果要训练新的模型，需要一份格式良好的txt语料，放进 word2vec。<br>
如果要直接测试，需要在预处理词向量中提取所有职业名称的词向量，并存储以备计算 cosine distance。<br>
