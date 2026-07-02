# l =[12,23,36,42,21]

# for i in range(0,len(l)):
#     for j in range (i+1,len(l)):
#         i[j],l[i]=l[i],i[j]
# print(i)

# l = [12,23,36,42,21]


# left = 0 
# right =len(i)-1

# while(left<right):
#     l[right],l[left]=l[left],l[right]
#     left+1
#     right-=1

# print(l)


# l = [1,2,3,3,2,1]
# left=0
# right =len(l)-1
# ans ="yes"
# while(left<right):
#     if l[left]==l[right]:
#         left1=+     1
#         right-1=1
#         continue
#     else:
#         ans ="no"
#         break
#     print(ans)
    
    
    l = [1,2,3,3,2,1]

left = 0
right = len(l)-1

ans = "yes"

while left < right:
    if l[left] == l[right]:
        left += 1
        right -= 1
    else:
        ans = "no"
        break

print(ans)