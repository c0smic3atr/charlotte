label trust_endings:
    scene black
  

    if(orion_facts['status'] == "Dead"):
        jump scumbag_ending
    
    elif (trust >= 100):
        jump high_trust_ending
    elif (trust>= 51):
        jump med_trust_ending
    elif (trust<=50):
        jump low_trust_ending
    else:
        jump no_trust_ending


label scumbag_ending:
    "Oh my god..."
    "The hell is wrong with you?"
    "***Vomiting noises***"
    "Not even hell wants you"
    "If I were in a room with you and Hitler..."
    "... and I had a gun with two bullets"
    "... I would shoot you twice."
    return

label high_trust_ending:
    "in the end your compliance with death left them utterly happy to keep you and to even make you one of them, now you shall never be the same"
    "You have been taken"
    "Game Over"
    return

label med_trust_ending:
    "You did right by us but you just were not enough for us you don't even deserve to be one of us"
    "we might aswell let you rot with that disease"
    "you were left to rot"
    return

label low_trust_ending:
   
    return

label no_trust_ending:
    e "Walker."
    p "Mullan, how come nobody-"
    e "You think after all the shit you pulled we were still going to come get you?"
    e "Waste of resources, I'd say."
    e "Can't keep around workers who don't know how to work."
    e "I won't be made a fool, trying to use a gun with no trigger."
    p "But, I have the notes, don't you need-"
    e "I don't need anything from you. Never did."
    e "I assume you've learned a few things during your stay?"
    p "I- I don't know what I-"
    e "You know I can't have that information getting out. Sensitive stuff."
    p "Then why did you even send me in the first place?"
    e "Well, what would you do with a gun that won't shoot?"
    pause 1.5
    e "You throw it away."
    e "That's what this place is, now."
    e "A dumping ground. And a damn good one."
    e "You know, it didn't have to be this way."
    e "All the people here, these people you've been interviewing so futilely for, how long's it been?"
    e "Eight months?"
    e "They never had a chance, like a fetus flushed down the drain."
    e "Doomed from the start."
    e "But you, you could have been so much more."
    e "We were never going to come get you, I think you understand that now, but even before all of this"
    e "You couldn't just sit back and do what you were told. Always falling just out of line."
    e "Never asking any questions, but always having this look on your face that said 'I'm missing something'."
    e "Well, you were definately missing something."
    e "Sorry you had to find out the hard way, but that's what happens when you can't trust your tools to work as they should."
    e "Couldn't deny the risk of injury."
    pause 3.0
    e "Goodbye, Walker."
    return