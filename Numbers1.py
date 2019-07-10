import math

class LimitError(Exception):
    '''Custom Exception'''
    pass

def find_decimal_places():
    '''This function asks the user how mnay decimal places Pi should be printed out
    There is a lower limit of 1 and an upper limit of 48 (inclusive). A while
    loop continues asking until the conditions are satisfied. Function returns
    an integer
    '''
    
    decimals = ""
    while decimals == "":
        try:
            decimals = int(input("How many decimal places would you like Pi in? "))
            if decimals > 0:
                if decimals < 49:
                    break
                else:
                    decimals = ""
                    raise LimitError
            else:
                decimals = ""
                raise ValueError

        except ValueError:
            print("Please enter an positive integer value")
        except LimitError:
            print("There is an upper limit of 48 decimal places")


    return decimals

def print_pi(decimals):
    '''This function prints out Pi to the desired number of decimal places'''
    print("{:.{decimals}f}".format(math.pi, decimals = decimals))

def main():
    '''The main function which runs the other subfunctions'''
    decimals = find_decimal_places()
    print_pi(decimals)

main()
