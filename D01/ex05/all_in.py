import sys

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

def find_state(city):
	for ab, cap in capital_cities.items():#renvoit un couple du dictionnaire
		if cap.lower() == city.lower():
			for state, abb in states.items():
				if ab == abb:
					print(cap, "is the capital city of",state)
					return True
	return False

def find_cap(state):
	for st in states:
		if st.lower() == state.lower():
			cc=capital_cities[states[st]]
			print(cc, "is the capital of", st)
			return True
	return False

def all(val):
	val1 = val.split(',')
	print(val1)
	for n in val1:
		n_propre = n.strip(" ")
		if n_propre:
			if not find_state(n_propre):
				if not find_cap(n_propre):
					print(n_propre, "is neither a capital city nor a state")


if __name__ == '__main__' :
	if len(sys.argv) == 2:
		all(sys.argv[1])