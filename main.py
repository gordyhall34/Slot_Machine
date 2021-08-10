import random


def main():
    user = input("Would you like to spin the machine? (yes/no) ")
    answer = str(user)
    if answer == str("yes"):
            roll1, roll2, roll3 = generate_num()
            roll1, roll2, roll3 = convert_num(roll1, roll2, roll3)
            compare_nums(roll1, roll2, roll3)
    else:
        print("Thanks for running this I guess")


def generate_num():
    l = []
    for i in range(3):
        i = random.randint(0, 9);
        l.append(i)
        print(i)
    print(l)
    roll1 = l[0]
    roll2 = l[1]
    roll3 = l[2]
    return (roll1, roll2, roll3)


def convert_num(roll1, roll2, roll3):
    if roll1 >= 0 and roll1 <= 2:
        roll1 = str("lemon")
    elif roll1 > 2 and roll1 <= 4:
        roll1 = str("cherry")
    elif roll1 > 4 and roll1 <= 6:
        roll1 = str("peach")
    elif roll1 > 6 and roll1 <= 8:
        roll1 = str("apple")
    elif roll1 > 8 and roll1 <= 9:
        roll1 = str("tomato")
    # print(roll1)

    if roll2 >= 0 and roll2 <= 2:
        roll2 = str("lemon")
    elif roll2 > 2 and roll2 <= 4:
        roll2 = str("cherry")
    elif roll2 > 4 and roll2 <= 6:
        roll2 = str("peach")
    elif roll2 > 6 and roll2 <= 8:
        roll2 = str("apple")
    elif roll2 > 8 and roll2 <= 9:
        roll2 = str("tomato")
    # print(roll2)

    if roll3 >= 0 and roll3 <= 2:
        roll3 = str("lemon")
    elif roll3 > 2 and roll3 <= 4:
        roll3 = str("cherry")
    elif roll3 > 4 and roll3 <= 6:
        roll3 = str("peach")
    elif roll3 > 6 and roll3 <= 8:
        roll3 = str("apple")
    elif roll3 > 8 and roll3 <= 9:
        roll3 = str("tomato")
    # print(roll3)

    print(roll1, roll2, roll3)
    return (roll1, roll2, roll3)


def compare_nums(roll1, roll2, roll3):
    if roll1 == roll2 and roll2 == roll3:
        print("YOU WON THE GRAND PRIZE")
        win = swap()
    elif roll1 == roll2 and roll2 != roll3:
        print("close try again")
    elif roll1 == roll3 and roll2 != roll3:
        print("close try again")
    elif roll1 != roll2 and roll2 == roll3:
        print("close try again")
    elif roll1 != roll2 and roll2 != roll3:
        print("close try again")


def swap():
    win += 1


if __name__ == '__main__':
    main()
