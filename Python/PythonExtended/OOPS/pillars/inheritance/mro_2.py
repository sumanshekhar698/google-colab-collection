
# object
#  C3 Linearization
class LeftBase:
    def who(self):
        return "LeftBase"

#  C3 Linearization
class RightBase:
    def who(self):
        return "RightBase"

class Left(LeftBase):
    def who(self):
        return "Left  --> " + super().who()


class Right(RightBase):
    def who(self):
        return "Right  --> " + super().who()


class Both(Left, Right):
    def who(self):
        return "Both  --> " + super().who()


print(Both().who())
print(Both.__mro__)
print("MRO:", [c.__name__ for c in Both.__mro__])