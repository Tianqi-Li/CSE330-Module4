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


if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])
 
filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])





f = open(filename, "r")
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

Player = collections.namedtuple('Player', 'score name')
leaderboard = sorted([Player(v,k) for (k,v) in scores.items()], reverse=True)
for item in leaderboard:
	print item[1],':',"%.3f" %item[0]


f.close()