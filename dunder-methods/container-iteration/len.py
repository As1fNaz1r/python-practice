
# __len__ tells Python how many items are in your container. It's what gets called when you use len(my_object).
# Key Point: __len__ should return an integer representing the number of items.

class Playlist:
    def __init__(self):
        self.lectures = []

    def add_lecture(self,lecture):
        self.lectures.append(lecture)

    def __len__(self):
        return len(self.lectures)
    

my_playlist = Playlist()

my_playlist.add_lecture("LLM overview")
my_playlist.add_lecture("LLM basics")

print(len(my_playlist))

# output 
# 2