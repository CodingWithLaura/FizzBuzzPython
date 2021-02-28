

def fizz_buzz():
    for i in range(1,101):
        if(check_fizz(i) | check_buzz(i)):
            if(check_fizz(i)):
                print("fizz", end = '')
            if(check_buzz(i)):
                print("buzz", end = '')
            print('')
        else:
            print(i)

def check_fizz(number):
    if(number % 3 == 0):
        return True
    return False

def check_buzz(number):
    if(number % 5 == 0):
        return True
    return False

if __name__ == "__main__":
    fizz_buzz()
