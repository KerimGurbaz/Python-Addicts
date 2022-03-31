Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter/chars of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.


word="hippo runs to us!"
from collections import Counter

print(Counter(word))


or 


string = "Hello World !!!"

word_dict={}

for i in string :
  if i in word_dict:
    word_dict[i] +=1

  else:
    word_dict[i]=1
print(word_dict)
