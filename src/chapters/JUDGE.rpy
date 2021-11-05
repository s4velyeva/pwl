label pwl_JUDGE:

    # -- cleanup -- #
    window hide
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    stop sound fadeout 1.0

    play music play_the_hero fadein 6
    scene bg black with dissolve2
    show text "{size=88}{color=#ff0000}С У Д Ь Я{/color}{/size}" at truecenter with dissolve
    pause(2)
    stop music fadeout 6

    pause(1.0)
    hide text with dissolve

    if PWL_GIT:
        show text "{size=74}You are using git version.\nSome bugs may appear.{/size}" at truecenter
        with dissolve
    pause(2.0)

    hide text with dissolve

    # show text "{size=74}{PWL_NOTICE_TEXT}{size=74}" at truecenter
    # with dissolve

    pause(2.0)
    hide text with dissolve

    pause(1.5)

    play music distract_n_enter_cut
    window show dissolve2

    alwix "Привет, друг."
    alwix "Давно мы не разговаривали."
    alwix "..{w}как у тебя дела?"
    alwix "..{w}ах, да.{w} Ты же никогда не отвечаешь...{w} Хотел бы я оказаться на твоём месте и просто наблюдать за всем со стороны."
    alwix "Я опять что-то упускаю...{w} Что ты помнишь?"
    alwix "...{w}Почему ты никогда не разговариваешь?"
    
    "..."
    ulwix "Эй?{w} Лёш, ты меня слышишь?"

    alwix "Чего..?"
    alwix "Юля?{w} З..{w} Зачем ты здесь?.."
    
    ulwix "Я не здесь..."

    alwix "Ты...{w} Не здесь?"
    alwix "А как тогда..."

    ulwix "Лёха!{w} {b}Лёха, твою мать!{/b} Очнись! {w}{b}Очнись, идиот!{/b}"

    alwix "А-а!?.."
    
    window hide
    with Dissolve(0.0001)
    stop music
    scene bg semen_room

    show un normal sport close at cleft
    window show

    "Я проснулся.{w} Надо-мной нависала Лена со стаканом воды."
    
    show un rage sport close at cleft with dspr
    lenkar "Ты чего, блять, творишь!?"

    alwix "Ха-а-а...{w} Фуф...{w} Тебе-то какое дело?"
    alwix "Просто решил вздремнуть."

    "Я говорил как всегда тихо, монотонно, и размеренно, пытаясь не проявлять эмоций."

    lenkar "В смысле, блять, вздремнуть!? Ты, конечно, и так редко выходишь наружу, но я тебя уже четыре дня не видела!"

    alwix "Увидела?{w}..{w} Лена, прости, мне нужно работать..."
    lenkar "Работать?!{w} Ты совсем с дуба рухнул!?"

    window hide
    show un angry sport close at cleft with dspr
    pause(0.5)
    window show

    alwix "Лена, уйди..."
    alwix "Ты меня отвлекаешь..."

    "Лена фыркнула, и резко выпалила:"
    lenkar "Ну и пожалуйста!"

    window hide
    hide un with easeoutleft
    play sound sfx_slam_door_campus
    window show

    "Она вышла из моей квартиры, хлопнув дверью.{w} Я сел за компьютер и решил продолжить начатое."
    
    window hide
    play music distract_n_enter
    scene cg prologue_monitor_custom with dissolve2
    pause(1.5)
    window show

    "Лена моя соседка, мы хорошо с ней ладим...{w} Но вот мы с ней характерами не схожи."
    "..."

    "\[ n1tr0l@parrot-sec \] ~ $ netstat"
    "\[ n1tr0l@parrot-sec \] ~ $ sudo ip set eth0 down"

    "..."
    
    window hide
    pause(0.5)
    scene bg black with dissolve
    pause(6)

    stop music
    scene bg semen_room
    pause(1)
    window show

    alwix "И всё?"
    return
