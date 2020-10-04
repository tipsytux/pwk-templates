#!/usr/bin/python
ideal=open('ideal_space','r')
ideal_seq=(ideal.readline()).split()
check=open('check_space','r')
check_seq=(check.readline()).split()
badChars='\\x00'
bChars='\\x00'
flag=0
if len(check_seq) != len(ideal_seq):
    print ("Enter correct values")
for i in range(len(ideal_seq)):
    if check_seq[i] != ideal_seq[i]:
        badChars = badChars+'\\x'+ ideal_seq[i]
        if flag%2==0:
            bChars= bChars+'\\x'+ideal_seq[i]
        print ("Located Bad Char %s " % ideal_seq[i])
        flag=flag+1

print("Done")
print(badChars)
print(bChars)
