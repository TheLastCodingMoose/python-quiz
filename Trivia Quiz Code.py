def main():

    print("Welcome to the Quiz!")
    print("Let's test your knowledge.\n")
    
    score = 0 # Initialize score
    
    #List of questions: each question is a dictionary with the question text and the correct answer.
    
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "answer_letters": ["c"],
            "answer_words": ["paris"]
            
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
            "answer_letters": ["b"],
            "answer_words": ["mars"]
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain"],
            "answer_letters": ["b"],
            "answer_words": ["William shakespeare"]
        }
    ]
    
    # Loop through each question and ask the user for their answer.
    
    for i, q in enumerate(questions, start = 1):
        print(f"{i}. {q['question']}")
        for choice in q['choices']:
            print(choice)
        answer = input("Your Answer is: ").lower().strip()
    
        # Check if the answer matches letter or full word(s)
        if answer in q["answer_letters"] or answer in q["answer_words"]:
            print('\nCorrect! 🎉\n')
            score += 1
        else:
            correct_letter = q["answer_letters"][0]
            correct_word = q["answer_words"][0].title()
            print(f"\nIncorrect. The correct answer is {correct_letter}) {correct_word}. 🙁 \n")
    
    #This prints a line of starts after each question to break them up and make it easier to read.
    
        SEPARATOR_LENGTH = 50
        print("*" * SEPARATOR_LENGTH)
        
        print() # Bank line for spacing below the stars
    
    # Final Score Output
    print(f"You've got {score} out of {len(questions)} correct.")
        
if __name__ == '__main__':
    main()