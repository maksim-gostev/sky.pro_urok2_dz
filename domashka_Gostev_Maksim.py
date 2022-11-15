# Создаём два списка
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]


def runner():
    readiness_response = input('Привет! Что бы вы хотели cделать?'
                               ' Если проверить свои знания английского!'
                               ' Наберите "ready", чтобы начать!\n'
                               'Если добавить вопровы напишите "question"'
                               'Закончить напишите "exit"\n')

    if readiness_response == "ready":
        return check_of_knowledge()
    elif readiness_response == "question":
        return questions_adding()
    elif readiness_response == "exit":
        return function_exit()
    else:
        print('Непонятный ответ. Попробуйте ответить снова')
        return runner()


# Оброботка  ответов
def check_of_knowledge():
    # Создаем счетчик для баллов
    points = 0
    # Создаем счетчик правельных ответов
    counter = 0
    answer_ending = ['вопрос', 'вопроса', 'вопросов']
    for i in range(len(questions)):
        # Создаем счетчик попыток
        attempts = 3
        while attempts > 0:
            user_answer = input(questions[i] + ': \n')
            if user_answer == answers[i]:
                print('Ответ верный!')
                counter += 1
                points += attempts
                break
            attempts -= 1
            if attempts > 0:
                print(f'Осталось попыток: {attempts}, попробуйте еще раз!')
            else:
                print(f'Увы, но нет. Верный ответ: {answers[i]}')
    if counter > 100:
        counter_100d = counter % 100
        if counter_100d == 0:
            answer_ending = answer_ending[2]
        elif counter_100d == 1:
            answer_ending = answer_ending[0]
        elif 0 < counter_100d < 5:
            answer_ending = answer_ending[1]
        else:
            answer_ending = answer_ending[2]
    elif counter > 20:
        counter_d10 = counter % 10
        if counter_d10 == 0:
            answer_ending = answer_ending[2]
        elif counter_d10 == 1:
            answer_ending = answer_ending[0]
        elif 0 < counter_d10 < 5:
            answer_ending = answer_ending[1]
        else:
            answer_ending = answer_ending[2]
    else:
        if counter == 0:
            answer_ending = answer_ending[2]
        elif counter == 1:
            answer_ending = answer_ending[0]
        elif 0 < counter < 5:
            answer_ending = answer_ending[1]
        else:
            answer_ending = answer_ending[2]
    # Вывод результатов
    print(f'Вот и все! Вы ответили на {counter} {answer_ending} из {i + 1} верно,'
          f' вы набрали {points} баллов.')
    return runner()


# Добовление вопросов
def questions_adding():
    question_new = input('Напишите новый вопрос:\n')
    new_answer = input('Напишите ответ на него:\n')
    questions.append(question_new)
    answers.append(new_answer)
    return continuation_of_addition()


def continuation_of_addition():
    continuation = input('Хотите ещё добавить вопрос если да то напишите "yes" ,\n'
                         'если нет то напишите "no":\n')
    if continuation == "yes":
        return questions_adding()
    elif continuation == 'no':
        return runner()
    else:
        print('Непонятный ответ поробуёте ответить снова')
        return continuation_of_addition()


# Выход
def function_exit():
    print('Всего доброго')


runner()
