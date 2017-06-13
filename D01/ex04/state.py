import sys

def ville(val):
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

	for ab, cap in capital_cities.items():
		if cap == val:
			for state, abb in states.items():
				if ab == abb:
					print(state)
					return		
	print("Unknown city")

if __name__ == '__main__' :
	if len(sys.argv) == 2:
		ville(sys.argv[1])