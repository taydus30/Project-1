"""
todo:
#upper division requirements
- from_json() and from_txt() functions *
- docstring / doctest functions
- seperate file that shows how to interact with class (with comments) (instructions)
- "final formatting of output / results", so, tabulate some advanced funcs?
#dna class features
- protein start / stops
- more types of comparisons for sequences
#other features
- show changes / mutations of a DNA strand over time
    - turtle /.pygame for drawing a graph where colors represent ATCG
"""
import random
import os
import json

class DNA:

    strand : str = ""

    def __init__(self, string = None):
        if(string is None):
            return
        if(self.validate_sequence(string)):
            self.strand = string.lower()

    def validate_sequence(self, string):
        out = True
        string = string.lower()
        for c in string:
            if c == "a" or c == "t" or c == "c" or c == "g":
                None
            else:
                out = False
                print("Invalid Input! String is not a proper DNA sequence:")
                print(c)
                print("Sequence not set.")
                return(out)
        return(out)

    def from_file(self, filename):
        self.strand = ""
        f = open(filename).read().lower()
        if (self.validate_sequence(f)):
            self.strand = f
        return(self)

    def from_json(self, filename):
        if(os.path.isfile(filename)):
            file = open(filename)
            j = json.load(file)
            f = j['sequence'].lower()
        else:
            print("Invalid JSON file path.")
            return
        if (self.validate_sequence(f)):
            self.strand = f
        return(self)

    def set_sequence(self, seq):
        if(self.validate_sequence(seq)):
            self.strand = seq

    def compliment(self):
        """Returns the complimentary DNA sequence, reversed."""
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
        """Return the equivalent mRNA sequence."""
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

    def mutation(self, iterations = None):
          """Return a string based on the DNA strand with one randomly mutated base."""
          bases = 'ATCG'
          if isinstance(iterations, int):
              mutations = []
              for i in range(iterations):
                  out = list(self.strand)
                  while out == list(self.strand):
                      r = random.choice(bases)
                      index = random.randint(0, len(self.strand)-1)
                      out[index] = r
                  mutations.append(''.join(out))
              return mutations


          out = list(self.strand)
          while out == list(self.strand):
              r = random.choice(bases)
              index = random.randint(0, len(self.strand-1))
              out[index] = r
          return(''.join(out))

    def compare(self, comp):
        """Compare DNA strand with another and returns number of matching bases.

        ---
        comp : Str, DNA
            DNA sequence to compare to.
        """
        if isinstance(comp, str):
            same_chars = 0
            for i in range(min(len(comp), len(self.strand))):
                if comp[i] == self.strand[i]:
                    same_chars += 1
            print("comparing ", comp, ", ", self.strand)
            print(same_chars, " matches \n")
            return(same_chars)
        elif isinstance(comp, DNA):
            #if input is DNA object, recursively call with a string
            self.compare(comp.strand)
        else:
            print("ERROR: Comparison not of another DNA or String")

    def gc_comp(self):
        return(self.base_frequencies("g") + self.base_frequencies("c"))

    def base_frequencies(self, base):
        """Return frequency percentage of a given base.

        ---
        base : Str
            Specifies which base to return frequency of.
        """
        counts = {
            "a": 0,
            "t": 0,
            "c": 0,
            "g": 0
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
