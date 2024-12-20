#В соревнованиях участвуют три команды по 6 человек. Результаты соревнований представлены в виде мест участников каждой команды (1 - 18). 
# Определить команду-победителя, вычислив количество баллов, набранное каждой командой. 
# Участнику, занявшему 1-е место, начисляется 5 баллов, 2-е - 4, 3-е - 3, 4-е - 2, 5-е - 1, остальным - 0 баллов. 
# При равенстве баллов победителем считается команда, за которую выступает участник, занявший 1-е место.

from random import *
class Member:
    def __init__(self, points, team):
        self.points=points
        self.team = team
members = []
for i in range (0, 18):
    if i < 7:
        name = "team1"
    if 6 < i < 13:
        name = "team2"
    if 12 < i :
        name = "team3"   
    members.append(Member(0, name))
for i in range (0, 1000):
    a = randint(0,17)
    b = randint(0,17)
    members[a],members[b] = members[b],members[a]
for i in range (0, 5):
    members[i].points = 5 - i

teamPoints = [0,0,0]

for member in members:
    if member.team == "team1":
        teamPoints[0] += member.points
    if member.team == "team2":
        teamPoints[1] += member.points
    if member.team == "team3":
        teamPoints[2]+= member.points
if teamPoints [0]> teamPoints[1] and teamPoints [0]> teamPoints[2]:
    print ("team1 победила")
if teamPoints [2]> teamPoints[1] and teamPoints [2]> teamPoints[0]:
    print ("team3 победила")
if teamPoints [1]> teamPoints[0] and teamPoints [1]> teamPoints[2]:
    print ("team2 победила")
if teamPoints [1] == teamPoints[0]:
    print ("{members[0].team} победила")
if teamPoints [1] == teamPoints[2]:
    print ("{members[0].team} победила")
if teamPoints [0] == teamPoints[2]:
    print ("{members[0].team} победила")




