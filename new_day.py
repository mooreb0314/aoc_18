from shutil import copyfile
import sys, os

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
