from pathlib import Path
path_obj = Path("C:/Users/suman/Downloads/code/G Collab/google-colab-collection/.gitignore")
print(path_obj)
print(type(path_obj))


# path = "C:\Users\suman\Downloads\code\G Collab\google-colab-collection\.gitignore"
# path = "C:\\Users\\suman\\Downloads\\code\\G Collab\\google-colab-collection\\.gitignore"
# path = "C:/Users/suman/Downloads/code/G Collab/google-colab-collection/.gitignore"
# path = r"C:\Users\suman\Downloads\code\G Collab\google-colab-collection\.gitignore"


# print(path_obj.read_text())

with open(path_obj) as f:
    print(f.read())