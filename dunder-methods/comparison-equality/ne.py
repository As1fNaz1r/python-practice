# Python auto-generates != as not ==. Only define it if inequality has special logic:


def __ne__(self,other):
    return not self.__eq__(other)

