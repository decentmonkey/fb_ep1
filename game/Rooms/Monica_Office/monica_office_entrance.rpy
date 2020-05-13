default entranceTalkedWithMonkeys = False
default entranceMonkeys = True
default entranceMonkeysLooked = False

label monica_office_entrance:
    $ print "enter_monica_office_entrance"
    $ miniMapData = []

    $ scene_name = "monica_office_entrance"
    $ scene_caption = _("Monica's Office Entrance")
    $ clear_scene_from_objects(scene_name)

    if entranceMonkeys == True:
        $ scene_image = "scene_Monica_Office_Entrance_Monica_Monkeys_" + cloth
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Monica_Office_Entrance_Monica_Monkeys_" + cloth, "click" : "monica_office_entrance_environment", "actions" : "l", "zorder":10})
        $ add_object_to_scene("Monkeys", {"type" : 2, "base" : "Monica_Office_Entrance_Monkeys", "click" : "monica_office_entrance_environment", "actions" : "lt", "zorder":10})
    else:
        $ scene_image = "scene_Monica_Office_Entrance_Monica_" + cloth
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Monica_Office_Entrance_Monica_" + cloth, "click" : "monica_office_entrance_environment", "actions" : "l", "zorder":10})


    $ add_object_to_scene("Chest", {"type" : 2, "base" : "Monica_Office_Entrance_Chest", "click" : "monica_office_entrance_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Composition", {"type" : 2, "base" : "Monica_Office_Entrance_Composition", "click" : "monica_office_entrance_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Paint", {"type" : 2, "base" : "Monica_Office_Entrance_Paint", "click" : "monica_office_entrance_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Plants", {"type" : 2, "base" : "Monica_Office_Entrance_Plants", "click" : "monica_office_entrance_environment", "actions" : "l", "zorder":0})

    if monicaOfficeDay2PhoneLost == True:
        $ add_object_to_scene("Phone", {"type" : 2, "base" : "Monica_Office_Entrance_Phone", "click" : "monica_office_tea_phone", "actions" : "lh", "zorder":0})


    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : _("ЛИФТ"), "larrow" : "arrow_left_2", "base":"Monica_Office_Entrance_Lift", "click" : "monica_office_entrance_teleport", "xpos" : 691, "ypos" : 884, "zorder":11})
    $ add_object_to_scene("Teleport_Street_Monica_Office", {"type":3, "text" : _("НАЗАД"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_entrance_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_entrance_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary", "Fade_long", "snd_lift") from _call_change_scene_79
        return
    if obj_name == "Teleport_Street_Monica_Office":
        call change_scene("street_monica_office", "Fade_long", "highheels_run2") from _call_change_scene_80
        return

    return
label monica_office_entrance_environment(obj_name, obj_data):
    if obj_name == "Chest":
        m "Это просто декорация.
        Он не открывается на самом деле."
        "Но если кто-то попытается, то я узнаю ;)"
        "Люди должны вести себя прилично, когда находятся в гостях!"
        "Это, можно сказать, своеобразная проверка для них."

    if obj_name == "Composition":
        m "Веселая композиция.
        Я сама подобрала её сюда."

    if obj_name == "Plants":
        m "Я люблю цветы, вы уже знаете об этом..."

    if obj_name == "Paint":
        m "О, Marcela Gutierrez."
        "Я люблю ее работы.
        Я вешаю их повсюду."
        "Здесь, и даже в моем кабинете."
        "Я подумываю о том чтобы повесить одну из ее работ вместо той дурацкой картины мужа, напротив фонтана."

    if obj_name == "Monica":
        m "Это мой личный вход в здание."
        "Я оформила его по своему вкусу."
        "Посторонние здесь появляются очень редко, если только не собираются прямо ко мне на прием."

    if obj_name == "Monkeys":
        if obj_data["action"] == "l":
            $ entranceMonkeysLooked = True
            img 1134
            mt "А это еще что за мартышки?"

            img 1135
            mt "Какие-то убожества."
            w
            return
        if obj_data["action"] == "t":
            if entranceMonkeysLooked == False:
                img 1134
                mt "А это еще что за мартышки?"

                img 1135
                mt "Какие-то убожества."
                $ entranceMonkeysLooked = True
            $ entranceTalkedWithMonkeys = True
            img 1136
            m "Вы кто еще такие?"

            "И чего ждете?"

            img 1137
            gray_mouse "Мэм, мы ждем, когда нас вызовут."

            "Мы никому не мешаем, Мэм!"

            img 1138
            gray_mouse "Не трогайте нас."

            "И идите дальше."

            img 1139
            m "Вот нахалки."

            "Может проучить их?"

            "Ладно, нет времени."
    return
