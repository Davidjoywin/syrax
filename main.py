text = None
with open("text", 'r') as file:
    text = file.read()


tokenize = {}

for id, sentence in enumerate(text.split('.')):
    tokenize[f"sentence_{id}"] = sentence.strip()

print(tokenize)

class SentenceObject:
    def __init__(self, obj):
        for key, value in obj.items():
            self.__dict__[key] = value

sen = SentenceObject(tokenize)
print(sen.sentence_0, sen.sentence_1, sen.sentence_2)
