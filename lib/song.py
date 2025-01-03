class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, song):
        if not song.genre in cls.genres:
            cls.genres.append(song.genre)


    @classmethod
    def add_to_artists(cls, song):
        if not song.artist in cls.artists:
            cls.artists.append(song.artist)

    @classmethod
    def add_to_genre_count(cls, song):
        if cls.genre_count.get(song.genre, "None") == "None":
            cls.genre_count.update({song.genre:1})
        else:
            cls.genre_count[song.genre] += 1
    
    @classmethod
    def add_to_artist_count(cls, song):
        if cls.artist_count.get(song.artist, "None") == "None":
            cls.artist_count.update({song.artist:1})
        else:
            cls.artist_count[song.artist] += 1

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self)
        self.add_to_artists(self)
        self.add_to_genre_count(self)
        self.add_to_artist_count(self)