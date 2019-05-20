import random

class DNA:

    def __init__(self, string):
        self.strand = string

    def compliment(self):
        """ Returns the complimentary DNA strand, reversed.
        """
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
        """ Returns the equivalent mRNA strand.
        """
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
        """ Returns a string based on the DNA strand with one randomly mutated base.
        """
        bases = 'ATCG'
        r = random.choice(bases)
        index = random.randint(0, len(self.strand))
        out = list(self.strand)
        while out == list(self.strand):
            out[index] = r
        return(''.join(out))

    def compare(self, comp):
        """ Compares DNA strand with another and returns number of matching bases.
        ---
        Str, DNA comp
            DNA sequence to compare to.
        """
        if isinstance(comp, str):
            same_chars = 0
            for i in range(min(len(comp), len(self.strand))):
                if comp[i] == self.strand[i]:
                    same_chars += 1
            print("comparing ", comp, ", ", self.strand)
            print(same_chars, " matches")
            return(same_chars)
        elif isinstance(comp, DNA):
            self.compare(comp.strand)
        else:
            print("ERROR: Comparison not of another DNA or String")

    def base_frequencies(self, base):
        """ Returns frequency percentage of a given base.
        ---
        Str base
            Specifies which base to return frequency of.
        """
        counts = {
            "a": 0,
            "t": 0,
            "c": 0,
            "g":0
        }

        for i in self.strand:
            if i == 'a' or i == 'A':
                counts["a"] += 1
            if i == 't' or i == 'T':
                counts["t"] += 1
            if i == 'c' or i == 'C':
                counts["c"] += 1
            if i == 'g' or i == 'G':
                counts["g"] += 1
        percents = {}
        percents["a"] = round((counts["a"] / len(self.strand))*100,3)
        percents["t"] = round((counts["t"] / len(self.strand))*100,3)
        percents["c"] = round((counts["c"] / len(self.strand))*100,3)
        percents["g"] = round((counts["g"] / len(self.strand))*100,3)
        return(percents[base])


nnn = DNA("atcg")
print(nnn.compliment())
print(nnn.mrna())
print(nnn.mutation())
nnn.compare("catg")
print(nnn.base_frequencies("a"))
