import random

class DNA:

    def __init__(self, string):
        self.strand = string

    def compliment(self):
        out = ""
        for c in self.strand:
            if c == 'a':
                out = out + "t"
            elif c == 't':
                out = out + "a"
            elif c == 'g':
                out = out + "c"
            elif c == 'c':
                out = out + "g"
        #return reversed
        return(out[::-1])

    def mrna(self):
        out = ""
        for c in self.strand:
            if c == 'a':
                out = out + "u"
            elif c == 't':
                out = out + "a"
            elif c == 'g':
                out = out + "c"
            elif c == 'c':
                out = out + "g"
        return(out)

    def mutation(self):
        bases = 'ATCG'
        r = random.choice(bases)
        index = random.randint(0, len(self))
        out = list(self)
        while out == list(self):
            out[index] = r
        return(''.join(out))



nnn = DNA("atcg")
print(nnn.compliment())
print(nnn.mrna())
print(nnn.mutation())
