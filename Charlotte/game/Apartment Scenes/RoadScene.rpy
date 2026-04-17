define l = Character ("Lydia")


label sixth_apartment_scene:
    scene bg parking lot
    call screen sixthApartmentNav

    "In parking lot"
    menu:
        "Go back":
            jump fifth_apartment_scene

label seventh_apartment_scene:
    scene bg aptdoors
    call screen seventhApartmentNav

    #"At apartments2"
    #menu: 
        #"Talk":
            #show chara4colorr at left
            #p "Hello, I'm agent Walker, I'm here to-"
            #l "What's with the gas mask?"
            #p "Huh? Why?"
            #l "Just makes you look a little weird 's all."
            #p "Thanks for the note."
            #l "So what's with it?"
            #thought "What's with your persistence?"
            #Choice - tell her the truth
            #p "We're, uh, worried. About the disease."
            #p "Spreading further, that is."
            #l "Oh, you're one of them."
            #l "You should do yourself, and all of us, a favor and get lost."
            #l "We haven't been fooled by your bullshit."
            #p "..."
            #p "Are you alright?"
            #l "What?"
            #p "You look pretty roughed up."
            #l "..."
            #l "'S nothing..."
            #l "But I'm being serious when I tell 'ya"
            #l "Get out of here."

    #menu:
        #"Go back":
            #jump fifth_apartment_scene

label Door3Conversation:

    # Door 3 stuff!

    show chara4colorr at left
    p "Hello, I'm agent Walker, I'm here to-"
    l "What's with the gas mask?"
    p "Huh? Why?"
    l "Just makes you look a little weird 's all."
    p "Thanks for the note."
    l "So what's with it?"
    thought "What's with your persistence?"
    #Choice - tell her the truth
    p "We're, uh, worried. About the disease."
    p "Spreading further, that is."
    l "Oh, you're one of them."
    l "You should do yourself, and all of us, a favor and get lost."
    l "We haven't been fooled by your bullshit."
    p "..."
    p "Are you alright?"
    l "What?"
    p "You look pretty roughed up."
    l "..."
    l "'S nothing..."
    l "But I'm being serious when I tell 'ya"
    l "Get out of here."

    jump seventh_apartment_scene

label eigth_apartment_scene:
    scene bg park
    call screen eigthApartmentNav

    "At park"
    menu:
        "Go back":
            jump fifth_apartment_scene


label ninth_apartment_scene:
    scene bg blockedroad
    call screen ninthApartmentNav

    "You cannot go here"
    menu: 
        "Explore alley":
            jump tenth_apartment_scene
        "Go back":
            jump fifth_apartment_scene



screen sixthApartmentNav():
    #back to 5th apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background "#6527F5"

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")


screen seventhApartmentNav():
    #back to 5th apartment scene

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

        action Jump("fifth_apartment_scene")

    # Talk with Door 3

    frame:
        xpos 255
        ypos 220
        xsize 690 - 255
        ysize 800 - 220
        background None

    button:
        xpos 255
        ypos 220
        xsize 690 - 255
        ysize 800 - 220
        background None
        hover_background None

        mouse "move"

        action Jump("Door3Conversation")

    #Talk with Door 4 (Commented out until we get the character in)
    
    frame:
        xpos 1220
        ypos 220
        xsize 1660 - 1220
        ysize 800 - 220
        background None

    button:
        xpos 1220
        ypos 220
        xsize 1660 - 1220
        ysize 800 - 220
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")


screen eigthApartmentNav():
    #back to 5th apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background "#6527F5"

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")


screen ninthApartmentNav():

    # to the alley

    frame:
        xpos 1465
        ypos 730
        xsize 1740 - 1465
        ysize 870 - 730
        background "#e0005d88"

    button:
        xpos 1465
        ypos 730
        xsize 1740 - 1465
        ysize 870 - 730
        background None
        hover_background None

        mouse "move"

        action Jump("tenth_apartment_scene")



    #back to 5th apartment scene

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

        action Jump("fifth_apartment_scene")