define x = Character("Aster")
default timesTalkedtoAster = 0

label eleventh_apartment_scene:
    scene bg officeone
    call screen firstOffice



   

label OfficeConversation:
    show character1office
    if timesTalkedtoAster == 0:
    
        $ timesTalkedtoAster += 1
        $ aster_facts['portrait'] = "aster portrait"
        $ aster_facts['name'] = "Aster Han"

        if anna_facts['status']== "Dead" or sarah_facts['status']== "Dead" or rick_facts['status']=="Dead" or lydia_facts['status']== "Dead" or orion_facts['status']== "Dead":
            p "Um, hello?"
            x "Jane, is that you?"
            p "No, it's not."
            x "I figured as much"
            x "Been waitin' a while for you."
            p "Waiting for what?"
            x "Don't kid yourself, Jane."
            x "You started all this..."
            x "Guess it's been so long, you've forgotten as well."
            p "..."
            p "You know what?"
            p "I'm getting pretty sick of you people wasting my time."
            p "Can I- can I be blunt?"
            p "It's like every time I turn a corner in this godforsaken place"
            p "Things change, I don't even know how to explain it."
            p "Either my watch is broken or- or something is going on here that's just beyond me."
            p "I used to work security, I don't know what I'm doing here"
            p "So just..."
            p "Tell me"
            p "Something"
            p "Something concrete."
            x "..."
            x "I'm used to you telling me what's what, not the other way around."
            x "You people are always so bossy..."
            x "Liars and..."
            x "Liars."
            x "But I know what you do when you decide we're too far gone."
            x "Never thought I'd see the day, but"
            x "It seems you've lost your way, Jane."
            p "Yeah."
            p "Guess so."
            $ aster_facts['fact1']= "What's that saying about doing the same thing over and over and expecting a different result?"
            
            hide character1office

        else:
            p "Um, hello?"
            x "Jane? Is that you?"
            p "No, I'm not Jane. I'm agent Walker..."
            x "Hmm, I figured."
            x "You people were always liars, weren't you Jane?"
            x "Can't keep your story straight."
            p "I told you-"
            x "First, it's a worldwide phenomenon. But then you cut off the news... Get all  quiet when I ask anything about it..."
            x "Jane's never quiet. She used to be so..."
            x "But then it's just here. Just in town."
            x "How does that happen, Jane?"
            p "Um, you seem- do you need help?"
            p "Your face... are you okay?"
            x "Hmph, first time you've cared to ask"
            x "Think a nurse'd be more helpful..."
            x "You're a bit late."
            p "Yeah, I can see that..."
            p "Do you know what's going on around here?"
            x "You're kidding. Jane, this is your doing. You tell me"
            p "I'm sorry, I can't... I don't-"
            p "I'm not even-"
            p "I was barely told anything."
            x "..."
            x "Liar."
            $ aster_facts['fact1'] = "These people really are sick. Really, really sick. We need some kind of medical team here, not me. Just scribbling away on this notepad isn't dong anything. Don't you people know that? She said some weird stuff about the disease, and the news, and... I don't know."
            
        hide character1office
    #$ aster_facts['portrait'] = "aster portrait"
    #$ aster_facts ['name'] = "Aster Carroll"
    #if aster_facts['status']= "undiscovered":
        #$ aster_facts['fact1'] == "These people really are sick..."
    #if aster_facts['status']= "Dead":
        #$ aster_facts ['fact1']== "Just because they're sick doesn't mean they deserve to die. This is insane."

    elif timesTalkedtoAster == 1 and aster_facts['status']!= "Dead":
        show character1office at left
        
        x "You don't have anything to say that I want to hear."
        hide character1office
        $ timesTalkedtoAster += 1
        
if aster_facts['resolved']== True and timesTalkedtoAster:
    thought "I've got to get going."
    jump eleventh_apartment_scene
        
        
    #else:
        #thought "..."      
    
    jump aster_menu

    
    jump eleventh_apartment_scene

label aster_menu:
    if aster_facts['resolved']== False:

        menu:
                    "Kill Her" if aster_facts['status'] != "Dead":
                        $ aster_facts['status'] = "Dead"
                        $ aster_facts['portrait'] = "aster dead"
                        hide character1office
                        show character6mono
                        pause 3.0
                        hide character6mono
                        $ trust -=10
                        $ aster_facts['fact1'] = "These people really are sick... if you know they're in this state, why aren't we helping them? Can we help them?"
                    "Keep Doing Nothing" if aster_facts['resolved']== False:
                        if aster_facts['status']!= "Dead":
                            $ aster_facts['status'] = "Spared"
                        $ aster_facts['resolved']= True

                        $ trust -=10

                    "Mark as Dead" if aster_facts['marked']== False:
                        $ aster_facts['marked']= True
                        $ trust +=10

    else:
        if aster_facts['resolved']== False:
            menu:
                    "Kill Her" if aster_facts['status']!= "Dead":
                        $ aster_facts['status'] = "Dead"
                        $ aster_facts['portrait'] = "aster dead"
                        hide character1office
                        show character6mono
                        pause 3.0
                        hide character6mono
                        $ trust +=10 
                        $ aster_facts['fact1'] = "These people really are sick..."
                    "Do Nothing" if aster_facts['resolved']== False:
                        if aster_facts['status']!="Dead":
                            $ aster_facts['status']= "Spared"
                        $ trust -=5  
                        $ aster_facts['fact1'] = "She's confused... thinks I'm someone she used to know. Guess that's one of the side-effects."
                    "Mark as Dead" if aster_facts['marked']== False:
                        $ aster_facts['marked']= True
                        $ trust+=10

    #"Menu exit"          

    if aster_facts['status']== "Dead" and aster_facts['marked']== True:
        $ aster_facts['resolved']= True

    #"Start next menu"

    menu:
        "Go back":
            jump tenth_apartment_scene
        #"this is a test":
            #jump eleventh_apartment_scene

#label twelvth_apartment_scene:
    #scene bg officeone
    
    #menu:
        #"Leave office":
            #jump tenth_apartment_scene
    


screen firstOffice():
    #Talk to violet
    frame:
        xpos 345
        ypos 50
        xsize 735- 345
        ysize 334 - 50
        background "#6527F5"

    button:
        xpos 345
        ypos 50
        xsize 735 - 345
        ysize 335 - 50
        background None
        hover_background None

        mouse "move"

        action Jump("OfficeConversation")


    # Go back
    frame:
        xpos 590
        ypos 835
        xsize 1310-590
        ysize 1055-835
        background "#6687F5"

    button:
        xpos 590
        ypos 835
        xsize 1310-590
        ysize 1055-835
        background None
        hover_background None

        mouse "move"

        action Jump("tenth_apartment_scene")