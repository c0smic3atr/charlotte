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
    e "Walker!"
    thought "Finally."
    e "We are stunned, I've got to put it out there."
    e "Never thought you'd show up like this."
    e "You certainly never had before."
    p "So I was right."
    p "You just wanted me to kill them all?" 
    e "Oh, no."
    e "I've never wanted anything from you a day in my life."
    e "But I'm certainly not diappointed."
    p "..."  
    p "So, will you tell me?"
    p "What was the profile?"
    e "You still haven't caught on?"
    e "There never was a profile."
    e "I told you, you're not incompetent."
    e "Clearly competent enough to do your job when under the threat of death."
    e "That's a quality I admire."
    e "And for that, I'm going to do you a rare favor."
    e "We're going to take you back with us."
    e "Your prayers have been answered."
    p "You're kidding?"
    e "You know I'm not one to kid, Walker."
    e "Sure, things won't be the same."
    e "You can see Charlotte was out little test subject"   
    e "And while you were gone we're run into quite a bit of trouble over it."
    e "So we're going back to square one, individual human tests."
    e "And you're going to spearhead the whole thing."
    e "As our first subject, of course."
    e "Pro tip, don't try to fight it."
    e "You've proved yourself to just fall to your knees in the face of real danger, and that means you're just the right kind of person for this."
    e "Won't do anything about it."

    return


label high_trust_ending:
    thought "Finally, this can be over with."
    e "Took you long enough, Walker."
    p "I don't even know how long it's been."
    e "Yeah, I figured you'd notice the whole time dilation thing."
    e "Eight months, give or take."
    e "Bet it felt like a couple of days."
    e "That's the great thing about this place."
    e "You can just lock people up and throw away the key."
    p "What the hell are you talking about?"
    e "Come on, I told you"
    e "You're not incompetent."
    e "Denial is the most useless stage of grief."
    e "I'm surprised about your level of competence here, Walker."
    e "You've never quite showed up like this before."
    e "Almost makes me want to go back on it all."
    p "No it doesn't."
    e "No, it doesn't."
    e "If I'm being honest, I'm not totally sure why I showed up at all."
    e "Usually we just send in a message over your earpiece, there."
    e "A quick apology, assurance we'll tell your families some story to make it sound like you went out with purpose."
    e "But for people like you..."
    e "Got no family, no friends."
    e "Nobody to go home to, anyway."
    e "I guess part of me relishes in delivering the news personally."
    p "No news to give. I get it."
    p "You're at the top of the totem pole, I'm at the bottom."
    p "I'm not going to misplace my anger on you, or the people of Charlotte."
    p "I just wish I wasn't stupid enough to show up in the first place."
    e "And here I was thinking these people were the closest thing to a community you've ever had."
    p "Maybe."
    p "Not much to learn about people who've lost their minds."
    e "Maybe."
    e "You'll surely get the chance."
    e "Until that mask of yours runs out"
    e "Or your organs shut down and leave you like it's left them."
    e "Can't deny the inevitable, wether it was dying here or staying dead there."
    e "Goodbye, Walker."
    pause 1.5
    e "Hey, I just realized"
    e "I never caught your name."


    return

label med_trust_ending:
    thought "Finally this can all be over with."
    e "Took you long enough."
    thought "I don't even know how long it's been"
    p "I got the notes."
    e "I'm sure."
    e "And I presume you've also got some information?"
    p "This place isn't exactly subtle."
    p "So, it's all true, huh?"
    e "Well, it's like I said. You're not incompetent."
    p "So why'd you send me here at all?"
    p "It's pretty clear you already know everything about this place."
    e "If I told you I'm not sure you'd even believe me."
    e "But if you've managed to make it this long, it's no skin off my back."
    p "How long's it been, anyway?"
    e "Hmm, eight months, give or take?"
    e "That's not what I care about, though."
    e "I'm only following up on my end of the deal."
    e "You go to Charlotte, take out the undesirables, and write down what you find."
    e "I come and get you."
    e "Well, I come and meet you."
    e "You've done a pretty poor job out here."
    p "What does it matter? was clearly all for nothing, anyway."
    e "Not for nothing."
    e "One might call this a teachable moment."
    e "Don't let yourself get locked up in a place that's not good for you."
    p "Yeah."
    e "Not wondering why we actually sent you?"
    pause 1.5
    e "We have proof of it all, you know."
    e "The stolen backups"
    e "The phone calls"
    e "The under-the-table inteviews, the allegations-"
    e "Sorry, alleged allegations."
    e "The whole project. Thought you and your team could get away with it, huh?"
    e "Might be feeling pretty embarassed right about now."
    thought "..."
    thought "What?"
    e "Well, all good things must come to an end."
    e "Surely you've come to grasp the severity of your situation."
    e "We all saw it coming to this"
    e "I saw it in you from the very start."
    e "Not just since you arrived in Charlotte, but even years before."
    e "There was never going to be a happy ending for you, Walker"
    e "And from the moment you pulled the trigger on an innocent life for the first time"
    e "I could tell you knew it too."
    e "This job,"
    e "It's cyclical- in nature."
    e "I've met you dozens of times."
    e "In the form of the overinvolved"
    e "The domineering"
    e "The wildly out of their depth."
    e "And now you, the-"
    e "What's that on your face? Confusion?"
    e "You're the confused?"
    e "What a legacy."
    e "Thing is, it always ends the same for you, no matter how confused you may or may not be."
    e "With you losing out, and me continuing on."
    e "I can only hope that in your final moments you'll allow yourself to feel the anger."
    e "Even though the countless disappointments, you've earned that."
    e "And the day will come when I'll have earned it too"
    e "And we will meet again."
    e "Until then, Walker."
    return

label low_trust_ending:
   
    return

label no_trust_ending:
    thought "Nobody's here..."
    e "Walker."
    thought "Why the hell's he in my earpiece?"
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