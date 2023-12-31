﻿label Day_one:
#Сцена 1
    scene fon
    with showdissolve
    "Был холодный ясный день, часы пробили тринадцать."

    "Уткнув подбородок в грудь, чтобы спастись от злого ветра, Дэниел Райан торопливо шмыгнул за стеклянную дверь огромного офисного здания, но все-таки впустил за собой вихрь зернистой пыли."

    "В вестибюле пахло вареной капустой и старыми половиками. Дэниел работает здесь далеко не первый год. Инженеры по кибербезопасности всегда пользовались спросом, тем более в такое непростое время."

    "Не сказать, что Дэниел был яркой и запоминающейся личностью. Юношеская молодость лица с каждым годом лишь увядала - на ее место становились ровные ряды морщин. Хотя и на совсем взрослого он был не похож."

    p_D "Моя работа не делает меня сильным мира сего. Хотя, признаюсь, с самого детства мне нравилась электроника. Телеэкраны, работающие на прием и передачу, микрофоны, с помощью которых подслушивают за людьми, камеры, подобно глазам государства, следящие за каждым шагом человеческим. Много ли изменилось с тех пор?"

##сцена 2

    scene fon2
    with showdissolve
    "Мир снаружи, за закрытыми окнами, дышал холодом. Ветер закручивал спиралями пыль и обрывки бумаги; и хотя светило солнце, а небо было резко-голубым, все в городе выглядело бесцветным."
    "Вдалеке между крышами скользнул вертолет, завис на мгновение, как трупная муха, и по кривой унесся прочь."
    p_D "Не сказать, что моя работа мне наскучила. Однообразность и обыденность действий давно переросли в рутину."

    p_D "Подобно винтику в большой системе, я из последних сил держу весь механизм."

    "Дэниэл откинулся на спинку стула. Им овладело чувство полной беспомощности. Он сидел, бессмысленно уставившись на потолок."
    p_D "Каждый человек ставит перед собой цели. Кто-то желает купить новый мобильник, кто-то машину, у кого-то все ограничивается стандартным 'сын, дерево, дом'."
    p_D "Или дом, дерево, сын? Зачем здесь дерево? А если куст? Что если не дом, а трешка в 'Сити'?"
    p_D "..."
    p_D "Считаю ли я себя счастливым?"

#Сцена 3

    scene fon3
    with showdissolve
    p_D "После окончания института передо мной были открыты все двери. Назвать себя гением? Слишком пафосно. Скорее правильное распределение времени позволило быть на пару шагов дальше сверстников."
    p_D "Думаю, что только кибербезопасность действительно привлекала меня. Куда, если не в ИБ?"
    p_D "Я представлял себе хакеров в черных капюшонах, огромные датацентры, находящиеся под атакой, и команду инженеров, защитников, администраторов, которые, подобно благородным рыцарям, сражались с темным злом."
    p_D "Хах.."

    scene fon4
    with showdissolve
    p_D "Правильный ли выбор я сделал? Так ли себе я представлял свою жизнь?"
    p_D "..."

#Сцена 4

    show alice_base at left

    p_A "Дэниел!"
    p_A "Дэниел!!!"
    p_A "ДЭНИЕЛ!!! Опять витаешь в облаках? У нас много задач впереди!"
    "Это Алиса. Еще недавно она пришла к нам стажером. Хотя с ее знаниями и потенциалом она вырастет очень быстро."
    p_D "А, что, что? Да-да, сейчас"
    hide alice_base
    with moveoutleft
    "И Дэниел вернулся к своим, уже порядком поднакопившимся, делам."

#Сцена 5

    scene fon5
    with showdissolve
    "Солнце неумолимо садилось за горизонт, закатная тень семимильными шагами захватывала и без того мрачный город. Наступал вечер."

    scene fon6
    with showdissolve
    "Все меньше людей оставалось в офисе. Немногие работали честно. Кто-то спешил к семье, кто-то забирать детей со школы, кому-то просто осточертело сидеть в офисе."
    "Дэниелу спешить было некуда."
    play sound gmail
#оповещение
    #"Звук оповещения (это я так на будущее - Разраб)"

    p_D "Кто там еще..."
#интерактив

    show screen map

label Day_return:

    p_A "Дэниел, не сиди до поздна! А то опять с уборщицами ночевать будешь :) Не задерживайся. Пока!"

    "Внезапный голос Алисы напугал героя. Посмотрев на часы, Дэниел принял решение отложить чтение письма на завтра."
    "Утро вечера мудренее - подумал он. И выключил компьютер."

#сцена 6

    scene fon7
    with showdissolve
    "Выйдя на пустынную ночную улицу, он направился к метро."
    "Бесшумный поезд поглотил его, пролетел, как челнок, по хорошо смазанной трубе подземного туннеля и вместе с сильной струей теплого воздуха выбросил на выложенный желтыми плитками эскалатор, ведущий на поверхность в одном из пригородов."


    scene fon8
    with showdissolve
    "Насвистывая, Дэниел поднялся на эскалаторе навстречу ночной тишине."
    "Не думая ни о чем, во всяком случае, ни о чем в особенности, он дошел до поворота. Но еще раньше, чем выйти на угол, он вдруг замедлил шаги, как будто ветер, налетев откуда-то, ударил ему в лицо или кто-то окликнул его по имени."


    scene fon9
    with showdissolve
    "Уже несколько раз, приближаясь вечером к повороту, за которым освещенный звездами тротуар вел к его дому, он испытывал это странное чувство."
    "Ему казалось, что за мгновение до того, как он повернёт, за углом кто-то стоит."
    "В воздухе была какая-то особая тишина, словно там, в двух шагах, кто-то притаился и ждал и лишь за секунду до его появления вдруг превратился в тень и пропустил его сквозь себя."
    p_D "Бррр... Видимо, я слишком устал на работе."

    scene black
    with showdissolve
    pause(3.5)

    jump Day_two
    return
