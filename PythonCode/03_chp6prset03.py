text = input("enter your text\n")


if("make a lot of money" in text):
    spam = True

elif("buy now" in text):
    spam = True

elif("click this" in text):
    spam = True

elif("subscribe now" in text):
    spam = True 

else:
    spam = False

if(spam):
    print("this text is spam")

else:
    print("this text is not spam")   