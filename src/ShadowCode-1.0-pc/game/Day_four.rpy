label Day_four:
#сцена 1

    scene fon4_1
    with showdissolve
    #звук будильника
    play sound Budi
    "В этот раз обошлось без кошмаров. Жизнь стала играть новыми красками возможностей и больших перспектив"
    "Все было, как в раю."

#сцена 2

    scene fon4_2
    with showdissolve
    "Одурманенный невероятным успехом разум героя принял волевое решение. Сегодня Дэниел на свою обычную работу не пойдет."
    "В тот же момент он связался с новым боссом, попросив выдать новое задание."

#сцена 3

    scene fon4_3
    with showdissolve
    "Ответ последовал незамедлительно"
    "Дэниел моментально получил диапазон IP-адресов, на которых нужно найти и проэксплуатировать уязвимости"
    "Вновь на внешнем контуре организации висело множество уязвимых служб. Дэниел писал, создавал, модифицировал эксплойты, чтобы обойти все встающие на пути средства защиты"

#сцена 4

    scene fon4_4
    with showdissolve
    $renpy.music.set_volume(0.2)
    play music klava
    #$renpy.music.set_volume(0.0001)
    #звук https://www.youtube.com/watch?v=YBSxn2uPje4%3E

    "Последний оплот защиты сгорел спичкой перед мастерством Дэниела"
    "Дэниел успешно пробился в сеть организации, нашел админа и стащил его учетку! Теперь он - власть, царь, отец и Бог этой компании"
    "Такая скорость обрадовала нового босса. Редко какие проекты закрываются за утро"
    show boss_base at left
    show daniel_smile at right
    Boss "Эххххххххх!! Дэнчик! Ты красавец! КРА-СА-ВЕЦ! Наконец-то 'СЕКУР-КОМПАНИ' стала нашей!"
    Boss "Деньги в миксере, скоро поступят тебе на крипту."
    "Опять звон золотых биткоинов ослепил Дэниела. Он не смог понять, что теперь он не типовой инженер по кибербезопасности. Он теперь - настоящий хакер!"
    stop music
#сцена 5

    scene fon4_5
    with showdissolve
    #звук https://www.youtube.com/watch?v=Y-WTvCyXObg%3E
    play sound kassa
    "Миф о сладкой жизни, некогда заполнявший душевную пустоту героя, воплотился в жизнь"
    "Недолго думая Дэниел, взяв в охапку золотую кредитницу, направился в автосалон"

    scene fon4_6
    with showdissolve
    "У героя всегда была одна мечта желтого цвета. Двухдверная, в четыре сотни лошадиных сил..."
    "Думаю, мечты на то и созданы - они должны сбываться."

    scene fon4_7
    with showdissolve

    "Вдоволь погоняв новую тачку по улицам серого города, Дэниел возвращается домой"
    "Я так далеко от этого тела, что мне дали пользовать ради забавы."
    "Я так высоко — уровень неба. И я не вернусь, будто пол — это лава"

    scene black
    with showdissolve
    pause(3.5)
    jump Day_five
    return
