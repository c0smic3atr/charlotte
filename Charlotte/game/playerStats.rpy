default numberOfPeopleKilled = 0
default trust = 50
default oxygen = 100

default max_trust = 100
default max_oxygen = 100

default oxygen_loss = 1



label use_oxygen:
    $ oxygen -= oxygen_loss
    
    
    return

label lose_trust:
    $ trust -= 5
    return

label gain_trust:
    $ trust +=5
    return