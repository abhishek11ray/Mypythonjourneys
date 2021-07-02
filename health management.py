def getdate():
    import  datetime
    return datetime.datetime.now()
def take(k):
    if k == 1:
        c = int(input("enter 1 for food & 2 for exercise\n"))
        if c == 1:
            value = input("type food name\n")
            with open ("abhi-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully updated")
        elif c == 2:
            value = input("type of exercise name\n")
            with open("abhi-ex.txt","a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully updated")

    elif k == 2:
        c = int(input("enter 1 for food & 2 for exercise\n"))
        if c == 1:
            value = input("type food name\n")
            with open("lambu-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully updated")
        elif c == 2:
            value = input("type of exercise name\n")
            with open("lambu-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully updated")

    elif k == 3:
        c = int(input("enter 1 for food & 2 for exercise\n"))
        if c == 1:
            value = input("type food name\n")
            with open("madhu-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully updated")
        elif c == 2:
            value = input("type of exercise name\n")
            with open("madhu-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully updated")


    else:
        print("plz enter valid input (1(abhi),2(lambu),3(madhu)")

def retrive(k):
    if k == 1:
        c = int(input(" enter 1 for food & 2 for exercise\n"))
        if c == 1:
            with open("abhi-food.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("abhi-ex.txt") as op:
                for i in op:
                    print(i, end="")

    elif k == 2:
        c = int(input(" enter 1 for food & 2 for exercise\n"))
        if c == 1:
            with open("lambu-food.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("lambu-ex.txt") as op:
                for i in op:
                    print(i, end="")

    elif k == 3:
        c = int(input(" enter 1 for food & 2 for exercise\n"))
        if c == 1:
            with open("madhu-food.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("madhu-ex.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("please enter valid input (abhi, lambu,madhu)")
print("Health Management System")
a = int(input("press 1 for log the value and 2 for retrieve \n"))

if a == 1:
    b = int(input("press 1 for abhi 2 for lambu 3 for madhu \n"))
    take(b)
else:
    b = int(input("press 1 for abhi 2 for lambu 3 for madhud \n"))
    retrive(b)





