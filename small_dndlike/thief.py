import random
random.seed()
class CThief : 
    _m_life = 23
    _m_mana = 12
    _m_initiative = 6

    def get_life(self) :
        return self._m_life


    def set_life(self, value) :
        self._m_life = value

    def get_mana(self) :
        return self._m_mana
    
    def set_mana(self, value) :
        self._m_mana = value

    def get_initiative(self) :
        return self._m_initiative

    def set_initiative(self, value) :
        self._m_initiative = value

    def ability1(self) :
        self.set_mana(self, self.get_mana(self)-2)
        d1 = random.randint(1,7)
        d2 = random.randint(1,7)
        return d1 + d2

    def albility2(self) :
        self.set_mana(self, self.get_mana(self)-1)
        d1 = random.randint(1,6)
        return d1

    def ability_screen() :
        print("01 : fireball")
        print("01 : lightinig-strike")






