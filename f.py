import sys
sides = input().split("=")
a = sides[0]
big = 1
for i in a:
    if i.isdigit():
        big=max(big,int(i))
    
b = sides[1]

for i in b:
    if i.isdigit():
        big=max(big,int(i))
big += 1
import re

number_or_symbol = re.compile('(\d+|[^ 0-9])')
nums1 = re.findall(number_or_symbol, a)
nums2 = re.findall(number_or_symbol, b)
       
sols = []
def check(base):
    a = [x for x in nums1]
    b = [x for x in nums2]
    for i in range(len(nums1)):
        if nums1[i].isdigit():
            a[i]=str(int(nums1[i],base))
    for i in range(len(nums2)):
        if nums2[i].isdigit():
            b[i]=str(int(nums2[i],base))
    val1 = eval("".join(a))
    val2 = eval("".join(b))
    return [val1,val2]
for base in range(big,11):
    vals = check(base)
    if vals[0]==vals[1]:
        sols.append(base)
if len(sols)>0 and len(sols)==10-sols[0]+1:
    print(str(sols[0])+"+")
    sys.exit(0)
    
small = 11
bigg = 10**17
while small <= bigg:
    mid1 = small + (bigg - small) //3
    mid2 = bigg - (bigg - small) //3

    # Check if key is present at any mid
    a = check(mid1)
    if a[0]==a[1]:
        sols.append(mid1)
    b = check(mid2)
    if b[0]==b[1]:
        sols.append(mid2)

    if a[0]<a[1]:
        bigg=mid1-1
    elif (b[0]>b[1]):
        small=mid2+1
        
    else:

        # The key lies in between mid1 and mid2
        return ternarySearch(mid1 + 1,
                                mid2 - 1, key, ar)