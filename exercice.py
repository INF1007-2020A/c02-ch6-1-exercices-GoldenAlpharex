#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(elem) for elem in numbers]

def join_integers(numbers):
	return int("".join([str(elem) for elem in numbers]))  # Big brain, à la place de créer une variable string, fait juste mettre "".whateverLaFonctionQueTuVeuxFaire

def generate_prime_numbers(limit):
	# premiers = liste vide
	premiers = []
	# nombres = liste des entiers de 2 à limite
	nombres = [i for i in range(2, limit+1)]
	# TANT QUE nombres est non vide FAIRE
	while nombres != []:
		# Ajouter à premiers le premier entier de nombres
		premiers.append(nombres[0])
		# nombres = liste des entiers de nombres non multiples du premier
		nombres = [elem for elem in nombres if elem % nombres[0] != 0]
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	# En plusieurs lignes, bonne façon de commencer avant de raccourcir ça en une seule ligne
	# result = []
	# for i in range(1, num_combinations+1):
	# 	if excluded_multiples == None:
	# 		result += [elem+str(i) for elem in strings]
	# 	elif i % excluded_multiples != 0:
	# 		result += [elem+str(i) for elem in strings]
	#
	# En deux lignes
	# result = [elem+str(i) for elem in strings for i in range(1, num_combinations+1) if excluded_multiples == None or i % excluded_multiples != 0]
	return [elem+str(i) for i in range(1, num_combinations+1) for elem in strings if excluded_multiples == None or i % excluded_multiples != 0]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
