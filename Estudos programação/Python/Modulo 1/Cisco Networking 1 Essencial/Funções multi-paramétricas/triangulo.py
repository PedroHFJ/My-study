def triangulo(a,b,c):
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    return True

print(triangulo(10,15,40))

#Podemos compactar ainda mais

def triangulo1(e,f,g):
    return e + f > g and f + g > e and e + g > f

print(triangulo1(20,20,30))
