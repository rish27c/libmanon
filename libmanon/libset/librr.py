#This is error-handler for libmanon, log function is for recording errors in Error_logs.txt for tracebag

#Function to record errors
def log(words:any, type:str='Error'):
    try:
        with open('lib.env.blib', 'r') as dd:
            data=dd.read()
        deb=False
        data=data.split('\n')
        for i in data:
            i=i.strip()
            if i=='Debug:True':
                deb=True
            elif i=='Debug:False':
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
        with open('lib.env.blib', 'r') as df:
            dd=df.read()
        dd=dd.split('\n')
        dd.append('Debug:True')
        dd='\n'.join(dd)
        with open('lib.env.blib', 'w') as df:
            df.write(dd)
    elif tf=='False':
        try:
            with open('lib.env.blib', 'r') as df:
                dd=df.read()
            dd=dd.split('\n')
            al=[]
            for i in dd:
                if i[0:6]!='Debug:':
                    al.append(i)
            dd='\n'.join(al)
            with open('lib.env.blib', 'w') as df:
                df.write(dd)
        except:
            log('Missing "lib.env.blib" file')
            raise FileNotFoundError('Missing env file that deals with var handling.')
    else:
        if tf.lower() in ['true', 'false']:
            print(f'\nIt\'s not "{tf}", it\'s "{tf.capitalize()}"\n')
        else:
            print(f'\n"{tf}" -> debug only accepts value: ["True", "False"]\n', flush=True)

def env(tf:str='None'):
    try:
        tf=int(tf)
        tf=bool(tf)
        tf=str(tf)
        #Allows numbers(0s and 1s) as boolean values
    except:
        pass
    if tf=='True':
        with open('lib.env.blib', 'r') as df:
            dd=df.read()
        dd=dd.split('\n')
        dd.append('Env:bk')
        dd='\n'.join(dd)
        with open('lib.env.blib', 'w') as df:
            df.write(dd)
    elif tf=='False':
        try:
            with open('lib.env.blib', 'r') as df:
                dd=df.read()
            dd=dd.split('\n')
            al=[]
            for i in dd:
                if i[0:4]!='Env:':
                    al.append(i)
            dd='\n'.join(al)
            with open('lib.env.blib', 'w') as df:
                df.write(dd)
        except:
            log('Missing "lib.env.blib" file')
            raise FileNotFoundError('Missing env file that deals with var handling.')
    else:
        if tf.lower() in ['true', 'false']:
            print(f'\nIt\'s not "{tf}", it\'s "{tf.capitalize()}"\n')
        else:
            print(f'\n"{tf}" -> debug only accepts value: ["True", "False"]\n', flush=True)