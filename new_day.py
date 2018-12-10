from shutil import copyfile
import sys, os

# Example: python3 .\new_day.py day_2

if len(sys.argv) != 2:
    raise Exception("You must provide one argument.\nExample: python3 .\\new_day.py day_2")

# Create the directory
try:
    os.mkdir(sys.argv[1])
except FileExistsError:
    print("Directory " + sys.argv[1] + " already exists.")

try:
    s1 = open(sys.argv[1] + "/solution_1.py")
    s1.close()
    print("File: " + sys.argv[1] + "/solution_1.py already exists.")
except FileNotFoundError:
    copyfile("./template.py", "./" + sys.argv[1] + "/solution_1.py")
    print("Created: " + sys.argv[1] + "/solution_1.py.")

try:
    s1 = open(sys.argv[1] + "/solution_2.py")
    s1.close()
    print("File: " + sys.argv[1] + "/solution_2.py already exists.")
except FileNotFoundError:
    copyfile("./template.py", "./" + sys.argv[1] + "/solution_2.py")
    print("Created: " + sys.argv[1] + "/solution_2.py.")

try:
    f = open(sys.argv[1] + "/input.txt", "w")
    f.close()
    print("Created: " + sys.argv[1] + "/input.txt.")
except:
    print("Error creating " + sys.argv[1] + "/input.txt.")
