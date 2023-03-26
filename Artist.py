class Artist:
    def __init__(self, name, genre, location, portfolio, availability):
        self.name = name
        self.genre = genre
        self.location = location
        self.portfolio = portfolio
        self.availability = availability
        
class ArtistManagementSystem:
    def __init__(self):
        self.artists = []
        
    def add_artist(self, name, genre, location, portfolio, availability):
        artist = Artist(name, genre, location, portfolio, availability)
        self.artists.append(artist)
        
    def get_artists(self):
        artists_df = pd.DataFrame(columns=["Name", "Genre", "Location", "Portfolio", "Availability"])
        for artist in self.artists:
            artists_df = artists_df.append({"Name": artist.name, "Genre": artist.genre, "Location": artist.location, "Portfolio": artist.portfolio, "Availability": artist.availability}, ignore_index=True)
        return artists_df
