label Day_two:
#Сцена 1
    scene fon2_1
    with showdissolve
    show bg_person1 at left
    N_A "Шевелящимися виноградинами угрожают нам эти миры"
    N_A "И висят городами украденными, золотыми обмолвками ябедами, ядовитого холода ягодами"
    N_A "Растяжимых созвездий шатры"
    N_A "Золотые созвездий жиры"
    hide bg_person1
    p_D "ААААААААААААААААААААААААААААААААААА"

    scene fon2_2
    with fade
    "Перемены - вот что одновременно влекло и пугало Дэниела."
    "Он устал от пучины ежедневных тягот, монотонности, однообразия и скукоты жизни. Лишь изменения могли внести в эту жизнь новые краски. Но какие?"

#сцена 2
    show fon2_2_2
    with showdissolve
    p_D  " 'Ииииии всееее идееет по плаааанууу' "
    "Как видите, Дэниел быстро пришел в себя и перестал думать о серости жизни"

#сцена 3

    scene fon2_3
    with showdissolve
    show alice_base at left
    show daniel_base at right
    p_A "Привет, Дэниэл! Как ты? Смотрю мешки от глаз все не уходят, может хватит работать так много? Ты же сгоришь!"
    p_D " 'Знала бы она, что мешки под глазами из-за моих кошмаров. Я плевать хотел на эту работу.' "
    p_A "Дэниел?"
    p_D "А, что? Да, привет, ты права, не переживай, я скоро все закончу."
    p_A "Помочь тебе?"
    p_D "НЕТ"
    show alice_angry at right
    hide alice_base
    p_D "Извини, пока помощи не нужно, спасибо"
    p_A "Странный ты..."
    hide alice_angry
    with moveoutleft
    hide daniel_base


#сцена 4

    scene fon2_4
    with showdissolve
    "Вчерашнее письмо до сих пор висело на главном экране Outlook, бросаясь в глаза ярко-красным, неизвестным Дэниелу, логотипом"
    p_D "Приглашение в группировку хакеров? Это что, шутка? Идите вы…"

#сцена 5

    scene fon2_5
    with showdissolve

    "После долгожданного обеда часы тянулись предательски медленно"
    "Дэниел давно автоматизировал свои задачи. Ему достаточно было запустить лишь один скрипт, который зайдет в Jira, достанет таски, поймет задачу и выполнит ее."
    "Конечно, лентяем Дэниел не был. Но все свои задачи, которые можно было решить компьютером, он старался закодить."
    "Говорят,  даже в магазин за него ходил робот…"
    "Поэтому, Дэниелу ничего не оставалось, кроме как сидеть на стуле, исследовать однотипный рисунок потолка типового бизнес-центра, разглядывать миловидных девушек на ресепшне и с ехидной улыбкой наблюдать за упорством новеньких стажеров, коих в компанию приходят десятки."
    "Обычно он так и коротал часы в ожидании заветных 18:00. Но сегодня это дурацкое письмо морочило его голову"
    show daniel_angry
    p_D "Хакеры…. Тьфу. Даже звучит оскорбительно. К хакерам идите вк взламывать. Петька из 7Б всем поможет."
    "Желание перемен, любопытство, энтузиазм и, что уж скрывать, романтический азарт захватили голову Дэниела"
    "Обещая себе, что это лишь детская шалость, герой отвечает на письмо…"

#сцена 6

    show fon2_6
    with showdissolve

    "Ответ на письмо пришел неожиданно быстро. Дэниел поначалу даже несколько растерялся."
    "Собеседник по ту сторону монитора уже порядком знал о Дэниеле. И определенно был рад его согласию."
    "К удивлению Дэниела, здесь от него не требовали никаких документов, подписей и бумаг. Зарплата за месяц составляла практически полный его годовой заработок! А вместо собеседования новый знакомый многозначительно ответил:"
    show bg_person1 at right
    N_AT "На практике убедимся в твоих скиллах."
    hide bg_person1
    "Такой расклад событий, несомненно радовал Дэниела, но он чувствовал душой неладное, хотя и пытался отчаянно перестать об этом думать."

#сцене 7

    scene fon2_7
    with showdissolve
    "Впрочем, чувство эйфории и гордости за себя прошло достаточно быстро, и все неторопливо поплыло по давно привычной рутине."
    "Дэниел, по уже проторенному до дыр маршруту, вышел на перрон и плюхнулся в первый вагон метро, который, подобно большому длинному червю, повез людей сквозь городские джунгли."
    "Знаете, Дэниел был чем-то похож на Маркиза де Сада. Скучный быт, скучная жизнь, монотонность. Он определенно в ловушке. Лишь сердце преследует идею абсолютной свободы."

    scene black
    with showdissolve
    pause(3.5)
    jump Day_three
    return
