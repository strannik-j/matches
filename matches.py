#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  sp1.py
#  
#  Copyright 2011 Strannik-j <strannik-j.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from random import randrange
from sys import *
def __init__():
	x1 = 30
	x2 = 60
	sp = randrange(x1,x2,1)

	M = [1,]
	ch1 = 1
	while ch1 <= x2:
		ch1 += 4
		M.append(ch1)
		
	#t = 0
	while sp > 1:
		print("На столе ", sp,"спичек. Возьмите 1,2 или 3 спички")
		t = input()
		#t = int(t)
		while t not in (1,2,3,'1','2','3'):
			t = input('''
Ошибка! Возьмите 1, 2 или 3 спички
''')
		t = int(t)
		sp = int(sp)
		sp += -t
		
		if sp > 2:
			x3 = 4
		elif sp == 2:
			x3 == 3
		else:
			x3 = 2
			
		if sp in M:
			ch2 = randrange(1,x3,1)
			sp += -ch2
			if ch2 == 1:
				print("Я беру 1 спичку")
			else:
				print("Я беру ", ch2, " спички")
		else:
			ch3 = 0
			while sp not in M:
				sp +=-1
				ch3 +=1
			else:
				if ch3 == 1:
					print("Я беру 1 спичку")
				else:
					print("Я беру ", ch3, " спички") 
				
		if sp == 1:
			print("На столе 1 спичка. Я победил!")
			_more()
		elif sp == 0:
			print("Ты победил!!")
			_more()
def _more():
	q = ""
	q = str(q)
	no = ('n','N','no','NO','No','н','нет','Нет','НЕТ','Н')
	print("")
	q = input("Сыграем еще? (y/n) :")
	q = str(q)
	if q not in no:
		print('''
		
*********************
		
		''')
		__init__()
	else:
		exit

print('''
Игра СПИЧКИ
Правила просты:
На столе лежит случайное количество спичек.
Игрок и компьютер ходят по очереди. За ход можно взять 1, 2 или 3 спички.
Кто берёт последнюю, тот ПРОИГРАЛ!!!
Удачи!!!

*********************


''')
__init__()
#_more()
