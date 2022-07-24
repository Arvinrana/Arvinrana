sub1 = int(input("enter the marks1: "))
sub2 = int(input("enter the marks2: "))
sub3 = int(input("enter the marks3: "))
sub4 = int(input("enter the marks4: "))

if (sub1<33 or sub2<33 or sub3<33 or sub4<33):
    print("you are fail due to low marks one of the subject under 33%")

elif(sub1+sub2+sub3+sub4)/4 <40:
    print("you are fail")  

else:
    print("you are passed")

# this querry is solved...    please do practise . 