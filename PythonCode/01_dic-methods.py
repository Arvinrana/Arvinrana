MyDict = {
    "Arvin" : "A Coder",
    "Marks" : [1, 2, 3,],
    "anotherdict" : {'Arvin': 'guitarist'},
     1: 3
}

# dictionary methods 
print(MyDict.keys())
print(MyDict.values())
print(MyDict.items())
print(MyDict)
updateDict = {
    "rana" : "freind",
    "hardik" : "mate",
    "class" : "college",
    "Arvin" : "guitarist"
}
#  upodate the dic. by adding key value from updatedict
MyDict.update(updateDict)
print(MyDict)

print(MyDict.get("Arvin2")) # returns none as arvin2 is not present in the dict.
print(MyDict["Arvin2"])  # throws an error as Arvin2 is not present in the dict.

# {} this column is use for dictionary etc .