define l = Character ("Lydia")
default timesTalkedtoLydia =0
default timesTalkedtoOrion = 0
define o = Character ("Orion")

label sixth_apartment_scene:
    
    $ contamination_level = 1
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
        p "Hello, I'm agent Walker, I'm here to-"
        #"At apartments2"
        #menu: 
            #"Talk":
                #show chara4colorr at left
                
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
                l "Just makes you look a little weird's all."
                p "Thanks for the note..."
                l "So what's with it?"
                thought "What's with your persistence?"
                
                p "I was sent to check up on you residents, because, you know..."
                p "We're, uh, worried. About the disease."
                p "Spreading further, that is."
                l "Oh, you're here for that?"
                p "Yeah, there was the whole quarentine thing put in place so-"
                l "You should do us all a favor and get lost. Probably doing yourself a favor in the process."
                l "We haven't been fooled by your bullshit."
                if anna_facts['status']!= "Dead" and sarah_facts['status']!= "Dead" and rick_facts['status']!= "Dead":
                    thought "What's her problem? I haven't pulled anything."
                p "..."
                p "Are you alright?"
                p "You look pretty roughed up."
                l "..."
                l "'S nothing..."
                l "But I'm being serious when I tell 'ya"
                l "Get out of here."
                l "I know what you being here means, and it's not goin' end well for anybody."
                $ timesTalkedtoLydia +=1
                $ lydia_facts['fact1'] = "I was kinda condescending, but she deserved it. Wouldn't tell me anything, total waste of time... is everybody gonna be like this? All cryptic and shit?"

            elif timesTalkedtoLydia == 1:
                show character1apt
                l "Look, I can't say anything for anybody else, but I've come to accept things as they are."
                l "Your involvement is going to do nothing but cause us problems. So get out."

                jump lydia_menu

            elif lydia_facts['resolved'] == False:
                jump lydia_menu     

            else: 
                thought "I need to leave..."

        #if lydia_facts['status']== "Dead": and anna_facts['status']=="Spared" and sarah_facts['status']=="Spared" and rick_facts['status']=="Spared":
            #$ lydia_facts['fact1']= "She looked young. How old was she? Did she even fit the profile?"

        #if lydia_facts['status']== "Dead":
            #$ lydia_facts['fact1']= "She looked young. How old was she? Did she even fit the profile?"

        #if lydia_facts['status']== "Spared":
            #$ lydia_facts['fact1']= "I was kinda condescending, but she deserved it. Wouldn't tell me anything, total waste of time... is everybody gonna be like this? All cryptic and shit?"



                


    #Discovered Lydia!!
            $ lydia_facts['portrait'] = "lydia portrait"
            $ lydia_facts['name'] = "Lydia Qualley"

            jump seventh_apartment_scene

            label lydia_menu:
            if lydia_facts['resolved']== False:

                menu: 
                        "Kill her" if lydia_facts['status']!="Dead":
                            $ lydia_facts ['status'] = "Dead"
                            $ lydia_facts['portrait'] = "lydia dead"
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
                            $ lydia_facts['fact1']= "I was kinda condescending, but she deserved it. Wouldn't tell me anything... total waste of time. Is everybody gonna be like this? All cryptic and shit?"

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
        o "Woah, cool gas mask!"
        p "Uh, I'm, um, agent Walker and -"
        o "Agent! No way!"
        p "Hah, yeah. I'm here to-"
        o "Are you, like, some kind of spy?"
        o "Do you work for the government or something?"
        p "Or something..."
        o "Woah... So have you ever killed someone?"
        
        if anna_facts['status']== "Dead" or sarah_facts['status']=="Dead" or rick_facts['status']=="Dead" or lydia_facts['status']=="Dead":
            thought "My head hurts..."
        
        p "..."
        o "It's okay, I get it. My dad used to have a super secret job too, couldn't tell me anything about it."
        p "Your dad?"
        o "Yeah, he was awesome, but he's gone now..."
        o "Most people are."
        p "Where'd they go?"
        o "Dunno... different places."
        o "Like Heaven, I guess. Or they were taken, or just ran away."
        p "..."
        thought "Taken away? What's he mean by that?"
        thought "I kinda doubt he even know..."
        thought "Poor kid's whole mood changed."
        p "Um"
        p "Cool shirt."
        p "Crabs."
        thought "What am I doing?"
        o "Thanks... Wait, actually I know where one person went. My mom."
        o "She's in the hospital."
        p "Hospital's a good place to be, all things considering."
        p "What happened?"
        o "She got all sick... long time ago. Couldn't stay home."
        o "Are you gonna go save her?"
        thought "Christ, kid. Didn't come here to be Superman."
        p "If I see her, I'll try to help."
        o "Really? Her name's Violet Carlton- Oh, I'm Orion! What's your name?"
        p "I told you, I'm agent Walker-"
        o "Yeah, yeah, I know that. I mean your real name!"
        p "Um..."
        p "Wait, if both your parents- are you all alone here?"
        o "Oh, nah. Lydia next door takes care of me. Of everyone in the apartments, really."
        o "Whenever she can..."
        o "She's really nice."
        if lydia_facts['status']=="Dead":
            thought "Nice... wouldn't call her nice..."
            thought "What do I know?"
            thought "Never got the chance to really find out."
        
        p "I see... thanks for telling me, kid."
        o "Yeah!"
        p "Uh. stay safe."
        $ orion_facts['portrait'] = "orion portrait"
        $ orion_facts['name'] = "Orion Carlton"  
        $ orion_facts['fact1'] = "Little kid, all alone. Said some people have run away, which means it could be spreading already. Gonna look for his mom, I guess. I feel like an errand boy."


        $ timesTalkedtoOrion +=1
        jump seventh_apartment_scene

    elif timesTalkedtoOrion==1:
                show character2apt
                $ timesTalkedtoOrion +=1
                o "Hmm? You're back?"
                p "Yeah, I was wondering... about Lydia?"
                o "Oh, well my mom used to babysit her when she was young, and they kinda became friends."
                o "So when Lydia had her baby when I was little, my mom and I were around a lot, to help."
                o "Then my mom got sick..."
                o "So I wanted to help her, but her boyfriend's got it covered"
                o "I guess..."
                o "That's what he tells me anyway."
                o "I don't think he's very good at it, though."
                p "Right... thanks kid."
                jump orion_menu

                



    #else :
        #thought "..."

    
            
label orion_menu:
    if orion_facts['resolved']== False:
        menu:
                    "Kill Him" if orion_facts['status']!="Dead":
                        o "Aren't you gonna go look for my mom?"
                        $ orion_facts['status']= "Dead"
                        $ orion_facts['portrait'] = "orion dead"
                        hide character2apt
                        show character5mono
                        pause 3.0
                        hide character5mono
                        $ trust -=10
                        if anna_facts['status']== "Dead" or sarah_facts['status']== "Dead" or rick_facts['status']== "Dead" or lydia_facts['status']== "Dead":
                            $ orion_facts['fact1']= "I used to want kids. Knew I'd never find the time, thanks to you. Don't any more."
                        else:
                            $ orion_facts['fact1'] = "Guess he fit the profile."

                    "Do Nothing" if orion_facts['resolved']== False:
                        if orion_facts['status']!="Dead":
                            $ orion_facts['status']= "Spared"
                        $ orion_facts['resolved']= True
                        $ trust -=10
                        if orion_facts['status']!="Dead":
                            $ orion_facts['fact1'] = "Little kid, all alone. Said some people have run away, which means it could be spreading already. Gonna look for his mom, I guess. I feel like an errand boy."
                        call BadChoice
                    "Mark as Dead" if orion_facts['marked']== False:
                        $ orion_facts['marked']= True
                        $ trust += 10
                        call GoodChoice
    
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