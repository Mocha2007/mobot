from random import shuffle

# q format:
# ((sum, play count), question, [right answers], [wrong answers]),
# u format:
# id: (sum, play count)
questions = []
users = {}


def elo(responses: (int, int)) -> float:
	# assert len(responses) == 2
	# assert responses[0] >= 0 <= responses[1] and type(responses[0]) == int == type(responses[1])
	try:
		return responses[0] / responses[1]
	except ZeroDivisionError:
		return 1000


def addgame(question_id: int, p_elo: float, result: bool):
	q = list(questions[question_id][0])
	q[0] += p_elo + 400 * (1 if result else -1)
	q[1] += 1
	questions[question_id][0] = tuple(q)


def ask_question(question_id: int) -> str:
	shuffle(questions[question_id][2])
	shuffle(questions[question_id][3])
	q = questions[question_id][1]
	a_correct = questions[question_id][2][:1]
	a_incorrect = questions[question_id][3][:3]
	a = a_incorrect + a_correct
	shuffle(a)
	return 'Q: '+q+'\n'+'\n'.join(a)


def check_answer(question_id: int, response: str) -> bool:
	return response in questions[question_id][2]
