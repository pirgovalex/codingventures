n=int(input())
pos=[]
neg=[]# create empty lists to store variables
for _ in range(n):#iterating n times
    j=int(input())
    (lambda: pos.append(j) if j>0 else neg.append(j))()#sorting each input as larger or smaller than zero with lambda func..
    
print(f"{pos}\n{neg}")
print(f"Count of positives: {len(pos)}\nSum of negatives: {sum(neg)}")
#alternatively...
"""
num_count = int(input())
nums = [int(input()) for _ in range(num_count)] 

#list comprehention to iterate n times

positive_nums = [num for num in nums if num > 0]
negative_nums = [num for num in nums if num <= 0]#sorting input as larger than zero or smaller with list compr.

print(f"{positive_nums}\n{negative_nums}")
print(f"Count of positives: {len(positive_nums)}\nSum of negatives: {sum(negative_nums)}")
"""
