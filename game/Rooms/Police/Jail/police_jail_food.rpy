default jailFoodLastScene = ""
default jailFoodInteractLabel = ""
label police_jail_food_scene:
    $ print "enter_police_jail_food_scene"
    $ miniMapData = []

    if scene_name != "police_jail_food_scene":
        $ jailFoodLastScene = scene_name
    $ scene_name = "police_jail_food_scene"
    $ scene_caption = t_("JAIL")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Police_Cell_Food"
    $ add_object_to_scene("Food", {"type":2, "base": "Police_Cell_Food", "click" : "police_jail_food_scene_environment", "actions" : "lh", "zorder" : 1})

    $ cageInteractCnt = cageInteractAmount
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_jail_food_scene_teleport(obj_name, obj_data):
    return
label police_jail_food_scene_environment(obj_name, obj_data):
    if obj_name == "Food":
        if act == "l":
            mt "БОЖЕ! НУ И МЕРЗОСТЬ!!!"
        if act == "h":
            mt "Моника! Заставь себя! Иначе ты умрешь с голода!!!"
            sound snd_eating
            stop music fadeout 1.0
            sound snd_eating
            call textonblack(t_("Спустя 5 минут...")) from _call_textonblack_16
            img black_screen
            with Dissolve(1)
            call change_scene(jailFoodLastScene, "Fade", False) from _call_change_scene_191
            call expression jailFoodInteractLabel from _call_expression_14
            return

    return
