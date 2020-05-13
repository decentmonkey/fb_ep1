label floor1_fountain:
    $ print "enter_floor1_fountain"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_9

    $ scene_name = "floor1_fountain"
    $ scene_caption = t_("Fountain")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Floor1_Fountain" + day_suffix

    $ add_object_to_scene("Fountain", {"type":2, "base":"Floor1_Fountain_Fountain", "click" : "floor1_fountain_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Floor1_Fountain_Curtains", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.2})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Floor1_Fountain_Lamps", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Windows", {"type":2, "base":"Floor1_Fountain_Windows", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Picture", {"type":2, "base":"Floor1_Fountain_Picture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Fountain_Furniture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})

    if gameStage >= 3:
        if bardieLocation == "Floor1":
            $ scene_image = "scene_Floor1_Fountain_Bardie" + day_suffix
            $ add_object_to_scene("Bardie", {"type" : 2, "base" : "Floor1_Fountain_Bardie" + day_suffix, "click" : "bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})


    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor1_fountain_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label floor1_fountain_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor1":
        call change_scene("floor1") from _call_change_scene_15
        return

label floor1_fountain_environment(obj_name, obj_data):
    if obj_name == "Fountain":

        m "Люстра может упасть только в фонтан."

        "Но я же не полезу в него, верно?"
        if gameStage > 2:
            return

        "Так что я в безопасности.
        Можно не бояться этой люстры."

        "Вообще не представляю кому бы понадобилось в него залезать."

        "Может только этой бестолковой Юлии, чтобы что-то в нем почистить?"

        "Наверное Юлия бы не испугалась этого сделать.
        Потому что она просто глупая."

        "Глупость рождает бесстрашие."

        "Мне повезло что я умная!"
