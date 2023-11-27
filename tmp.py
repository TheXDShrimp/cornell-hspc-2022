line = input().split("+")
line[1]=line[1].split("=")
line = [line[0],line[1][0],line[1][1]]
import itertools
curr = list(itertools.permutations("0123456789"))
for i in curr:
    check = []
    for j in line:
        num = ""
        for char in j:num += i[int(char)]
        check.append(int(num))
    if check[0]+check[1] == check[2]:
        ans = ["0"]*10
        for pos in range(10):
            ans[int(i[pos])]=str(pos)
        print("".join(ans))
        break