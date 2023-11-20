#Assignment5 (part 2)
#Amir Al Kowshik
#Data analysis
#22 Feb. '21

import csv

with open('vaccinations.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	
	# save the csv
	saved_csv = []
	for row in csv_reader:
		saved_csv.append(row)

	# get a list of all countries from the saved csv file
	all_countries = []
	for row in saved_csv:	
		all_countries.append(row['location'])

	# get a set of all countries (set contains only one instance of each item)
	all_countries = set(all_countries)

	final_dictionary = {}

	for country in all_countries:
		# in each country, looping over all rows about that country
		percentages = []
		for row in saved_csv:
			if row['location'] == country and row['total_vaccinations_per_hundred'] != "" and float(row['total_vaccinations_per_hundred']) != 0.0:

				# when we are in a row of the specific country, get the percentage
				percentage = (float(row['total_vaccinations_per_hundred']))
				final_dictionary[country.upper()] = "{:.1f}".format(percentage)

	print(final_dictionary)
