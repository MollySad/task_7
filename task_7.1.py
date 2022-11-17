text = "hello, word of word"
chars_popularity = {}
words_popularity = {}


for word in text.split():
    for chars in word:
        if chars.isalpha() is False:
            word = word.split(chars)[0]
            continue
        if chars in chars_popularity:
            chars_popularity[chars] += 1
        else:     
            chars_popularity[chars] = 1
    if word in words_popularity:
        words_popularity[word] += 1
    else:
        words_popularity[word] = 1

print(chars_popularity)
print(words_popularity)