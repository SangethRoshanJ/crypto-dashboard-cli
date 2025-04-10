import requests
from rich.console import Console
from rich.table import Table

console = Console()

def show_trending():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/search/trending")
        data = response.json()['coins']

        table = Table(title="🔥 Trending Cryptocurrencies", style="white on black")

        table.add_column("Rank", style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Symbol", style="green")
        table.add_column("Market Cap Rank", style="yellow")

        for i, coin in enumerate(data, start=1):
            info = coin['item']
            table.add_row(str(i), info['name'], info['symbol'].upper(), str(info['market_cap_rank']))

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")