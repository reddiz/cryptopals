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
    for i,j in zip(in1, in2):
        tmp = int(i) ^ int(j)
        if tmp == 1:
            cnt += 1
    return cnt

tes1 = "this is a test"
tes2 = "wokka wokka!!!"
assert Hamming(s2b(tes1), s2b(tes2)) == 37, "False!"
KEYSIZE = range(2, 41)
