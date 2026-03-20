class GameStats:
    """Track statistics"""
    def __init__(self,ai_game):
        """Initialize statistics"""
        self.settings=ai_game.settings
        self.reset_settings()

    def reset_settings(self):
        """Stats to be reset"""
        self.ships_left=self.settings.ship_limit