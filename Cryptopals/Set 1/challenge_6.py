def s2b(inp):
    bn = []
    for i in inp:
        b = bin(i).replace("0b", '')
        if len(b) < 8:
            b = "0"*(8 - len(b)) + b
        bn.append(b)
    res = "".join(bn)
    return res

def Hamming(in1, in2):
    cnt = 0
    for i,j in zip(in1, in2):
        tmp = int(i) ^ int(j)
        if tmp == 1:
            cnt += 1
    return cnt

def edt(df, inp1, inp2):
    h1, h2 = [], []
    for i in df:
        tmp1 = ord(i) ^ inp1
        tmp2 = ord(i) ^ inp2
        h1.append(tmp1)
        h2.append(tmp2)
    res =  Hamming(s2b(h1), s2b(h2))
    return res/len(KEYSIZE)

data = open("chal6inp.txt", "r").read()
KEYSIZE = range(2, 41)
