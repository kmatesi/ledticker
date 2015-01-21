import elementtree.ElementTree as ET
import datetime

class DatedGame:
    '''
    classdocs
    '''
    league = None
    start_time = None
    home_team = None
    home_score = None
    away_team = None
    away_score = None
    game_status = None
    clock = None
    clock_state = None

    def __init__(self,league, game_str):
        self.league = league
        game_tree = ET.XML(game_str)
        away_tree = game_tree.find('visiting-team')
        home_tree = game_tree.find('home-team')
        gamestate_tree = game_tree.find('gamestate')
        
        self.start_time = datetime.datetime.strftime((datetime.datetime.strptime(gamestate_tree.get('gametime'), '%I:%M %p') - datetime.timedelta(hours=1)),'%I:%M %p')
        self.home_team = home_tree.get('alias').strip('#1234567890 ')
        self.home_score = home_tree.get('score').rstrip()
        self.away_team = away_tree.get('alias').strip('#1234567890 ')
        self.away_score = away_tree.get('score').rstrip()
        self.game_status = gamestate_tree.get('status').rstrip()
        self.clock = gamestate_tree.get('display_status1')
        self.clock_state = gamestate_tree.get('display_status2')
        
class GolfMatch:
    
    league = None
    tournament_name = None
    golfer_name = None
    score = None
    standing = None
    tournament_progress = None
    display_status2 = None
    current_hole = None
    round_status = None
    tee_time = None
    
    def __init__(self,league,golfer):
        self.league = league
        self.golfer_name = golfer.find('golfer-one').get('alias')[3:]
        self.score = golfer.find('golfer-one').get('score')
        self.standing = golfer.find('golfer-one').get('place')
        self.tournament_progress = golfer.find('gamestate').get('display_status1')
        self.display_status2 = golfer.find('gamestate').get('display_status2')
        self.current_hole = golfer.find('gamestate').get('hole')
        self.round_status = golfer.find('gamestate').get('status')
        self.tee_time = golfer.find('gamestate').get('tee-time')

