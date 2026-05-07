def imc(weight, height):
    return weight/ height**2


def libra(lb):
    return lb * 0.4535923

def to_metro(ft, inch = 0):
    return ft * 0.3048 + inch* 0.0254

print(imc(weight= libra(175), height= to_metro(5,7)))
