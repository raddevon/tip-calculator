"""
Tip calculator app
"""

meal = float(raw_input('Meal cost: '))
tax = float(raw_input('Tax rate (in decimal format): '))
tip = float(raw_input('Tip rate (in decimal format): '))
tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "The base cost of your meal was ${:.2f}".format(meal)
print "You need to pay ${:.2f} for tax".format(tax_value)
print "Tipping at a rate of {:.2%}, you should leave ${:.2f} for a tip." \
    .format(tax, tip_value)
print "The grand total of your meal is ${:.2f}".format(total)
