def read_array():
    n = int(input("How many lines are you entering? "))
    return [input("Enter text: ") for _ in range(n)]
 
def print_array(a):
    print("Printing lines:")
    for i in range(len(a)):
        print(i, a[i])
 
def main():
    a = read_array()
    print_array(a)
 
if __name__ == "__main__":
    main()