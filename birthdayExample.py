# Gabriel Solomon, 2020

import json

#
# this is a relative path to the .json data file
# you can also use a "full" or "absolute path" to the file
# windows and mac paths are different.  You should google and youttube to learn about paths if you are
# not familiar with them.  They are important fundamental computer concepts.
#
# this is a full windows path, note the forward slashes "/" used in python
# pathToFile = "E:/Users/jerome/GitHub/evc-cit134a-python/birthday/birthday.json"
#
# mac (which is built on linux) and linux paths are like this: "a/b/c/d/e/f.json"
#

# relative path
pathToFile = "./birthday.json"


# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)


# read the whole json file into a variable
birthdayList = json.load(jsonFile)

# create an empty dictionary
birthdayDictionary = {}

# loop json list of data and put each name and birthday into a dictionary
for elem in birthdayList:

    # fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]

    print("name = " + name)
    print("birthday = " + birthday)

    birthdayDictionary[name] = birthday


# to print a value in the dictionary by giving it a string with the name as the key
print("Carlie Miller's birthday is: " + birthdayDictionary["Carlie Miller"])

# to get user input as a function

def lookUp():
    print("name = " + name)
    print("birthday = " + birthdayDictionary[name]) 
   

name = input("Enter a name (type q to quit):")

for x in name:
    if name == "q":
        print("Quitting program")
        quit
        break
    else:
        lookUp()
        name = input("Enter a name (type q to quit):")
   


    

