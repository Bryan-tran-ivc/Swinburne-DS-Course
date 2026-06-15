import math
def quadratic_expression():
    a = int(input("The a number is: "))
    b = int(input("The b number is: "))
    c = int(input("The c number is: "))
    if a == 0:
        print("This is not a quadratic expression.")
    else: 
        delta = b^2 - 4*a*c 
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / 2*a
            x2 = (-b - math.sqrt(delta)) / 2*a
            print("Two real solutions: ")
            print("x1 =", x1)
            print("x2 =", x2)
        elif delta == 0:
            x = -b/2*a
            print("One real solution: ")
            print("x =", x)
        else:
            print("There is no solution")
quadratic_expression()

        



        


    
