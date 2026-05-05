init:
    transform indicator_fade(x, y, t):
        pos (x, y) anchor (0.5, 0.5)
        alpha 0.0
        linear 0.3 alpha 1.0
        pause t
        linear 0.3 alpha 0.0

label oxygen_warning(x=0.5, y=0.4, t=1.0):
    show warningIndicator at indicator_fade(x, y, t)
    pause (t + 0.6)
    hide warningIndicator
    return
   

