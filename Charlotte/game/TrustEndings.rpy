label trust_endings:
    scene black
  

    if (trust >= 100):
        jump high_trust_ending
    elif (trust>= 51):
        jump med_trust_ending
    elif (trust<=50):
        jump low_trust_ending
    elif (trust<=0):
        jump no_trust_ending




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
    "you left us with no choice goodbye j...... you don't even deserve to know your name"
    "who am i"
    "your are forever lost goodbye"
    return

label no_trust_ending:
  " you have hurt us walker, at this point you don't deserve to rot with that disease"
  "i believe we have something better planned for you"
  "You are now there little expermiment"
  return