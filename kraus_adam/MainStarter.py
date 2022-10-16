from Box import Box
from Belt import Belt
from Station import Station
from Conveyer import Conveyer

def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input( )

    return result

def main( ):
    menu = "\n" \
           "1) Add Default Box\n" \
           "2) Move Belt One Time Unit\n" \
           "3) Move Belt X Time Units\n" \
           "4) Show Station Details\n" \
           "5) Add Box\n" \
           "6) Make Tester Conveyer Belt\n" \
           "7) Make New Conveyer Belt\n" \
           "0) Quit\n"

    system = Conveyer()
    print(system)

    choice = -1
    while choice != 0:
        try:
            print( menu )
            choice = cleanInput( "Choice:> " )
            choice = int(choice)

            # add default box
            if choice == 1:
                system.addBox(Box())
                print(system)

            # update one time
            elif choice == 2:
                box = None
                for section in system:
                    oldBox = section.moveBox(box)
                    box = oldBox
                print(system)

            # update X number of times
            elif choice == 3:
                x = int(cleanInput("How many updates:> "))
                if(x <= 0):
                    raise ValueError
                for i in range(x):
                    box = None
                    for section in system:
                        oldBox = section.moveBox(box)
                        box = oldBox
                    print(system)

            # print out station details
            elif choice == 4:
                print( "TODO" )

            # make a new box of any size
            elif choice == 5:
                max = int(cleanInput("How many units:> "))
                system.addBox(Box(max))
                print(system)

            # make new system
            elif choice == 6:
                print( "TODO" )

            # make new system
            elif choice == 7:
                print( "TODO" )

            # debug/check for D in SOLID in __str__
            elif choice == -1:
                box1 = Box()
                box2 = Box()
                box3 = Box()
                belt = Belt()
                belt.addBox(box1)
                station = Station()
                station.addBox(box2)
                system.addBox(box3)

                print(box1)
                print(box2)
                print(belt)
                print(station)
                print(system)

            elif choice == 0:
                choice = 0
            else:
                print( "Input an option in the range 0-7" )
        except ValueError:
            print("Please, input a positive integer")
        except:
            import traceback
            print(traceback.format_exc())

if __name__ == '__main__':
    main( )
