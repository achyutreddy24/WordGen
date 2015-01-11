import random

class Pattern(object):

    def __init__(self, pattern):
        self.consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        self.vowels = ['a','e','i','o','u']
        self.pattern_dict = {'C': self.consonants, 'V': self.vowels}
        self.pattern = pattern
        
                
    def create_word(self):
        string_list = []
        for letter in self.pattern:
            if letter not in self.pattern_dict:
                raise TypeError("Error: pattern is incorrectly formatted")
            string_list.append(random.choice(self.pattern_dict[letter]))
        return "".join(string_list)
                
x = Pattern('CVCV')
print(x.create_word())
print(x.pattern_dict)