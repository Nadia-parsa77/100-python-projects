print("Welcome to the Smart Quiz Game!")

playing = input("Do you want to play? (yes/no): ").strip().lower()

if playing != "yes":
  print("Maybe next time! ")
  quit()

print("Okay, lets play!\n")

questions = {
    "What does URL stand for? " : "uniform resource locator",

    "What does DNS stand for? " : "domain name system",

    "What does VPN stand for? " : "virtual private network",

    "What does API stand for? " : "application programming interface",

    "What does USB stand for? " : "universal serial bus",
                 
}

score = 0

for question, correct_answer in questions.items():
  answer = input(question).strip().lower()
  if answer == correct_answer:
    print("Correct!\n")
    score += 1
  else:
    print(f"Incorrect! The correct answer was: {correct_answer}\n")


percentage = (score / len(questions)) * 100
print(f"You got {score} out of {len(questions)} correct!")
print(f"Your score: {percentage}%")
