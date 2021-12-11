#1
a = int(input("Value:  "))

if a < 200:
    print("U are a budget guy")

elif a == 200:
    print("Not less, not more")

else: 
    print("Yeah u rich")

#2
about = input("About you: ")
wordCnt = 1
charatersCnt = 0

for i in about:
    charatersCnt = charatersCnt + 1

    if(i == " "):
        wordCnt = wordCnt + 1

print(charatersCnt)
print(wordCnt)
