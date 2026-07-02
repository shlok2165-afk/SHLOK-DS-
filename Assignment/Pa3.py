meaning = input("Enter:")
word  =meaning.lower().split()

count ={}
for m in word :
    count [m] =count.get(m,0) + 1


print(count)


# meaning = input("Enter: ")
# word = meaning.lower().split()

# count = {}
# for m in word:
#     count[m] = count.get(m, 0) + 1

# print(count)