tes = open("chal4inp.txt", "r")
wew = []
for i in tes:
    if i[-1] =='\n':
        wew.append(i[:-1])
wow = "".join(wew)
inp = wow.decode("hex")
print wow
