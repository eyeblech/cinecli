import webbrowser
import urllib.parse
from transmission_rpc import Client

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

def open_magnet(magnet_url: str, transmission: dict = {}):
    download_torrent(magnet_url, transmission)

def download_torrent(url: str, transmission: dict = {}):
    if transmission.get("enable", False):
        client_options = { k : v for k, v in transmission.items() if k != "enable" }
        Client(**client_options).add_torrent(url)
    else:
        webbrowser.open(url)


def select_best_torrent(torrents: list[dict]) -> dict:
    """
    Pick the torrent with the highest quality and seeds.
    Quality order: 2160p > 1080p > 720p
    """
    quality_rank = {"2160p": 3, "1080p": 2, "720p": 1}

    return max(
        torrents,
        key=lambda t: (quality_rank.get(t["quality"], 0), t.get("seeds", 0))
    )
