import comfig

while True:
    operation = input('operation: \n')
    if operation == 'create' or operation == '+':
        comfig.create()
    elif operation == 'exit':
        break
