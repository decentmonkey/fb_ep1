label monica_office_cabinet:
    $ print "enter_monica_office_cabinet"
    $ miniMapData = []

    $ scene_name = "monica_office_cabinet"
    $ scene_caption = t_("Monica's Office")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Office_Monica_Cabinet_Monica_" + cloth + day_suffix
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Cabinet_Monica_" + cloth, "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Flowers", {"type" : 2, "base" : "Office_Monica_Cabinet_Flowers", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0, "b":0.15})
    $ add_object_to_scene("Paints", {"type" : 2, "base" : "Office_Monica_Cabinet_Paints", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0, "b":0.15})
    $ add_object_to_scene("Table", {"type" : 2, "base" : "Office_Monica_Cabinet_Table", "click" : "monica_office_cabinet_environment", "actions" : "lw", "zorder":1})
    $ add_object_to_scene("Windows", {"type" : 2, "base" : "Office_Monica_Cabinet_Windows", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Projector", {"type" : 2, "base" : "Office_Monica_Cabinet_Projector", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":0})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : t_("К СЕКРЕТАРЮ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_cabinet_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_cabinet_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary") from _call_change_scene_77
        return
    return
label monica_office_cabinet_environment(obj_name, obj_data):
    if obj_name == "Monica":
        m "Мой...
        Офис..."
    if obj_name == "Projector":
        m "Этот световой проектор я иногда использую для презентаций."
        "Я могу опускать экран на противоположной стене."
        "Иногда надо показать презентацию.
        Но до всех можно донести информацию просто словами."
        "Ведь не все такие умные как Я!!"
        call bitch(1, "monica_office_cabinet_projector") from _call_bitch_72

    if obj_name == "Flowers":
        m "Цветы украшают не только мой дом, но и мой офис."
    if obj_name == "Paints":
        m "Marcela Gutierrez, в моем офисе."
        "Это модно."
    if obj_name == "Windows":
        m "Из этих окон ужасный вид на город.
        Там дым и машины!"
        "Поэтому я закрыла их, чтобы не портить себе настроение!"
    if obj_name == "Table":
        if obj_data["action"] == "l":
            m "Мой стол, за которым я провожу время во время работы."
            "Я работаю когда у меня есть настроение."
            "Я вовсе не обязана это делать, в отличие от других."
        if obj_data["action"] == "w":
            call change_scene("monica_office_cabinet_table") from _call_change_scene_78
            return
    return








#
