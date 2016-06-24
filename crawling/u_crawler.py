from nltk.tag import pos_tag

sentence = "John Connor is a very bad movie. Marvel Civil War is far better than that. Dr. Who rocks. Hate"
tagged_sent = pos_tag(sentence.split())
names = [word for word,pos in tagged_sent if pos == 'NNP']
all_words = sentence.split(' ')
for i,word in enumerate(all_words):
    try:
        if all_words[i-1] in names and all_words[i] in names:
            print all_words[i-1] + ' ' + all_words[i] +'\n'
    except:
        x = 1
