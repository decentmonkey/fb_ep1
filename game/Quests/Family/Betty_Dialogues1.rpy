label bettyDialogue1:
    #render+
    #Моника говорит с Бетти в спальне днем (у зеркала)
    music Groove2_85
    img 5801
#    imgr Dial_Betty_1
    with fadelong
    betty "Я буду следить за тем как ты работаешь."
    music casualMusic
    call refresh_scene_fade() from _call_refresh_scene_fade_58
    return
