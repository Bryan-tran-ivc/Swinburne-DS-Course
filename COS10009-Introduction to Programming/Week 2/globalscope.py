PI = 3.14159265359

def main():
    rad = float(input("Enter the radius of the circle: "))
    circle_area(rad)
    circle_perimeter(rad)

def circle_area(radius):
    area = PI * radius**2
    print("The area of the circle is: ", area)

def circle_perimeter(radius):
    perimeter = 2 * PI * radius
    print("The perimeter of the circle is: ", perimeter)
main()
