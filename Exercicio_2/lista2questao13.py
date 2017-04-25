#!/usr/bin/env python
# -*- coding: utf-8 -*-

def nasc(x):
	aniversario = 2013 - x
	return aniversario

def main():
	data = int(input("Entre com o ano de nascimento: "))
	idade = nasc(data)
	print("Em 31/12/2013 você terá ",idade,"anos")

main()