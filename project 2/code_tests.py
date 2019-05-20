"""
>>> from project_2 import DNA
>>> test_dna = DNA("atcg")
>>> test_dna.mrna()
'uagc'
>>> test_dna.compliment()
'cgat'
>>> test_dna.validate_sequence("atcgh")
Invalid Input! String is not a proper DNA sequence:
h
Sequence not set.
False
>>> test_dna.validate_sequence("atcg")
True
>>> isinstance(test_dna.mutation(), str)
True
>>> test_dna.gc_comp()
50.0
>>> test_dna.base_frequencies('a')
25.0
>>> test_dna.base_frequencies('t')
25.0
>>> test_dna.base_frequencies('c')
25.0
>>> test_dna.base_frequencies('g')
25.0

"""

import doctest
doctest.testmod()
