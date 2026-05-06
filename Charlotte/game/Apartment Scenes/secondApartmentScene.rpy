default secondAptDoor1NumberOfVisits = 0
default secondAptDoor2NumberOfVisits = 0


label second_apartment_scene:
    $ current_time = "12:17"
    $ contamination_level = 1
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
    
    scene bg doors

    call screen secondApartmentNavigation
   
    #call screen secondApartmentNavigation

    #menu:
        #"Knock on door 1":
            #show chara1first at left
            #a "..."
            #a "You don't look familiar"
            #a "I'd know, being there's so few people in town these days"
            #a "Not like there ever was many"
            #a "What's your deal? If you're here to tell me to keep the noise down, you can get lost"
            #p "Um, no"
            #p "I've been sent to check up on the residents here. See how you're handling... things"
            #a "Huh. I guess that checks out"
            #a "Some of us will be pretty happy to see you here"
            #a "But most of us gave up on an intervention a long time ago"
            #p "Intervention?"
            #a "Yeah. I mean, you can't blame us for wanting out"
            #p "You know we can't just let you go"
            #a "Some of us know better than others"
            #a "Make sure to talk to samantha next door. She's something of an optimist"
            #a "Seems to be handling things better than most"

            #jump second_apartment_scene

        #"Knock on door 2":
            #show chara2second at left
          
            #s "No way!"
            #s "You've finally come back..."
            #p "Huh?"
            #s "We've been waiting so long, some of us started to give up hope"
            #s "Not me though, I knew you'd come and rescue us."
            #p "I'm sorry, I think you have the wrong idea"
            #p "I'm officer Walker, I'm here to evaluate the wellbeing of y'all here."
            #s "Oh..."
            #s "Well, I was still right to trust you"
            #s "Comin' back at all"
            #s "It proves it."
            #p "I guess..."
            #p "Anyway, how have you been feeling? Any aches, nausea..."
            #p "Uh, fatigue? Anything like that?"
            #s "Oh, I dunno."
            #p "How about your neighbors?"
            #s "The only neighbor I really talk to is Anna, and she's a real stiff"
            #s "We've been neighbors for I can't remember how long, and I still barely know anything about her!"
            #p "Alright, well thank you for your time."
            #s "Wait!"
            #s "Uh"
            #s "Are you gonna stay long?"
            #p "Just as long as I have to."
            #s "Well, before you go, can you check on someone for me?"
            #s "My grandpa... He's too far away, I can't risk going to visit."
            #p "What do you mean?"
            #s "We were told to stay inside. Quarentine, ya' know?"
            #s "Can you check on him for me? His name's Huan."
    
            #p "Yeah, I'll keep my eye out."
            #s "Thank you!"



        #"Go Back":
            #jump first_apartment_scene

    #jump second_apartment_scene


label DoorOneConversation:

    $ secondAptDoor1NumberOfVisits += 1

    #door 1 stuff

    if secondAptDoor1NumberOfVisits == 1:

            show character1one at left
            a "..."
            a "You don't look familiar"
            a "There's so few people in town these days, we don't have the luxury of slipping through the cracks anymore."
            a "What's your deal? If you're here to tell me to keep the noise down, you can get lost"
            p "No... no I've been sent- My name is officer Walker. I was sent here to check up on the residents, see how you're handling things."
            a "I guess that checks out."
            a "We've been waiting a while."
            a "Some of us will be pretty happy to see you here"
            a "But most of us gave up on an intervention a long time ago"
            p "Intervention?"
            a "Yeah. I mean, you can't blame us for wanting out"
            p "You have to know that's not gonna happen..."
            a "Some of us know better than others"
            a "Got a couple of optimists around here, you should go talk to them."
            a "I'm not gonna tell you what you want to hear."
            p "And what's that?"
            a "That it all worked out, and you're forgiven."

            #Discovered Anna!!
            $ anna_facts['portrait'] = "anna portrait"
            $ anna_facts['name'] = "Anna Martina"
    
            if anna_facts ['status'] == "Undiscovered":
                $ anna_facts['fact1'] = "Disinterested, I guess. Trying to convince herself she's alright here. Mentions a low population."
           
            jump second_apartment_scene
    elif secondAptDoor1NumberOfVisits == 2:
        
        show character1one at left

        a "Come on, lady."
        a "Might not look it, but I'm a busy person."

        jump anna_menu
        
        

            



                
        jump second_apartment_scene

    else:

        jump anna_menu

        thought "She's not gonna answer..."
        jump second_apartment_scene
#if
    #$ anna_facts ['status']= "Dead"
        #$ anna_facts['fact2']= "Blabla2ndfacts"


label anna_menu:

    if anna_facts['resolved'] == False:
        menu:
                "Kill Her" if anna_facts['status']!="Dead":
                    show character1one
                    a "I told you to leave-"
                    
                    hide character1one
                    show character1mono
                    pause 3.0
                    hide character1mono
                    $ anna_facts['status'] = "Dead"
                    $ anna_facts['portrait'] = "anna dead"
                    # increase trust
                    #call GoodChoice
                
                    $ anna_facts['fact1'] = "What do I write? Can't feel my fingers. Her body sounded heavy when it hit the floor. She didn't say much. Guess the people here are pretty hopeless. Can't say I blame them."   

                "Do nothing" if anna_facts['resolved'] == False:
                    if anna_facts['status'] != "Dead":
                        $ anna_facts['status'] = "Spared"
                    $ anna_facts['resolved']= True
                    p "..."
                    $ trust-=5
                    call BadChoice
                    $ anna_facts['fact1'] = "Disinterested, I guess. Trying to convince herself she's alright here. Mentions a low population."
        
                
                "Mark as Dead" if anna_facts['marked'] == False:
                    $ anna_facts['marked']= True
                    $ trust += 10
                    call GoodChoice

        if anna_facts['status']== "Dead" and anna_facts['marked']== True:
            $ anna_facts['resolved']= True
    
    #if  anna_facts['status']== "Dead" and anna_facts['marked']== False:
        #$ anna_facts['resolved']= True


    elif anna_facts['resolved']== True:
        thought "She's not gonna answer..."
        jump second_apartment_scene

      
    jump second_apartment_scene





label DoorTwoConversation:
    $ secondAptDoor2NumberOfVisits += 1
    #door 2 stuff!
    if secondAptDoor2NumberOfVisits == 1:

            show char2apt at center
          
            p "Hello, my name is-"
            s "No way..."
            s "I knew it!"
            thought "What?"
            s "So many people have given up hope, but not me"
            s "I knew you'd come and save us."
            p "I think you have the wrong idea"
            p "I'm just here for a, um, welfare check."
            s "Oh. What, for me?"
            p "For everyone in town. I'm sure you can guess why."
            s "Oh, well..."
            s "I was still right. That you cared"
            s "Comin' back at all"
            s "It proves it."
            p "I'm sorry, do we know each other?"
            s "No, but I know you."
            s "Uh, sorry, that sounded weird"
            s "I mean, I know who you are. Who you work for."
            thought "Were the people here given warning that I was coming?"
            thought "Doesn't matter. I just need to get my notes and get out of here."
            p "Right... so how are you feeling?"
            p "Any headaches, nausea"
            p "Uh, fatigue? Maybe?"
            s "Mmm, no."
            p "Wuh- what about your neighbors? Know about them?"
            s "The only neighbor I really talk to is Anna, and she's a total stiff"
            s "We've lived next to each other for who-knows-how-long, and I still barely know anything about her!"
            thought "Guess she's that tight-lipped with everyone."
            s "I think maybe she doesn't like me... it was always hard to make friends around here."
            p "Right, well, thank you for your time."
            thought "She didn't tell me anything useful at all!"
            s "Wait!"
            s "Uh, how long are you planning to stay?"
            p "Why?"
            s "Well, I was wondering if you could do me a favor?"
            s "Check up on my sister? I haven't seen her in forever, and she's just across town, so it'd be no problem."
            p "How come you can't go yourself?"
            s "Well, we were told to stay inside. Quarentine, right?"
            thought "Oh. Yeah"
            p "Fine, sure."
            s "Thank you! She should be somewhere in the offices, I think. Her name's Aster."
            s "She's such a worrier, please tell her I'm ok."
            p "Right, I will."
            s "Thanks! Uh, good luck with your walfare checks!"

            #Discovered Samantha!!
            $ samantha_facts['portrait'] = "samantha portrait"
            $ samantha_facts['name'] = "samantha Han"
            if samantha_facts ['status'] == "Undiscovered":
                $ samantha_facts['fact1'] = "Not much... gonna find her sister, see if she knows anything."

            hide char2apt

            # boolean (?) After first interaction with samantha Employer will have conversation with player character which goes as follows
    if secondAptDoor2NumberOfVisits == 1:
            e "Walker." 
            thought "Woah, I didn't expect contact so soon..."
            p "Yuh- yes?"
            e "Remember when we told you to watch out for people who 'fit the profile'?"
            e "That's people like her."
            p "People like her? What do you mean?"
            p "She seems-"
            e "I trust you'll figure it out."
            e "You're a lot of things, but incompetent ain't one of them."
            e "You know what to do."
            e "And for the love of God, remember to mark disposals in your logbook. It's the only way we'll know if you're actually doing your job or not."

            
            thought "Press N to Access the Logbook"
                
               
            #Goes to front doors again, in which you can click on samantha again and now have the option to execute
            # Immediately after, the player gains access to their logbook for the first time which has tutorial information, character info, gas mask management, and employer trust management
            # From here you can interact with samantha again and choose whether or not to kill her, and whether or not to mark her as killed in your logbook

            $ samantha_facts['status'] = "Targeted"

            jump second_apartment_scene
            


    elif secondAptDoor2NumberOfVisits == 2:
        show char2apt at center
        s "Oh, hey! You're back!"
        s "Do you need something?"
        jump samantha_menu
        

                
    elif samantha_facts['resolved'] == False:

        
        jump samantha_menu
        
    else:
        
        thought "What am I doing?"
        jump second_apartment_scene

    
label samantha_menu:

#  default somethingToDo = True
# if samantha_facts['status'] != "Dead" or samantha_facts['marked'] == False:
    #    $ somethingToDo = True
    #else:
    #   $ somethingToDo = False

if samantha_facts['resolved']== False:

    menu:
            "Kill Her" if samantha_facts['status'] !="Dead":
                s "Um... is there something wrong??"

                $ samantha_facts ['status'] = "Dead"
                $ samantha_facts['portrait'] = "samantha dead"
                hide char2apt
                show char22mono at center
                pause 3.0
                $ samantha_facts['fact1']= "So, what, I'm just supposed to write something? Something... she didn't say anything that matters. Is that why you had me kill her? Why'd I kill her? My head hurts."
                #call GoodChoice
                $ trust-=10

                #jump bossConversation
            
            "Do Nothing" if samantha_facts['resolved']== False:
                if samantha_facts['status']!="Dead":
                    $ samantha_facts['status'] = "Spared"
                $ samantha_facts['resolved'] = True
                if samantha_facts['status']!= "Dead":
                    p "Um... no. Never mind."
                
                if samantha_facts['status']!="Dead":
                    $ samantha_facts['fact1'] = "Sounded easier in my head. How do you look someone in the eyes and just... She seemed fine. She's fine, and it's fine. I'm gonna look for her sister, see if she knows anything."
                call BadChoice
                $ trust-=10

                #jump bossConversation

            "Mark as Dead" if samantha_facts['marked']== False:
                $ samantha_facts['marked']= True
                $ trust +=10
                call GoodChoice

    if samantha_facts['status']== "Dead" and samantha_facts['marked']== True:
            $ samantha_facts['resolved']= True
    
    
elif samantha_facts['resolved']== True:
    thought "What am I doing?"
    jump second_apartment_scene
   
    




label bossConversation:
    #scene black
    #"boss"
    if samantha_facts['status'] == "Dead":
        
        # increase trust
        $ trust += 10
    elif samantha_facts['status'] == "Hiding":
        
        $ trust += 2
    elif samantha_facts['status'] == "Spared":
        
        $ trust -= 20
    jump second_apartment_scene
    

screen secondApartmentNavigation():
    #image button test
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        action Jump("first_apartment_scene")
    

    # to door 1 convo
    frame:
        xpos 440
        ypos 210
        xsize 720 - 440
        ysize 920 - 210
        background None

    button:
        xpos 440
        ypos 210
        xsize 720 - 440
        ysize 920 - 210
        background None
        hover_background None

        mouse "move"

        action Jump("DoorOneConversation")

    # to door 2 convo
    frame:
        xpos 840
        ypos 210
        xsize 1110 - 840
        ysize 920 - 210
        background None

    button:
        xpos 840
        ypos 210
        xsize 1110 - 840
        ysize 920 - 210
        background None
        hover_background None

        mouse "move"

        action Jump("DoorTwoConversation")