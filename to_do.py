import config

while True:
    operation = input('operation: \n')
    if operation == 'create' or operation == '+':
        config.create()
    elif operation == 'remove' or operation == '-':
        config.remove()
    elif operation == 'overwrite' or operation == "=":
        config.overwrite()
    elif operation == 'all':
        config.show_all()
    elif operation == 'exit':
        break
