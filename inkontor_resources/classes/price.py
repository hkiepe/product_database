from math import ceil

class PriceGls:

    def __init__(self, country, to05kg, to10kg, to15kg, to25kg, to30kg, to40kg, duration):
        self.country = country
        self.to05kg = ceil((to05kg * 1.105 + 0.87) / 4.5547)
        self.to10kg = ceil((to10kg * 1.105 + 0.87) / 4.5547)
        self.to15kg = ceil((to15kg * 1.105 + 0.87) / 4.5547)
        self.to25kg = ceil((to25kg * 1.105 + 0.87) / 4.5547)
        self.to30kg = ceil((to30kg * 1.105 + 0.87) / 4.5547)
        self.to40kg = ceil((to40kg * 1.105 + 0.87) / 4.5547)
        self.duration = duration
