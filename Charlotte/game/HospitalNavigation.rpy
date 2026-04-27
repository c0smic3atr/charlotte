define v = Character("Violet")
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
    scene bg front hospital
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
    scene bg operating room
    "You're in the operating room"
    menu: 
        "Go back":
            jump twentyfirst_apartment_scene

label twentyfourth_apartment_scene:
    scene bg hospital hallway
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
    scene bg hospital room two
    "Youre in the first hospital room"
    show character1onehospital
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
    p "Isn't that what you've been saying this whole time?"
    p "Like a dog."
    jump violet_menu

#no violet script yet so it crashes here!!
    label violet_menu:
    if violet_facts['resolved']==  False:
        menu:
            "Do What Needs to Be Done" if violet_facts['status']!= "Dead":
                hide character1onehospital
                show chara1hospitalmono
                pause 3.0
                hide chara1hospitalmono
                $ violet_facts['status']= "Dead"

            "Do nothing" if violet_facts ['resolved']== False:
                if violet_facts['status']!= Dead:
                    $ violet_facts['status']= "Spared"
                $ violet_facts['resolved']= True
                $ trust-=10
            "Mark as Dead" if violet_facts['marked']= False:
                $ violet_facts['marked']= True
                $ trust += 10
        if violet_facts['status']== "Dead" and violet_facts['marked']== True:
            $ violet_facts['resolved']= True
    
    elif violet_facts['resolved']== True:
        thought "I can't do this any more."


    
    menu:
        "Go back":
            jump twentyfourth_apartment_scene

label twentysixth_apartment_scene:
    scene bg hos2hos
    "You're in the second hospital room"
    menu:
        "Go back":
            jump twentyfourth_apartment_scene

label twentyseventh_apartment_scene:
    scene bg back room hospital
    "You're in the back room"
    show char2hos
    pause 3.0
    show hospital2charamono
    menu:
        "Exit the hospital":
            jump twentyeigth_apartment_scene

        "Go back":
            jump twentyfourth_apartment_scene

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

        action Jump("eigteenth_apartment_scene")

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