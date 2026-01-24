
# __setitem__ lets you modify items using square brackets.

class Playlist:
    def __init__(self):
        self.lectures = []
    
    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def __len__(self, lectures):
        return len(self.lectures)

    def __getitem__(self, index):
        return self.lectures[index]

    def __setitem__(self, index, lecture):
        self.lectures[index] = lecture

my_playlist = Playlist()
my_playlist.add_lecture("LLM overview")
my_playlist.add_lecture("LLM basics")

print(my_playlist[0])

my_playlist[0] = "LLM ML"
print(my_playlist[0])

# output
# LLM overview
# LLM ML