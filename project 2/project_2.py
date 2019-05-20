"""
# TODO: 3' end, 5' end
"""

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

    def compare(self, comp):
        if isinstance(comp, str):
            same_chars = 0
            for i in range(min(len(comp), len(self.strand)):
                if comp[i] == self.strand[i]:
                    same_chars +=
            print("comparing ", comp, ", ", self.strand)
            print(same_chars, " matches")
            return(same_chars)
        elif isinstance(comp, DNA):
            self.compare(comp.strand)
        else:
            print("ERROR: Comparison not of another DNA or String")


nnn = DNA("atcg")
print(nnn.compliment())
print(nnn.mrna())
