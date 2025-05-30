class Song:
    count = 0
    genres = []
    artists = []
    _songs = []  # keeps track of all Song instances

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song._songs.append(self)

        if genre not in Song.genres:
            Song.genres.append(genre)
        if artist not in Song.artists:
            Song.artists.append(artist)

    @classmethod
    def genre_count(cls):
        genre_dict = {}
        for genre in cls.genres:
            genre_dict[genre] = 0
        for song in cls._songs:
            if song.genre in genre_dict:
                genre_dict[song.genre] += 1
        return genre_dict

    @classmethod
    def artist_count(cls):
        artist_dict = {}
        for artist in cls.artists:
            artist_dict[artist] = 0
        for song in cls._songs:
            if song.artist in artist_dict:
                artist_dict[song.artist] += 1
        return artist_dict

    @classmethod
    def _all(cls):
        return cls._songs

