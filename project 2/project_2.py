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
        index = random.randint(0, len(self.strand))
        out = list(self.strand)
        while out == list(self.strand):
            out[index] = r
        return(''.join(out))

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

    def base_frequencies(self):
        count_a = 0
        count_t = 0
        count_c = 0
        count_g = 0

        for i in self.strand:
            if i == 'a' or i == 'A':
                count_a += 1
            if i == 't' or i == 'T':
                count_t += 1
            if i == 'c' or i == 'C':
                count_c += 1
            if i == 'g' or i == 'G':
                count_g += 1

        percent_a = round((count_a / len(self.strand))*100,3)
        percent_t = round((count_t / len(self.strand))*100,3)
        percent_c = round((count_c / len(self.strand))*100,3)
        percent_g = round((count_g / len(self.strand))*100,3)
        return(percent_a, percent_t, percent_c, percent_g)


nnn = DNA("atcg")
print(nnn.compliment())
print(nnn.mrna())
print(nnn.mutation())
print(nnn.base_frequencies())
