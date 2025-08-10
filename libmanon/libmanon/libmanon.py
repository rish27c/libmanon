try:
    with open('lib.env.blib', 'r') as dd:
        df=dd.read()
    ob=True
    df=df.split('\n')
    for i in df:
        if i=='Env:org':
            ob=True
        elif i=='Env:bk':
            ob=False
except:
    ob=True
    with open('lib.env.blib', 'w') as dd:
        dd.write('Env:org')

try:
    if ob==True:
        from libset import libman
    else:
        from libset import libman_backup
except Exception as e:
    try:
        from libset.librr import log
        log(e)
        print()
        print('Check logs')
        log('To prevent this issue, you may try:\n\t"liber env"')
    except:
        print(f'Failed to log Errors!\n\tPrinting Error due to failure in logging\n\t\tFailure reason: {e}')
    print()
    print('Libman->Crashed')
    print()
    from libset import getpass
    getpass.getpass('Exit...')