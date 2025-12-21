import typer
from rich.prompt import Prompt
from rich.console import Console

from cinecli.api import search_movies, get_movie_details
from cinecli.ui import (
    show_movies,
    show_movie_details,
    show_torrents,
)
from cinecli.magnets import (
    build_magnet,
    open_magnet,
    download_torrent,
)

# -------------------------------------------------
# App + Console
# -------------------------------------------------

app = typer.Typer(
    help="🎬 CineCLI — Browse and torrent movies from your terminal",
)

console = Console()

# -------------------------------------------------
# Search command
# -------------------------------------------------

@app.command()
def search(
    query: str = typer.Argument(..., help="Movie name to search for"),
    limit: int = typer.Option(10, help="Number of results to show"),
):
    """
    Search movies on YTS
    """
    movies = search_movies(query, limit)

    if not movies:
        console.print("[red]❌ No movies found.[/red]")
        raise typer.Exit(code=1)

    show_movies(movies)

# -------------------------------------------------
# Watch command
# -------------------------------------------------

@app.command()
def watch(movie_id: int):
    """
    View movie details and open torrent (magnet or .torrent file)
    """
    movie = get_movie_details(movie_id)

    show_movie_details(movie)

    torrents = movie.get("torrents", [])
    if not torrents:
        console.print("[red]❌ No torrents available.[/red]")
        raise typer.Exit(code=1)

    show_torrents(torrents)

    index = Prompt.ask(
        "Select torrent index to use",
        choices=[str(i) for i in range(len(torrents))],
    )

    torrent = torrents[int(index)]

    action = Prompt.ask(
        "Choose action",
        choices=["magnet", "torrent"],
        default="magnet",
    )

    if action == "magnet":
        magnet = build_magnet(
            torrent["hash"],
            f"{movie['title']} {torrent['quality']}",
        )
        open_magnet(magnet)
        console.print("[green]🧲 Magnet link opened in your torrent client![/green]")
    else:
        download_torrent(torrent["url"])
        console.print("[green]⬇ Torrent file download started in browser.[/green]")

# -------------------------------------------------
# Interactive command
# -------------------------------------------------

@app.command()
def interactive():
    """
    Interactive movie browser (search → select → torrent)
    """
    query = Prompt.ask("🔍 Search movies")

    movies = search_movies(query, limit=10)
    if not movies:
        console.print("[red]❌ No movies found.[/red]")
        raise typer.Exit()

    # Show movie list
    for idx, movie in enumerate(movies):
        console.print(
            f"[cyan][{idx}][/cyan] "
            f"{movie['title']} ({movie['year']}) "
            f"⭐ {movie['rating']}"
        )

    movie_index = Prompt.ask(
        "Select movie index",
        choices=[str(i) for i in range(len(movies))]
    )

    movie_id = movies[int(movie_index)]["id"]

    movie = get_movie_details(movie_id)
    show_movie_details(movie)

    torrents = movie.get("torrents", [])
    if not torrents:
        console.print("[red]❌ No torrents available.[/red]")
        raise typer.Exit()

    show_torrents(torrents)

    torrent_index = Prompt.ask(
        "Select torrent index",
        choices=[str(i) for i in range(len(torrents))]
    )

    torrent = torrents[int(torrent_index)]

    action = Prompt.ask(
        "Choose action",
        choices=["magnet", "torrent"],
        default="magnet"
    )

    if action == "magnet":
        magnet = build_magnet(
            torrent["hash"],
            f"{movie['title']} {torrent['quality']}"
        )
        open_magnet(magnet)
        console.print("[green]🧲 Magnet opened in torrent client![/green]")
    else:
        download_torrent(torrent["url"])
        console.print("[green]⬇ Torrent file download started.[/green]")

# -------------------------------------------------
# Entry point
# -------------------------------------------------

if __name__ == "__main__":
    app()
