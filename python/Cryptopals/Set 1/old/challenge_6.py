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
    return ttl

def edt(d, k):
    tes = {}
    for i in k:
        res = []
        for j in range(0, len(d), i):
            if j+i < len(data):
                b1 = s2b(d[j:(j+i)])
                b2 = s2b(d[j+i:(j+i)+i])
                tmp = Hamming(b1, b2)
            res.append(tmp)
        tes[i] = sum(res)/(i*j)
    return min(tes, key=tes.get)

def block_key(df, ky):
    v29 = {}
    blk = {}
    cnt = 1
    for i in range(0,len(df)+1, ky):
        if i+ky <= len(df)+1:
            v29[cnt] = df[i:i+ky]
            cnt += 1
        else:
            v29[cnt] = df[i:]
    for i in range(0, ky):
        for j in v29.values():
		print j[i],


file = open("chal6inp.txt", "r")
data = file.read()
strl = []
KEYSIZE = range(2, 41)

for x in data:
    if x != '\n':
        strl.append(x)

strc = "".join(strl)
print block_key(strc, edt(strc.decode("base64"), KEYSIZE))

file.close()
