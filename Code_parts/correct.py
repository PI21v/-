"""s=["2.78\n54.67\n45.75",
"-2.78\n54.67\n-45.75",
"8\n54.67\n45.75",
"2.78\n54.\n45.75",
"2.45\n.67\n45.75",
"2.78\n.\n45.75",
"2.78\n.\n45.75",
"2.78\n3-4.56\n45.75",
"2.78\n-.75\n45.75",
"2.78\n56.-75\n45.75",
"2.78\n54.67\n\n45.75",
"aaaaaaaa",
"2.aa\n-.75\n45.75",]"""

def ok(s):
	for i in range(len(s)):
		if ord(s[i])<44 and ord(s[i])!=10:
			#print(s[i])
			return -1
		elif ord(s[i])==47:
			#print(s[i])
			return -1
		elif ord(s[i])>57:
			#print(s[i])
			return -1
	test_list=list(s.split("\n"))
	for i in test_list:
		test_i=list(i.split("."))
		if len(test_i)!=2:
			return -1
		elif len(test_i[0])==0 or len(test_i[1])==0:
			return -1
		for k in range(len(test_i[0])):
			if ord(test_i[0][k])==45:
				if len(test_i[0])==1 or k!=0:
					return -1
		for k in range(len(test_i[1])):
			if ord(test_i[1][k])==45:
				return -1
	return 0

"""for i in range(45,58):
	print(i,chr(i))
	print(ord("-"))"""
