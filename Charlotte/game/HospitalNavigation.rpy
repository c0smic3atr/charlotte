define v = Character("Violet")
define m = Character("Martin")
default timesTalkedtoMartin = 0
default timesTalkedtoViolet = 0
label eigteenth_apartment_scene:
    $ oxygen_loss = 6
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen


  
    scene bg road to hospital
    call screen eigteenthApartmentNav

    "You've left the office building"
    menu: 
        "Continue toward the road":
            jump ninteenth_apartment_scene
        "Investigate blockade":
            jump twentieth_apartment_scene
        "Go back":
            jump fifteenth_apartment_scene

label twentieth_apartment_scene:
    scene bg blockade
    "Youre at the blockade"
    menu:
        "Go back":
            jump eigteenth_apartment_scene

label ninteenth_apartment_scene:
    scene bg hospitallook
    call screen enteringHospital

    "You're approaching the hospital"
    menu:
        "Enter Hospital":
            jump twentyfirst_apartment_scene
        "Go back":
            jump eigteenth_apartment_scene

label twentyfirst_apartment_scene:
    scene bg fronthos
    call screen hospitalMainRoom
    "Youre in the hospital"
    menu:
        "Enter storage room":
            jump twentysecond_apartment_scene
        "Enter operating room":
            jump twentythird_apartment_scene
        "Enter hallway":
            jump twentyfourth_apartment_scene
        "Go back":
            jump ninteenth_apartment_scene

label twentysecond_apartment_scene:
    scene bg storageroom
    "You're in the storage room"
    menu: 
        "Go back":
            jump twentyfirst_apartment_scene

label twentythird_apartment_scene:
    scene bg hosor
    "You're in the operating room"
    menu: 
        "Go back":
            jump twentyfirst_apartment_scene

label twentyfourth_apartment_scene:
    scene bg hall
    call screen hallwayNav
    "You're in the hallway"
    menu:
        "Enter left door":
            jump twentyfifth_apartment_scene
        "Enter right door":
            jump twentysixth_apartment_scene
        "Investigate door at the end of the hall":
            jump twentyseventh_apartment_scene
        "Go back":
            jump twentyfirst_apartment_scene

label twentyfifth_apartment_scene:
    scene bg hos2room
    call screen leftRoomNav
    
    #show char2hoss
    #p "Woah! Uh, I'm sorry, you scared me..."
    #m "UhhH- aGH..."
    #thought "He looks dead already..."
    #p "I wish you could tell me more about what's happening here. I guess I wasn't the first person to come check on you, was I?"
    #m "..."
    #p "Guess you won't solve a probelm if you're the one who created it, huh..."
    #p "Mullan should be sorry."
    #$ martin_facts['portrait']= "martin portrait"
    #$ martin_facts['name'] "Martin Kelly"
    #$ martin_facts['fact1']= "This is inhumane. I can't just... kill him, though. That's not how people handle this... people wouldn't have done this in the first place. Am I just your clean-up crew? Here to take out those who are left and tell you how far along everyone else is?"
    #jump martin_menu

label martinConvo:
    if timesTalkedtoMartin == 0:
        show char2hoss
        if anna_facts['status']!= "Dead" and sarah_facts['status']!= "Dead" and rick_facts['status']!= "Dead" and lydia_facts['status']!= "Dead" and orion_facts['status']!= "Dead":
            p "Woah! Uh, I'm sorry, you scared me..."
            m "UhhH- aGH..."
            thought "He looks dead already..."
            p "I wish you could tell me more about what's happening here. I guess I wasn't the first person to come check on you, was I?"
            m "..."
            p "Guess you won't solve a probelm if you're the one who created it, huh..."
            p "Mullan should be sorry."
            $ martin_facts['fact1']= "Would you call this a fate worse than death?"
            $ martin_facts['portrait']= "martin portrait"
            #$ martin_facts['name'] "Martin Kelly"
        else:
            p "Woah! Uh, I'm sorry, you scared me..."
            m "..."
            thought "He looks dead already..."
            p "Look like you've been here a while."
            p "How long has it been, anyway?"
            p "I haven't heard from Mullan in a while"
            p "Got kind of sick of hearing his voice, anyway."
            p "Voice of a killer."
            p "Guess I can't say anything, anymore..."
            p "Is that why they sent me here?"
            p "To become like them?"
            p "Get used to it?"
            p "Does it matter?"
            pause 2.0
            p "They should be sorry."
            $ martin_facts['fact1']= "Would you call this a fate worse than death?"
            $ martin_facts['portrait']= "martin portrait"
        
    $ timesTalkedtoMartin += 1
    jump martin_menu

label martin_menu:
    if martin_facts['resolved']== False:
        menu:
                "Kill Him" if martin_facts['status']!= "Dead":
                    $ martin_facts['status']= "Dead"
                    $ martin_facts['portrait']= "martin dead"
                    hide char2hoss
                    show hospital2charamonooo
                    pause 3.0
                    hide hospital2charamonooo
                    $ trust-=10
                    $ martin_facts['fact1']= "I won't leave him to rot, too. Might just be trying to prove I'm not as sick as you are."

                "Do Nothing" if martin_facts['resolved']== False:
                    if martin_facts['status']!= "Dead":
                        $ martin_facts['status']= "Spared"
                        $ martin_facts['fact1']= "This is inhumane. I can't just... kill him, though. That's not how people handle this... people wouldn't have done this in the first place. Am I just your clean-up crew? Here to take out those who are left and tell you how far along everyone else is?"
                    $ martin_facts['resolved']= True
                        
                    $ trust -=5

                "Mark as Dead" if martin_facts['marked']== False:
                    $ martin_facts['marked']= True
        
    if martin_facts['status']== "Dead" and martin_facts['marked']== True:
        $ martin_facts['resolved']= True

    if martin_facts['resolved']== True:
        p "I can't..."
        jump twentyfifth_apartment_scene

    jump twentyfifth_apartment_scene



    #pause 3.0
    #show hospital2charamono
    
    #menu:
    #    "Go back":
    #        jump twentyfourth_apartment_scene

label twentysixth_apartment_scene:
    scene bg hos2hos
    "You're in the second hospital room"
    menu:
        "Go back":
            jump twentyfourth_apartment_scene

label twentyseventh_apartment_scene:
    scene bg back room hospital
    call screen backRoomNav
    "You're in the back room"
    #show character1onehospital
    #p "Hey, are you awake?"
    #v "..."
    #p "Hmm?"
    #p "..."
    #p "I'm here-"
    #p "I'm here to..."
    #thought "To what, ask if she's feeling alright?"
    #thought "Write down her symptoms for what? Just so they know? Don't they already?"
    #pause 2.0
    #p "I'm sorry this happened."
    #p "I don't know what to do."
    #v "..."
    #p "Hah, kind of hard to tell if you fit the profile if you won't talk to me."
    #p "Is this what the sickness really does?"
    #p "Just... destroys your mind and body"
    #p "Leaves you unable to move"
    #p "Or talk..."
    #thought "Somebody should be talking care of her, not coming to-"
    #p "Put you out fo your misery..."
    #p "Isn't that what you've been saying this whole time?"
    #p "Like a dog."
    #$ violet_facts['portriat'] = "violet portrait"
    #$ violet_facts['name'] = "Violet Carlton"
    #jump violet_menu

label violetConvo:
if timesTalkedtoViolet == 0:
    show character1onehospital
    if anna_facts['status']!= "Dead" and sarah_facts['status']!= "Dead" and rick_facts['status']!= "Dead" and lydia_facts['status']!= "Dead" and orion_facts['status']!= "Dead" and martin_facts['status']!= "Dead":
        p "Hey, are you awake?"
        v "..."
        p "Hmm?"
        p "..."
        p "I'm here-"
        p "I'm here to..."
        thought "To what, ask if she's feeling alright?"
        thought "Write down her symptoms for what? Just so they know? Don't they already?"
        pause 2.0
        p "I'm sorry this happened."
        p "I don't know what to do."
        v "..."
        p "Hah, kind of hard to tell if you fit the profile if you won't talk to me."
        p "Is this what the sickness really does?"
        p "Just... destroys your mind and body"
        p "Leaves you unable to move"
        p "Or talk..."
        thought "Somebody should be talking care of her, not coming to-"
        p "Put you out fo your misery..."
        p "Isn't that what they've been saying this whole time?"
        p "Like a dog."
        $ violet_facts['portriat'] = "violet portrait"
        $ violet_facts['name'] = "Violet Carlton"
        $ timesTalkedtoViolet += 1
        jump violet_menu
    if orion_facts['status']== "Dead":
        p "Hey, are you awake?"
        v "..."
        p "Hmm?"
        p "I'm here-"
        p "I'm here to..."
        thought "To what, ask if she's feeling alright?"
        thought "Write down her symptoms... for what? Just so they know? Don't they already?"
        p "I'm sorry."
        p "You're Violet, right?"
        p "Violet Carlton?"
        p "I'm- not sure whether to be sorry or not, honestly."
        p "He wasn't gonna live long anyway..."
        p "Just a short, miserable life before he inevitably ended up like you."
        p "You can't tell me you're happy"
        p "You can't tell me that's what you would have wanted for your son."
        p "You know, once upon a time, I wanted kids."
        p "Wanted some simple life in a small town, just like you."
        p "Just... wasn't in the cards, I guess."
        p "If I had a kid, I wouldn't have wanted him to live through this."
        p "It was-"
        p "It was the right thing to do and you know it."
        p "Don't look at me like that."
        p "I just... put him out of his misery..."
        p "Hah, isn't that what they've been telling me this whole time?"
        p "Like a dog."
        $ violet_facts['portriat'] = "violet portrait"
        $ violet_facts['name'] = "Violet Carlton"
        $ timesTalkedtoViolet += 1
        jump violet_menu
    else:
        p "Hey, are you awake?"
        v "..."
        p "Hmm?"
        p "..."
        p "I'm here-"
        p "I'm here to..."
        thought "To what, ask if she's feeling alright?"
        thought "Write down her symptoms for what? Just so they know? Don't they already?"
        pause 2.0
        p "I'm sorry this happened."
        p "I can't pretend my involvement is going to help anything"
        p "Won't pretend I've helped at all since I got here..."
        p "I can't undo what Mullan and his people did all those years ago"
        p "And I can't change things now..."
        p "All I can do is pull the trigger, I guess."
        p "Put you out of your misery"
        p "Like a dog."
        $ violet_facts['portriat'] = "violet portrait"
        $ violet_facts['name'] = "Violet Carlton"
    $ timesTalkedtoViolet += 1       
    $ violet_facts['fact1']= "I'm sick of writing in this thing." 
    jump violet_menu



label violet_menu:
    if violet_facts['resolved']==  False:
        menu:
                "Do What Needs to Be Done" if violet_facts['status']!= "Dead":
                    hide character1onehospital
                    show hosonrchar
                    pause 3.0
                    hide hosonrchar
                    $ violet_facts['status']= "Dead"
                    $ violet_facts['portrait']= "violet dead"
                    $ violet_facts['fact1']= "Sometimes it's the moral thing to do, right? Was it ever a hard decision for you? Did you ever even think twice?"

                "Do nothing" if violet_facts ['resolved']== False:
                    if violet_facts['status']!= "Dead":
                        $ violet_facts['status']= "Spared"
                    $ violet_facts['resolved']= True
                    $ trust-=10
                    $ violet_facts['fact1']= "Feels like an execution. Unjust. I doubt it matters one way or another to you."
                "Mark as Dead" if violet_facts['marked']== False:
                    $ violet_facts['marked']= True
                    $ trust += 10

        if violet_facts['status']== "Dead" and violet_facts['marked']== True:
            $ violet_facts['resolved']= True
    
    elif violet_facts['resolved']== True:
        thought "I can't do this any more."
    
    jump twentyseventh_apartment_scene


    #menu:
        #"Exit the hospital":
            #jump twentyeigth_apartment_scene

        #"Go back":
            #jump twentyfourth_apartment_scene

screen eigteenthApartmentNav():
    # to blockage

    frame:
        xpos 175
        ypos 105
        xsize 415 - 175
        ysize 255 - 105
        background "#6527F5"

    button:
        xpos 175
        ypos 105
        xsize 415 - 175
        ysize 255 - 105
        background None
        hover_background None

        mouse "move"

        action Jump("twentieth_apartment_scene")

    # down the road

    frame:
        xpos 1600
        ypos 30
        xsize 1790 - 1600
        ysize 190 - 30
        background "#6527F5"

    button:
        xpos 1600
        ypos 30
        xsize 1790 - 1600
        ysize 190 - 30
        background None
        hover_background None

        mouse "move"

        action Jump("ninteenth_apartment_scene")

    #go back

    frame:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background "#6527F5"

    button:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background None
        hover_background None

        mouse "move"

        action Jump("fifteenth_apartment_scene")

screen enteringHospital():
    # enter the hospital

    frame:
        xpos 790
        ypos 430
        xsize 960 - 790
        ysize 560 - 430
        background "#6527F5"

    button:
        xpos 790
        ypos 430
        xsize 960 - 790
        ysize 560 - 430
        background None
        hover_background None

        mouse "move"

        action Jump("twentyfirst_apartment_scene")


    #go back

    frame:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background "#6527F5"

    button:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background None
        hover_background None

        mouse "move"

        action Jump("fifteenth_apartment_scene")

screen hospitalMainRoom():

    #Hallway

    frame:
        xpos 5
        ypos 180
        xsize 195 - 5
        ysize 660 - 180
        background "#6527F5"

    button:
        xpos 5
        ypos 180
        xsize 195 - 5
        ysize 660 - 180
        background None
        hover_background None

        mouse "move"

        action Jump("twentyfourth_apartment_scene")

    #Storage room

    frame:
        xpos 1425
        ypos 150
        xsize 1545 - 1425
        ysize 450 - 150
        background "#6527F5"

    button:
        xpos 1425
        ypos 150
        xsize 1545 - 1425
        ysize 450 - 150
        background None
        hover_background None

        mouse "move"

        action Jump("twentysecond_apartment_scene")

    #Operating room

    frame:
        xpos 1650
        ypos 125
        xsize 1915 - 1650
        ysize 820 - 125
        background "#6527F5"

    button:
        xpos 1650
        ypos 125
        xsize 1915 - 1650
        ysize 820 - 125
        background None
        hover_background None

        mouse "move"

        action Jump("twentythird_apartment_scene")

screen hallwayNav():
    #Left room

    frame:
        xpos 85
        ypos 20
        xsize 305 - 85
        ysize 800 - 20
        background "#6527F5"

    button:
        xpos 85
        ypos 20
        xsize 305 - 85
        ysize 800 - 20
        background None
        hover_background None

        mouse "move"

        action Jump("twentyfifth_apartment_scene")

    #Right room

    frame:
        xpos 1495
        ypos 20
        xsize 1665 - 1495
        ysize 765 - 20
        background "#6527F5"

    button:
        xpos 1495
        ypos 20
        xsize 1665 - 1495
        ysize 765 - 20
        background None
        hover_background None

        mouse "move"

        action Jump("twentysixth_apartment_scene")

    #Back room

    frame:
        xpos 700
        ypos 10
        xsize 1125 - 700
        ysize 230 - 10
        background "#6527F5"

    button:
        xpos 700
        ypos 10
        xsize 1125 - 700
        ysize 230 - 10
        background None
        hover_background None

        mouse "move"

        action Jump("twentyseventh_apartment_scene")

    #Go back

    frame:
        xpos 210
        ypos 900
        xsize 1640 - 210
        ysize 1060 - 900
        background "#6527F5"

    button:
        xpos 210
        ypos 900
        xsize 1640 - 210
        ysize 1060 - 900
        background None
        hover_background None

        mouse "move"

        action Jump("twentyfirst_apartment_scene")

screen leftRoomNav():
    #Talk with Martin

    frame:
        xpos 95
        ypos 340
        xsize 530 - 95
        ysize 1040 - 340
        background "#6527F5"

    button:
        xpos 95
        ypos 340
        xsize 530 - 95
        ysize 1040 - 340
        background None
        hover_background None

        mouse "move"

        action Jump("martinConvo")

    #Go back

    frame:
        xpos 1160
        ypos 930
        xsize 1885 - 1160
        ysize 1060 - 930
        background "#6527F5"

    button:
        xpos 1160
        ypos 930
        xsize 1885 - 1160
        ysize 1060 - 930
        background None
        hover_background None

        mouse "move"

        action Jump("twentyfourth_apartment_scene")

screen backRoomNav():
    #Talk with violet

    frame:
        xpos 45
        ypos 440
        xsize 305 - 45
        ysize 810 - 440
        background "#6527F5"

    button:
        xpos 45
        ypos 440
        xsize 305 - 45
        ysize 810 - 440
        background None
        hover_background None

        mouse "move"

        action Jump("violetConvo")

    #Exit the hospital

    frame:
        xpos 570
        ypos 305
        xsize 740 - 570
        ysize 490 - 305
        background "#6527F5"

    button:
        xpos 570
        ypos 305
        xsize 740 - 570
        ysize 490 - 305
        background None
        hover_background None

        mouse "move"

        action Jump("twentyeigth_apartment_scene")

    #Go back

    frame:
        xpos 580
        ypos 925
        xsize 1475 - 580
        ysize 1060 - 925
        background "#6527F5"

    button:
        xpos 580
        ypos 925
        xsize 1475 - 580
        ysize 1060 - 925
        background None
        hover_background None

        mouse "move"

        action Jump("twentyfourth_apartment_scene")