text = input("enter the text\n")
if ("buy lottery to get prize" in text):
    spam = True

elif ("click this" in text):
    spam = True

elif (" subscribe us" in text):
    spam = True

else:
    spam = False    

if (spam):
    print("this is spam")
else:
    print("this is not spam")    

    # question solved 