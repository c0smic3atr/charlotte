default numberOfPeopleKilled = 0
default trust = 50
default oxygen = 100

default max_trust = 100
default max_oxygen = 100


label use_oxygen:
    $ oxygen -= 5
    
    return

label lose_trust:
    $ trust -= 5
    return

label gain_trust:
    $ trust +=5
    return