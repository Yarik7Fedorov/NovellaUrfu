# DAY 1

init:
    # Persons
    define perDaniel = Character('Дэниел', color="#efc8ff")
    define perMichael = Character('Майкл', color="#f3ffc8")
    define perAuthor = Character('Повествователь', color="#e9530d")


    # Persons Images
    image imgDanielBase = "persons/daniel/daniel_base.png"
    image imgMichaelBase = "persons/michael/michael_base.png"

    # bg
    image bgGrayCity = "bg/day1_scene1.png"
    image bgProgrammerSpace = "bg/day1_scene2.png"
    image bgGraduation = "bg/day1_scene3.png"
    image bgRoutineDays = "bg/day1_scene4.png"
    image bgEmail = "bg/day1_scene5.png"
    image bgOfficeClose = "bg/day1_scene6.png"
    image bgBusStop = "bg/day1_scene7.png"
    image bgBackyard = "bg/day1_scene8.png"

label start:

    scene bgGrayCity
    show imgDanielBase
    with dissolve    
    perDaniel "Я Дэниел Райан, гений, миллиардер, плейбой - это все не про меня."
    perDaniel "Работа инженером по кибербезопасности в этой огромной корпорации еще никого не сделала сильным мира сего."
    perDaniel "Хотя признаюсь, ещё в школе, пока все мои одноклассники впустую тратили свое время, я уже вовсю изучал компьютеры.Мне нравилось копаться в железках"

    scene bgProgrammerSpace
    perDaniel "Вам не кажется, что намного любопытнее всегда смотреть чуть дальше? Видеть больше и знать глужбе?"

    scene bgGraduation
    perDaniel "После окончания ВУЗа передо мной были открыты все двери."
    perDaniel "Сотни HR писали мне, каждая компания жаждила увидеть меня в своих рядах. И что же? Что сейчас?"

    scene bgRoutineDays
    perDaniel "Серые будни сменяются редкими выходными и долгожданным отпуском. Обыденность и день сурка."
    perDaniel "Разве ради этого я жил?"
    perDaniel "Мне говорят остатки знакомых: загадка природы. зачем от гринпарка до дома через давку в вагонах бежать на посадку в автобус, коли есть в рамках диплом, по лавкам торговым..."

    scene bgEmail
    perDaniel "Что ж, отправлять сообщения в конце рабочего дня, а уж тем более открывать их - моветон. Разберу завтра"

    scene bgOfficeClose
    show imgMichaelBase at right
    perMichael "Эй, пора по домам! Или опять ночевать с уборщицами здесь будешь? Жду тебя у гардероба"


    scene bgBusStop
    perDaniel "Что мне, вкалывать в банке как робот?"

    scene bgBackyard
    perDaniel "Казалось бы, создание множества"

    return
