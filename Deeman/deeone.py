import deezloader

link = "https://www.deezer.com/en/track/486361382"
arl = "063df3f1d2e45edd2dd01d2a69349ee2d857cc00d45f7a88ff64993d50a0b2e78ab83a7c290fbec4395a74dc6d9feb6519bf3f2191eeaccf87da8359a2c7b18c674682df59d83629956cd47be3f2d557e865cc4b3b705cf0ab7021a4471b48ef"
samini = "https://www.deezer.com/en/track/428150842"

downloa = deezloader.Login(arl)

downloa.download_trackdee(
    samini,
    output = "./",
    quality = "MP3_320",
    recursive_quality = False,
    recursive_download = False,
    not_interface = False
)