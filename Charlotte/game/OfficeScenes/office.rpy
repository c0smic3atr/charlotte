define x = Character("Aster")
default timesTalkedtoAster = 0

label eleventh_apartment_scene:
    scene bg officeone
    show chara6a at left
if timesTalkedtoAster == 0:
    
    $ timesTalkedtoAster += 1

    if anna_facts['status']== "Dead" or sarah_facts['status']== "Dead" or rick_facts['status']=="Dead":
        p "Um, hello?"
        x "Jane, is that you?"
        p "No, it's not."
        x "I figured as much"
        x "Been waitin' a while for you."
        p "Waiting for what?"
        x "Don't kid yourself, Jane."
        x "You started all this..."
        x "Guess it's ben so long, you've forgotten as well."
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
        hide chara6a

    else:
        p "Um, hello?"
        x "Jane? Is that you?"
        p "No, I'm not Jane. I'm agent Walker."
        x "Hmm, I figured."
        x "You people were always liars, weren't you Jane?"
        x "Can't keep your story straight."
        p "I told you, I'm not Jane."
        p "You seem- do you need help? Are you ok?"
        x "Hmph, first time you've cared to ask"
        x "You're a bit late."
        p "Yeah, I can see that..."
        p "Do you know what's going on around here?"
        x "You're kidding. Jane, this is your doing. You tell me"
        p "I'm sorry, I can't... I don't-"
        p "I'm not even-"
        p "I was barely told anything."
        x "..."
        x "Liar."
        $ timesTalkedtoAster +=1
        hide chara6a
#$ aster_facts['portrait'] = "aster portrait"
    #$ aster_facts ['name'] = "Aster Carroll"
    #if aster_facts['status']= "undiscovered":
        #$ aster_facts['fact1'] == "These people really are sick..."
    #if aster_facts['status']= "Dead":
        #$ aster_facts ['fact1']== "Just because they're sick doesn't mean they deserve to die. This is insane."

    if timesTalkedtoAster == 1:
        show chara6a at left
        x "You don't have anything to say that I want to hear."
        if anna_facts ['status']== "Spared" and sarah_facts ['status']== "Spared" and rick_facts ['status']== "Spared":
            menu:
                "Kill Her":
                    #$ aster_facts['status'] = "Dead"
                    hide chara6a
                    show chara6monoa at left
                    pause 3.0
                    hide chara6monoa
                    $ trust +=10
                "Keep Doing Nothing":
                    $ trust -=10
        else:
            menu:
                "Kill Her":
                    #$ aster_facts['status'] = "Dead"
                    hide chara6a
                    show chara6monoa at left
                    pause 3.0
                    hide chara6monoa
                    $ trust +=10 
                "Do Nothing":
                    $ trust -=5  




    call screen firstOffice

 



    menu:
        "Go inside office":
            jump twelvth_apartment_scene
        "Go back":
            jump tenth_apartment_scene

label twelvth_apartment_scene:
    scene bg officeone
    "You are in the office"
    menu:
        "Leave office":
            jump tenth_apartment_scene

screen firstOffice():
    # into the office

    frame:
        xpos 515
        ypos 850
        xsize 720 - 515
        ysize 1075 - 850
        background "#6527F5"

    button:
        xpos 515
        ypos 850
        xsize 720 - 515
        ysize 1075 - 850
        background None
        hover_background None

        mouse "move"

        action Jump("twelvth_apartment_scene")