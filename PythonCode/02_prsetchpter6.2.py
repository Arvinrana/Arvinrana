sub1 = int(input("enter 1st subject marks\n:"))
sub2 = int(input("enter 2nd subject marks\n:"))
sub3 = int(input("enter 3rd subject marks\n:"))
sub4 = int(input("enter 4th subject marks\n:"))

if(sub1<33 or sub2<33 or sub3<33 or sub4<33):
    print("you are fail due to low marks")

elif(sub1+sub2+sub3+sub4)/4 < 40 :
    print("you are fail  because total percentage is less than 40")

else:
    print("congrats! you are passed")

