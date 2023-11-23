hangman={0:'''
        ____________
         |''',
        1:'''
        ____________
         |
         O''',
        2:'''
        ____________
         |
         O
        /''',
        3:'''
        ____________
         |
         O
        / \\''',
        4:'''
        ____________
         |
         O
        / \\
         |''',
        5:'''
        ____________
         |
         O
        / \\
         |
        /''',
        6:'''
        ____________
         |
         O
        / \\
         |
        / \\ '''}


word = "GANDALF"
mistake_count = 6
letter_count = 0
hidden_word = ""
for c in word:
  hidden_word += '-'
print(f"Searching for Word {word}")
print(f"Hidden Word is {hidden_word}")
print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("")


while (mistake_count > 0) and (hidden_word != word):
 index_count = 0
 picked_letter = input("Pick a letter: ").upper()[0];
 if word.count(picked_letter) > 0:
  print(f"CORRECT! The word contains the letter {picked_letter}")
  letter_count += 1
  for l in word:
    if l == picked_letter:
      hidden_word = hidden_word[:index_count] + picked_letter + hidden_word[index_count+1:]
    index_count += 1
  print(hidden_word)
 else:
  mistake_count -= 1
  print(f"WRONG! Number of mistakes left: {mistake_count}")
  print(hangman[6 -mistake_count])
  print("=================================================")

if mistake_count == 0:
    print('HANGED!!!')
else:
    print('CONGRATULATIONS!!!')