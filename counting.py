count=dict()
print("Enter Text: ")
line=input('')

words=line.split()

print("Words:", words)

for word in words:
    count[word]=count.get(word, 0)+1
print("\nCount:", count)

'''he was a good and lonely man in the town 
and he got married to a nice woman from 
the same town and also after an year the 
couple had twins a boy and a girl and 
forever lived the family happily everafter'''