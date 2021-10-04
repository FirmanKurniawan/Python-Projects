# this game get from hackerank
vowels = set('AEIOU')
stuart = kevin = 0
word = input("Input your text : ")
for i, c in enumerate(word):
    if c in vowels:
        kevin += len(word) - i
    else:
        stuart += len(word) - i
if stuart > kevin:
    print('Stuart', stuart)
elif kevin > stuart:
    print('Kevin', kevin)
else:
    print('Draw')