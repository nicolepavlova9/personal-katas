class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours: int = 0

    def play(self, game: str, hours: int) -> str:
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"

    def buy_game(self, game: str) -> str:
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        return f"{game} is already in your library"

    def status(self) -> str:
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
