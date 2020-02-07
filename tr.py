#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Nom del codi: tr.py"""
# Treballant amb funcions - I
#
# IMPORTS
import math # Mòdul math amb les funcions math.sqrt() i atan 
#
# FUNCIONS
#
def tr(a,b):
	hip=math.sqrt((a**2)+(b**2))
	ang=math.atan(a/b)*(180.0/math.pi)
	print "La hipotenusa és: %.2f" % (hip)
	print "L'angle és: %.2f graus" % (ang)
	area=(a*b)/2
	print "L'àrea és: %.2f" % (area)
	return
#
# PROGRAMA PRINCIPAL
a = input("Catet oposat a: ")
b = input("Costat adjacent b: ")
tr(a,b)
