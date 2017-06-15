from local_lib.path import Path

def dossier():
	d = Path('/Users/xmillero/python/d03/D03/ex01/dossier')
	d.mkdir_p()

def fichier():
	f = Path('/Users/xmillero/python/d03/D03/ex01/dossier/fichier')
	f.touch()

def EcrireLireAfficher():
	f = Path('/Users/xmillero/python/d03/D03/ex01/dossier/fichier')
	f.open()
	f.write_text("Comme vous pouvez le constater,\nJ'ai réussi l'exercice !\nMais avant de me donner tous les points, il faut vérifier qu'il y a bien la version de pip, le fichier log, la local_lib, le dossier et le fichier dedans avec ce message...")
	
	print(f.text()) 
	
if __name__ == '__main__':
	dossier()
	fichier()
	EcrireLireAfficher()