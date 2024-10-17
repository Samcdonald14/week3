user_input = input (f"please enter the word that you want the vowels in it counted")
user_input = user_input.lower()
vowel_a,vowel_o,vowel_i,vowel_u,vowel_e = 'a','o','i','u','e'
num_vowel = user_input.count(vowel_a) + user_input.count(vowel_o) + user_input.count(vowel_e) + user_input.count(vowel_i) +user_input.count(vowel_u)
print (f"the number of vowels in the word is {user_input} + {num_vowel}")