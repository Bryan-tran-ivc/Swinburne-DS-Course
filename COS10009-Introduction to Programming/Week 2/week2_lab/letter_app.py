def main():
    label = return_label() #store the value of return_label into variable label
    message = return_message() #store the value of return_message into variable message
    print_letter(label, message) #print all the information
def return_label():
    #This is used for getting the users information and return it 
    title = input("Please enter your title (Mr, Mrs, Ms, Miss, Dr):\n")
    first_name = input("Please enter your first name:\n")
    last_name = input("Please enter your last name:\n")
    unit_number = input("Please enter the house or unit number:\n")
    street_name = input("Please enter the street name:\n")
    suburb = input("Please enter the suburb:\n")
    #Get and validate the postcode
    while True:
        postcode = input("Please enter a postcode (0000 - 9999):\n")
        #Check if the input contains letters, change it to integer and compare between 0-9999
        if postcode.isdigit() and 0 <= int(postcode) <= 9999: 
            break
        print("Invalid postcode. Please try again.")

    label = (
        title + " " + first_name + " " + last_name + "\n"
        + unit_number + " " + street_name + "\n"
        + suburb + " " + postcode
    )

    return label
    #This is for returns the letter message
def return_message():
    message_subject = input("Please enter your message subject line:\n")
    print("Please enter your message content:\n")
    content = input()
    message = "RE: " + message_subject
    message = message + "\n\n"
    message = message + content
    return message
#This is for printing all the information
def print_letter(label, message):
    print() #Create blank space
    print(label) #print label
    print() #Create blank space
    print(message)#print message
main()





