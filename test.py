sentence = "as ere, erei dfdee. dfeoer, eroemdd."
param = [',', '.']
word = ''
new_sen = []
print(sentence)
for i in sentence:
    word += i
    if i in param:
        new_sen.append(word.strip(i))
        word = ''

print(new_sen)

