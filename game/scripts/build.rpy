init python:
    # Declare two archives.
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("sounds", "all")
    build.archive("music", "all")
    build.archive("video", "all")

    # Put script files into the scripts archive.
    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")

    # Put images into the images archive.
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")

    # Put sounds into the sounds archive.
    build.classify("game/Sounds/*.ogg", "sounds")

    # Put music into the music archive.
    build.classify("game/Music/*.ogg", "music")

    # Put video into the video archive.
    build.classify("game/video/*.mp4", "video")
    build.classify("game/video/*.mkv", "video")
    build.classify("game/video/*.webm", "video")
