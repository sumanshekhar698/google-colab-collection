
import pickle
from pathlib import Path


with open("data_obj.pkl","rb") as f:
    obj_recovered = pickle.load(f)
print(obj_recovered)


print("file size:", Path("data_obj.pkl").stat())
print("file size:", Path("data_obj.pkl").stat().st_size, "bytes")