#exceptional handling - try mehtod
while(True):
    print("press q to quit")

    a = int(input("enter the number"))
    if a == 'q':
        break
    try:
        if a>6:
            print("your number is greater then 7")
    except Exception as e:
        print(f"your input result in error {e}")

print("thanks for playing the game")        

# this is try method to handle the programme