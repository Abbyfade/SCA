def PythagoreanTrippleChecker():
    print('Welcome to the pythagorean triplle checker!')
    checker = input('Enter yes to continue or quit to end the program: ').lower()
    while checker == 'yes':
        try:
            sides = []
            side1 = int(input("Enter side 1: "))
            side2 = int(input("Enter side 2: "))
            side3 = int(input("Enter side 3: "))

            sides.append(side1)
            sides.append(side2)
            sides.append(side3)
            sides = sorted(sides)

            if sides[0]** 2 + sides[1]**2 == sides[2]**2:
                print("{}, {}, and {} is a pythagorean tripple".format(side1, side2, side3))

            else:
                print("{}, {}, and {} is not a  pythagorean tripple".format(side1, side2, side3))

            checker = input('Enter yes to continue or quit to end the program: ').lower()

        except:
            print("An error occured!")
            print('Make sure you enter integers ')
            checker = input('Enter yes to continue or quit to end the program: ').lower()


PythagoreanTrippleChecker()
