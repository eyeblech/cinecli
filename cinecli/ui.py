# cinecli/ui.py

from rich.table import Table
from rich.console import Console

console = Console()

def show_movies(movies):
    table = Table(title="🎬 Search Results")

    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Title", style="bold")
    table.add_column("Year", justify="center")
    table.add_column("Rating", justify="center")

    for movie in movies:
        table.add_row(
            str(movie["id"]),
            movie["title"],
            str(movie["year"]),
            str(movie["rating"]),
        )

    console.print(table)

from rich.panel import Panel

def show_movie_details(movie):
    description = (
        movie.get("summary")
        or movie.get("description_full")
        or "No description available."
    )

    text = (
        f"[bold]{movie['title']} ({movie['year']})[/bold]\n\n"
        f"⭐ Rating: {movie['rating']}\n"
        f"⏱ Runtime: {movie['runtime']} min\n"
        f"🎭 Genres: {', '.join(movie.get('genres', []))}\n\n"
        f"{description}"
    )
    console.print(Panel(text, title="🎬 Movie Details", expand=False))


def show_torrents(torrents):
    table = Table(title="🧲 Available Torrents")

    table.add_column("Index", justify="center")
    table.add_column("Quality")
    table.add_column("Size")
    table.add_column("Seeds", justify="center")
    table.add_column("Peers", justify="center")

    for idx, torrent in enumerate(torrents):
        table.add_row(
            str(idx),
            torrent["quality"],
            torrent["size"],
            str(torrent["seeds"]),
            str(torrent["peers"]),
        )

    console.print(table)
