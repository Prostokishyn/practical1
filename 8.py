number=int(input())
def is_prime(number):
    if number<2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i==0:
            return False
    return True
p=number-1
while not is_prime(p):
    p = p - 1
print("Перше просте число, яке передує", number, "дорівнює", p)