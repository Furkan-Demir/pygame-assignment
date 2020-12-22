import json
def save_func(kare):
    try:
        kare_bilgi = {"maxcan":kare.max_can,
        "hasar":kare.hasar,
        "maxsarjor":kare.max_sarjor,
        "para":kare.para,
        "stage":kare.stage}
        with open('player.txt', 'w+') as _player:
            json.dump(kare_bilgi, _player)
        return True
    except:
        return False

def load_func(kare):
    try:
        with open('player.txt') as _player:
            data = json.load(_player)
        kare.max_can = data["maxcan"]
        kare.hasar = data["hasar"]
        kare.max_sarjor = data["maxsarjor"]
        kare.para = data["para"]
        kare.stage = data["stage"]
        return True
    except:
        return False
