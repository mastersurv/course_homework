def game(word, list_word):
	"""
	Функция для игры в угадывание слов.

	Parameters:
	    word (str): Длинное слово, которое нужно угадать.
	    list_word (list): Список возможных ответов.

	Returns:
	    None
	"""
	# Выводим длинное слово, которое нужно угадать
	print(word)
	# Инициализируем список ответов
	answer = list_word
	# Инициализируем счетчик очков
	score = 0
	# Получаем первый ответ от игрока
	player = input('Введите ваше слово: \n').lower()
	# Начинаем бесконечный цикл игры
	while True:
		# Проверяем, есть ли ответ игрока в списке ответов
		if player in answer:
			# Если ответ правильный, увеличиваем счетчик очков
			score += 1
			# Выводим сообщение об угаданном слове и текущем счете
			print(f'Слово угадано!\nКоличество набранных очков: {score}\n')
			# Удаляем угаданное слово из списка ответов
			answer.remove(player)
			# Проверяем, все ли слова угаданы
			if len(answer) == 0:
				print(f'Игра окончена, все слова отгаданы. Вы набрали следующее количество очков: {score}')
				break
		else:
			# Если ответ неправильный или уже угадан, выводим сообщение об ошибке
			print('Нет такого слова или оно угадано ранее\n')
		# Получаем следующий ответ от игрока
		player = input('Введите ваше слово: \n').lower()


slovo = 'Конкатенация'
otvet = ["кот", "тон", "нота", "нация", "нотация"]
game(slovo, otvet)
slovo2 = "Крокодил"
otvet2 = ["род", "дол", "рок"]
game(slovo2, otvet2)
