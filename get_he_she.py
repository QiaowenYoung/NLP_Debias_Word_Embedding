import numpy as np
import string

class Final(object):

    def __init__(self, num):
        self.num = num

    def process(self):
        '''
        USAGE
        get the top num words closest to "he" and "she"

        INPUT
        - num: how many words you want to get

        OUTPUT
        two lists of words, one for "he", another for "she"

        '''
        f = open('glove.6B/glove.6B.50d.txt', 'r')
        vecs = list() # aggregation of lists that store the vectors for each word
        words = list() # aggregation of words
        he_v = list() # vector for "he"
        she_v = list() # vector for "she"
        he_dist = list() # words' distances to "he"
        she_dist = list() # words' distances to "she"
        he_words = list()
        she_words = list()
        result = list()
        i = 0
        punc = string.punctuation

        for line in f.readlines():
            l = line.split(" ")
            if l[0] == "he":
                he_v = list(map(eval, l[1:]))
            if l[0] == "she":
                she_v = list(map(eval, l[1:]))
            if l[0] not in punc:
                words.append(l[0])
                vecs.append(list(map(eval, l[1:])))

        for vec in vecs:
            he_dist.append(self.cosine_dist(he_v, vec))
            she_dist.append(self.cosine_dist(she_v, vec))

        for i, j in enumerate(np.argsort(she_dist)) and i < self.num + 1:
            he_words.append(words[j])
        
        for i, j in enumerate(np.argsort(she_dist)) and i < self.num + 1:
            she_words.append(words[j])

        result.append(he_words)
        result.append(she_words)

        open('result.txt', 'w').write('%s' % '\n'.join(result))

    def cosine_dist(self, l1, l2):
        '''
        USAGE
        calculate the cosine distance of two words' vectors

        INPUT
        - l1: vector for either "he" or "she"
        - l2: vector for the word to be compared

        OUTPUT
        a floating number in [-1, 1] representing the cosine distance of l1 and l2

        '''
        result = np.dot(l1, l2)
        len_l1 = np.dot(l1, l1)
        len_l2 = np.dot(l2, l2)
        result /= len_l1 * len_l2
        return result

final = Final(10)
final.process()