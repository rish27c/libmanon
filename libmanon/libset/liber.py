#This is an important file that handles commands

from librr import log
import sys
from time import ctime


def sug(entry:str, words:list):
    #This function is to sort out and give suggestions that were provided by suggest
    s=suggest(entry=entry, words=words)
    if len(s)>1:
        sl=', '.join(s[0:-1])
        sl+=' or '+s[-1]
        print(f'\nSuggestion: Did you mean {sl} instead of "{entry}"?\n')
    elif len(s)==1:
        sl=s[0]
        print(f'\nSuggestion: Did you mean {sl} instead of "{entry}"?\n')
    else:
        print(f'\nErLib: Unknown arguement "{entry}" was recieved in liber ¯\\_(ツ)_/¯\n', flush=True)

#This function will br for suggestions
def suggest(entry:str, words:list):
    ls=[]
    for i in words:
        ls+=[0]
    #Give points for words
    for i in range(len(words)):
        if len(entry)>=len(str(words[i])):
            c=len(str(words[i]))
        else:
            c=len(entry)
        for j in range(c):
            if entry[j]==str(words[i])[j]:
                ls[i]+=3
            if entry[j] in str(words[i]):
                ls[i]+=1
    nls=[]
    m=max(ls)
    #It is to find the closest word match
    for i in range(len(ls)):
        if ls[i]==m:
            nls.append(f'"{words[i]}"')
    if m>3 and len(entry)>2:
        return nls
    else:
        return []

#A custom function to censor words into * and tell lenth, it is made for sole purpose of config fata check without exposing actual data to allow user to know if they has ahy typo(by knowing length) and **** is to make it look cool
def hash(words:str, type:str='#None~'):
    h=''
    if words!='#Hash*~':
        for i in words:
            h+='*'
        if h=='':
            h='#None*~'
        if type!='#None~':
            print(f'{type}: {h} (length:{len(h)})', flush=True)
        else:
            return h
    else:
        print('\nIt is bad to ask hash for hashing escape-hash word ( ᴗ͈ˬᴗ͈)ഒ\n ', flush=True)

#Allows user to add custom logs
def slog(arg, data):
    arg=' '.join(arg)
    if arg[-1]!=';' and ';' not in arg:
        arg=[arg] #This allows differentiating what user log was done without proper closing, may look senseless but it's not
        log(words=arg, type='UserDefined')
    else:
        scan=arg.split(';')
        if len(scan)==2:
            if scan[1]!='':
                log(words=scan[0], type=scan[1]) #Allows log manipulation and flexiblity
            else:
                log(words=scan[0], type='UserDefined')
        else:
            log(words=scan, type='UserDefined')

#The extra 'true' variable is to avoid direct use, this is a repair function which is not supposed to be accessed by non-technincal person and theirfore, also not included in help
#This function is for config correction without core-authentication, although, leaves vulnerable security loophole, it is made for the same purpose in case config file fails, in case, we would like to advice not to use same password for multiple sql-server
def emerge(scan, data, true:bool=False):
    from time import sleep as wait
    def bt(true:bool=true):
        if true!=True:
            wait(5)
    #Emergency mode doesn't focus on user-friendly env as it is not made for non-technical people, Emrg logs are not explained in simple language for that purpose as error-catching is made vague(yet enough to tell the problem) because we assume that the person using it known what he/she is doing
    #This is also a reason their is no emoticon or frinedly explaination
    cmd=scan.split()
    #The reason no password is asked is, assuming possiblity, that the config may have password typo that crashes the connection building, it is a backdoor
    if cmd[0]=='update':
        log(f'Use of "update">>EmrgLog\t[{ctime()}]', '#None*~')
        if len(cmd)==1:
            print(f'\n\'{cmd[0]}\'::Invalid (lack of char*) arguement>>Condition=False [Doesn\'t fulfill minimum requirement]', flush=True)
            log('"update"->bab output::Length->tokens->1(Failed)', 'WarnEmrg')
        else:
            #Another reason for vague error-catching logs is that everything below is tightly packed together, so we didn't put error-catcher on every small task performed but everythin as a whole
            try:
                from libprocess import libcrypt, compresser
                log(f'"update"->accessed "libprocess"->loaded>>EmrgLog\t[{ctime()}]', '#None*~')
            except:
                log('Failed to load libprocess->libcrypt', 'Emrg')
                log('Failed to load libprocess->compresser', 'Emrg')
            try:
                bt()
                user=data[0]
                host=data[1]
                password=data[2]
                log(f'"update"->Config-data->loaded>>EmrgLog\t[{ctime()}]', '#None*~')
            except:
                log('Failed to load libman->config-data', 'Emrg')
            if len(cmd)==2 and cmd[1]=='*':
                cmd=cmd[0:-1]; cmd+=['user', 'host', 'password']
                log(f'"update"->input(> {cmd} <)>>EmrgLog', '#None*~')
            for e in cmd[1:]:
                bt()
                if e=='user':
                    bt()
                    user=input('(EMERGENCY!!)\n\t!![@core] _user==')
                elif e=='host':
                    bt()
                    host=input('(EMERGENCY!!)\n\t!![@core] _host==')
                elif e=='password':
                    bt()
                    password=input('(EMERGENCY!!)\n\t!![@core] _password==') #No getpass here because backdoor can't afford typo, it is not a secure setup but emergency correction
                    if password=='':
                        password='#None*~'
                else:
                    print(f'!!(@core-librr)>>Use of unknown variable: {e}\n\tSkipping...', flush=True)
                    log(f'"update"->not defined var*::> {e} <>>EmrgLog\t[{ctime()}]', '#None*~')
            try:
                bt()
                with open('config.blib', 'r') as rec:
                    file_data=rec.read()
                rec=file_data.split('\n')
                log(f'"update"->FileCheck->True::Condition=True>>EmrgLog\t[{ctime()}]', '#None*~')
                lvl=False
                for e in rec:
                    if e[0:5]=='lkvl:':
                        if lvl==False:
                            lock=int(libcrypt(e[5:], 'decrypt', security_level=2))
                        else:
                            pass
                if lock!=0:
                    user=libcrypt(user, 'encrypt', security_level=lock-1)
                    host=libcrypt(host, 'encrypt', security_level=lock-1)
                    password=libcrypt(password, 'encrypt', security_level=lock)
                    user=compresser(user)
                    host=compresser(host)
                    password=compresser(password)
                bt()
                if true==True:
                    with open('config.blib', 'w') as rec:
                        rec.write(f"lkvl:{lock}\nuser:{user}\nhost:{host}\npassword:{password}")
                else:
                    wait(5)
                log(f'"update"->Protocol Completion Comfirmation->Done!->Config-data updated(> {cmd} <)>>EmrgLog\t[{ctime()}]', '#None*~')
            except:
                log(f'"update"->FileCheck->Void::Condition=Null>>EmrgLog\t[{ctime()}]', '#None*~')
                log(f'Protocol failure::"return value 1;"->Config file maybe corrupted', 'Emrg')
    elif cmd[0]=='reset':
        log(f'Use of "reset">>EmrgLog\t[{ctime()}]', '#None*~')
        #[@core] is for the sole prupose to tell that it should have been a high authentication command even though no password was asked for priviledge elevation
        if len(cmd)==1:
            print(f'\n\'{cmd[0]}\'::Invalid (lack of char*) arguement>>Condition=False [Doesn\'t fulfill minimum requirement]', flush=True)
            log('"update"->bab output::Length->tokens->1(Failed)', 'WarnEmrg')
        worry=input('(EMERGENCY!!)\n\t[@core] echo "Are you sure?[y/n]" --(You are about to perform a dangerous operation):')
        if worry.lower()=='y':
            log(f'"reset"->Protocol Proceed Confirmation::True>>EmrgLog', '#None*~')
            from os import remove as rem
            try:
                if true==True:
                    rem('config.blib')
                else:
                    wait(5)
                    raise EnvironmentError
                log(f'"reset"->Delete Conf file:: resulted 0;>>EmrgLog\t[{ctime()}]', '#None*~')
            except:
                log(f'"reset"->Attempt mad: Delete Config file->result(1)::FileNotFound>>EmrgLog', '#None*~')
                log('Operation: Delete Conf file:: resulted 1;', 'Emrg')
            try:
                from libdata import new_conf
                log(f'"reset"->libdata->Loaded>>EmrgLog\t[{ctime()}]', '#None*~')
                if true==True:
                    new_conf()
                else:
                    wait(5)
                    raise EnvironmentError
                log(f'"reset"->libdata->Called>>EmrgLog\t[{ctime()}]', '#None*~')
            except:
                log('"reset"->Error::Failed to call libdata: resulted 1;', 'Emrg')
        else:
            print('Cancelling...', flush=True)

#libman is main and starting point, as it is the first function I defined after making this file
def libman(arg, data):
    if len(arg)==1:
        print('\nLibman: Extra Aguement! ૮₍ ˶>⤙<˶  ₎ა\n', flush=True)
    elif arg[1] in ['--help', '-help', 'help', 'helpme', 'help-me']:
        if len(arg)>2:
            print(f'\'{arg[1]}\' doesn\'t need extra arguement: "{' '.join(arg[2:])}"', flush=True)
        #The help is written here instead of having external file like older version is to prevent changes in it, although, still possible
        print('\nHelp:\n\thelp:\tEnds up showing this\n\ttest:\tConfigure test\n\tconf_sec_rev:\t(Vulnerable)::Allows check without permission\n\n', flush=True)
        #I have lot of things to add, help will help in guidance, lol. I made help first and am using it as guide to write logic. I don't even remember what I was thinking when writing test, bruh
    elif arg[1]=='conf_sec_rev':
        if len(arg)==2:
            print(f'\n\'{arg[1]}\' needs an arguement! (づ ᴗ _ᴗ)づ\n', flush=True)
        else:
            if len(arg)==3 and arg[3]=='*':
                arg=arg[1:-1]; arg+=['user', 'host', 'password']
            print('\n#Hashing...ᓚ₍ ^. .^₎\n', flush=True)
            for e in arg[1:]:
                if e=='user':
                    hash(type='user', words=data[0])
                elif e=='host':
                    hash(type='host', words=data[1])
                elif e=='password':
                    hash(type='pasword', words=data[2])
                elif hash=='#':
                    hash(words='#Hash*~')
                else:
                    #It is better than throwing error to not be 'strict' in command use, also allows non-config things to be hashed(although I don't see any reason to do so but this is just for flexiblity)
                    if e[0]!='"' and e[-1]!='"':
                        qot='"'
                    elif e[0]!="'" and e[-1]!="'":
                        qot="'"
                    elif e[0]!='^' and e[-1]!='^':
                        qot='^'
                    else:
                        qot=''
                    print(f'Hashing word:< {qot}{e}{qot} > -->> <{qot}{hash(e)}{qot}>(Hashed)\n\t\t[Length:{len(e)}]')
            print('\n')
    elif arg[1]=='core:break->force':
        if len(arg)==2:
            print(f'\n\'{arg[1]}\' needs an arguement! (づ ᴗ _ᴗ)づ\n', flush=True)
        else:
            pey=arg[2].split('@')
            #Remember? I said it doesn't ask for password assuming password typo, is is because password is not visible using getpass
            #But user and host uses input and are visible, so typo shouldn't go unnoticed, so we ask them for authentication instead
            if pey[0]==data[0] and pey[1]==data[1]:
                print('\nCaution: Entering emergency-mode, it is not user-friendly and may break the system (｡>﹏<)\n')
                log('Emergency-mode activated:\n\tThis is a backdoor system, only to be used for error-connection', 'Warning')
                log(f'Emergency-mode->activation::Protocol was activated\t[{ctime()}]', 'Announcement')
                while True:
                    ask=input('EMERGENY-MODE![]')
                    if ask!='':
                        if ask=='exit':
                            break
                        else:
                            emerge(ask, data, True)
            else:
                #To prevent re-attempts, it is just to confuse person if he entered wrong authentication(user and host)
                log('Emergency-mode(Fake) activated:\n\tTheir was an attempt to emergency-mode without proper authentication\n\tOr The config file setup had typo', 'Echo')
                while True:
                    ask=input('EMERGENCY-MODE![]')
                    if ask!='':
                        if ask=='exit':
                            break
                        #just so he doesn't remain in oblivion, this is enough
                        else:
                            emerge(ask, data, False) #Deceptive secuirty measure
    elif arg[1]=='new-db-->on': #This is kind of complex command, again not in help, it is added in ReadMe.md file instead, it is also for non-technical person but it is not my fault if you ingore basic instructions and believing in help arguement only
        if len(arg)==2:
            print('Hang on! We will prepare it! ദ്ദി ˉ͈̀꒳ˉ͈́ )✧', flush=True)
            try:
                import mysql.connector
            except:
                #(12-06-2005): oracle reported that latest mysql-connector-python is not stable with new python versions. This news maybe outdated depending upon time
                #Although, we do provide solution in libman, so it is unlikely, unless we have a stubborn user who rejects our patch protocol (which can be kind of valid as we make him rollback to old yet stable version of mysql-coonector-python)
                log('Unable to access mysql-connector\n\tCheck the above logs to see if this issue occured before\n\tIf not then it is best to rerun the program\n\tUse "pip list" to check mysql-connector')
            try:
                #This is again another tightly packed tasks but some of them have been tested individually before running this task, so it helps in narrowing down things
                user=data[0]
                host=data[1]
                password=data[2]
                if password=='#None*~':
                    password=''
                db=mysql.connector.connect(user=user, host=host, password=password)
                cur=db.cursor()
                try:
                    cur.execute('Drop database libgo')
                except:
                    log('libgo doesn\'t exist yet their was an attempt to remove it\n\tThis is not an issue', 'Warning')
                cur.execute('Create database libgo')
                db.commit()
                db.close()
                db=mysql.connector.connect(user=user, host=host, password=password, database='libgo')
                cur=db.cursor()
                cur.execute('''Create table libstudent(
                std_id char(6) PRIMARY KEY,
                std_name varchar(30) NOT NULL,
                bkl varchar(50),
                bkl_dot date)''')
                cur.execute('''Create table booklib(
                bk_name varchar(50) PRIMARY KEY,
                bk_status char(1) NOT NULL ,
                bk_shell varchar(5) NOT NULL)''')
                db.commit()
                print('Done! Database has been created ⸜(｡˃ ᵕ ˂)⸝', flush=True)
                sql_ask=input('\nShould we create test-data(For testing purposes?)[y/N]')
                if sql_ask.lower()=='y':
                    cur.execute('Insert into libstudent(std_id, std_name, bkl, bkl_dot) values("102001", "Aman Thakur", "Harry Potter", "2005-06-12")')
                    cur.execute('Insert into libstudent(std_id, std_name, bkl, bkl_dot) values("120101", "Arjun Singh", "Matrix-sim", "2005-06-07")')
                    cur.execute('Insert into libstudent(std_id, std_name, bkl, bkl_dot) values("112001", "Daksh", "Atomic Habits", "2005-06-1")')
                    cur.execute('Insert into booklib(bk_name, bk_status, bk_shell) values("Atomic Habits", "1", "A-6")')
                    cur.execute('Insert into booklib(bk_name, bk_status, bk_shell) values("Matrix-sim", "1", "B-4")')
                    cur.execute('Insert into booklib(bk_name, bk_status, bk_shell) values("Harry Potter", "1", "B-12")')
                    cur.execute('Insert into booklib(bk_name, bk_status, bk_shell) values("Fun-day", "0", "A-10")')
                    cur.execute('Insert into booklib(bk_name, bk_status, bk_shell) values("Eat the Frog", "0", "A-1")')
                    cur.execute('Insert into booklib(bk_name, bk_status, bk_shell) values("Shadow Slave", "0", "c-9")')
                    db.commit()
                    print('Done! ⸜(｡˃ ᵕ ˂)⸝', flush=True)
                else:
                    print('Cancelling...', flush=True)
            except:
                log('Failed to connect with sql\n\tIf config file or module "mysql-connector" is not the issue then:\n\t\tIt could be sql server is not active\n\t\tOr Something interrupted the new-test protocol')
    elif arg[1]=='test':
        if len(arg)==2:
            print('\nTest Result:', flush=True, end='')
            try:
                import mysql.connector
                try:
                    db=mysql.connector.connect(user=data[0], host=data[1], password=data[2])
                    print('\tSuccess!\n', flush=True)
                except:
                    print('\tFailure!!\n', flush=True)
            except:
                print('\tCritical Failure!!\n', flush=True)
                print('\n\nUnable to conduct test, something went wrong!\n:(\n', flush=True)
                log('mysql-connector failed to load\n\tThis error ocurred due to mysql-connector isn\'t installed or inaccessible\n\tTry reinstalling it through pip\n\tIt could be due to server not running')
    else:
        sug(arg[1], ['--help', '-help', 'help', 'helpme', 'help-me', 'conf_sec_rev', 'test', 'new-db-->on'])


#Defining core: It is authority elevation tool
def core(arg, data):
    import os
    if len(arg)==1:
        print('\nCore: Extra Aguement! ૮₍ ˶>⤙<˶  ₎ა\n', flush=True)
    else:
        if arg[1]=='show':
            if len(arg)==2:
                print('\n"show"?\tShow what? (＾_-)\n', flush=True)
            else:
                for c in arg[2:]:
                    if c=='conf' or c=='config':
                        print(f'\n\nConfData:\n     User:     {data[0]}\n     Host:     {data[1]}\n!Password:     {hash(words=data[2])}        length:{len(data[2])}\n\n\n') #How will someone acess this without command? Why show it?
                    if c=='sql-data' or c=='sql_data' or c=='sqldata':
                        try:
                            import mysql.connector
                            db=mysql.connector.connect(user=data[0], host=data[1], password=data[2], database='libgo')
                            cur=db.cursor()
                            cur.execute('Describe libstudent')
                            std=cur.fetchall()
                            print('\nStudent Database!\n', flush=True)
                            for i in std:
                                for j in i:
                                    j=str(j)
                                    while len(str(j))<=20: #Helps in maintaining unformity while showing data
                                        j+=' '
                                    print(j, end='  |  ', flush=True)
                                print()
                            cur.execute('Describe booklib')
                            bk=cur.fetchall()
                            print('\nBook Database!\n', flush=True)
                            for i in bk:
                                for j in i:
                                    j=str(j)
                                    while len(str(j))<=20:
                                        j+=' '
                                    print(j, end='  |  ', flush=True)
                                print()
                            print()
                        except:
                            print('\nNo way! We failed! Check log, duh! (っ ͡ ͡º - ͡ ͡º ς)\n', flush=True)
                            print('May I suggest? ( •̯́ ^ •̯̀)\n\n\tTry: "libman new-db-->on" if you haven\'t in case.\n\n', flush=True)
                            log('Failed to collect data from sql server\n\tI hope, the above log is self explainatory\n\tOr check if their are other logs above\n\t\tIf no, then issue may not be module or connection but execution\n\t\tOne common reason execution failed is because the database doesn\'t exists\n\t\tOr no table in database: libgo')

#This will be the main function
def libql(arg, data):
    user=data[0]
    host=data[1]
    password=data[2]
    if password=='#None*~':
        password=''
    import mysql.connector
    db=mysql.connector.connect(user=user, host=host, password=password, database='libgo')
    cur=db.cursor()
    if len(arg)==1:
        print('\nLibQL: Extra Aguement! ૮₍ ˶>⤙<˶  ₎ა\n', flush=True)
    else:
        if arg[1]=='reveal':
            if len(arg)==2:
                print('\n"reveal"?\tReveal what? (＾_-)\n', flush=True)
            elif arg[2]=='data':
                if len(arg)==3:
                    cur.execute('SELECT * FROM libstudent')
                    x=cur.fetchall()
                    c=0
                    for i in x:
                        for j in i:
                            if len(str(j))>c:
                                c=len(str(j))
                    cur.execute('SELECT * FROM booklib')
                    y=cur.fetchall()
                    for i in y:
                        for j in i:
                            if len(str(j))>c:
                                c=len(str(j))
                    print('\nStudent data:\n', flush=True)
                    for i in x:
                        for j in i:
                            j=str(j)
                            while len(j)<=(c+4):
                                j+=' '
                            print(j, end='  |  ', flush=True)
                        print()
                    print()
                    print('Book data:\n')
                    for i in y:
                        for j in i:
                            j=str(j)
                            while len(j)<=(c+4):
                                j+=' '
                            print(j, end='  |  ', flush=True)
                        print()
                    print()
                elif len(arg)>3:
                    scmd=arg[3:]
                    c=0
                    sym=False
                    for scan in scmd:
                        try:
                            for sn in scan:
                                if sn.lower()>='a' and sn.lower()<='z':
                                    pass
                                elif sn.isdigit():
                                    pass
                                else:
                                    sym=True
                            if sym==True:
                                print('Bad input! :(', flush=True)
                                break
                            else:
                                cur.execute(f'SELECT * FROM {scan}')
                                d=cur.fetchall()
                                for i in d:
                                    for j in i:
                                        if len(str(j))>c:
                                            c=len(str(j))
                        except:
                            print('\nSkipping <', scan, '> due to bad return value ¯\\_(ツ)_/¯\n', flush=True)
                    for scan in scmd:
                        if sym==True:
                            break
                        try:
                            cur.execute(f'SELECT * FROM {scan}')
                            d=cur.fetchall()
                            print('\nRequested data:', scan, flush=True)
                            print()
                            for i in d:
                                for j in i:
                                    j=str(j)
                                    while len(j)<=(c+4):
                                        j+=' '
                                    print(j, end='  |  ', flush=True)
                                print()
                            print()
                        except:
                            print('\nSkipping <', scan, '> due to bad return value ¯\\_(ツ)_/¯\n', flush=True)
            else:
                sug(arg[2], ['data'])
        elif arg[1]=='issue':
            if len(arg)==2:
                print('\n"issue"?\tIssue what? (＾_-)\n', flush=True)
            elif len(arg)==3:
                print('\nISSUE: Needs Extra Aguement! ૮₍ ˶>⤙<˶  ₎ა\n', flush=True)
            else:
                try:
                    stid=arg[2]
                    bkname=arg[3:]; bkname=' '.join(bkname)
                    cur.execute('UPDATE libstudent SET bkl=%s WHERE std_id=%s', [bkname, stid])
                    cur.execute('SELECT bk_status FROM booklib WHERE bk_name=%s', [bkname])
                    x=int(cur.fetchall()[0][0])
                    x+=1
                    cur.execute('UPDATE booklib SET bk_status=%s WHERE bk_name=%s', [x, bkname])
                    db.commit()
                    print('Done! ^~^', flush=True)
                except:
                    print('Unable to retrieve data :(', flush=True)
        elif arg[1]=='alignment':
            if len(arg)==2:
                print('\nLacks arguement! ૮₍ ˶>⤙<˶  ₎ა\n', flush=True)
            else:
                if arg[2]=='check' and len(arg)==3:
                    try:
                        print('\n\tConducting Check:\n', flush=True)
                        cur.execute('SELECT bkl FROM libstudent')
                        bk=cur.fetchall()
                        cur.execute('SELECT bk_name FROM booklib')
                        lb=cur.fetchall()
                        cur.execute('Select bk_status FROM booklib')
                        kk=cur.fetchall()
                        bkk=[]
                        nbkk=[]
                        dkk=[]
                        nl=[]
                        for i in bk:
                            for j in i:
                                j=str(j)
                                if j!='':
                                    bkk.append(j)
                        for i in lb:
                            for j in i:
                                j=str(j)
                                nbkk.append(j)
                        for i in kk:
                            for j in i:
                                j=str(j)
                                dkk.append(j)
                        dk=dict(zip(nbkk, dkk)) #Something I learnt new about is that zip returns tuple in order iteration
                        for i in dk.keys():
                            c=bkk.count(i)
                            if str(c)!=dk[i]:
                                nl.append(i)
                        print('\nList of books not aligning with data:\n')
                        if len(nl)>0:
                            for j in nl:
                                print(f'\t{j}', flush=True)
                            print()
                        else:
                            print('\t[Empty]\n', flush=True)
                    except:
                        print('\nWe ran into a problem while conducting this command :(\n', flush=True)
                elif arg[2]=='realign' and len(arg)==3:
                    try:
                        print('\nRealignment in progress...', flush=True, end='')
                        cur.execute('SELECT bkl FROM libstudent')
                        bk=cur.fetchall()
                        cur.execute('SELECT bk_name FROM booklib WHERE bk_status!="0"')
                        lb=cur.fetchall()
                        bkk=[]
                        nbkk=[]
                        for i in bk:
                            for j in i:
                                j=str(j)
                                if j!='':
                                    bkk.append(j)
                        for i in lb:
                            for j in i:
                                j=str(j)
                                if j not in bkk:
                                    nbkk.append(j)
                        for i in nbkk:
                            c=str(bkk.count(i))
                            cur.execute('UPDATE booklib SET bk_status=%s WHERE bk_name=%s', [c, i])
                        db.commit()
                        print('Done!\n', flush=True)
                    except:
                        print('Failure!', flush=True)
                        print('\nWe failed to realign :(\nSomething went wrong...\n', flush=True)
                else:
                    sug(arg[2], ['check', 'realign'])
        else:
            sug(arg[1], ['reveal', 'issue', 'alignment'])

#Can't have only one libman function, else scancmd won't have a choice, I need to add core, libql, libgui(I will also make GUI, although, conf file creation needs to be done in CLI)
#I will add these in ReadMe.md instead of libman help