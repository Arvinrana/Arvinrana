def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()


this = ("       Arvin is good       ")
n = remove_and_split(this, "Arvin")
print(n)

# def method is understood . please do it again


# another method to do 
# print(this)
# print(this.strip())