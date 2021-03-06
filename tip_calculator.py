import sys
from tip_calculator_as_functions import calculate_rate, calculate_meal_costs

"""
Tip calculator app
"""


def get_data_interactive():
    while True:
        try:
            meal = float(raw_input("Meal cost: "))
            tax = float(raw_input("Tax rate: "))
            tip = float(raw_input("Tip rate: "))
            break
        except ValueError:
            print "All values should be numeric"
    return meal, tax, tip


def main():
    try:
        meal = float(sys.argv[1])
        tax = float(sys.argv[2])
        tip = float(sys.argv[3])
    except ValueError:
        print "All values should be numeric."
        meal, tax, tip = get_data_interactive()
    except IndexError:
        print "You didn't provide all the values needed for the calculation."
        meal, tax, tip = get_data_interactive()

    tax_value = meal * tax
    meal_with_tax = meal + tax_value
    tip_value = meal_with_tax * tip
    total = meal_with_tax + tip_value

    print "The base cost of your meal was ${0:.2f}".format(meal)
    print "You need to pay ${0:.2f} for tax".format(tax_value)
    print "Tipping at a rate of {0:.2%}, you should leave ${1:.2f} for a tip.".format(tax, tip_value)
    print "The grand total of your meal is ${0:.2f}".format(total)

if __name__ == "__main__":
    main()
