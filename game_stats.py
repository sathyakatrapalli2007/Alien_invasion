class GameStats:
    """Track statistics"""
    def __init__(self,ai_game):
        """Initialize statistics"""
        self.settings=ai_game.settings
        self.high_score=0
        self.reset_settings()

    def reset_settings(self):
        """Stats to be reset"""
        self.ships_left=self.settings.ship_limit-1
        self.score=0
        self.level=1
        self.bullet_count=0
        self.hits=0

        #reset current stats
        self.current_stats=[]
        self.shots_last_taken=0
        self.current_game_data={}
    
   


