import webbrowser
import urllib.parse

TRACKERS = [
    "udp://open.demonii.com:1337/announce",
    "udp://tracker.openbittorrent.com:80/announce",
    "udp://tracker.coppersurfer.tk:6969/announce",
    "udp://glotorrents.pw:6969/announce",
]

def build_magnet(hash_: str, name: str) -> str:
    trackers = "".join(f"&tr={urllib.parse.quote(t)}" for t in TRACKERS)
    dn = urllib.parse.quote(name)
    return f"magnet:?xt=urn:btih:{hash_}&dn={dn}{trackers}"

def open_magnet(magnet_url: str):
    webbrowser.open(magnet_url)

def download_torrent(torrent_url: str):
    webbrowser.open(torrent_url)
