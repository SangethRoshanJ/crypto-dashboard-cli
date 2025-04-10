from tracker import run_tracker
from dashboard import show_trending

def main():
    print("📈 Welcome to the Real-Time Crypto Dashboard!\n")
    print("1. 🔥 Show Trending Coins")
    print("2. 📊 Track Custom Coin in Real-Time")
    print("0. ❌ Exit")

    while True:
        choice = input("\nEnter your choice (0-2): ")

        if choice == "1":
            show_trending()
        elif choice == "2":
            symbol = input("Enter the coin symbol (e.g., btc, eth): ").lower()
            run_tracker(symbol)
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()