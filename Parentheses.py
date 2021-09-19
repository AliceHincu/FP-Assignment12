from iterative import Iterative
from recursive import Recursive

if __name__ == '__main__':
    print("Choose option:\n\t1.Recursive\n\t2.Iterative\n\t3.Exit")
    unicorns_exist = True
    while unicorns_exist:
        try:
            cmd = input("\n>option: ")
            if cmd == "1" or cmd == "2":
                n = input("n= ")
                if n.isdigit():
                    n = int(n)
                    if n % 2 == 0:
                        if cmd == "1":
                            Recursive().generate_parentheses(n)
                        else:
                            Iterative().generate_parentheses(n)
                    else:
                        raise ValueError("n can't be odd")
                else:
                    raise ValueError("Please insert a number")
            else:
                if cmd == "3":
                    unicorns_exist = False
                else:
                    raise ValueError("Wrong command!")
        except ValueError as err:
            print(err)
