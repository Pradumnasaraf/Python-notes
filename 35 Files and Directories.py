from pathlib import Path

#Absolute Path
# Windows: c:\Program File\Microsoft
# Linux/Mac : /user/

# Check whether the dir exists or not
path = Path("ecommerce")
print(path.exists())

path2 = Path("ecommerce1")
print(path.exists())

# Make a Dir

# makePath = Path("test")
# makePath.mkdir()

# Delete a Dir

# delPath = Path("test1")
# delPath.rmdir()

#Search all the file having particular extention or name
path3 = Path()
for file in path3.glob("*.py"):
    print(file)


