class Soldier:

    soldier = 'Ryan'

class Guns(Soldier):

    def __init__(self):
        self.weopon = 'AK 47'
        self.s_weopon = 'pistol'
        self.ammo_1 = 30
        self.ammo_2 = 7

class Act_of_Shooting(Guns):

    def shoot_AK47(self):
        times = int(input('Сколько раз выстрельнуть из АК 47?'))
        for bullet in range(times):
            print('тиги-тигитиш')
            self.ammo_1 -= 1
            while self.ammo_1 == 0:
                print('Нету патронов, нужно перезаридить АК 47!')
                self.reload_AK47()

    def shoot_pistol(self):
        times = int(input('Сколько раз выстрельнуть из пистолета?'))
        for bullet in range(times):
            print('тиги-тигитиш')
            self.ammo_2 -= 1
            while self.ammo_2 == 0:
                print('Нету патронов, нужно перезаридить пистолет!')
                self.reload_pistol()

    def reload_AK47(self):
        print('Перезарижаю АК47!!!')
        self.ammo_1 = 30

    def reload_pistol(self):
        print('Перезарижаю пистолет!!!')
        self.ammo_2 = 7

trial = Act_of_Shooting()
trial.shoot_AK47()
trial.shoot_pistol()