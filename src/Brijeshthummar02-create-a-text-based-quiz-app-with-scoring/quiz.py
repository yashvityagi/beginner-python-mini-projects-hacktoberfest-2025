# Text-Based Quiz App with Scoring

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) London", "c) Berlin"],
        "answer": "a"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["a) 7", "b) 8", "c) 9"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter"],
        "answer": "b"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["a) Atlantic", "b) Indian", "c) Pacific"],
        "answer": "c"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen"],
        "answer": "b"
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Text-Based Quiz App!")
    print("Answer each question by typing a, b, or c.\n")
    
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer: ").lower().strip()
        if ans == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    
    print(f"Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent! You got all answers right.")
    elif score >= len(questions) // 2:
        print("Good job!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    run_quiz()