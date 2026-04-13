define l = Character ("Lydia")
define o = Character ("Orion")

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

    "At apartments2"
    menu: 
        "Talk":
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
        "Go back":
            call screen seventhApartmentNav
    menu: 
        "Talk to the other door":
            show chara5kid at center
            if timesTalkedtoOrion == 0:
                o "What's up?"
                thought "There's kids here... of course there are."
                p "I'm, um, agent Walker and-"
                o "Agent! Woah!"
                p "Hah, yeah"
                p "I'm here to see if you're doing alright?"
                o "Wait, so do you, like, work for the government or something?"
                p "Uh..."
                o "Have you ever killed someone?"

            if anna_facts['status']=="Dead" or sarah_facts['status']=="Dead" or rick_facts['status']=="Dead" or nolan_facts['status']=="Dead" or lydia_facts['status']=="Dead":
                thought "I'm gonna be sick..."
            else: 
                    p "..."
                    o "It's ok, my dad used to have a total secret job too. Couldn't tell me anything about it."
                    p "Your dad?"
                    o "Yeah, he's gone now though..."
                    o "Most people are."
                    p "Where'd they go?"
                    thought "Finally getting some information."
                    o "Dunno..."
                    thought "Never mind I guess."
                    p "..."
                    p "Um, cool shirt."
                    p "Crabs."
                    thought "What am I doing?"
                    o "Thanks... Wait, so you're here to make sure everybody's ok?"
                    p "Yes."
                    o "Even my mom?"
                    p "Of course."
                    o "Well, she's not ok. She's in the hospital."
                    p "Okay."
                    p "I mean, uh"
                    p "What happened?"
                    o "She's all sick... couldn't stay home. Are you going to save her?"
                    thought "Christ, kid."
                    thought "At least I have some kind of lead; someone's sick."
                    p "If I see her, I'll find a way to help her. What's her name?"
                    o "She's Violet- Oh, I'm Orion! What's your name?"
                    p "I'm agent Walker."
                    o "Yeah, I know that. I mean your real name!"
                    p "..."
                    p "Wait, if both your parents- are you all alone here?"
                    o "Oh, nah. Lydia takes care of me. Of everyone in the apartments, really."
                    o "Well, whenever she can..."
                    o "She's really nice."
            if lydia_facts['status']=="Dead"
                    thought "Oh my God"
                    thought "I'm gonna throw up"
                    thought "What am I-"
                    thought "Ugh..."
            else:
                    p "I see... Thanks for telling me, kid"
                    o "Yeah, no problem!"
                    p "Stay safe."
                    o "You too!"
            
            if timesTalkedtoOrion == 1:


    menu:
        "Go back":
            jump fifth_apartment_scene

label eigth_apartment_scene:
    scene bg park
    call screen eigthApartmentNav

    "At park"
    menu:
        "Go back":
            jump fifth_apartment_scene


label ninth_apartment_scene:
    scene bg blocked area
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