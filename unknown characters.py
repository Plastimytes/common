#cocatenate uncommon characters
s1="abcd"
s2="cdefg"
s3=(s1[0],s1[1])+(s2[2],s2[3],s2[4])
print(s3)

#method 2
s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
#find common??
compare=list(set(s1)&set(s2))
for i in compare:
    print(i)
    i.append
    print(i.append) 