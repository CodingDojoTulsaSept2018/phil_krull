from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	# context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
		# 1)...all baseball leagues
		# 'leagues': League.objects.filter(sport__icontains = 'baseball')

		# 2)...all womens' leagues
		# 'leagues': League.objects.filter(name__icontains = 'women')

		# 3)...all leagues where sport is any type of hockey
		# 'leagues': League.objects.filter(sport__icontains='hockey')

		# 4)...all leagues where sport is something OTHER THAN football
		# 'leagues': League.objects.exclude(sport__icontains='football')

		# 5)...all leagues that call themselves "conferences"
		# 'leagues': League.objects.filter(name__icontains='conference')

		# 6)...all leagues in the Atlantic region
		# 'leagues': League.objects.filter(name__icontains = 'atlantic')

		# 7)...all teams based in Dallas
		# 'teams': Team.objects.filter(location__icontains='dallas')

		# 8)...all teams named the Raptors
		# 'teams': Team.objects.filter(team_name__icontains='raptors')

		# 9)...all teams whose location includes "City"


		# 10)...all teams whose names begin with "T"
		# 'teams': Team.objects.filter(team_name__istartswith='t')

		# 11)...all teams, ordered alphabetically by location
		# 'teams': Team.objects.all().order_by('location')

		# 12)...all teams, ordered by team name in reverse alphabetical order
		# 'teams': Team.objects.all().order_by('-location')

		# 13)...every player with last name "Cooper"


		# 14)...every player with first name "Joshua"


		# 15)...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		# 'players': Player.objects.filter(last_name = "Cooper").exclude(first_name='Joshua')

		# 16)...all players with first name "Alexander" OR first name "Wyatt"
		# 'players': Player.objects.filter(first_name = 'Alexander') | Player.objects.filter(first_name = 'Wyatt')

	# }
	context = {
		# ...all teams in the Atlantic Soccer Conference
		# 'teams': Team.objects.filter(league__name = "Atlantic Soccer Conference"),

		# ...all (current) players on the Boston Penguins
		# 'players': Player.objects.filter(curr_team__location='Boston', curr_team__team_name='Penguins')

		# ...all (current) players in the International Collegiate Baseball Conference
		# 'players': Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		'player': Player.objects.get(first_name = 'Samuel', last_name =  'Evans'),
		'league': League.objects.get(name = 'International Collegiate Baseball Conference')

		# ...all (current) players in the American Conference of Amateur Football with last name "Lopez"
		# ...all football players
		# ...all teams with a (current) player named "Sophia"
		# ...all leagues with a (current) player named "Sophia"
		# ...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
		# ...all teams, past and present, that Samuel Evans has played with
		# ...all players, past and present, with the Manitoba Tiger-Cats
		# ...all players who were formerly (but aren't currently) with the Wichita Vikings
		# ...every team that Jacob Gray played for before he joined the Oregon Colts
		# ...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		# ...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
		# ...all players and count of teams played for, sorted by the number of teams they've played for
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")