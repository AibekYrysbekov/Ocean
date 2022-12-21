import random
from random import randint
class desk:
    def __init__(self, kards):
        self.kards = kards
    def razdacha(self):
        a = self.kards[randint(0, 52)]
        print(a)
        self.kards.remove(a)
    def smeshivanie(self):
        c = 0
        for i in self.kards:
            c += 1
        if c == 52:
            random.shuffle(self.kards)
            print(f'В колоде {c} карт')
            print(self.kards)
        if c != 52:
            print(f'В колоде всего лишь {c} карт')

a = desk(['2 черв','3 черв', '4 черв', '5 черв', '6 черв', '7 черв', '8 черв', '9 черв', '10 черв', 'J черв', 'Q черв',  'K черв', 'A черв', '2 бубен','3 бубен', '4 бубен', '5 бубен', '6 бубен', '7 бубен', '8 бубен', '9 бубен', '10 бубен', 'J бубен', 'Q бубен',  'K бубен', 'A бубен', '2 треф','3 треф', '4 треф', '5 треф', '6 треф', '7 треф', '8 треф', '9 треф', '10 треф', 'J треф', 'Q треф',  'K треф', 'A треф', '2 пик','3 пик', '4 пик', '5 пик', '6 пик', '7 пик', '8 пик', '9 пик', '10 пик', 'J пик', 'Q пик',  'K пик', 'A пик'])
a.razdacha()
a.smeshivanie()