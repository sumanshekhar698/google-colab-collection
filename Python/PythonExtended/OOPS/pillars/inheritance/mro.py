
# object
#  C3 Linearization
class Base:
    def who(self):
        return "Base"


class Left(Base):
    def who(self):
        return "Left  --> " + super().who()


class Right(Base):
    def who(self):
        return "Right  --> " + super().who()


class Both(Left, Right):
    def who(self):
        return "Both  --> " + super().who()


print(Both().who())
print(Both.__mro__)
print("MRO:", [c.__name__ for c in Both.__mro__])