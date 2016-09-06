# Copyright 2015 Demasset Gregoire Balu tristan
""" This file is part of Blindial.

    Blindial is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

	Blindial is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar. If not, see http://www.gnu.org/licenses/.
"""

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
