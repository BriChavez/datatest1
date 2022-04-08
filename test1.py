
class Artist:
    def __init__(self, artist, name_id, artist_id, dob, genre):
        self.artist = artist
        self.artist_id = artist_id
        self.name_id = name_id
        self.dob = dob
        self.genre = genre
        
        print(artist)
        print(artist_id)
        print(name_id)
        print(dob)
        print(genre)

class Song:
    def __init__(self, name_id, title, length, lyrics):
        self.name_id = name_id
        self.title = title
        self.length = length
        self.lyrics = lyrics
        
        print(name_id)
        print(title)
        print(length)
        print(lyrics)

        
id_l7=id(l7)
id_l7 = f'{id_l7}'        
l7 = Artist("L7", "L7-" + id_l7, id_l7, "August 1st, 1960", "Riot Grrrls")
l7_song = Song(id_l7, "Fast and Frightening", "2:24", "Her glance hits me like lightning, I heard that girl is fast and frightening, Dirty hair and a laugh that's mean, Her neighbors call her an evil machine.")

id_badu=id(badu)
id_badu = f'{id_badu}'
badu = Band("Erykah Badu", "Erykah Badu-" + id_badu, id_badu, "Febuary 26th, 1971", "Next Lifetime", "6.30", "R&B")
badu_song = Song(id_badu, "Next Lifetime", "6:30", "Now what am I supposed to do, When I want you in my world, (Want you in my world), But how can I want you for myself, When I'm already someone's girl.")
    
id_manu = id(manu)
id_manu = f'{id_manu}'
manu = Band("Manu Chao", "Manu Chao-" + id_manu, id_manu, "June 20th, 1961", "Bongo Bong", "4:13", "Reggae")
manu_song = Song(id_manu, "Bongo Bong", "4:13", "Mama was queen of the mambo, Papa was king of the Congo, Deep down in a jungle, I started banging my first bongo, Every monkey like to be, In my place instead of me, 'Cause I'm the king of Bongo, baby, I'm the king of Bongo Bong.")
