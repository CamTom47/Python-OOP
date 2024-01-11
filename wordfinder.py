"""Word Finder: finds random words from a dictionary."""

import random;

class WordFinder:

    def __init__(self):
        input_file = open('words.txt', 'r');

        self.words = self.parse(input_file);
        
        print(f'{len(self.words)} words read');

        input_file.close();
    
    def parse(self, input_file):
        return [word.strip() for word in input_file];


    def random(self):
        return random.choice(self.words);


    
class SpecialWordFinder(WordFinder):
    def parse(self, input_file):
        return [word.strip() for word in input_file 
                    if word.strip() and not word.startswith('#')];