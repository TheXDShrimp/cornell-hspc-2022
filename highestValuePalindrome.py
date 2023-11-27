
# read in the input
s = "3943"
k = 1


newString = [*s]
changed = [0 for i in range(len(s))]
for i in range(len(s) // 2):
    if (s[i] != s[-i-1]):
        if (k > 0):
            if (s[i] > s[-i-1]):
                newString[-i-1] = s[i]
                changed[-i-1] = 1
            else:
                newString[i] = s[-i-1]
                changed[i] = 1
            k -= 1
        else:
            print(-1)
            exit()


for i in range(len(s) // 2):
    if (k > 0):
        if (newString[i] != '9'):
            if (changed[i] == 1):
                newString[i] = '9'
                newString[-i-1] = '9'
                k -= 1
            elif (k >= 2):
                newString[i] = '9'
                newString[-i-1] = '9'
                k -= 2

if (k > 0 and len(s) % 2 == 1):
    newString[len(s) // 2 + 1] = '9'
    
print(''.join(newString))