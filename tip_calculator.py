from optparse import OptionParser

"""
Tip calculator app
"""

parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal", help="The cost of the meal")
parser.add_option("-t", "--tax", dest="tax",
                  help="The tax rate as a decimal value")
parser.add_option("-p", "--tip", dest="tip",
                  help="The tip rate as a decimal value")

(options, args) = parser.parse_args()

meal = float(options.meal)
tax = float(options.tax)
tip = float(options.tip)

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "The base cost of your meal was $%.2f" % meal
print "You need to pay $%.2f for tax" % tax_value
print "Tipping at a rate of %s%%, you should leave $%.2f for a tip." \
    % (tax * 100, tip_value)
print "The grand total of your meal is $%.2f" % total
