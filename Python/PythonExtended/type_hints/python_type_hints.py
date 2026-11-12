
class UserService:
    # id_ : int  == parameter hint
    # -> str : return hint
    def get(self, id_ : int) -> str:
        return f"User {id_}"

print(UserService.get.__annotations__)
print(UserService.get.__annotations__["id_"])
print(UserService.get.__annotations__["return"])



def get_min_age_for_voting() -> int:
    return 18

def get_salary() -> float:
    return 180000.0

def is_active() -> bool:
    return True

def get_names() -> list[str]:
    return ["Suman", "Rahul"]

def get_users() -> dict[str,str]:
    return {"Suman": "BLR", "Rahul": "MUM"}


# BAD EXAMPLES
def get_user_by_id(id:int) -> str:
    return 100


def get_salary_wrong() -> float:
    return "50000"

def add(a: int, b: int) -> int:
    return a + b
  
print(get_user_by_id(5))

print(add("Hello"," World"))
# print(add("Hello",8))