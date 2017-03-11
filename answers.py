def get_answer(question):
	answers = {'привет': 'И тебе привет!', 'как дела?': 'Отлично!', 'до свидания': 'пока'}
	lower_question = question.lower()
	print(answers.get(lower_question, 'Don\'t understand you!'))
	return answers.get(lower_question)
	
user_question = input('Enter question ')
get_answer(user_question)





