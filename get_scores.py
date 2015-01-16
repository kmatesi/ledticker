import pytz
import datetime
import time
import urllib2
import json
#import os
import elementtree.ElementTree as ET
import games

### URL TO GRAB SCORES
##############################################################
URL = "http://scores.nbcsports.msnbc.com" + \
"/ticker/data/gamesMSNBC.js.asp?jsonp=true&sport=%s&period=%d"
##############################################################
def today(league):
    entries = []
    if league == 'NFL':
        period = 20
    elif league == 'GOLF':
        if time.strftime('%A') in ['Thursday','Friday','Saturday','Sunday']:
            period = 20150007
        else:
            period = 1
    else:
        period = int(datetime.datetime.now(pytz.timezone('US/Central')).strftime("%Y%m%d"))
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            f = urllib2.urlopen(URL % (league, period)) # open up the url to ge the json data
            jsonp = f.read()                            # read the json data
            f.close                                     # close the url connection
            json_str = jsonp.replace('shsMSNBCTicker.loadGamesData(','').replace(');','')
            json_parsed = json.loads(json_str)
            if league != 'GOLF':
                for game_str in json_parsed.get('games',[]):
                        entries.append(games.DatedGame(league,game_str))
            else:
                for game_str in json_parsed.get('games',[]):
                    game_tree = ET.XML(game_str) 
                    golfers = []
                    golfers = game_tree.findall('ticker-entry')
                    for player in golfers:
                        match = games.GolfMatch(league,player)
                        match.tournament_name = game_tree.get('name')
                        entries.append(match)
        except Exception, e:    # catch any exceptions
            print e             # print the error that occurred
            time.sleep(4)       # sleep before trying again (if within the att
            continue            
        break
    
    return entries
#############################################################
def get_game_text(game):
    lines = []
    
    if game.__class__.__name__ == "DatedGame":
        if "In-Progress" in game.game_status or "Final" in game.game_status:
            lines = [
                    "%s:%s %s:%s" % (game.away_teamy, game.away_score, \
                            game.home_team, game.home_score),
                    ]
            if "In-Progress" in game.game_status:
                lines += ["%s %s (%s)" % \
                        (game.clock, game.clock_state, game.league)]
            else:
                lines += ["%s (%s)" % (game.clock, game.league)]
        elif "Pre-Game" in game.game_status:
            lines = [
                    "%s v. %s" % (game.away_team, game.home_team),
                    "%s (%s)" % (game.start_time, game.league)
                    ]
        elif "Postponed" in game.game_status:
            if game.home_score and game.away_score:
                lines = [
                        "%s:%s %s:%s" % (game.away_team, game.away_score, \
                                game.home_team, game.home_score),
                        "%s (%s)" % (game.clock, game.league)
                        ]
            else:
                lines = [
                        "%s v. %s" % (game.away_team, game.home_team),
                        "%s (%s)" % (game.clock, game.league)
                        ]
        elif "Suspended" in game.game_status:
            if game.home_score and game.away_score:
                lines = [
                        "%s:%s %s:%s" % (game.away_team, game.away_score, \
                                game.home_team, game.home_score),
                        "%s (%s)" % (game.clock_state, game.league)
                        ]
            else:
                lines = [
                        "%s v. %s" % (game.away_team, game.home_team),
                        "%s (%s)" % (game.clock_state, game.league)
                        ]
    else:
        if "In-Progress" in game.round_status or "Round Over" in game.round_status:
            lines = [
                    "%s:%s (%s %s)" % (game.standing, game.golfer_name, game.score, game.tournament_progress),
                    "%s" % (game.tournament_name)
                    ]
    
    return lines
#############################################################
def main():
    game_list = []
    for league in ['NFL', 'MLB', 'NBA', 'NHL', 'CBK', 'CFB', 'GOLF', 'EPL']:
        entries = today(league)
        for entry in entries:
            game_list.append(entry)
    
    lines = []
    for game in game_list:
        print get_game_text(game)
        lines.append(get_game_text(game))
    
    return lines
#############################################################
if __name__ == "__main__":
    main()