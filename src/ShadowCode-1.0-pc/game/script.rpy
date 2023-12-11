# DAY 1
init:
    define showdissolve = Dissolve(1.25)
    ## Persons text/dialogs
    define Boss = Character ('Босс', color = "FB3939")
    define N_AT = Character('Неизвестный', color="ff2400")
    define N_A = Character('Неизвестный голос', color="ff0000")
    define p_D = Character('Дэниел', color="#efc8ff")
    define p_A = Character('Алиса', color = "#FF8C00")
    define p_M = Character('Майкл', color="#f3ffc8")
    ##define p_A = Character('Повествователь', color="#e9530d")


    ## Persons Images
    image Daniel = "people/daniel/daniel_base.png"
    image Michael = "people/michael/michael_base.png"
    image Alice = "people/alice/alice_base.png"

    ## bg day 1
    image fon = "bg/Day1/day1_scene1_1.png"
    image fon1 = "bg/Day1/day1_scene1_2.png"
    image fon2 = "bg/Day1/day1_scene2.png"
    image fon3 = "bg/Day1/day1_scene3_1.png"
    image fon4 = "bg/Day1/day1_scene3_2.png"
    image fon5 = "bg/Day1/day1_scene5_1.png"
    image fon6 = "bg/Day1/day1_scene5_2.png"
    image fon7 = "bg/Day1/day1_scene6_1.png"
    image fon8 = "bg/Day1/day1_scene6_2.png"
    image fon9 = "bg/Day1/day1_scene6_3.png"
    #интерактив
    image fontocomp = "images/interaktiv/map.png"
    image massange = "images/interaktiv/massange.png"
    ## bg day 2
    image fon2_1 = "bg/Day2/day2_scene1_1.png"
    image fon2_2 = "bg/Day2/day2_scene1_2.png"
    image fon2_2_2 = "bg/day2/day2_scene2_1.png"
    image fon2_3 = "bg/Day2/day2_scene3_1.png"
    image fon2_4 = "bg/Day2/day2_scene4_1.png"
    image fon2_5 = "bg/Day2/day2_scene5_1.png"
    image fon2_6 = "bg/Day2/day2_scene6_1.png"
    image fon2_7 = "bg/Day2/day2_scene7_1.png"

    # bg day 3
    image fon3_1 = "bg/Day3/day3_scene1_1.png"
    image fon3_2 = "bg/Day3/day3_scene2_1.png"
    image fon3_3 = "bg/Day3/day3_scene3_1.png"
    image fon3_4 = "bg/Day3/day3_scene4_1.png"
    image fon3_5 = "bg/Day3/day3_scene5_1.png"

screen map:
    modal True
    zorder 100

    fixed:
        xsize 1920 ysize 1080
        add "images/interaktiv/map.png" align(.5,.5)
    fixed:
        xsize 1920 ysize 1080

        button:
            xpos 251 ypos 130
            xsize 120 ysize 120
            idle_background "images/interaktiv/coolGm.png"
            hover_foreground "images/interaktiv/coolGm1.png"
            focus_mask True
            action Hide("map"), Jump("gmail")
label gmail:
    show fontocomp
    show massange
    pause
#
    jump Day_return
#Основная новела
label start:

    jump Day_one

    return
