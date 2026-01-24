
# These two work together to let you use for loops on your object.
# __iter__: Returns an iterator object (often self)
# __next__: Returns the next item, or raises StopIteration when done

class Playlist:
    def __init__(self):
        self.lectures = []

    def add_lecture(self,lecture):
        self.lectures.append(lecture)
    
    def __iter__(self):
        # Reset the counter and return self
        self.current_index = 0
        return self
    
    def __next__(self):
        # Return the next song, or stop if we're done
        if self.current_index < len(self.lectures):
            lecture = self.lectures[self.current_index]
            self.current_index += 1
            return lecture
        else:
            raise StopIteration  # Signal we're done


my_playlist = Playlist()
my_playlist.add_lecture("LLM")
my_playlist.add_lecture("ML")
my_playlist.add_lecture("DL")


for lecture in my_playlist:
    print(lecture)


# __len__() → len(obj) - How many items?
# __getitem__(index) → obj[index] - Get an item
# __setitem__(index, value) → obj[index] = value - Set an item
# __contains__(item) → item in obj - Is item inside?
# __iter__() → for x in obj - Start iteration
# __next__() → Get next item (or raise StopIteration)