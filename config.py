import os


def remove():
    task = input('enter name of remove task: ')
    os.remove('tasks/' + task + '.txt')


def create():
    task_name = input('enter task name: ')
    task = open('tasks/' + task_name + '.txt', 'w')
    text = input('enter your task : ')
    task.write(text)
    task.close()
