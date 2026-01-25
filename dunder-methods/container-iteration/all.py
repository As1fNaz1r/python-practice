class SimplePlaylist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    # Get the size
    def __len__(self):
        return len(self.songs)
    
    # Access by index: playlist[0]
    def __getitem__(self, index):
        return self.songs[index]
    
    # Modify by index: playlist[0] = "New"
    def __setitem__(self, index, value):
        self.songs[index] = value
    
    # Check membership: "Song" in playlist
    def __contains__(self, song):
        return song in self.songs
    
    # Make it iterable
    def __iter__(self):
        return iter(self.songs)  # Simple way: use list's iterator

# Try everything:
playlist = SimplePlaylist()
playlist.add_song("Track 1")
playlist.add_song("Track 2")
playlist.add_song("Track 3")

print(f"Length: {len(playlist)}")           # __len__
print(f"First song: {playlist[0]}")         # __getitem__
playlist[1] = "Updated Track 2"             # __setitem__
print(f"Contains Track 1: {'Track 1' in playlist}")  # __contains__

print("\nAll songs:")
for song in playlist:                       # __iter__
    print(f"  - {song}")
