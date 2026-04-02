
define t = Character("Placeholder")
define r = Character ("Rick")
default fenceInteract1NumberOfVisits = 0


label third_apartment_scene:
    
    $ fenceInteract1NumberOfVisits +=1
    
    scene bg dumpster
    if fenceInteract1NumberOfVisits == 1:

        t "You are at the fence"

        menu:
            "Return":
                jump first_apartment_scene

            "Talk":
                show chara3colorr at left


        if numberOfPeopleKilled == 0:
            p "What'cha doin'?"
            p "..."
            p "Don't thank you're gonna find anything useful in that trash can."
            r "Might."
            p "What are you looking for?"
            p "..."
            p "You- you feeling alright?"
            r "Get outta here, lady, ain't your business."
            p "It is my business, I was sent-"
            r "Yeah, I heard"
            r "Small, town, could hear your chat with the girls from a mile away."
            p "Alright, then, are you gonna cooperate or not?"

             
        
            r "And why would I?"
            r "You just here to interrogate the lot of us?"
            p "I mean, yeah."
            r "Nobody got time for that"
            p "No time? You're dumpster-diving, don't exactly look like somebody with a bustling schedule."
            r "Yeah, screw you too."

            #Discovered Rick!!
            $ rick_facts['portrait'] = "rick portrait"
            $ rick_facts['name'] = "Rick Madden"
            $ rick_facts['fact1'] = "Just a hick searching the trash. Do the people here not have enough supplies?"

        jump third_apartment_scene

    elif fenceInteract1NumberOfVisits==2:
        menu:
            "Return":
                jump first_apartment_scene

            "Talk":
                show chara3colorr at left
        show chara3colorr at left
        r "I told ya', I'm busy"
        menu:
            "Kill Him":
             
                $ rick_facts ['status'] = "Dead"
                hide chara3colorr
                show chara3thirdmono at left
                pause 3.0
                # increase trust
                $ trust += 5
                "Bang"
                jump third_apartment_scene
                

            "Do nothing":
                $ rick_facts['status'] = "Spared"   
                jump third_apartment_scene


    else:
        menu:
            "Return":
                jump first_apartment_scene

            "Talk":
                if rick_facts['status'] == "Spared":

                    show chara3colorr at left
                    r "I'm just tryna keep myself fed here, girl. Quit buggin me."
                    jump third_apartment_scene
                else:
                    thought "He's not gonna answer..."   
                    jump third_apartment_scene
    

         



    menu:
        "Go back":
            jump first_apartment_scene

