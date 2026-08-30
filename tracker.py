import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def fetch_anime_stats(username):
    # Fixed GraphQL query structure for AniList
    query = '''
    query ($username: String) {
      User (name: $username) {
        name
        statistics {
          anime {
            count
            meanScore
            minutesWatched
            episodesWatched
          }
        }
      }
    }
    '''
    url = 'https://graphql.anilist.co'
    try:
        response = requests.post(url, json={'query': query, 'variables': {'username': username}}, timeout=10)
        data = response.json()
        if 'errors' in data:
            return None
        return data
    except Exception:
        return None

def display_stats(data):
    user = data['data']['User']
    anime_stats = user['statistics']['anime']
    
    minutes = anime_stats.get('minutesWatched', 0)
    episodes = anime_stats.get('episodesWatched', 0)
    count = anime_stats.get('count', 0)
    mean_score = anime_stats.get('meanScore', 0.0)
    
    days_watched = round(minutes / 1440, 1)

    table = Table(title=f"[bold magenta]Anime Profile: {user['name']}[/bold magenta]")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    table.add_row("Total Anime", str(count))
    table.add_row("Episodes Watched", f"{episodes:,}")
    table.add_row("Time Spent", f"{days_watched} Days ({minutes:,} mins)")
    table.add_row("Mean Score", f"{mean_score:.1f} / 100")

    console.print(Panel(table, expand=False))

if __name__ == "__main__":
    username = input("Enter AniList Username: ").strip()
    data = fetch_anime_stats(username)
    if data and data.get('data') and data['data'].get('User'):
        display_stats(data)
    else:
        console.print("[bold red]User not found or AniList server unreachable.[/bold red]")