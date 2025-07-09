import random

print("🎮 Rock-Paper-Scissors Game")
print("Choose one: rock, paper, or scissors")

user_score = 0
comp_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("👉 Your choice: ").lower()
    if user_choice not in options:
        print("❌ Invalid choice. Try again!")
        continue

    comp_choice = random.choice(options)
    print(f"🤖 Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("⚖️ It's a tie!")
    elif (
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "scissors" and comp_choice == "paper") or
        (user_choice == "paper" and comp_choice == "rock")
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round.")
        comp_score += 1

    print(f"📊 Score — You: {user_score} | Computer: {comp_score}")

    play_again = input("🔁 Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break