name = "Ryequell"

print('before for loop')

for letter in name:
  print(letter)
  if letter == 'e':
    print('an e')
    print('vowel!')
  print('\n')

birthday_month = str(input("Birthday Month..."))
lowercase = birthday_month.lower()
print(lowercase)

Vowel = ("i", "u", "e", "a", "o")
I = str(input("My name is..."))
uI = I.lower
print(uI)
for i in range(len(I)):
  if I[i] in Vowel:
    print(I[i], " : Vowel")
  else:
      print(I[i]," : Consonant")