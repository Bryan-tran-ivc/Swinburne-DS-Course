#Algorithm Workbench
#Test 1:
if x > 100:
    y = 20
    z = 40
#Test 2:
if a == 100:
    b = 10
    c = 50
#Test 3:
if a < 10:
    b = 0
else:
    b = 99
#Test 4:
if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
#Test 5:
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1)
    else:
        print(amount2)
#Test 6:
if 40 <= score <= 49:
    again = True
else:
    again = False
#Test 7:
if points < 9 or points > 51:
    print("Invalid points.")
else:
    print("Valid points.")
#Test 8:
if 0 <= turtle.heading() <= 45:
    turtle.penup()
#Test 9:
if turtle.pensize() > 1 or turtle.pencolor() == 'red':
    turtle.pensize(1)
    turtle.pencolor('blue')
#Test 10:
if 100 <= turtle.xcor() <= 200 and 100 <= turtle.ycor() <= 200:
    turtle.hideturtle()

#Loop
#Test 1:
product = 0
while product < 100:
    number = float(input("Enter a number: "))
    product = number * 10
#Test 2:
again = 'y'
while again.lower() == 'y':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Sum: {num1 + num2}")
    again = input("Do you wish to perform the operation again? (y/n): ")
#Test 3:
for i in range(1, 101, 2):
    print(i)
#Test 4:
text = ""
while len(text) < 10:
    word = input("Type a word: ")
    text += word
    print(text)
#Test 5:
total = 0
for i in range(1, 31):
    total += i / (31 - i)
print(total)



