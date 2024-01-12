def compare_answers(answers_file, responses_file):
    with open(answers_file, 'r') as e_file, open(responses_file, 'r') as a_file:
        correct_answers = e_file.read().splitlines()
        user_responses = a_file.read().splitlines()
        wrong_amount = 0
        for i, (correct, response) in enumerate(zip(correct_answers, user_responses), start=1):
            if correct != response:
                wrong_amount = wrong_amount + 1
                print(f"Question {i}: Your answer was {response}, correct answer is {correct}")
        print(f"\n\n[ANALYSIS]\n\nYou got {wrong_amount} questions wrong, and {54 - wrong_amount} right.\nThat is a about\n{round(((54-wrong_amount)/54) * 100,2)}% correct, and {round((wrong_amount/54)*100,2)}% wrong.\nDo better next time!\n")
compare_answers('answers.txt', 'responses.txt')
