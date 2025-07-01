#This is error-handler for libmanon, log function is for recording errors in Error_logs.txt for tracebag

#Function to record errors
def log(words:any, type:str='Error'):
    try:
        with open('lib.env.blib', 'r') as dd:
            data=dd.read()
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
                    al.append()
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

def correction():
    import os
    def cor(file):
        try:
            os.remove(os.path.join(os.path.pardir(__file__), file+'.py'))
        except:
            pass
        os.system(f'git clone https://github.com/rish27c/{file}.git')
    print('Rescue Mode Activated!')
    print()
    print('Type: "librr -h", for help.')
    print()
    os.system('pip install git')
    while True:
        lr=input('Rescue>')
        if lr=='':
            continue
        lr=lr.strip(); lr=lr.split()
        if lr[0]=='quit':
            exit()
        elif lr[0]=='conf' or lr[0]=='config':
            if lr[1]=='-del':
                os.remove('config.blib')
        elif lr[0]=='recover':
            for i in lr[1:]:
                if i=='librr':
                    print('[Info] Self-recovery cannot be done while file is running\n\tRun: sr.py')
                elif i=='lidata':
                    print('Recovering: libdata (Data-handler)')
                    cor('libdata')
                elif i=='liber':
                    print('Recovering: liber (Task-handler)')
                    cor('liber')
                elif i=='libman':
                    print('Recovering: libman (Main-handler)')
                    cor('libman')
                elif i=='libprocess':
                    print('Recovering: libprocess (data-process-handler)')
                    cor('libprocess')
                elif i=='*':
                    print('To recover all files, type: "Fake Crash librr"')
                elif i=='sr':
                    try:
                        os.remove(os.path.join(os.path.pardir(__file__), 'sr.py'))
                    except:
                        pass
                    with open(os.path.join(os.path.pardir(__file__), 'sr.py'), 'w') as f:
                        f.write('''import os
pth=os.path.pardir(__file__)
os.remove(os.path.join(pth, '__init__.py'))
os.remove(os.path.join(pth, librr.py))
with open('__init__.py', 'w') as f:
    f.write()
os.system('git clone https://github.com/rish27c/librr.git')''')
                else:
                    print(f'Unknown flag: {i}\nSkipping...')
        elif lr[0]=='Fake' and lr[1]=='Crash' and lr[2]=='librr':
            raise Exception('Fake Crash was initiated...')