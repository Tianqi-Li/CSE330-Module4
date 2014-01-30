#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import math
import collections
import sys, os





def search(name):
    for p in records:
        if p['name'] == name:
            return p

def update(name,bat,hit):
	player = search(name)
	if player is None:
		newP = {'name':name,'bats':bat,'hits':hit}
		records.append(newP)
	else:
		player['bats'] += bat
		player['hits'] += hit


filename = raw_input("Enter name of file:") + '.txt'

try:
	f = open(filename, "r")
except IOError:
        print 'cannot open', filename
else:
	records = []
	scores = {}
	line = f.readline()
	while line:
		pat = '(?P<name>[\w\s]+)\sbatted\s(?P<bats>\d)[\w\s]+with\s(?P<hits>\d)'
		result = re.match(pat,line)
		if result:
			name = result.group('name')
			bat = int(result.group('bats'))
			hit = int(result.group('hits'))
			#print 'Match found: ', name, bat, hit
			update(name,bat,hit)
		line = f.readline()



	for p in records:
		avg = round(float(p['hits']) / p['bats'],3)
		scores[p['name']] = avg
		#scores['avg'] = avg

	sorted(scores.items(), key=lambda avg:avg[1], reverse=True)

	#Player = collections.namedtuple('Player', 'score name')
	#leaderboard = sorted([Player(v,k) for (k,v) in scores.items()], reverse=True)
	for item in scores:
		#print item['name'],':',"%.3f" %item['avg']
		print item

	f.close()