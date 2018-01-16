
'''
To do:

- Make float work as input for amount
- Offer user options in a better way
- Validate user input
- Immediately convert user input of measurement to variable name
- Maybe have ingredient as class or more complex dict, with each measurement within it
'''

originalmeasurement = input('What measurement are you using? (cup/tbsp/tsp) ').lower()
originalquantity = int(input('Input amount: '))
ingredient = input('What ingredient is it? (flour/sugar/butter/honey/salt/bakingpowder) ')

def convertToMetric(originalquantity, ingredient, originalmeasurement):

	# The following is one measure of the variable name to grams
	# e.g. 1 cup of flour == 125g
	# Vales taken from https://www.leaf.tv/articles/cup-to-gram-conversions/

	ingredients = {
		"flour":{"cup":125},
		"sugar":{"cup":200},
		"butter":{"cup":227},
		"honey":{"cup":339},
		"salt":{"tbsp":18, "tsp":6},
		"bakingpowder":{"tbsp":12, "tsp":4},
	}

	newquantity = originalquantity * (ingredients[ingredient][originalmeasurement])
	metricmeasurement = "grams"

	responsedict = {"newquantity":newquantity, "ingredient":ingredient, "metricmeasurement":metricmeasurement}

	# print(originalquantity + ' ' + originalmeasurement + ' of ' + ingredient + ' is the same as ' + newquantity + ' ' + metricmeasurement)
	print(responsedict)
	return responsedict

convertToMetric(originalquantity, ingredient, originalmeasurement)
