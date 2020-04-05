     ''' 
    #Users = ["test1","test2","test3","test4","test5","test6","test7","test8","test9","test10","test11","test12","test13","test14","test15","test16","test17" ] #Test data
    squadno = 1 # Defines the initial Squad number
    squadsize = 3 # Defines the number of players in a squad
    count = 0 # counter for loop
    VCL = channel_names() 
    Users = (VCL[0].members)
    random.shuffle(Users)  # shuffles the user list around to create random teams
    while (len(Users) > 0):
        print ("\nSquad "+str(squadno)) 
        
        while (count < squadsize):
            try:
                print(Users.pop())
            except:
                print('\n')
            count +=1
        else:
            squadno +=1
            count = 0
    print ("Assignments Complete Good hunting") 

        


# END Working CODE :D

        while (count != squadsize):
            print("\n" , Users.pop())
            userno = len(Users)
            count+=1
            print(userno)

        else:
            squadno+=1
            print("Squad " + str(squadno))
            '''
    
    
    #VCL = channel_names()
    #print(len(VCL[0].members))
    #print(random.shuffle(VCL[0].members))
    #print("Channels", list(bot.get_all_channels()))
    #voice_channel_list = channel_names()
    #print (len(voice_channel_list)) 
    #print (voice_channel_list)  
    