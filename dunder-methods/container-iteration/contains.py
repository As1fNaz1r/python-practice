# __contains__ is what gets called when you use the in keyword.

class Playlist:
    def __init__(self):
        self.lectures = []

    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def __contains__(self, lecture):
        return lecture in self.lectures

    
my_playlist = Playlist()
my_playlist.add_lecture("LLM")
my_playlist.add_lecture("ML")

print("LLM" in my_playlist)
print("LL" in my_playlist)

# output
# True
# False