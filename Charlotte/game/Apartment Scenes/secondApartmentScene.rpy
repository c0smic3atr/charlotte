label second_apartment_scene:
    scene bg apartments2

    menu:
        "Knock on door 1":
            show first apartment npc
            a "..."
            a "You don't look familiar"
            a "I'd know, being there's so few people in town these days"
            a "Not like there ever was many"
            a "What's your deal? If you're here to tell me to keep the noise down, you can get lost"
            p "Um, no"
            p "I've been sent to check up on the residents here. See how you're handling... things"
            a "Huh. I guess that checks out"
            a "Some of us will be pretty happy to see you here"
            a "But most of us gave up on an intervention a long time ago"
            p "Intervention?"
            a "Yeah. I mean, you can't blame us for wanting out"
            p "You know we can't just let you go"
            a "Some of us know better than others"
            a "You should talk to Sarah next door. She's something of an optimist"
            a "Seems to be handling things better than most"

            jump second_apartment_scene

        "Knock on door 2":
            show second apartment npc
            "you talked to door 2"
        "Go Back":
            jump first_apartment_scene

    jump second_apartment_scene