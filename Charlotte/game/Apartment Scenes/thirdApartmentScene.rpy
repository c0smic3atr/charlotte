
define t = Character("Placeholder")
define m = Character ("Rick")

label third_apartment_scene:
    scene bg dumpster

    t "You are at the fence"

    menu:
        "Return":
            jump first_apartment_scene

        "Talk":
            show chara3colorr at left

    p "Bla bla bla placeholder"
    m "Bla bla bla responce vague disinterest"

    menu:
        "Go back":
            jump first_apartment_scene

