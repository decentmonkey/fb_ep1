default miniMapData = []
default miniMapSubst = {}
default miniMapEnabledOnly = []
default miniMapDisabled = []
default miniMapTurnedOff = False
default miniMapOpened = False

label miniMapOpen:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = True
    show screen hud_minimap(miniMapData)
    return
label miniMapClose:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = False
    show screen hud_minimap(miniMapData)
    return

label miniMapHouseGenerate:
    $ miniMapOpened = False
    $ miniMapData = []
    $ miniMapData.append({"name":"Bedroom", "caption":t_("Bedroom"), "img":"Bedroom_Map", "teleport_scene":"bedroom2", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Bathroom", "caption":t_("Bathroom"), "img":"Bathroom_Map", "teleport_scene":"bathroom_bath", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Floor1", "caption":t_("Down Floor"), "img":"Floor1_Map", "teleport_scene":"floor1", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Floor2", "caption":t_("Up Floor"), "img":"Floor2_Map", "teleport_scene":"floor2", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Kitchen", "caption":t_("Kitchen"), "img":"Kitchen_Map", "teleport_scene":"kitchen2", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Basement", "caption":t_("Basement"), "img":"Basement_Map", "teleport_scene":"basement_pool", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Yard", "caption":t_("Street Yard"), "img":"Street_Yard_Map", "teleport_scene":"house_out", "teleport_type":"function"})
    return

label miniMapDisabled(name, minimapCell):
    sound snd_ui_not_working
    return

label miniMapAddDisabled(name):
    if name not in miniMapDisabled:
        $ miniMapDisabled.append(name)
    return

label miniMapRemoveDisabled(name):
    if name in miniMapDisabled:
        $ miniMapDisabled.remove(name)
    return

label miniMapHouseGenerateTeleport(name, minimapCell):
    if interface_blocked_flag == True:
        return
#    $ print renpy.get_screen("say")
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    $ _return = True
    if miniMapSubst.has_key("all") and miniMapSubst["all"] != False:
        call expression miniMapSubst["all"] from _call_expression_10
    if miniMapSubst.has_key(name) and miniMapSubst[name] != False:
        call expression miniMapSubst[name] from _call_expression_11
    if _return != False:
        if minimapCell["teleport_type"] == "function":
            call expression minimapCell["teleport_scene"] from _call_expression_12
        if minimapCell["teleport_type"] == "scene":
            call change_scene(minimapCell["teleport_scene"]) from _call_change_scene_153
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
