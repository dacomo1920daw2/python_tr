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
	print "La hipotenusa és: %.3f" % (hip)
	print "L'angle és: %.3f graus" % (ang)
	return
#
# PROGRAMA PRINCIPAL
a = input("Catet oposat a: ")
b = input("Costat adjacent b: ")
tr(a,b)
