print("Login Playing")
print("=======================")
user_name=input("To begin, enter a username: ")
password=input("Now enter a password: ")
quitval = str()
while quitval!="quit":
    quitval = input("Do you want to lock? ")
    if quitval=="lock":
        uname=str()
        pword=str()
        trips=0
        while(uname!=user_name or pword!= password):
            if trips==0:
                print(">>>AHA!")
            else:
                print(" Try Again!")
            trips = trips+1
            print("  Trip # ",trips)
            print("You must enter the username and password")
            uname = input("Username: ")
            pword = input("Password: ")
            if(uname==user_name and pword==password):
                print("Very good!")
        
