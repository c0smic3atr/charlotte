define l = Character ("Lydia")
default timesTalkedtoLydia =0
default timesTalkedtoOrion = 0
define o = Character ("Orion")

label sixth_apartment_scene:
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
   
    scene bg parking lot
    call screen sixthApartmentNav

    "In parking lot"
    menu:
        "Go back":
            jump fifth_apartment_scene

label seventh_apartment_scene:
    scene bg aptdoors
    call screen seventhApartmentNav
    if timesTalkedtoLydia == 0:

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

            if timesTalkedtoLydia == 0:
                # Door 3 stuff
                show character1apt at left
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
                $ timesTalkedtoLydia +=1
                $ lydia_facts['fact1'] = "I was kinda condescending, but she deserved it. Wouldn't tell me anything, total waste of time... is everybody gonna be like this? All cryptic and shit?"

            elif timesTalkedtoLydia == 1:
                show character1apt
                l "Look, I can't say anything for anybody else, but I've come to accept things as they are."
                l "Your involvement doesn't effect anything for us, so get out of here before they start effecting things for you."
                jump lydia_menu

            elif lydia_facts['resolved'] == False:
                jump lydia_menu     

            else: 
                thought "I need to get out of here..."

        #if lydia_facts['status']== "Dead": and anna_facts['status']=="Spared" and sarah_facts['status']=="Spared" and rick_facts['status']=="Spared":
            #$ lydia_facts['fact1']= "She looked young. How old was she? Did she even fit the profile?"

        #if lydia_facts['status']== "Dead":
            #$ lydia_facts['fact1']= "She looked young. How old was she? Did she even fit the profile?"

        #if lydia_facts['status']== "Spared":
            #$ lydia_facts['fact1']= "I was kinda condescending, but she deserved it. Wouldn't tell me anything, total waste of time... is everybody gonna be like this? All cryptic and shit?"



                


    #Discovered Lydia!!
    $ lydia_facts['portrait'] = "lydia portrait"
    $ lydia_facts['name'] = "Lydia"

    jump seventh_apartment_scene

    label lydia_menu:
    if lydia_facts['resolved']== False:

        menu: 
                    "Kill her" if lydia_facts['status']!="Dead":
                        $ lydia_facts ['status'] = "Dead"
                        hide character1apt
                        show character4mono at left
                        pause 3.0
                        hide character4mono
                        if anna_facts['status']== "Dead" or sarah_facts['status']== "Dead" or rick_facts['status']== "Dead":
                            $ lydia_facts['fact1'] = "Wouldn't say much. So, what, do unhelpful people deserve to die? That your profile?"
                        else:
                            $ lydia_facts['fact1'] = "She looked young. How old was she? Did she even fit the profile?"
                        
                        
                        
                        #if anna_facts['status']== "Spared" and sarah_facts['status']=="Spared" and rick_facts['status']=="Spared":
                            #$ lydia_facts['fact1']= "Oh my God, she looked young. How old was she? Did she even fit the profile?"
                        #else:
                            #$ lydia_facts['fact1'] = "Wouldn't say much. Do unhelpful people deserve to die? Is that the profile?"
                        $ trust += 10

                    "Do nothing" if lydia_facts['resolved']== False:
                        if lydia_facts['status']!="Dead":
                            $ lydia_facts ['status']= "Spared"
                        $ lydia_facts['resolved'] = True
                        $ trust -= 5
                        $ lydia_facts['fact1']= "I was kinda condescending, but she deserved it. Wouldn't tell me anything, total waste of time. Is everybody gonna be like this? All cryptic and shit?"

                    "Mark as Dead" if lydia_facts['marked']== False:
                        $ lydia_facts['marked']= True
                        $ trust +=10
    if lydia_facts['status']== "Dead" and lydia_facts['marked']== True:
            $ lydia_facts['resolved']= True
    $ timesTalkedtoLydia += 1
        

                    
    jump seventh_apartment_scene

        



label Door4Conversation:
    
    if timesTalkedtoOrion == 0:
        show character2apt
        o "What's up?"
        thought "There's kids here... of course there are."
        p "I'm, um, agent Walker and -"
        o "Agent! Woah!"
        p "Hah, yeah"
        p "I'm here to see if you're doing alright?"
        o "Wait, so do you, like, work for the government or something?"
        p "Uh, or something."
        o "So have you ever killed someone?"
        if anna_facts['status']== "Dead" or sarah_facts['status']=="Dead" or rick_facts['status']=="Dead" or lydia_facts['status']=="Dead":
            thought "I'm gonna be sick"
        else:
            p "..."
            o "It's ok, my dad used to have a total secret job too. Couldn't tell me anything about it"
            p "Your dad?"
            o "Yeah, but he's gone now though..."
            o "Most people are."
            p "Where'd they go?"
            o "Dunno..."
            p "..."
            p "Um"
            p "Cool shirt."
            p "Crabs."
            thought "What am I doing?"
            o "Thanks... Wait, so you're here to make sure everybody's okay?"
            p "Yes."
            o "Even my mom?"
            p "Of course."
            o "Well, she's not okay, she's in the hospital."
            p "Hospital's a good place to be, all things considering."
            o "Maybe, but she's been there for so long, I can't even remember..."
            p "Wuh- what happened?"
          
            o "She's all sick... couldn't stay at home. Are you going to save her?"
            thought "Christ, kid."
            p "If I see her, I'll help her somehow. What's her name?"
            o "She's Violet- oh, I'm Orion! What's your name?"
            p "It's agent Walker, I already-"
            o "No no no, you're real name."
            p "Um..."
            p "Wait, if both your parents- are you all alone?"
            o "Oh, nah. Lydia next door takes care of me. Of everyone in the apartments, really."
            o "Whenever she can..."
            o "She's really nice."
            if lydia_facts['status']=="Dead":
                thought "Oh my God"
                thought "I'm gonna throw up"
                thought "Ugh"
            else:
                p "I see, thanks for telling me, kid."
                o "Yeah, sure."
                p "Stay safe."
                o "Oh, yeah, you too."
                $ orion_facts['fact1'] = "Little kid, both is parents are gone. Doesn't deserve to live like this. His mom's sick, I'm gonna go to the hospital to find her and hopefully get some answers."


                $ timesTalkedtoOrion +=1
                jump seventh_apartment_scene

    elif timesTalkedtoOrion==1:
                show character2apt
                $ timesTalkedtoOrion +=1
                o "Hmm? You're back?"
                p "Yeah... I was wondering... about Lydia?"
                o "Well, my mom used to babysit her when she was a teenager, and they kinda became friends"
                o "So when Lydia had her baby, my mom and I were around a lot, to help out"
                o "Then my mom got sick..."
                o "I want to keep helping her, but usually her boyfriend's got it covered"
                o "I guess..."
                o "I don't think he's very good at it, though."
                p "Right... thanks kid."
                jump orion_menu

                



    #else :
        #thought "..."

    $ orion_facts['portrait'] = "orion portrait"
    $ orion_facts['name'] = "Orion"
            
label orion_menu:
    if orion_facts['resolved']== False:
        menu:
                    "Kill Him" if orion_facts['status']!="Dead":
                        o "Aren't you gonna go look for my mom?"
                        $ orion_facts['status']= "Dead"
                        hide character2apt
                        show character5mono
                        pause 3.0
                        hide character5mono
                        $ trust -=10
                        if anna_facts['status']== "Dead" or sarah_facts['status']== "Dead" or rick_facts['status']== "Dead" or lydia_facts['status']== "Dead":
                            $ orion_facts['fact1']= "I used to want kids. Knew I'd never find the time. Don't any more."
                        else:
                            $ orion_facts['fact1'] = "Guess he fit the profile."

                    "Do Nothing" if orion_facts['resolved']== False:
                        if orion_facts['status']!="Dead":
                            $ orion_facts['status']= "Spared"
                        $ orion_facts['resolved']= True
                        $ trust -=10
                        if orion_facts['status']!="Dead":
                            $ orion_facts['fact1'] = "Little kid, both is parents are gone. Doesn't deserve to live like this. His mom's sick, I'm gonna go to the hospital to find her and hopefully get some answers."

                    "Mark as Dead" if orion_facts['marked']== False:
                        $ orion_facts['marked']= True
                        $ trust += 10
    
    elif orion_facts['resolved']== True:
        "..."
        jump seventh_apartment_scene
    if orion_facts['status']== "Dead" and orion_facts['marked']== True:
            $ orion_facts['resolved']= True

    elif orion_facts['resolved']== True:
        "..."
        jump seventh_apartment_scene

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
        xpos 580
        ypos 830
        xsize 1470 - 580
        ysize 1060 - 830
        background None

    button:
        xpos 580
        ypos 830
        xsize 1470 - 580
        ysize 1060 - 830
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

        action Jump("Door4Conversation")


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