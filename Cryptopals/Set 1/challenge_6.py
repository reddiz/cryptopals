def s2b(inp):
    bn = []
    for i in inp:
        b = bin(ord(i)).replace("0b", '')
        if len(b) < 8:
            b = "0"*(8 - len(b)) + b
        bn.append(b)
    res = "".join(bn)
    return res

def Hamming(in1, in2):
    cnt = 0
    res = []
    for i,j in zip(in1, in2):
        tmp = int(i) ^ int(j)
        if tmp == 1:
            cnt += 1
            res.append(cnt)
    ttl = sum(res)
    #print ttl
    return ttl

def edt(df, ky):
    tes = {}
    for i in ky:
        res = []
        for j in range(0, len(df), i):
            if j+i < len(data):
                b1 = s2b(df[j:(j+i)])
                b2 = s2b(df[j+i:(j+i)+i])
                tmp = Hamming(b1, b2)
            res.append(tmp)
        tes[i] = sum(res)
    for k,j in tes.items():
        print k, j/i
    #return tes

file = open("chal6inp.txt", "r")
data = file.read()
strl = []
KEYSIZE = range(2, 41)

for x in data:
    if x != '\n':
        strl.append(x)

strc = "".join(strl)
print edt(strc, KEYSIZE)
#for i in KEYSIZE:
#    for j in range(0, len(strc), i):
#            if j+i < len(strc):
#                print i, strc[j:j+i], strc[j+i:(j+i)+i]

file.close()
