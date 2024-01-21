import math
a=int(input("Введіть a: "))
b=int(input("Введіть b: "))
c=int(input("Введіть c: "))
d=b**2-4*a*c
if d < 0:
    print("Дискрмиінант менше нуля, без розвязків")
else:
    root1=(-b+(math.sqrt(d)))/(2*a)
    root2=(-b-(math.sqrt(d)))/(2*a)
    print("Перший корінь: ", root1)
    print("Другий корінь :", root2)
