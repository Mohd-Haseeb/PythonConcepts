try :
    pass
except :
    pass
#   raise -> to reraise the exception
else:
    pass 
    # -> will come in else block if try is successfull
finally:
    pass



def power_of_two():
    user_input = input("Please enter the number : ")
    try:
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        print('Input is invalid. Check again !!')

# power_of_two()


## ANOTHER EXAMPLE

def interact():
    while True:
        try:
            user_input = int(input('Enter a number : '))
        except ValueError:
            print('Please enter a valid integer')
        else:
            print('{} is {}'.format(user_input, 'Even' if user_input%2==0 else 'Odd'))
        finally:
            user_input = input('Do you want to play again ? (y/n)')
            if user_input != 'y':
                print('Good BYe !!!')
                break

interact()
