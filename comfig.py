def create():
    task_name = input('enter task name: ')
    task = open('tasks/' + task_name + '.txt', 'w')
    text = input('enter your task : ')
    task.write(text)
    task.close()
