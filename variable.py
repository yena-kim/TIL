
#1 문제.

x = 4
y = 7

print(x+y)
print(x*y) 

#2 문제.

a = 10
b = 4

print(a)
print(b)

# #2-1

print(a/b)

# #2-2
c = a/b
print(c)

# #2-3
print(a//b)

# #2-4
print(a%b)

print ("mile을 입력해주세요.(숫자)")
mile = input()
print(mile)

change = 1.6

print("km로 환산하면?")
print(int(mile)*change)

print("km를 입력해주세요.")
km = input()
print(km)
print("km를 mile로 환산하면?")
print(int(km)/change)

print("화씨(f)온도를 입력해주세요.")
f = input()
cc = (float(f)-32)*5/9
print("섭씨온도로 변환하면?")
print(cc)

print("섭씨온도(c)를 입력해주세요.")
c = input()
ff = (float(c)*9/5+32)
print(ff)


#문자자료형

#1
a = "토마토 만세만세\n토마토 만세만세"
print(a)
print("---")

b = "토마토 만세만세"
print(b)
print(b)
print("---")

c = """토마토 만세만세
토마토 만세만세"""
print(c)


d = """
\\    /\\
 )  ( ')
(  /  )
 \\(__)|
 """

print(d)

hongsid = "881120-1068234"

bday = hongsid.split("-")
print(bday[0])
print(bday[1])

a = "a:b:c:d"
a = a.replace(":","#")
print(a)
