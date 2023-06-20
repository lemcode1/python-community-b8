# a="python"
# print(a[3])
# print(a[-1])
# print(a[5])
# print(len(a))
# print(a[len(a)-1])
# print(a[12])
# I want to get pyth from python?
# step1: I need to get substring from a string
# step2: I need to start from first character in the string
# step3: I need to stop at 5th character in the string
# print(a[0:4])
# print(a[:4])
# print(a[4:6])
# print(a[4:])
# print(a[-6:-2])  # -6  -5  -4 -3  p y t h
# print(a[-2:])
a="python"  # pto   # yhn
print(a[0:5:2]) # 0 2 4 # pto
print(a[1:6:2]) # 1 3 5 # y h n
print(a[1::2]) # 1 3 5 # y h n
# hty
print(a[-3:-6:-1]) # -3 -4 -5 hty
print(a[-2:-7:-2]) # -2 -4 -6 otp
print(a[-2::-2]) # -2 -4 -6 otp
# print(a[:len(a):1]) # -1:6:-2 # -1 -3 -5 -7
# reverse a string --> it takes atleast 10 lines of code
# python ---> nohtyp
# kasi --> isak
print(a[::-1]) # -1::-1
b="kasi"
print(b[::-1])
# madam # radar
# madam # radar
s1="madam"
s2=s1[::-1]
print(s1==s2)

