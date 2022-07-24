myDict = {
    
    "phool" : "A flower",
    "dost" : "A freind",
    "paagal" : "A neurological syndrome"


}
print("options are ", myDict.keys())
a = input("enter the hindi word\n")
# print("the meaning of your word is:", myDict[a])

print("the meaning of your word is:", myDict.get(a))



# print(myDict['dost'])
# print(myDict['phool'])