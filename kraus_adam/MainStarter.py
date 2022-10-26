"""
Grading tags in for all lines marked with *		DONE

Tierless str meets D in SOLID (hidden test)*	DONE MARKED
Check if done, but not all tiers are passing	DONE

1. Initial Show system\Got it compiling	
Menu\initial system working						DONE
Bad input handled								DONE

2. Add Default Box	
Added and shown properly						DONE
Second+ box ignored								DONE

3. Basic Update 
Moves along belts								DONE
Moves to next station\belt						DONE
Drops off the end when reached					DONE
String format correct							DONE
Iterator used*									DONE MARKED

4. Multi Update 	
Updates correct amount							DONE
Bad input handled								DONE
String format correct							DONE

5. Show station details (default)			
Shows stations details properly 				DONE
Iterator used*									DONE
				
6. Add box	
Added and shown properly						DONE
Second+ box ignored								DONE
Bad input handled								DONE

7. Tester Conveyer part 1	
Initial system and station details correct 	    DONE
A single box still able to be added				DONE
Update with one default box works				DONE
Loading works 									DONE
Formatting correct 								DONE

8. Tester Conveyer part 2	
Packaging works 							    DONE
Formatting correct 								DONE
Strategy pattern for loading*					DONE MARKED
Strategy pattern for packaging*					DONE MARKED


9. Custom belt **
String formatting correct						DONE
Everything still works 							DONE
Bad input handled 								DONE


** This tier has 3 tests associated with it. 9A tests all belt/station orderings. 9B tests all combinations of packaging and fill. 9C tests error checking.
"""

from kraus_adam.Box import Box
from kraus_adam.Belt import Belt
from kraus_adam.Station import Station
from kraus_adam.Conveyer import Conveyer
from kraus_adam.Behaviors.BasicLoad import BasicLoad
from kraus_adam.Behaviors.PercentLoad import PercentLoad
from kraus_adam.Behaviors.BasicPack import BasicPack
from kraus_adam.Behaviors.RestrictedPack import RestrictedPack

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
            choice = int(cleanInput( "Choice:> " ))

            # add default box
            if choice == 1:
                system.addBox(Box())
                print(system)

            # update one time
            elif choice == 2:
                box = None
                # GRADING: LOOP_ALL
                for section in system:
                    box = section.moveBox(box)
                print(system)

            # update X number of times
            elif choice == 3:
                x = int(cleanInput("How many updates:> "))
                if(x <= 0):
                    raise ValueError
                for i in range(x):
                    box = None
                    for section in system:
                        box = section.moveBox(box)
                    print(system)

            # print out station details
            elif choice == 4:
                station_num = 1
                for station in system.stations():
                    output = "Station " + str(station_num) + \
                        "\nHas box: " + str(station.hasBox()) + \
                        "\n" + str(station.getPackInfo()) + "\n"
                    print(output)
                    station_num += 1

            # make a new box of any size
            elif choice == 5:
                max = int(cleanInput("How many units:> "))
                if(max <= 0):
                    raise ValueError
                system.addBox(Box(max))
                print(system)

            # make new system
            elif choice == 6:
                system.clear()
                system.addSection(Belt())
                station1 = Station()
                system.addSection(station1)
                system.addSection(Belt())
                system.addSection(Belt())
                station2 = Station(BasicLoad(2), BasicPack(2))
                system.addSection(station2)
                system.addSection(Belt())
                system.addSection(Belt())
                station3 = Station(PercentLoad(50), RestrictedPack(3, 0, 1000))
                system.addSection(station3)

                print(system)

            # make new system
            elif choice == 7:
                system.clear()
                while True:
                    try:
                        selection = int(cleanInput("Belt (1) or Station (2):> "))
                        if selection == 1:
                            length = int(cleanInput("Length:> "))
                            if(length <= 0):
                                raise Exception
                            for i in range(length):
                                system.addSection(Belt())
                        elif selection == 2:
                            loadBehavior = None
                            packBehavior = None

                            loadOption = int(cleanInput("Load behavior: None (1), Basic (2), or Percentage (3):> "))
                            if loadOption not in range(1,4):
                                raise Exception
                            
                            if loadOption == 2: # basic load
                                numUnits = int(cleanInput("Number of units:> "))
                                if numUnits <= 0:
                                    raise Exception
                                loadBehavior = BasicLoad(numUnits);
                            elif loadOption == 3: # percent load
                                percentage = int(cleanInput("Percentage of box:> "))
                                if percentage <= 0 or percentage > 100:
                                    raise Exception
                                loadBehavior = PercentLoad(percentage)
                            
                            packOption = int(cleanInput("Packaging behavior: None (1), Basic (2), or Restricted (3):> "))
                            if packOption not in range(1,4):
                                raise Exception
                            
                            if packOption == 2: # basic pack
                                numBox = int(cleanInput("Number of boxes per package:> "))
                                if numBox <= 0:
                                    raise Exception
                                packBehavior = BasicPack(numBox);
                            elif packOption == 3: # restricted pack
                                numBox = int(cleanInput("Number of boxes per package:> "))
                                if numBox <= 0:
                                    raise Exception
                                minUnits = int(cleanInput("Minimum units:> "))
                                if minUnits < 0:
                                    raise Exception
                                maxUnits = int(cleanInput("Maximum units:> "))
                                if maxUnits < minUnits:
                                    raise Exception
                                packBehavior = RestrictedPack(numBox, minUnits, maxUnits);

                            station = Station(loadBehavior, packBehavior)
                            system.addSection(station)
                        else:
                            print("Input an option in the range 1-2")
                    except:
                        print("Cannot accept value")
                    another = cleanInput("Add another component (n to stop):> ")
                    if(another == "n"):
                        break;
                print(system)

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

                # GRADING: TO_STR
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
