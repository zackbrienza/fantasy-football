import nflgame


# Prints message with rushing statistics for a player
'''def rush_msg (*rush_stats):
    att, yds, tds = rush_stats
    msg = '%d att, %d yds, %d TDs'
    print (msg % (att, yds, tds))'''


def all_rb_weekly_stats (year):

  d={}
  msg = '%s %d carries for %d yards and %d TDs'

  for week in range (17):
    games = nflgame.games(int(year), int(week+1))
    players = nflgame.combine_game_stats(games)
    for p in players.rushing().sort('rushing_yds'):
      if str(p) in d:
        d[str(p)].append ((p.rushing_att, p.rushing_yds, p.rushing_tds))
      else:
        d[str(p)] = [(p.rushing_att, p.rushing_yds, p.rushing_tds)]


  for p,stats in d.items():
    print p+':'
    for elt in stats:
      att = elt[0]
      yds = elt[1]
      tds = elt[2]
      msg = '%d att, %d yds, %d TDs'
      print (msg % (att, yds, tds))
    print '\n'


# Prints message with receiving statistics for a player
def rec_msg (tars, rec, rec_yds, rec_tds):
  msg = '%d targets, %d rec, %d yds, %d TDS\n'
  print (msg % (tars, rec, rec_yds, rec_tds))


# Calculates important fantasy points for a player
def fps (rec, rush_yds, rush_tds, rec_yds, rec_tds):
  return 0.5*float(rec) + 0.1*float(rec_yds + rush_yds) + float(6 * (rush_tds+rec_tds))


# Prints a week number and a player's fantasy points for that week
def general_msg (week, fp):
  msg = ('Week %d: %.1f fantasy points')
  print (msg % (week, fp))


# Prints rushing statstics for all players in a given year
def rb_weekly_stats (year):
  d = {}
  for week in range(17):
    games = nflgame.games(int(year), int(week+1))
    players = nflgame.combine_game_stats(games)
    for p in players.rushing().sort('rushing_yds'):
      fp = 0.1*float (p.rushing_yds) + float(6 * p.rushing_tds)
      rush_msg(p.rushing_att, p.rushing_yds, p.rushing_tds)


# Finds the weekly stats of a flex player (only includes rushing/receiving stats) from a whole year
def flex_stats (name, year):
  player = nflgame.find(name)
  for week in range(17):
    games = nflgame.games(int(year), int(week+1))
    players = nflgame.combine_game_stats(games)
    for p in players:
      if str(name) == str(p):
        fp = fps(p.receiving_rec, p.rushing_yds, p.rushing_tds, p.receiving_yds, p.receiving_tds)
        general_msg(int(week+1), float(fp))
        rush_msg(p.rushing_att, p.rushing_yds, p.rushing_tds)
        rec_msg(p.receiving_tar, p.receiving_rec, p.receiving_yds, p.receiving_tds)


# Finds stats of a player in a given week
def week_stats (player, year, week):
  games = nflgame.games(year, week)
  players = nflgame.combine_game_stats(games)
  for p in players.rushing().sort("rushing_yds"):
    if p.name == player:
      rush_msg(p.rushing_att, p.rushing_yds, p.rushing_tds)


# Finds the top players of a given week and returns those players' stats from the previous week
# Week cannot be week 1
def prev_week_stats (year, week):
  games = nflgame.games(int(year), int(week))
  players = nflgame.combine_game_stats(games)
  for p in players.rushing().sort("rushing_yds").limit(10):
    return (week_stats(str(p.name), int(year), int(week-1)))


# Automatic function call to prev_week_stats
'''year = raw_input('Year: ')
name = raw_input('Name: ')
if __name__ == '__main__':
  flex_stats(name, year)'''
