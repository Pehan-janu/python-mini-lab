print("🖥️  Welcome to the Ultimate Computer Hardware Quiz! 🖥️")
print("Test your knowledge of computer components and acronyms!")
print("-" * 50)

playing = input("Are you ready to challenge yourself? (yes/no): ")
if playing.lower() not in ["yes", "y", "yeah", "sure"]:
    print("Maybe next time! Thanks for stopping by. 👋")
    quit()

print("\n🎮 Excellent! Let's begin the challenge!")
print("Type your answers carefully - spelling matters!\n")

score = 0
total_questions = 10

# Question 1
print("Question 1/10:")
answer = input("Most popular operating system? (Hint: Starts with 'W') ")
if answer.lower() in ["windows", "microsoft windows"]:
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Windows")

print()

# Question 2
print("Question 2/10:")
answer = input("Apple's laptop line? (Hint: Mac____) ")
if answer.lower() in ["macbook", "mac book"]:
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: MacBook")

print()

# Question 3
print("Question 3/10:")
answer = input("Popular web browser by Google? ")
if answer.lower() == "chrome":
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Chrome")

print()

# Question 4
print("Question 4/10:")
answer = input("What does AI stand for? (Two words) ")
if answer.lower() == "artificial intelligence":
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Artificial Intelligence")

print()

# Question 5
print("Question 5/10:")
answer = input("Microsoft's search engine? ")
if answer.lower() == "bing":
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Bing")

print()

# Question 6
print("Question 6/10:")
answer = input("What connects devices wirelessly? (Hint: B_______) ")
if answer.lower() == "bluetooth":
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Bluetooth")

print()

# Question 7
print("Question 7/10:")
answer = input("Tesla CEO's first name? ")
if answer.lower() == "elon":
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Elon")

print()

# Question 8
print("Question 8/10:")
answer = input("Popular video platform by Google? ")
if answer.lower() == "youtube":
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: YouTube")

print()

# Question 9
print("Question 9/10:")
answer = input("What does VPN stand for? (First word only) ")
if answer.lower() == "virtual":
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Virtual")

print()

# Question 10
print("Question 10/10:")
answer = input("Most popular programming language in 2024? ")
if answer.lower() in ["python", "javascript", "js"]:
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect! Answer: Python/JavaScript")

# Results
print("\n" + "=" * 50)
print("📊 QUIZ RESULTS 📊")
print("=" * 50)
print(f"You answered {score} out of {total_questions} questions correctly!")

percentage = (score / total_questions) * 100
print(f"Your score: {percentage:.1f}%")

# Performance feedback
if percentage == 100:
    print("🏆 Perfect score! You're a computer hardware expert! 🏆")
elif percentage >= 75:
    print("🌟 Great job! You have solid knowledge of computer hardware!")
elif percentage >= 50:
    print("👍 Not bad! You're on the right track. Keep learning!")
else:
    print("📚 Keep studying! Computer hardware is fascinating once you dive deeper!")

print("\nThanks for playing! 🎯")