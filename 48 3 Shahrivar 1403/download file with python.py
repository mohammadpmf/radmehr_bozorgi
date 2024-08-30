import requests
url = 'https://opengameart.org/sites/default/files/audio_preview/33_-_adventure_cats_pirate_radio.ogg.mp3'
r = requests.get(url, allow_redirects=True)
open('dld.mp3', 'wb').write(r.content)