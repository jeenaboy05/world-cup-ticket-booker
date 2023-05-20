'''
Created on Apr 23, 2022

@author: aryanjeena
'''
 
#this selectteam function is used to select a team to watch
def selectteam():
    print("Which team do you want to watch: ")
    print("1,Argentina ")
    print("2,Brazil ")
    print("3,Germany ")
    print("4,Spain ")
    print("5,Italy ")
    print("6,France ")
    print("7,USA ")
    print("8,Portugal ")
    print("9,Mexico ")
    print("10,Belgium ")
    print("11,back")
    team = int(input("Please choose your team by entering an integer from 1 to 11: "))
    if team == 11:
        selectstatus()
    elif (team>0) and (team<11):
        selectstage()
    else:
        print("Wrong Choice")
 
# this selectstage function used to select a stage
def selectstage():
    print("Which round do you want to watch: ")
    print("1,Group Stage ")
    print("2,stage of 16 ")
    print("3,Quarterfinals ")
    print("4,Semifinals ")
    print("5,Final or Third Place ")
    stage = int(input("Please choose your round by entering an integer from 1 to 5: "))
    if (stage>0) and (stage<6): 
        timing(stage)
    else: 
        print("Wrong Choice")

# this timing function used to select timing for game
def timing(stage):
    time1 = {
        1: "10:00am-12:00pm",
        2: "1:10pm-3:10pm",
        3: "4:20pm-6:20pm",
        4: "7:30pm-9:30pm"
    }
    time2 = {
        1: "10:00am-12:00pm",
        2: "1:10pm-3:10pm",
        3: "4:20pm-6:20pm",
        4: "7:30pm-9:30pm"
    }
    time3 = {
        1: "10:00am-12:00pm",
        2: "1:10pm-3:10pm",
        3: "4:20pm-6:20pm",
        4: "7:30pm-9:30pm"
    }
    time4 = {
        1: "11:00am-1:00pm",
        2: "4:00pm-6:00pm"
    }
    time5 = {
        1: "11:00am-1:00pm",
        2: "4:30pm-6:30pm"
    }
    #This stage algorithm selects the time depending on the stage, giving the user confirmation
    if stage<=4:
        print("What time is your selected game at: ")
        print(time1)
        userinputtime = input("Please select your time by entering an integer from 1 to 4:")
        selectedtime = time1[userinputtime]
        userinputtickets = int(input("How many tickets would you like to print: "))
        t = 0
        while t < userinputtickets:
            print("Printed ticket: " + str(t+1))
            if t == userinputtickets: 
               break
            t+=1
        print("Successfully Booked! Enjoy your game at "+selectedtime)

    else:
        print("What time is your selected game at: ")
        print(time1)
        userinputtime = input("Please select your time by entering an integer from 1 to 4:")
        selectedtime = time1[userinputtime]
        userinputtickets = int(input("How many tickets would you like to print: "))
        t=0
        while t< userinputtickets:
            print("Printed ticket: " + str(t+1))
            if t == userinputtickets:
                break
            t+=1
        print("Successfully Booked! Enjoy your game at "+selectedtime)

  
 

 
# this selectstatus function used to pick a level of ticket
def selectstatus():
    print("Which status level ticket do you want: ")
    print("1,VIP (Highest Level)")
    print("2,Elite")
    print("3,Prime")
    print("4,Normal (Lowest Level)")
    status = int(input("Please choose your status level by entering an integer from 1 to 4: "))
    if (status == 1) or (status==2) or (status==3) or (status==4):
        selectteam()
    else:
        print("Wrong Choice")

 
# this selectstadium function is used to select a stadium
def selectstadium():

    print("Hi welcome to the World Cup 2022 ticket booking: ")
    print("What stadium would you like to watch your game in: ")
    print("1,Lusail ")
    print("2,Al Khor ")
    print("3,Al Wakrah ")
    print("4,Al Rayyan ")
    print("5,Doha ")
    stadium = int(input("Please choose your stadium by entering an integer from 1 to 5: "))
    if (stadium == 1) or (stadium==2) or (stadium==3) or (stadium==4) or (stadium==5):
        selectstatus()
    else:
        print("Wrong Choice")
 
 
selectstadium() # This calls the function selectstadium, initiating the code


