![PyPI](https://img.shields.io/pypi/v/cinecli)
![Python](https://img.shields.io/pypi/pyversions/cinecli)
![License](https://img.shields.io/badge/license-MIT-green)
![Downloads](https://img.shields.io/pypi/dm/cinecli)


![YTS API Status](https://github.com/eyeblech/cinecli/actions/workflows/api-health.yml/badge.svg)

# 🎬 CineCLI

> Browse, inspect, and launch movie torrents directly from your terminal.  
> Fast. Cross-platform. Minimal. Beautiful.

![Demo](demo.gif)

---

![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-blue)
![CLI](https://img.shields.io/badge/interface-CLI-orange)
![Terminal](https://img.shields.io/badge/works%20in-terminal-black)


## ✨ Features

- 🔍 Search movies from **YTS**
- 🎥 View detailed movie information
- 🧲 Launch magnet links directly into your torrent client
- 📦 Download `.torrent` files if preferred
- ⚡ Auto-select best torrent (highest quality + healthy seeds)
- 🖥 Cross-platform (Linux, macOS, Windows)
- 🎨 Rich, clean terminal UI (powered by `rich`)
- 🧠 Smart defaults with full user control

---

![Built with Typer](https://img.shields.io/badge/built%20with-Typer-ff69b4)
![Built with Rich](https://img.shields.io/badge/built%20with-Rich-blueviolet)


## 📦 Installation

```bash
pip install cinecli

```

Requires **Python 3.9+**

----------

## 🚀 Usage

### 🔎 Search for movies

```bash
cinecli search matrix

```

Displays matching movies with IDs:

```
ID     Title                 Year   Rating
3525   The Matrix            1999   8.7
3526   The Matrix Reloaded   2003   7.2

```

----------

### 🎬 Watch a movie

```bash
cinecli watch 3525

```

What happens:

1.  Shows movie details
    
2.  Lists available torrents
    
3.  Auto-selects the best option (you can override)
    
4.  Launches magnet or downloads `.torrent`
    

----------

### 🧭 Interactive mode (recommended for exploration)

```bash
cinecli interactive

```

-   Search → select movie → choose torrent
    
-   Manual selection by design (safe & explicit)
    

----------

## ⚙️ How magnet launching works

CineCLI delegates magnet handling to your OS.

That means:

-   Whatever torrent client is registered (`qBittorrent`, `Transmission`, etc.)
    
-   CineCLI will launch it directly
    
Example (Linux):

```bash
xdg-mime query default x-scheme-handler/magnet

```

----------

## 🎞 Demo Video

Full terminal walkthrough:

https://github.com/user-attachments/assets/3e3df97f-d1e2-428f-a5a1-54cba121a2f8

----------

## 🛠 Tech Stack

-   **Python**
    
-   **Typer** — CLI framework
    
-   **Rich** — terminal UI
    
-   **Requests** — API communication
    
-   **YTS API** — movie data source
    

----------


## 📄 License

MIT—see [LICENSE](LICENSE).

Use it. Fork it. Improve it.

----------

## 🙌 Author

Built by **eyeblech**  
📧 [0x1123@proton.me](mailto:0x1123@proton.me)

----------

> STAR the repo if you like it! ⭐

![Open Source](https://img.shields.io/badge/open--source-yes-brightgreen)
![Maintained](https://img.shields.io/badge/maintained-yes-success)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-purple)

