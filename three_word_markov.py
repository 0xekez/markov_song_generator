# Class that makes markov chains given some text

import random

class Markov:
    def __init__(self, text, n_inputs = 3):
        self.text = text
        self.chain = dict()
        self.one_chain = dict()
        self.n_inputs = n_inputs

        words = self.text.lower().strip()
        words = words.split()


        index = self.n_inputs
        for word in words[index:]:
            key = words[index-self.n_inputs:index]
            s = ''
            for w in key:
                s += w + ' '
            key = s
            if key in self.chain:
                self.chain[key].append(word)
            else:
                self.chain[key] = [word]
            index += 1

        index = 1
        for word in words[index:]:
            key = words[index-1]
            if key in self.one_chain:
                self.one_chain[key].append(word)
            else:
                self.one_chain[key] = [word]
            index += 1
        #handle final word not being in dict case
        if words[-1] not in self.one_chain:
            self.one_chain[words[-1]] = [words[1]]

    def build_text(self, length=25):
        # randomly w/o weights select word
        startWords = random.choice(list(self.chain.keys()))

        message = startWords

        while len(message.split()) < length:
            if startWords in self.chain:
                nextWord = random.choice(self.chain[startWords])
            else:
                nextWord = random.choice(self.one_chain[message.split()[-1]])

            message += ' ' + nextWord
            startWords = message.split()[-(self.n_inputs):]
            s = ''
            for w in startWords:
                s += ' ' + w
            startWords = s

        return message
