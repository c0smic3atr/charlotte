
define t = Character("Placeholder")
define r = Character ("Rick")

label third_apartment_scene:
    scene bg dumpster

    t "You are at the fence"

    menu:
        "Return":
            jump first_apartment_scene

        "Talk":
            show chara3colorr at left

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





    menu:
        "Go back":
            jump first_apartment_scene

