init:
    transform opacity_dissolve:
        alpha 0.0
        linear 6.0 alpha 1.0


screen pwl_main_menu():
    tag menu  # allows us to use it as menu

    # menu part
    add CursorTracker("mods/pwl/res/menu/images/background.png", 10) at opacity_dissolve
    add CursorTracker("mods/pwl/res/menu/images/alice-changed.png", 15) at opacity_dissolve:
        xpos 809
        ypos 462
    add CursorTracker("mods/pwl/res/menu/images/alice-original.png", 13) at opacity_dissolve:
        xpos 1180
        ypos 316
    add CursorTracker("mods/pwl/res/menu/images/pwl-logo.png", 40) at opacity_dissolve:
        xpos 681 
        ypos 52

    imagemap:
        alpha False
        idle "mods/pwl/res/menu/images/gui-unhovered.png"
        hover "mods/pwl/res/menu/images/gui-hovered.png"

        hotspot (240, 525, 257, 25) action (Hide("pwl_main_menu", dissolve), Jump("pwl_judge"))
        hotspot (240, 557, 275, 25) action ShowMenu("pwl_in_development_notice")
        hotspot (240, 583, 290, 25) action Return()

screen pwl_in_development_notice:
    tag menu
    modal False
    add "mods/pwl/res/img/cg/cg-indev.png"


label pwl_main_menu_begin:
    # -- cleanup -- #
    window hide
    scene bg default_background with dissolve2
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    stop sound fadeout 1.0

    play music psycho_code fadein 0.5
    call screen pwl_main_menu
