inp1 = "1c0111001f010100061a024b53535009181c"
inp2 = "686974207468652062756c6c277320657965"

h1 = inp1.decode("hex")
h2 = inp2.decode("hex")

#print h1, "\n", h2
"""
#print zip(h1, h2[:len(h1)])
for (x,y) in zip(h1, h2[:len(h1)]):
	w1 = ord(x)
	w2 = ord(y)
	print w1, "\t", w2
	print w1 ^ w2, "\n"
	#print chr(w1), "\t", chr(w2), "\n"
	#print chr(w1 ^ w2), "\n"
"""
result = "".join(chr(ord(x) ^ ord(y))
			for (x,y) in zip(h1, h2[:len(h1)]))
hr = result.encode("hex")
print result + "\n"
print hr
