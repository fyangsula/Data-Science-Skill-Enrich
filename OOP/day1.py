class student:
    def __init__(self,name,gender,nationality):
        self.name = name
        self.gender = gender
        self.nationality = nationality
    
    def self_intro(self):
        print 'Hello Friends. My name is {}. I am from {}.'.format(self.name, self.nationality)
