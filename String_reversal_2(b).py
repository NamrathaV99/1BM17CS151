def reverseWords(sent):
    words=sent.split(" ")
    words=words[-1::-1]
    output=' '.join(words)
    return output
sentence=input("Enter the sentence : ")
print(reverseWords(sentence))
print(sentence[::-1])
