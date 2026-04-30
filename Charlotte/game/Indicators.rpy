# This transform works for both Good and Bad indicators
init:
    transform indicator_fade(x, y, t):
        pos (x, y) anchor (0.5, 0.5)
        alpha 0.0
        linear 0.3 alpha 1.0
        pause t
        linear 0.3 alpha 0.0

# --- GOOD CHOICE ---
label GoodChoice(x=0.5, y=0.4, t=1.0):
    show goodIndicator at indicator_fade(x, y, t)
    pause (t + 0.6)
    hide goodIndicator
    return

# --- BAD CHOICE ---
label BadChoice(x=0.5, y=0.4, t=1.0):
    show badIndicator at indicator_fade(x, y, t)
    pause (t + 0.6)
    hide badIndicator
    return