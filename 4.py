import math
a=int(input("Перша сторона: "))
b=int(input("Друга сторона: "))
c=int(input("Третя сторона: "))
p=(a+b+c)/2
kyt=math.acos((a**2+b**2-c**2)/(2*a*b))
s1=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Формула герона: ", s1)
s2=(1/2)*a*b*math.sin(kyt)
print("За сторонами і кутом: ", s2)