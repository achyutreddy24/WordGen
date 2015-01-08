class Pattern(object):

    def __init__(self, pattern):
        self.consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        self.vowels = ['a','e','i','o','u']
        self.pattern = pattern
        
        for letter in self.pattern:
            if letter != 'C' and letter != 'V':
                raise TypeError("Error: pattern is incorrectly formatted\nHere is and example pattern 'CVCVC'")
                
x = Pattern('CVCV')