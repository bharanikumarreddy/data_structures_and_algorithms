NO_OF_CHARS = 256
s1="ate"
s2="eat"
c1=[0]*NO_OF_CHARS
c2=[0]*NO_OF_CHARS


for i in s1:                                    
    c1[ord(i)]+=1
for i in s2:
    c2[ord(i)]+=1

if len(s1)!=len(s2):
    print("NOT ANAGRAM")

for i in range(NO_OF_CHARS):
    if c1[i]!=c2[i]:
        print("NOT ANAGRAM")

print("ANAGRAM")
