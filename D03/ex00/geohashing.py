import sys
import antigravity

def Traitement(lat, lon, reste):
	antigravity.geohash(lat, lon, reste.encode())

if __name__ == '__main__':
	
	try:
		lat = float(sys.argv[1]) #verif lattitude
	except ValueError:
		print("Parametre 1 : mauvais format")
		exit(1)

	try:
		lon = float(sys.argv[2]) #verif longitude
	except ValueError:
		print("Parametre 2 : mauvais format")
		exit(2)

	try:
		dj = float(sys.argv[4]) #dernier indice dow a la date
		inStr = sys.argv[3] + '-' + str(dj) #concatenation de la date et de l'indice
	except ValueError:
	   	print("Parametre 4 : mauvais format")
	   	exit(3)
	   	
	Traitement(lat, lon, inStr) #renvoie les coordonnees d'un point