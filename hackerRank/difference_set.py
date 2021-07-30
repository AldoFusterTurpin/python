# ALDO FUSTER TURPIN
# don't need to convert input to int, can work with strings

import sys

n_suscribed_to_english_paper = input()
suscribed_to_english_paper = input().split()

n_suscribed_to_french_paper = input()
suscribed_to_french_paper = input().split()

suscribed_to_english_paper_set = set(suscribed_to_english_paper)
suscribed_to_french_paper_set= set(suscribed_to_french_paper)

result = set(suscribed_to_english_paper_set.difference(suscribed_to_french_paper_set))
result_length = len(result)

print(result_length)
