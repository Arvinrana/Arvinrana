

letter = '''Dear <|NAME|>,
GREETINGS FROM WER COMPANY. I AM HAPPY TO TELL YOU ABOUT YOUR SELECTION.   
You are selected!
KOIMOI
05-05-2020
Date: <|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>",date)
print(letter)
