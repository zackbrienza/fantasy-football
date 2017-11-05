import nflgame

def rb_weekly_stats (year):
  d={}
  for week in range (17):
    games = nflgame.games(int(year), int(week+1))
    players = nflgame.combine_game_stats(games)
    for p in players.rushing().sort('rushing_yds'):
      if str(p) in d:
        d[str(p)].append ((p.rushing_att, p.rushing_yds, p.rushing_tds))
      else:
        d[str(p)] = [((p.rushing_att, p.rushing_yds, p.rushing_tds))]
  return d
        #msg = '%s %d carries for %d yards and %d TDs'
        #print (msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))



if __name__ == '__main__':
  rb_weekly_stats ((raw_input("year: ")))