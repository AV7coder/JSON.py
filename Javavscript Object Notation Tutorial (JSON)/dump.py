import json
name = input("Enter your name:")
age =(input("Enter your age:"))
gender = input("Enter your gender:")
myDict = {"Name":name,
          "Age":age,
          "Gender":gender}
out_file = open("data.json", "w")
json.dump(myDict, out_file, indent=6)
out_file.close()
# this how to make and save and edit json files