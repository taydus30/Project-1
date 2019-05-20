

class DNA:

    def __init__(self, string):
        self.strand = string

    def compliment(self):
        out = ""
        for c in strand:
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
        for c in strand:
            if c == 'a':
                out = out + "u"
            elif c == 't':
                out = out + "a"
            elif c == 'g':
                out = out + "c"
            elif c == 'c':
                out = out + "g"
        return(out)
