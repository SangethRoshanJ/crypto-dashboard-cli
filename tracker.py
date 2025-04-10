import time
from rich.console import Console
from rich.live import Live
from rich.table import Table
from utils import get_crypto_price

console = Console()

def run_tracker(symbol):
    with Live(console=console, refresh_per_second=1) as live:
        while True:
            try:
                price = get_crypto_price(symbol)
                table = Table(title=f"Real-Time Price: {symbol.upper()}", style="white on black")

                table.add_column("Symbol", style="cyan")
                table.add_column("Price (USD)", style="green")
                table.add_row(symbol.upper(), f"${price:,.2f}")

                live.update(table)
                time.sleep(5)
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")
                break