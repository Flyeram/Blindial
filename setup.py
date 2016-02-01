import sys
from cx_Freeze import setup, Executable
 
executables = [
        Executable("Menu.py"),
        
]
 
buildOptions = dict(
        compressed = True,
        includes = ["sys", "random", "os", "pygame"],
        path = sys.path + ["affichages_joueurs", "affichages_mediator", "de", "fct_affichage", "fct_rect", "fct_texte", "fonction_Q", "Lanceur_question", "plateau_fct", "rect_cases", "renameMusiques", "tours_de_jeu", "variables"]
)
 
setup(
	name = "test",	
	options = dict(build_exe = buildOptions),
	executables = executables
)
