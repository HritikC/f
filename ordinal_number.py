numbers = ['1', '2' ,'3' ,'4','5','6','7','8','9']

for number in numbers:
    if number == '1':
        print( number + "st")
    elif number == '2':
        print( number + "nd")
    elif number == '3':
        print( number + "rd")
    elif number == '4':
        print( number + "th")
    elif number == '5':
        print( number + "th")
    elif number == '6':
        print( number + "th")
    elif number == '7':
        print( number + "th")
    elif number == '8':
        print( number + "th")
    elif number == '9':
        print(number + "th")


numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("\n1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

