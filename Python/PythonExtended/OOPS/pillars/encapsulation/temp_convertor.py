class Temperature:
    def __init__(self, celsius=0.0):
        self.celsius = celsius          # this goes THROUGH the setter below




    
    @property
    def celsius(self):
        """Read like an attribute, computed like a method."""
        print("celsius getter called")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"{value} is below absolute zero")
        print("setter called")
        self._celsius = float(value)

    @property
    def fahrenheit(self):
        """COMPUTED and read-only — there's no setter."""
        print("farhenheit called")
        return self._celsius * 9 / 5 + 32




t = Temperature(25)
print("celsius   :", t.celsius)          # looks like an attribute
print("fahrenheit:", t.fahrenheit)       # computed on access

t.celsius = 30                            # looks like assignment, runs validation
print("after set :", t.celsius, "->", t.fahrenheit)


t.celsius =100
print("after set :", t.celsius, "->", t.fahrenheit)


# t.celsius =-500
# print("after set :", t.celsius, "->", t.fahrenheit)