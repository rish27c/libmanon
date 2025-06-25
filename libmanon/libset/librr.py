#This is error-handler for libmanon, log function is for recording errors in Error_logs.txt for tracebag

#Function to record errors
def log(words:any, type:str='Error'):
    try:
        with open('Debug.blib', 'r') as dd:
            data=dd.read()
        if data=='Debug:True':
            deb=True
        else:
            deb=False
    except:
        deb=False
    try:
        with open('Error_logs.txt', 'r') as report:
            logs=report.read()
        c=logs.count('Log#')+1
        logs=logs.split('\n')
    except:
        c=1
        logs=[]
    if type!='#None*~':
        record=f'[{type} Log#{c}] {words}'
    else:
        record=f'[Log#{c}] {words}'
    logs.append(record)
    if deb==True:
        print('>>', record)
    record='\n'.join(logs)
    with open('Error_logs.txt', 'w') as crash:
        crash.write(record)

def debug(tf:str='None'):
    try:
        tf=int(tf)
        tf=bool(tf)
        tf=str(tf)
        #Allows numbers(0s and 1s) as boolean values
    except:
        pass
    if tf=='True':
        with open('Debug.blib', 'w') as dd:
            dd.write('Debug:True')
    elif tf=='False':
        try:
            import os
            os.remove('Debug.blib')
        except:
            pass
    else:
        if tf.lower() in ['true', 'false']:
            print(f'\nIt\'s not "{tf}", it\'s "{tf.capitalize()}"\n')
        else:
            print(f'\n"{tf}" -> debug only accepts value: ["True", "False"]\n', flush=True)