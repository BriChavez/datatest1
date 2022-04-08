# import random
# id_l7 = random.sample(range(1,100),1)
# print(id_l7)
# id_badu= random.sample(range(1,100),1)
# # print(id_badu)
# import random
# id_l7 = random.sample(range(1,100),1)
# # id_l7 = id_l7 = rng


# l7= "band"
# id_l7=id(l7)
# id_l7 = f'{id_l7}'
# type(id_l7)

# name_id="".join(str(id_l7))

class Band:
    def __init__(self, artist, name_id, artist_id, dob, title, length, genre):
        self.artist = artist
        self.artist_id = artist_id
        self.name_id = name_id
        self.dob = dob
        self.title = title
        self.author = length
        self.genre = genre
        
        print(artist)
        print(artist_id)
        print(name_id)
        print(dob)
        print(title)
        print(length)
        print(genre)
        
id_l7=id(l7)
id_l7 = f'{id_l7}'        
l7 = Band("L7", "L7-" + id_l7, id_l7, "August 1st, 1960", "Fast and Frightening", "2.24", "Riot Grrrls")

id_badu=id(badu)
id_badu = f'{id_badu}'
badu = Band("Erykah Badu", "Erykah Badu-" + id_badu, id_badu, "Febuary 26th, 1971", "Next Lifetime", "6.30", "R&B")

id_manu = id(manu)
id_manu = f'{id_manu}'
manu = Band("Manu Chao", "Manu Chao-" + id_manu, id_manu, "June 20th, 1961", "Bongo Bong", "4:13", "Reggae")










