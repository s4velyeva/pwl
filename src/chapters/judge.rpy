label pwl_judge:

    # -- cleanup -- #
    window hide
    scene bg black with dissolve
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    stop sound fadeout 1.0

    # BETA
    if persistent.show_now_playing:
        show pwl_gui now_playing at top with dissolve

    pause(1.5)
    play music alittlepush
    window show

    th "...{w}привет, друг.{w} Ты…{w} слышишь меня?{w} Ты правда слышишь?.."
    th "...{w}я хотела с тобой поговорить. Ты помнишь меня?.. Помнишь ведь, в-верно?.."
    th "Умоляю, не забывай меня…{w} Прошу тебя…"

    window hide
    pause(1)
    window show

    th "С-стой!{w} Н-не уходи…{w} Я тебе расскажу и покажу!..{w} П-п-покажу {b}всё{/b}!"
    th "Лишь останься со мной…{w} Молю…{w} Мне…{w} М{w=0.3}-мне так одиноко…"

    window hide
    pause(1)
    window show

    th "...{w}ты помнишь меня?..{w} Должен помнить…{w} А если и забыл, ничего страшного…{w}{w}"
    th "Это я, Алиса…{w} Твоя подруга…{w} Мы с тобой не в первый раз видимся..."
    th "У меня мало времени…{w}{w} Запомни лишь одно…{w} Не дове-"

    window hide
    pause(1)
    scene cg dv_alice_vik with Dissolve(5)
    show pwl_noise with Dissolve(5)
    pause(10)
    scene bg black with dissolve
    play music after_dark_muffled fadein 4
    pause(4)
    scene bg semen_room with Dissolve(8)
    window show

    "Я вновь стояла у зеркала и смотрела на своё отражение."
    dv "...{w}ничтожество...{w} Хотя нет, погоди, не ничтожество!{w} Нет!{w} Я велика…{w} Я хороша…{w} Я известна…{w}{w}"
    
    window hide
    show blink
    pause(0.8)
    window show

    dv "...{w}ничтожество.{w} Сама себя оправдываешь.{w} Не стыдно?..{w} Хотя почему мне должно быть стыдно?"

    window hide
    hide blink
    show unblink
    pause(1)
    window show

    dv "...{w}стыдно."
    dv "...{w}скучно."

    window hide
    show blink
    pause(2)
    window show

    dv "...{w}не скучно.{w} Очень даже вес-"
    dv "..."
    dv "..."

    "Я начала хнычить.{w} Я сама не поняла, почему.{w} Позже, я буквально начала захлёбываться рыданиями."
    "Я кричала, я била кровать, но позже…{w}{w} Я успокоилась."

    window hide
    hide blink
    show unblink
    stop music fadeout 2
    pause(1)
    return
