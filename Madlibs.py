"""Python Mad Libs"""
"""Mad Libs require a short story with blank spaces (asking for different types of words). Words from the player will fill in those blanks."""

# The template for the story
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Here we go!"

name = raw_input("Enter a name: ")
adjective1 = raw_input("Write the adjective: ")
adjective2 = raw_input("One more, please: ")
adjective3 = raw_input("And the last one: ")
verb = raw_input("Input the one verb: ")
noun1 = raw_input("and noun: ")
noun2 = raw_input("and one more noun, please: ")

print "This is where the story can get really fun! Input one of each of the following, please"

animal = raw_input("An animal: ")
food = raw_input("A food: ")
fruit = raw_input("A fruit: ")
superhero = raw_input("A superhero: ")
country = raw_input("A country: ")
dessert = raw_input("A dessert: ")
year = raw_input("A year: ")

print STORY % (name, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3, name, superhero, name, country, name, dessert, name, year, noun2)
