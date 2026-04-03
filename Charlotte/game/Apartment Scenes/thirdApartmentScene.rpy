
define t = Character("Placeholder")
define r = Character ("Rick")
default fenceInteract1NumberOfVisits = 0
default timesTalkedtoRick = 0


label third_apartment_scene:
    
    $ fenceInteract1NumberOfVisits +=1
    
    scene bg dumpster
    if timesTalkedtoRick == 0:

        t "You are at the fence"

        menu:
            "Return":
                jump first_apartment_scene

            "Talk":
                show chara3colorr at left
                $ timesTalkedtoRick +=1


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

            if $ sarah_facts['status']== "Dead" or anna_facts['status']== "Dead":
                    r "Think I'm gonna cooperate with a killer like you?"
                    r "What ya gonna do, shoot me too?"
                    p "..."
                    p "Wuh- well, why didn't you leave? When you saw?"
                    thought "I'm talking like he caught me in a... lie, or something"
                    thought "Something normal"
                    thought "It's not..."
                    thought "It's not, it can't be"
                    r "What, a creep in a gas mask poppin' off rounds on kids?"
                    r "Psh, why would I care one way or another..."
                    r "I got shit to do."
            r "And why would I?"
            r "You just here to interrogate the lot of us?"
            p "I mean, yeah."
            r "Nobody got time for that"
            p "No time? You're dumpster-diving, don't exactly look like somebody with a bustling schedule."
            r "Yeah, screw you too."

            #Discovered Rick!!
            $ rick_facts['portrait'] = "rick portrait"
            $ rick_facts['name'] = "Rick Madden"
            if rick_facts ['status'] == "undiscovered":
                $ rick_facts['fact1'] = "Just a hick searching the trash. Do the people here not have enough supplies?"

        jump third_apartment_scene

    elif timesTalkedtoRick == 1:
        
        menu:
            "Return":
                jump first_apartment_scene

            "Talk":
                $ timesTalkedtoRick += 1 
                show chara3colorr at left
                show chara3colorr at left
                r "I told ya', I'm busy"
                if rick_facts['status'] != "Dead":
                    menu:
                        "Kill Him":
                        
                            $ rick_facts ['status'] = "Dead"
                            hide chara3colorr
                            show chara3thirdmono at left
                            pause 3.0
                            # increase trust
                            $ trust += 5
                        

                            if sarah_facts ['status']== "Dead" or anna_facts ['status']== "Dead":
                                $ rick_facts['fact1']= "What's the profile? I don't get it. Helpfulness? Positivity? Do they even know... am I supposed to just kill everyone?"

                            elif rick_facts['status']== "Dead": 
                                $ rick_facts['fact1'] = "I forgot what it felt like to shoot a gun. I'd always been so nervous to hit a person by mistake, before... by mistake. This is a mistake. What am I doing?"
                            
                            jump third_apartment_scene
                            

                        "Do nothing":
                            $ rick_facts['status'] = "Spared"   
                            jump third_apartment_scene
                else:
                    thought "he's not gonna answer"
                    menu:
                        "Return":
                            jump first_apartment_scene



    else:
        menu:
            "Return":
                jump first_apartment_scene

            "Talk":
                if rick_facts['status'] == "Spared" and sarah_facts['status']== "Spared" and anna_facts['status']=="Spared":

                    show chara3colorr at left
                    r "I'm just tryna keep myself fed here, girl. Quit buggin me."
                    jump third_apartment_scene

                if rick_facts['status']== "Spared" and sarah_facts['status']== "Dead" or anna_facts['status']== "Dead":
                    show chara3colorr at left
                    r "What, you want me to do something about it?"
                    r "Assuage your guilt?"
                    r "Not gonna happen."
                else:
                    thought "He's not gonna answer..."   
                    jump third_apartment_scene
    

         



    menu:
        "Go back":
            jump first_apartment_scene

