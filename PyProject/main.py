
def main():
    print("Hello World")
    n = 0
    while (n < 5):
        print(n)
        n = n + 1
main()
line = ["1|2|3", "-+-+-", "4|5|6", "-+-+-", "7|8|9"]

def getInput():
    val = input("Where would you like to play? (1-9) ")
    return val

def display(list):
    for item in list:
        print(item)

    val = getInput()
    if val == "1":
        list[0] = "X|2|3" 

display(line)

