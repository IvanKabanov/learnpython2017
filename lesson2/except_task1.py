def get_answer(question):
    answers = {'привет': 'И тебе привет!', 'как дела?': 'Отлично!', 'пока': 'До свидания!'}
    lower_question = question.lower()
    print(answers.get(lower_question, "Don't understand you!"))
    
def ask_user():
    try:
        user_input = ''
        while user_input != 'пока':
            user_input = input("Каков твой вопрос? ").lower()
            get_answer(user_input)
    except KeyboardInterrupt:
        print("  До свидания!") 
    

ask_user()


    
