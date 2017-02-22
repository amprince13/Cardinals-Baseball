import sys, os, re, operator, decimal
import numpy as np

if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

# Get the line on which player info is ignore all other lines
bat_string = re.compile(r"\b\w+ \w+ batted \d+ \w+ with \d+ hits\b")
name_match = re.compile(r"[A-Z]([a-z]|[A-Z])+ [A-Z]([a-z]|[A-Z)])+")
bat_match = re.compile(r"\d+")
players = []
atBats = {}
hits = {}
average = {}


f = open(filename, 'r')
lines = f.readlines()[3:]
for line in lines:
	bat_line = bat_string.match(line)
	if bat_line is not None:
		name_string = name_match.match(line)
		bat_nums = bat_match.findall(line)
		player_name = name_string.group(0)
		players.append(player_name)
		if bat_nums is not None:
			singleBat = int(bat_nums[0])
			singleHit = int(bat_nums[1])
			if player_name not in atBats.keys():
				atBats[player_name] = singleBat
				hits[player_name] = singleHit
			else:
				atBats[player_name] += singleBat
				hits[player_name] += singleHit


players = np.unique(players)
f.close()

for player in players:
	average_value = float(hits[player]) / float(atBats[player])
	average[player] = round(average_value,  3)

sorted_players = sorted(average.items(), key=operator.itemgetter(1), reverse=True)

for i in range (0, len(sorted_players)):
	print sorted_players[i][0] + ": " + str(sorted_players[i][1])
