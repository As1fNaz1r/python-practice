# __bytes__ is called when you use bytes(obj). This is less common but useful for serialization.

class Message:
    def __init__(self,text):
        self.text = text

    def __bytes__(self):
        # Convert to bytes using UTF-8 encoding
        return self.text.encode('utf-8')
    def __str__(self):
        return self.text
        
msg = Message("Hello")
print(msg)
print(bytes(msg))
print(str(msg))
print(len(bytes(msg)))
# output
# Hello
# b'Hello'
# Hello
# 5
