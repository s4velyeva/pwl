label pwl_judge:

    # -- cleanup -- #
    window hide
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    stop sound fadeout 1.0

    pause(1.5)

    play music wicca
    window show dissolve2

    scene bg black with dissolve2

    alwix "..Привет, друг."
    alwix "..Почему ты никогда не отвечаешь?"
    "..."
    alwix "..Разумеется потому, что тебя нет..."
    alwix "..Ладно, пора вставать."

    window hide dissolve2
    scene bg alex_room with dissolve
    $ renpy.pause(4, hard=True)
    scene bg alex_room_i1 with dissolve
    $ renpy.pause(4, hard=True)
    scene bg alex_room_i2 with dissolve
    $ renpy.pause(4, hard=True)
    scene bg alex_room_i3 with dissolve
    $ renpy.pause(4, hard=True)

    scene bg alex_room with dissolve
    window hide dissolve2

    "Я снова лежал на кровати."
    "Радовался жизни."
    "Думал о хорошем."
    "Как и всегда.{w}{w} Но это только начало истории."

    window hide
    pause(1)
    window show

    "Хотите, чтобы я рассказал вам её полностью, детишки?"
    "Тогда слушайте внимательно. Это история великой любви хорошего человека."

    window hide
    scene bg black with dissolve2
    stop music fadeout 6
    pause(6)
    play music play_the_hero fadein 2
    scene bg alice_room_sunset with dissolve2
    window show

    "..." "...{w}ничтожество."
    "..." "...{w}не можешь даже свою жизнь наладить."

    window hide
    stop music fadeout 2
    play ambience silence fadein 2
    show black with dissolve
    pause(2)
    window show

    th "...привет, друг. Не знала, что ты здесь."
    th "...ты ведь не знаешь, что происходит, верно?"
    th "...я расскажу.{w}{w} Но сначала давай прогуляемся."

    window hide
    hide black with dissolve
    pause(1)
    window show

    th "Последние 3 дня я потратила на одного человека."
    th "Вроде бы ничем не примечателен.{w} Ходит в кафе, болтает там с друзьями."
    th "Иногда, как и все нормальные люди, приходит в это же кафе погрустить в одиночестве."
    th "Я тоже туда хожу.{w} Изредка."
    th "Целый день я потратила на раздумия, и под конец решила..."
    th "Я должна о нём узнать всё."

    window hide
    show black with dissolve
    pause(2)
    play music irc_fantasy
    hide black with dissolve
    window show

    th "Взломать его было сложнее, чем я думала."
    th "Судя по всему, он знает толк в этом деле."
    th "Мне нужно было пробиться через фаервол его сети, а потом и через систему безопасности линукса."
    th "Забавно, что он использует Кали. Я думала он ламер."
    th "Он часто летает по онионам, но что он там делает я не в силах узнать."
    th "В принципе, я нашла у него кое-какой документ..."
    th "Судя по всему он тайно работает с местной корпорацией."

    window hide
    show anim project_owl with dissolve2
    pause(1)
    window show

    th "...{w}Проект «СОВА».{w} Они протянули свои щупальца во многие сферы жизни, в том числе за границей."
    th "Мои знакомые из Америки называют корпорацию {b}Prowler{/b}, от слов Project OWL, крадущийся."
    th "Что?{w} Ты не понимаешь, почему так? Сейчас объясню."

    window hide
    stop music fadeout 5
    scene bg black with dissolve2
    show anim loading with dissolve
    pause(5)
    hide anim loading with dissolve
    play music thumb_cad fadein 2

    th "Корпорация пытается показаться всем хорошей, но это не так."
    th "Уже как 4 года они похищают мирных граждан для своих экспериментов."
    th "Никто об этом не знает, а у заявлений о пропаже просто истекают сроки."
    th "Никто не пытается их найти.{w} Потому что незачем."
    th "Мне неизвестно, куда именно пропадают граждане, и что с ними делают..."
    th "Но одно мне известно точно."
    th "{b}Это.{/b}" with hpunch
    th "{b}Пора.{/b}" with hpunch
    th "{b}Прекращать.{/b}" with hpunch

    return

