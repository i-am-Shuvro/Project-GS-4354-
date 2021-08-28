def greet(str):
    name1 = input("[N.B: Enter your name to start the program.] \n\t* First Name: ")
    name2 = input("\t* Last Name: ")
    return "Hello, " + str(name1) + " " + str(name2) + "! Welcome to this program, sir!"


print(greet(str))
print("This program helps you with some information on tax-rate on building construction. "
      "\nBesides it tells you about some facilities you can add to your cart within your budget.")

input("\tPress ENTER to start the program!")

from Module import getinput

def confirm():
    while True:
        budget = getinput("Please enter your budget amount for building construction in BDT (At least 1 crore): ")
        if budget < 10000000:
            print("\tThis budget is too low to construct a building, sir! The minimum budget should be of 1 crore!")
            continue
        else:
            input(f"\tGreat! {budget} BDT is quite a sufficient amount. \nNow please press ENTER & choose various options!")
            if budget >= 150000000:
                while True:
                    try:
                        marble = int(input("\tDo you want marble-flooring in your building? Type 1 if you want & type 2 if you don't: "))
                        if marble == 1:
                            print("\t\tOkay! Your building will be of marble-flooring, sir.")
                        elif marble == 2:
                            print("\t\tGot you! You will get tiles-flooring, sir.")
                        else:
                            print("\t\tPlease choose to type one option from 1 and 2!")
                            continue
                    except ValueError:
                        print("\t\tOops! Something is wrong. Please choose to type one option from 1 and 2!")
                        continue
                    break
            elif budget <= 50000000 or budget >= 15000000:
                while True:
                    try:
                        tiles = int(input("\tDo you want tiles-flooring in your building? Type 1 if you want & type 2 if you don't: "))
                        if tiles == 1:
                            print("\t\tOkay! our building will be of tiles-flooring, sir.")
                        elif tiles == 2:
                            print("\t\tGot you! You will get cement-flooring, sir.")
                        else:
                            print("\t\tPlease choose to type one option from 1 and 2!")
                            continue
                    except ValueError:
                        print("\t\tOops! Something is wrong. Please choose to type one option from 1 and 2!")
                        continue
                    break
            else:
                print("\t\tAlight! You will get cement-flooring, sir.")
            break

    return budget


my_budget = confirm()


def free():
    free_facilities = ["AI Security System", "Free Water Supply", "10 Years of free maintenance"]
    serial = [1, 2, 3]
    serial_of_services = [serial, free_facilities]
    print("\nAs a small present, we give all our customers these 3 facilities for free: ", *free_facilities, sep="\n\t")
    print("Besides you can suggest us for some more free-services.")
    try:
        n = int(input("Except these 3, enter how many facilities you would suggest us to provide for free (Press ENTER to skip): "))
        j = 1
        while j != n + 1:
            free_demands = input("\t* Suggestion " + str(j) + ": ")

            if not free_demands:
                j -= 1
                print("\tPlease enter your suggestions!")
            else:
                free_facilities.append(free_demands)
                serial.append(4 + j)

            j += 1

        t = len(free_facilities)
        print(f"Along with the 3 services, we will try to provide you with these {n} facilities:",
              *free_facilities[3:], sep="\n\t")
        print("\nSo, all you get from us as complementary is", *free_facilities, sep="\n\t")
        try:
            r = int(input("\nIf you wish to remove any of the above free services, just enter the serial number (Press ENTER to skip): "))
            z = free_facilities.index(serial_of_services[1][r - 1])
            free_facilities.pop(z)
            print("\tSo you will get these free-services:", *free_facilities, sep="\n\t\t")
            try:
                more_delete = int(input("Want to remove some more services? Then write here the number of services you want to delete (Press ENTER to skip): "))
                print("\t\tWrite down service name completely to delete from your cart! (eg: AI Security Service)")
                for a in range(0, more_delete):
                    items = str(input(f"\t\t\t{a + 1}. Remove the service = "))
                    free_facilities.remove(items)
                print("Alright! So, you are getting this fro free:", *free_facilities, sep="\n\t")
            except:
                print("So you do not want anything more to be removed. Great!")
        except:
            print("So, you don't want to remove anything from the list. Great!")
    except:
        print("So, you don't want to remove anything from the list. Great!")

free_service = free()


def paid():
    print("\nWe also provide some services to our customers. You can purchase them from us. They are:")
    internaldata = {1: 2000000,
                    2: 250000,
                    3: 800000,
                    4: 2000000,
                    5: 600000,
                    }

    paid_facilities = {'1. Car Parking': 2000000,
                       '2. Elevator': 250000,
                       '3. Jacuzzi': 800000,
                       '4. Roof-top Swimming Pool': 2000000,
                       '5. Sauna': 600000,
                       }

    for info in paid_facilities:
        print("\t", info)

    while True:
        try:
            y = int(input("To know the price in BDT, please list number (Press ENTER to skip): "))
            if 1 <= y <= 5:
                print("\tThe price of this item will be: ", internaldata.get(y))
            else:
                print("Please enter between 1 to 5 from this list!")
                continue
            z = input("Do you want to add more services? Type y to continue & press ENTER to skip: ")
            if z.lower() == 'y':
                continue
            else:
                print("Okay! No more prices!")
                break
        except:
            print("Okay! No more prices!")
            break

    print("\nHere is a complete list of services. You can order them later if need be. Have a look:")
    for key, value in paid_facilities.items():
        print(key, ": Price", value, "BDT")


paid_service = paid()

from Module import getinput
building_type = ('1. Garment', '2. Residential', '3. Commercial', '4. Corporate')
print("\n Now to know about tax-rates & your total cost, choose a building type from this list - ", *building_type, sep="\n\t")
b = getinput("Enter the number for your building type?: ")
tax_list = (12, 10, 20, 25)

from Module import TaxCalc

maxtax = TaxCalc(tax_list)
print(f"\tThe maximum tax-rate will be {maxtax.get_max_tax()}% ", end="")
print(f"and the minimum tax-rate will be {maxtax.get_min_tax()}% for your building!")


class Gar(TaxCalc):
    def get_addtax_gar(self):
        return my_budget * (3 / 100)


gar = Gar(TaxCalc)
gar.get_addtax_gar()


class Corp(TaxCalc):
    def get_addtax_corp(self):
        return my_budget * (2 / 100)


corp = Corp(TaxCalc)
corp.get_addtax_corp()


class Com(TaxCalc):
    def get_addtax_com(self):
        return my_budget * (4 / 100)


com = Com(TaxCalc)
com.get_addtax_com()
addtax_list = [gar.get_addtax_gar(), 0, com.get_addtax_com(), corp.get_addtax_corp()]

while True:
    if b == 1:
        print(f"[N.B: There will be additional tax of {gar.get_addtax_gar()} BDT for garments contraction.]")
    elif b == 2:
        print("There will be no additional tax!")
    elif b == 3:
        print(f"[N.B: There will be additional tax of {com.get_addtax_com()} BDT for commercial building contraction.]")
    elif b == 4:
        print(
            f"[N.B: There will be additional tax of {corp.get_addtax_corp()} BDT for corporate building contraction.]")
    else:
        print("Please enter between 1 & 4")
        b = getinput("Please re-enter the number for your building type?: ")
        continue
    break
max_total = my_budget + int(addtax_list[int(b) - 1]) + my_budget * 0.25
min_total = my_budget + int(addtax_list[int(b) - 1]) + my_budget * 0.1

print("\nYou total cost will fluctuate between ", max_total, "BDT & ", min_total, "BDT while completing the whole construction project!")

input("\nThanks a ton for running this code! Press ENTER to close.")
