import comfig

while True:
    operation = input('operation: \n')
    if operation == 'create':
        task_name = input('enter task name: ')
        comfig.create(task_name)
    elif operation == 'exit':
        break
