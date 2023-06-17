class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre 
        Song.count +=1
        Song.add_genre(genre)
        Song.add_artist(artist)


    @classmethod
    def add_genre(cls, genre):
        cls.genres.append(genre)
        if cls.genre_count.get(genre) != None:
            cls.genre_count[genre]+=1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_artist(cls, artist):
        cls.artists.append(artist)
        if cls.artist_count.get(artist) != None:
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist]=1

