print("")
print("Type a number to find out if it's prime.")

number = int(input(""))


def prime_check(number):
    if number > 1:
        for n in range(2, number // 2):
            mod = number % n
            if mod == 0:
                print("Not Prime")
                break
            else:
                print("Prime")
                break
    else:
        print("Not Prime")


prime_check(number)