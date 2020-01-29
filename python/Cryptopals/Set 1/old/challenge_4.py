import c3module as c3

tes = open("chal4inp.txt", "r")
content = tes.read()
tmp = []
dic = {}
cnt = 0
for i in content:
    if i != '\n':
        tmp.append(i)
    else:
        dic[cnt] = "".join(tmp)
        cnt += 1
        tmp = []
for k, v in dic.items():
    wll = v.decode("hex")
    print k, c3.maxScore(wll)
tes.close()
