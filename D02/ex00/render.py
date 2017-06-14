import sys
import os
#import re

def remtemp(filename):
	
	file, file_extension = os.path.splitext(filename)#verifie qu'il y a un template en splitant le nom du fichier
	if file_extension == ".template":
		t = filename, "settings.py"
		#t.write_html(file+".html")
	else:
		print("Le fichier {0} devrait avoir pour extension .template".format(filename))

	params = {} #je cree un dico

	try:
		with open("settings.py", 'r') as infile:#j'ouvre en lecture le fichier 
			for line in infile:#je parcours le fichier
				tmp_name = line.split('=')#je separe les deux membres du dico par le =
				params[tmp_name[0].strip(' ')] = tmp_name[1].strip('\n \"')#j'enleve les caracteres parasites

	except FileNotFoundError as e:
		print('le fichier {} n\'existe pas.'.format(e.filename))
		exit(1)
	except PermissionError as e:
		print('Droits de lecture absent sur le fichier{}'.format(e.filename))
		exit(2)
    
	fd = open("file.html", "w")


	with open(filename, 'r') as infile:
		try:
			for line in infile:
				for cle in params:
					line = line.replace("{"+cle+"}",params[cle])
				fd.write(line)

		except FileNotFoundError as e:
			print('le fichier {} n\'existe pas.'.format(e.filename))
			exit(1)
		except PermissionError as e:
			print('Droits de lecture absent sur le fichier{}'.format(e.filename))
			exit(2)

if __name__ == '__main__' :
	if len(sys.argv) == 2:
		remtemp(sys.argv[1])