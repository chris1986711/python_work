### **Exercise 2**

##Define a class called `Songs`, it will show the lyrics of a song.
##Its `__init__()` method should have two arguments:`self`anf `lyrics`.`lyrics`is a list. 
##Inside your class create a method called `sing_me_a_song`that prints each element of `lyrics`on his own line. 
##Define a varible:


##happy_bday = Song(["May god bless you, ",
                  # "Have a sunshine on you,",
                  # "Happy Birthday to you !"])



#Call the `sing_me_song`mehod on this variable.

class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_baby = Song(["May god bless you,","Have a sunshine on you,","Happy Brithday to you!"])

print (happy_baby.sing_me_a_song())

#none是從哪來的？？？