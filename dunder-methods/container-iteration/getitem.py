
# __getitem__ - Accessing Items by Index
# __getitem__ lets you use square brackets [] to access items, just like with lists.
# With __getitem__, you can also use slicing: my_playlist[0:2]
class Playlist:
    def __init__(self):
        self.lectures = []

    def add_lecture(self,lecture):
        self.lectures.append(lecture)

    def __len__(self):
        return len(self.lectures)
    
    def __getitem__(self, index):
        return self.lectures[index]
    

my_playlist = Playlist()

my_playlist.add_lecture("LLM overview")
my_playlist.add_lecture("LLM basics")

print(my_playlist[0])
print(my_playlist[1])


# output
# LLM overview
# LLM basics