#coding=utf-8
#create a mapping of state to abbreviation
states = {
	"Oregon": "OR",
	"Florida": "FL",
	"Califonia": "CA",
	"New York": "NY",
	"Michigan": "MI"
}

#create a basic set of states and some cities in them
cities = {
	"CA": "San Francisco",
	"MI": "Detroit",
	"FL": "Jacksonville"
}

#add some more cities
cities["NY"] = "New York City"
cities["OR"] = "Portland"

#print out some cities
print("-"*10)
print("NY State has:", cities["NY"])
print("OR state has:", cities["OR"])

#print some states
print("-"*10)
print("Michigan's abbreviation is:", states["Michigan"])
print("Florida's abbreviation is:", states["Florida"])

#do it by using state then cities dict
print("-"*10)
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Florida"]])

#print every state abbreviation
print("-"*10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
	
#print every city in state
print("-"*10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city of {city}")
	
#now do both at the same time
print("-"*10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
	print(f"{state} has the city of {cities[abbrev]}")
	
print("-"*10)
#safely get a abbreviation by state that might not be there
state = states.get("Texas")
if not state:
	print ("sorry, no Taxas.")

#get a city with a default values
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")