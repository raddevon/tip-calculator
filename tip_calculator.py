import argparse

"""
Tip calculator app
"""

parser = argparse.ArgumentParser(description="Calculate your total meal cost")

parser.add_argument("-m", "--meal", dest="meal", type=float,
                    help="The cost of the meal")
parser.add_argument("-t", "--tax", dest="tax", type=float,
                    help="The tax rate as a decimal value")
parser.add_argument("-p", "--tip", dest="tip", type=float, default=0.15,
                    help="The tip rate as a decimal value (default: 0.15)")

args = parser.parse_args()

tax_value = args.meal * args.tax
meal_with_tax = args.meal + tax_value
tip_value = meal_with_tax * args.tip
total = meal_with_tax + tip_value

print "The base cost of your meal was ${:.2f}".format(args.meal)
print "You need to pay ${:.2f} for tax".format(tax_value)
print "Tipping at a rate of {:.2%}, you should leave ${:.2f} for a tip." \
    .format(args.tax, tip_value)
print "The grand total of your meal is ${:.2f}".format(total)
