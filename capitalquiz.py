import random


# import txt file
def read_file(file_name):
	with open (file_name) as my_file:
		european_capitals = my_file.readlines()
		return european_capitals


# process into dictionary
def file_to_dictionary(country_list):
	capitals_dict = {}
	for countries in country_list:
		split_countries = countries.split(",")
		# print split_countries
		country = split_countries[0]
		capital = split_countries[1].strip()
		# print country, capital
		capitals_dict[country] = capital
	return capitals_dict


# print all capitals so the user can use correct spelling
def test_kickoff(capitals_dict):
	print "\nWelcome to the big European Capitals Quiz! Let's see how familiar you are with them.\n\nAs a hint, here are all the capitals you can choose from. Make sure your spelling is correct!\n\nType 'Exit' any time to finish the quiz and see your score.\n"
	print ", ".join(capitals_dict.values())


# function to select a random country and present to the user
def quiz(capitals_dict):
	correct_answers_list = [] 
	incorrect_answers = []
	counter = 0
	while len(capitals_dict) > 0 and counter <= 9:
		capital_asked = random.choice(capitals_dict.keys())
		correct_answer = capitals_dict.get(capital_asked)
		answer = raw_input("\nWhat is the capital of " + capital_asked + "? ")
		if answer == correct_answer:
			correct_answers_list.append(capital_asked)
			del capitals_dict[capital_asked]
			print "\nThat's correct, great job!"
		elif answer == "Exit":
			break
		else:
			incorrect_answers.append(capital_asked)
			del capitals_dict[capital_asked]
			print "\nSorry, that's not right. The correct answer is " + correct_answer + "."
		counter = counter + 1
		# print counter	
	print "\nQuiz over! You've missed", len(incorrect_answers), "countries out of", len(correct_answers_list) + len (incorrect_answers)

# How to make the test_kickoff dictionary print nicer? (remove ''s)


def main():
	file_name = "EuropeanCapitals.txt"
	country_list = 	read_file(file_name)
	capitals_dict = file_to_dictionary(country_list)
	test_kickoff(capitals_dict)
	quiz(capitals_dict)



if __name__ == '__main__':
	main()