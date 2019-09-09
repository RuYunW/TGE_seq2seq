from nltk import word_tokenize
from gensim import corpora

def word2int(path):
    with open(path) as f:
        lines = f.readlines()
        document = []
        for line in lines:
            document.append(line.split(' '))
        # 生成字典
        dic = corpora.Dictionary(document)
        # 保存字典到文本文件
        dic.save_as_text('./data/WordDic.txt')
        dic_set = dic.token2id
        # 将单词转换为整数
        values = []
        _ = []
        doc_source = []
        __ = []
        for line in lines:
            for word in line.split(' '):
                _.append(dic_set[word])
                __.append(word)
            values.append(_)
            _ = []
            doc_source.append(__)
            __ = []
    return values,doc_source
    # return doc_source

# doc_source = word2int('./data/describe.txt')
