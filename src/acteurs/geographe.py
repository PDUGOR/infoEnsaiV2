from acteurs.contributeur import Contributeur
from gestion.elements_fichiers.section import Section
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire

class Geographe(Contributeur):
	def __init__(self):
		super().__init__()
		self.statut = 'g'
		
	def correction(self, contenu, section_de_texte):
		gestionnaire = Gestionnaire()
		chemin = section_de_texte.chemin
		
		if chemin[-1] == 'conventional short form' or chemin[-1] == 'conventional long form':
			input('\nVous ne pouvez pas modifier le nom du pays.\nAppuyez sur entrer pour continuer.')
		else:
			rep = input('\nVoulez vous modifier le texte (O/N) ?\n> ')
			if rep in ['o', 'O']:
				if self.verification_connexion():
					while True:
						txt_correction = input('\nEntrez le nouveau texte :\n> ')
						if len(txt_correction) > 1:
							break
						print('\nVotre texte doit contenir au moins 1 caractère\n')
						
					section_de_texte.contenu['text'] = txt_correction
					
					confirmation = input("\nConfirmation de la modification #Cela écrasera le texte initial# (O/N) ?\n> ")
					if confirmation in ["o","O"]:
						gestionnaire.update(section_de_texte)
						input('\nVotre modification a bien été enregistrée.\nAppuyez sur entrer pour continuer.')
					else :
						input("\nVotre tentative de modification n'a pas abouti.\nAppuyez sur entrer pour continuer.")
						
	def ajout_section(self, contenu, section):
		gestionnaire = Gestionnaire()
		noms_indisponibles = section.get_noms_sous_sections()
		
		if self.verification_connexion():
			while True:
				nom_section = input('\nEntrez le nom de la nouvelle section :\n> ')
				if len(nom_section) <= 1 or len(nom_section) > 50:
					input('\nLe nom de la section doit contenir entre 1 et 50 caractères.\nAppuyez sur entrer pour continuer.')
					continue
				if nom_section in noms_indisponibles:
					input("\nCe nom est déjà celui d'une section existante, veuillez en choisir un autre.\nAppuyez sur entrer pour continuer.")
					continue
				if (nom_section == 'Government') or (nom_section == 'Country name') or (nom_section == 'conventional short form') or (nom_section == 'conventional long form'):
					input('\nLa section ne peut pas porter de nom tel que Government, Country name, conventional short form ou conventional long form.\nAppuyez sur entrer pour continuer.')
					continue
				break
			
			confirmation = input('\nConfirmation de la création de la section (O/N) ?\n> ')
			if confirmation in ['o', 'O']:
				section.contenu[nom_section] = {}
				gestionnaire.update(section)
				input('\nLa nouvelle section a été ajoutée.\nAppuyez sur entrer pour continuer.')
			else :
				input("\nVotre tentative d'ajout de section n'a pas abouti.\nAppuyez sur entrer pour continuer.")
				
		return self.afficher_section(section, contenu)