# import random
# id_l7 = random.sample(range(1,100),1)
# print(id_l7)
# id_badu= random.sample(range(1,100),1)
# print(id_badu)
import random
# id_l7 = random.sample(range(1,100),1)
# # id_l7 = id_l7 = rng


l7= "band"
id_l7=id(l7)
id_l7 = f'{id_l7}'
type(id_l7)

# name_id="".join(str(id_l7))

class Band:
    def __init__(self, artist, name_id, artist_id, title, length, genre):
        self.artist = artist
        self.artist_id = artist_id
        self.name_id = name_id
        self.title = title
        self.author = length
        self.genre = genre
        
        print(artist)
        print(artist_id)
        print(name_id)
        print(title)
        print(length)
        print(genre)
        
l7 = Band("L7", "L7-" + id_l7, id_l7, "Fast and Frightening", "2.24", "Riot Grrrls")
id_l7=id(l7)
id_l7 = f'{id_l7}'

badu = Band("Erykah Badu", "Erykah Badu-" + id_badu, id_badu, "Next Lifetime", "6.30", "R&B")
id_badu=id(badu)
id_badu = f'{id_badu}'

manu = Band("Manu Chao", "Manu Chao-" + id_manu, id_manu, "Bongo Bong", "4:13", "Reggae")
id_manu = id(manu)
id_manu = f'{id_manu}'









