default numberOfPeopleKilled = 0
default trust = 50
default oxygen = 100

default max_trust = 100
default max_oxygen = 100

default oxygen_loss_rate = 1

default filter_level = 1
default contamination_level = 1

default max_filter_level = 5
default max_contamination_level = 5



label use_oxygen:
    $ oxygen -= oxygen_loss_rate + (abs(filter_level - contamination_level) * oxygen_loss_rate)
    
    
    return

label lose_trust:
    $ trust -= 5
    return

label gain_trust:
    $ trust +=5
    return