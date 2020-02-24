import os

def show_all():
    for i in os.listdir('tasks'):
        print(i)


def overwrite():
    task = input('enter name of overwrite task: ')
    task = open('tasks/' + task + '.txt', 'w')
    text = input('new text: ')
    task.write(text)
    task.close()


def remove():
    task = input('enter name of remove task: ')
    os.remove('tasks/' + task + '.txt')


def create():
    task_name = input('enter task name: ')
    task = open('tasks/' + task_name + '.txt', 'w')
    text = input('enter your task : ')
    task.write(text)
    task.close()
