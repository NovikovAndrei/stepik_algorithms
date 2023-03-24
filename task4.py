from collections import Counter

def consensus_string(dna_strings):

    counter = [Counter() for _ in range(len(dna_strings[0]))]
    for dna in dna_strings:
        for i, j in enumerate(dna):
            counter[i][j] += 1
    consensus = ""
    for i in counter:
        most_common = i.most_common()
        most_common.sort(key=lambda x: (-x[1], x[0]))
        consensus += most_common[0][0]
    return consensus

dna_strings = ["ATTA", "ACTA", "AGCA", "ACAA"]
print(consensus_string(dna_strings))

def test_consensus_string():
    dna_strings = ["ATTA", "ACTA", "AGCA", "ACAA"]
    expected = "ACTA"
    assert consensus_string(dna_strings) == expected
    print('ok')

test_consensus_string()