import math
def inputCoef():
    while 1:
        try:
            a = float(input("Input a: "))
            if (a!=0.0):
                break
            print("Error, please input data again")
        except ValueError:
            print("Error, please input data again")

    while 1:
        try:
            b = float(input("Input b: "))
            break
        except ValueError:
            print("Error, please input data again")

    while 1:
        try:
            c = float(input("Input c: "))
            break
        except ValueError:
            print("Error, please input data again")
    return a,b,c



def calcelation():
    A,B,C = inputCoef()
    #print(type(inputCoef()))
    discriminant = B**2 - 4*A*C
    if discriminant >= 0:
        try:
            x1 = math.sqrt((-B + discriminant**0.5) / (2*A))
            print(f"x1: {x1}")
        except:
            print("x1: wrong root")
        try:
            x2 = -math.sqrt((-B + discriminant**0.5) / (2*A))
            print(f"x2: {x2}")
        except:
            print("x2: wrong root")
        try:
            x3 = math.sqrt((-B - discriminant**0.5) / (2*A))
            print(f"x3: {x3}")
        except:
            print("x3: wrong root")
        try:
            x4 = -math.sqrt((-B - discriminant**0.5) / (2*A))
            print(f"x4: {x4}")
        except:
            print("x4: wrong root")

        print(f"Discriminant: {discriminant}")
    else:
        print("discriminant < 0")



calcelation()