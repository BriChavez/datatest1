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

id_list = [id(1),id(2), id(3), id(4), id()]

id_l7=f'{id_list[0]}'   
l7 = Artist("L7", "L7-" + id_l7, id_l7, "August 1st, 1960", "Riot Grrrls")
l7_song = Song(id_l7, "Fast and Frightening", "2:24", "Her glance hits me like lightning, I heard that girl is fast and frightening, Dirty hair and a laugh that's mean, Her neighbors call her an evil machine")

id_badu=f'{id_list[1]}'
badu = Artist("Erykah Badu", "Erykah Badu-" + id_badu, id_badu, "Febuary 26th, 1971", "R&B")
badu_song = Song(id_badu, "Next Lifetime", "6:30", "Now what am I supposed to do, When I want you in my world, (Want you in my world), But how can I want you for myself, When I'm already someone's girl")
    
id_manu=f'{id_list[2]}'
manu = Artist("Manu Chao", "Manu Chao-" + id_manu, id_manu, "June 20th, 1961", "Reggae")
manu_song = Song(id_manu, "Bongo Bong", "4:13", "Mama was queen of the mambo, Papa was king of the Congo, Deep down in a jungle, I started banging my first bongo, Every monkey like to be, In my place instead of me, 'Cause I'm the king of Bongo, baby, I'm the king of Bongo Bong")

input_id = input()


input_id = input("Enter an artist's ID to see if they are in the database")
if input_id in id_list:
    print("Your artist is listed")
else: print("No Artist is listed with that ID")

artist_id_dict = {"l7_key": [id_l7, "L7", "Fast and Frightening"],
                  "badu_key": [id_badu, "Erykah Badu", "Next Lifetime"],
                  "manu_key": [id_manu, "Manu Chao", "Bongo Bong"]}
artist_list = list(artist_id_dict.values())

artist_list_dict = {"name_key": ["L7", "Erykah Badu", "Manu Chao"],
                    "song_key": ["Fast and Frightening", "Next Lifetime", "Bongo Bong"]}

artist_song_dict = {"l7_key": ["Fast and Frightening", "Pretend We're Dead", "Worn Out"],
                    "badu_key": ["Next Lifetime", "Tyrone", "Appletree"],
                    "manu_key": ["Bongo Bong"], ["Me Gusta Tu"], ["Rumba in Barcelona"]}
song_input = input("enter a song")
artist_input = input("enter a artist")
if artist_input in artist_list_dict['name_key'] and song_input in artist_list_dict['song_key']:
    print ("yay")
else:
    print{"try again"}

add_artist = input("Would you like to add an artist to this list?")
if add_artist == "yes":
    class New_Artist:
        def __init__(self, inputed_name, inputed_song):
            self.inputed_name = inputed_name
            self.inputed_song = inputed_song
            return self.inputed_name + '-' + self.inputed_song
        @classmethod
        def get_user_input(self):
            inputed_name = input('Enter an artists name: ')
            inputed_song = input('Enter a song name by this artist')
            print(inputed_name, inputed_song)
    new_artist = New_Artist.get_user_input()

else:
    print("That's okay, i hope you found what you're looking for")