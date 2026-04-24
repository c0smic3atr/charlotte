default secondAptDoor1NumberOfVisits = 0
default secondAptDoor2NumberOfVisits = 0


label second_apartment_scene:
    $ oxygen_loss = 2
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
    
    scene bg doors


    call screen secondApartmentNavigation

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
            #a "Make sure to talk to Sarah next door. She's something of an optimist"
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
            a "There's so few in town these days, people don't have the luxury of slipping through the cracks anymore."
            a "What's your deal? If you're here to tell me to keep the noise down, you can get lost"
            p "No... I've been sent to check up on the residents here. See how you're handling things"
            a "I guess that checks out."
            a "Some of us will be pretty happy to see you here"
            a "But most of us gave up on an intervention a long time ago"
            p "Intervention?"
            a "Yeah. I mean, you can't blame us for wanting out"
            p "You know that's not gonna happen..."
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
                    
                
                    $ anna_facts['fact1'] = "What do I write? Can't feel my fingers. Her body sounded heavy when it hit the floor. She didn't say much. Guess the people here are pretty hopeless. Can't say I blame them."   

                "Do nothing" if anna_facts['resolved'] == False:
                    if anna_facts['status'] != "Dead":
                        $ anna_facts['status'] = "Spared"
                    $ anna_facts['resolved']= True
                    p "..."
                    $ trust-=5
                    $ anna_facts['fact1'] = "Disinterested, I guess. Trying to convince herself she's alright here. Mentions a low population."
        
                
                "Mark as Dead" if anna_facts['marked'] == False:
                    $ anna_facts['marked']= True
                    $ trust += 10

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

            show character2two at center
          
            p "Hello, my name is-"
            s "Oh my gosh"
            s "I knew it!"
            p "What?"
            s "So many people have given up hope, but not me"
            s "I knew you'd come and save us."
            p "I think you have the wrong idea"
            p "I'm just here for a... welfare check."
            s "Oh. For me?"
            p "For everyone here."
            s "Oh, well"
            s "I was still right. That you cared"
            s "Comin' back at all"
            s "It proves it."
            p "I'm sorry, do we know each other?"
            s "No, but I know you."
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
            p "Right, well, thank you for your time."
            s "Wait!"
            s "Uh, how long are you planning to stay?"
            p "Why?"
            s "Well, I was wondering if you could do me a favor?"
            s "Check up on my mom? I haven't seen her in forever, she's just across town."
            p "How come you can't go yourself?"
            s "Well, we were told to stay inside. Quarentine, right?"
            thought "Oh, yeah"
            p "Fine."
            s "Thank you! She should be somewhere in the offices, I think. Her name's Iris."
            s "She's such a worrier, please tell her I'm ok."
            p "Right. Thank you for your time."
            s "Yeah! Thanks!"

            #Discovered Sarah!!
            $ sarah_facts['portrait'] = "sarah portrait"
            $ sarah_facts['name'] = "Sarah Han"
            if sarah_facts ['status'] == "Undiscovered":
                $ sarah_facts['fact1'] = "Not much, again... gonna find her mom, see if she knows anything."

            hide character2two

            # boolean (?) After first interaction with Sarah Employer will have conversation with player character which goes as follows
    if secondAptDoor2NumberOfVisits == 1:
            e "Walker." 
            thought "I didn't expect contact so soon..."
            p "Yuh- yes?"
            e "Remember when we told you to watch out for people who 'fit the profile'?"
            e "It's people like her."
            p "People like her? What do you mean?"
            p "She seems-"
            e "You'll figure it out"
            e "You're a lot of things, but incompetent ain't one of them."
            e "Dispose of her."
            e "And for the love of God, remember to mark it in your logbook."

            
            thought "Press N to Access the Logbook"
                
               
            #Goes to front doors again, in which you can click on Sarah again and now have the option to execute
            # Immediately after, the player gains access to their logbook for the first time which has tutorial information, character info, gas mask management, and employer trust management
            # From here you can interact with Sarah again and choose whether or not to kill her, and whether or not to mark her as killed in your logbook

            $ sarah_facts['status'] = "Targeted"

            jump second_apartment_scene
            


    elif secondAptDoor2NumberOfVisits == 2:
        show character2two at center
        s "Oh, hey! You're back!"
        s "Do you need something?"
        jump sarah_menu
        

                
    elif sarah_facts['resolved'] == False:

        
        jump sarah_menu
        
    else:
        
        thought "What am I doing?"
        jump second_apartment_scene

    
label sarah_menu:

#  default somethingToDo = True
# if sarah_facts['status'] != "Dead" or sarah_facts['marked'] == False:
    #    $ somethingToDo = True
    #else:
    #   $ somethingToDo = False

if sarah_facts['resolved']== False:

    menu:
            "Kill Her" if sarah_facts['status'] !="Dead":
                s "Um... is there something wrong??"

                $ sarah_facts ['status'] = "Dead"
                $ sarah_facts['portrait'] = "sarah dead"
                hide character2two
                show character2mono at center
                pause 3.0
                $ sarah_facts['fact1']= "So, what, I'm just supposed to write something? Something... she didn't say anything that matters. Is that why you had me kill her? Why'd I kill her. My head hurts."
                
                $ trust-=10

                #jump bossConversation
            
            "Do Nothing" if sarah_facts['resolved']== False:
                if sarah_facts['status']!="Dead":
                    $ sarah_facts['status'] = "Spared"
                $ sarah_facts['resolved'] = True
                if sarah_facts['status']!= "Dead":
                    p "Um... no. Never mind."
                
                if sarah_facts['status']!="Dead":
                    $ sarah_facts['fact1'] = "Sounded easier in my head. How do you look someone in the eyes and just... She seemed fine. She's fine, and it's fine. I'm gonna look for her mom, see if she knows anything."
                
                $ trust-=10

                #jump bossConversation

            "Mark as Dead" if sarah_facts['marked']== False:
                $ sarah_facts['marked']= True
                $ trust +=10

    if sarah_facts['status']== "Dead" and sarah_facts['marked']== True:
            $ sarah_facts['resolved']= True
    
    
elif sarah_facts['resolved']== True:
    thought "What am I doing?"
    jump second_apartment_scene
   
    




label bossConversation:
    #scene black
    #"boss"
    if sarah_facts['status'] == "Dead":
        
        # increase trust
        $ trust += 10
    elif sarah_facts['status'] == "Hiding":
        
        $ trust += 2
    elif sarah_facts['status'] == "Spared":
        
        $ trust -= 20
    jump second_apartment_scene
    

screen secondApartmentNavigation():
    # back to the first apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

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