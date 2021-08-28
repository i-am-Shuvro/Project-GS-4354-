tax_list = [12, 10, 20, 25]


class TaxCalc:
    def __init__(self, tax_list):
        self.tax = tax_list

    def get_max_tax(self):
        return max(self.tax)

    def get_min_tax(self):
        return min(self.tax)


def getinput(promt):
    while True:

        n = input(promt).strip()

        if n != '':

            # this try catch handle the type error situation
            try:
                n = eval(n, {}, {})
            except:
                print("{} is not valid! Please enter Numbers: ".format(n))

            else:
                if type(n) is int or type(n) is float:
                    return n
                else:
                    print(n, " is not a number!")
        else:
            print("Missing Input!")