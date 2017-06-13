import sys

def cap(val):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}

	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	if val in states: ## si arg est un etat
		cc=capital_cities[states[val]] 
		print(cc)
	else:
		print("Unknown state")

if __name__ == '__main__' :
	if len(sys.argv) == 2:
		cap(sys.argv[1])