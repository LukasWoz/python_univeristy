def check_combination(code):
    if code != '2345':
        print("Incorrect code")
        return False
    else:
        print('Access granted')
        return True


if __name__ == '__main__':
    print("\nCombination lock")
    correct = False
    counter = 4
    while correct is False and counter > 0:
        print("\n(%s tries remaining)" % counter)
        combination = input("Enter 4-digit code: ")
        correct = check_combination(combination)
        counter -= 1
