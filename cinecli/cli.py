import typer
from rich.prompt import Prompt

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

app = typer.Typer(
    help="🎬 CineCLI — Browse and torrent movies from your terminal",
    invoke_without_command=False,
)


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
        typer.echo("❌ No movies found.")
        raise typer.Exit(code=1)

    show_movies(movies)


@app.command()
def watch(movie_id: int):
    """
    View movie details and open torrent (magnet or .torrent file)
    """
    movie = get_movie_details(movie_id)

    show_movie_details(movie)

    torrents = movie.get("torrents", [])
    if not torrents:
        typer.echo("❌ No torrents available for this movie.")
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
        typer.echo("🧲 Magnet link opened in your torrent client!")
    else:
        download_torrent(torrent["url"])
        typer.echo("⬇️ Torrent file download started in browser.")


if __name__ == "__main__":
    app()
