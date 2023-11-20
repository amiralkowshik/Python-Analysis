
#Assignment 5(part 2)
#Amir AL KOWSHIK
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


	# get the % of population that has been vaccinated in the selected
	input_country = input("Which country would you like data for? ").upper()
	for key in final_dictionary:
		if input_country == key.upper(): 
			input_country_value = "{} has vaccinated {}% of their population.".format(input_country, final_dictionary[key])
		else:
			input_country_value = "There is no data for the country {}.".format(input_country)

	# get the % of population that has been vaccinated worldwide
	total_value = 0.0
	key_counter = 0
	for key in final_dictionary:
		key_counter += 1 
		total_value += float(final_dictionary[key])

	worldwide_percentage = total_value / key_counter

	# get the country with the highest and lowest
	value_list = []
	maximum_value = 0
	minimum_value = 0

	for key in final_dictionary:
		value_list.append(final_dictionary[key])
		maximum_value = max(value_list)
		minimum_value = min(value_list)
		
	for key in final_dictionary:

		if final_dictionary[key] == maximum_value:
			maximum_value_country = key
		if final_dictionary[key] == minimum_value:
			minimum_value_country = key

# printing out all the results
print(input_country_value)
print("Worldwide average: {:.1f}%".format(float(worldwide_percentage)))
print("Country with lowest percentage is {} with {}%.".format(minimum_value_country, minimum_value))
print("Country with highest percentage is {} with {}%.".format(maximum_value_country, maximum_value))
