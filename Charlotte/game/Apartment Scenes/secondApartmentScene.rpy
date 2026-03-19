label second_apartment_scene:
    scene bg apartments2

    menu:
        "Knock on door 1":
            show chara1first at left
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
            show chara2second at left
          
            s "No way!"
            s "You've finally come back..."
            p "Huh?"
            s "We've been waiting so long, some of us started to give up hope"
            s "Not me though, I knew you'd come and rescue us."
            p "I'm sorry, I think you have the wrong idea"
            p "I'm officer Walker, I'm here to evaluate the wellbeing of y'all here."
            s "Oh..."
            s "Well, I was still right to trust you"
            s "Comin' back at all"
            s "It proves it."
            p "I guess..."
            p "Anyway, how have you been feeling? Any aches, nausea..."
            p "Uh, fatigue? Anything like that?"
            s "Oh, I dunno. I guess, maybe."
            p "How about your neighbors?"
            s "The only neighbor I really talk to is Anna, and she's a real stiff"
            s "We've been neighbors for I can't remember how long, and I still barely know anything about her!"
            p "Alright, well thank you for your time."
            s "Wait!"
            s "Uh"
            s "Are you gonna stay long?"
            p "Just as long as I have to."
            s "Well, before you go, can you check on someone for me?"
            s "My grandpa... He's too far away, I can't risk going to visit."
            p "What do you mean?"
            s "We were told to stay inside. Quarentine, ya' know? Can you check on him for me?"
            s "His name's Huan."
            p "Yeah, I'll keep my eye out."
            s "Thank you!"



        "Go Back":
            jump first_apartment_scene

    jump second_apartment_scene