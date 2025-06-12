#This is an important file that handles commands

from librr import log

#A custom function to censor words into * and tell lenth, it is made for sole purpose of config fata check without exposing actual data to allow user to know if they has ahy typo(by knowing length) and **** is to make it look cool
def hash(type:str, words:str):
    h=''
    if words!='#Hash*~':
        for i in words:
            h+='*'
        if h=='':
            h='#None*~'
        print(f'{type}: {h} (length:{len(h)})', flush=True)
    else:
        print('\nIt is bad to ask hash for hashing escape-hash word ( ᴗ͈ˬᴗ͈)ഒ\n ', flush=True)

#The extra 'true' variable is to avoid direct use, this is a repair function which is not supposed to be accessed by non-technincal person and theirfore, also not included in help
#This function is for config correction without core-authentication, although, leaves vulnerable security loophole, it is made for the same purpose in case config file fails, in case, we would like to advice not to use same password for multiple sql-server
def emerge(scan, data, true:bool=False):
    if true==True:
        #Emergency mode doesn't focus on user-friendly env as it is not made for non-technical people, Emrg logs are not explained in simple language for that purpose as error-catching is made vague(yet enough to tell the problem) because we assume that the person using it known what he/she is doing
        #This is also a reason their is no emoticon or frinedly explaination
        cmd=scan.split()
        #The reason no password is asked is, assuming possiblity, that the config may have password typo that crashes the connection building, it is a backdoor
        if cmd[0]=='update':
            if len(cmd)==1:
                print(f'\n\'{cmd[0]}\'::Invalid (lack of char*) arguement>>Condition=False [Doesn\'t fulfill minimum requirement]', flush=True)
            else:
                #Another reason for vague error-catching logs is that everything below is tightly packed together, so we didn't put error-catcher on every small task performed but everythin as a whole
                try:
                    from libprocess import libcrypt, compresser
                except:
                    log('Failed to load libprocess->libcrypt', 'Emrg')
                    log('Failed to load libprocess->compresser', 'Emrg')
                try:
                    user=data[0]
                    host=data[1]
                    password=data[2]
                except:
                    log('Failed to load libman->config-data', 'Emrg')
                if len(cmd)==2 and cmd[1]=='*':
                    cmd=cmd[0:-1]; cmd+=['user', 'host', 'password']
                for e in cmd[1:]:
                    if e=='user':
                        user=input('(EMERGENCY!!)\n\t!![@core] _user==')
                    elif e=='host':
                        host=input('(EMERGENCY!!)\n\t!![@core] _host==')
                    elif e=='password':
                        password=input('(EMERGENCY!!)\n\t!![@core] _password==')
                        if password=='':
                            password='#None*~'
                    else:
                        print(f'!!(@core-librr)>>Use of unknown variable: {e}\n\tSkipping...', flush=True)
                try:
                    with open('config.blib', 'r') as rec:
                        rec.read()
                    rec=rec.split('\n')
                    lvl=False
                    for e in rec:
                        if e[0:5]=='lkvl:':
                            if lvl==False:
                                lock=int(libcrypt(info[5:], 'decrypt', security_level=2))
                            else:
                                pass
                    if lock!=0:
                        user=libcrypt(user, 'encrypt', lock-1)
                        host=libcrypt(host, 'encrypt', lock-1)
                        password=libcrypt(password, 'encrypt', lock)
                        user=compresser(user)
                        host=compresser(host)
                        password=compresser(password)
                    with open('config.blib', 'w') as rec:
                        rec.write(f"lkvl:{lock}\nuser:{user}\nhost:{host}\npassword:{password}")
                except:
                    log('Failed to follow backdoor-update protocol\n\tThis protocol has mutliple tightly packed tasks in it, which makes it harder for librr to trace', 'Emrg')
        elif cmd[0]=='reset':
            #[@core] is for the sole prupose to tell that it should have been a high authentication command even though no password was asked for priviledge elevation
            worry=input('(EMERGENCY!!)\n\t[@core] echo "Are you sure?[y/n]" --(You are about to perform a dangerous operation):')
            if worry.lower()=='y':
                from os import remove as rem
                try:
                    rem('config.blib')
                except:
                    log('Operation: Delete Conf file:: resulted 1;\n\tThis is not critical, this simply means:\n\t\tUnable to access Conf file\n\tThis could be ignored:\n\t\tIf conf file doesn\'t exist\n\tIf it shows up even though conf file exists then check permissions', 'Emrg')
                try:
                    from libdata import new_conf
                    new_conf()
                except:
                    log('Operation: Failed to execute new conf protocol\n\tIf you are seeing this, it could be because:\n\t\tIncorrect libdata (Possibly tampered due to external intervention)\n\t\tOr unable to access functions of libdata for any reason', 'Emrg')
            else:
                print('Cancelling...', flush=True)
    else:
        print('!!DO NOT ATTEMPT\n!!YOU MAY BREAK CONFIG AND LIBMANON （ꐦ𝅒_𝅒）', flush=True)

#libman is main and starting point, as it is the first function I defined after making this file
def libman(arg, data):
    if arg[0] in ['--help', '-help', 'help', 'helpme', 'help-me']:
        if len(arg)>1:
            print(f'\'{arg[0]}\' doesn\'t need extra arguement: "{' '.join(arg[1:])}"', flush=True)
        #The help is written here instead of having external file like older version is to prevent changes in it, although, still possible
        print('\nHelp:\n\thelp:\tEnds up showing this\n\ttest:\tConfigure test\n\trelib:\trestarts libmanon\n\tconf_sec_rev:\t(Vulnerable)::Allows check without permission\n\n', flush=True)
        #I have lot of things to add, help will help in guidance, lol. I made help first and am using it as guide to write logic. I don't even remember what I was thinking when writing test, bruh
    elif arg[0]=='conf_sec_rev':
        if len(arg)==1:
            print(f'\n\'{arg[0]}\' needs an arguement! (づ ᴗ _ᴗ)づ\n', flush=True)
        else:
            if len(arg)==2 and arg[1]=='*':
                arg=arg[0:-1]; arg+=['user', 'host', 'password']
            print('\n#Hashing...ᓚ₍ ^. .^₎\n', flush=True)
            for e in arg[1:]:
                if e=='user':
                    hash('user', data[0])
                elif e=='host':
                    hash('host', data[1])
                elif e=='password':
                    hash('pasword', data[2])
                elif hash=='#':
                    hash('#Hash*~')
                else:
                    #It is better than throwing error to not be 'strict' in command use, also allows non-config things to be hashed(although I don't see any reason to do so but this is just for flexiblity)
                    hash(e)
            print('\n')
    elif arg[0]=='core:break->force':
        if len(arg)==1:
            print(f'\n\'{arg[0]}\' needs an arguement! (づ ᴗ _ᴗ)づ\n', flush=True)
        else:
            pey=arg[1].split('@')
            #Remember? I said it doesn't ask for password assuming password typo, is is because password is not visible using getpass
            #But user and host uses input and are visible, so typo shouldn't go unnoticed, so we ask them for authentication instead
            if pey[0]==data[0] and pey[1]==data[1]:
                print('\nCaution: Entering emergency-mode, it is not user-friendly and may break the system (｡>﹏<)\n')
                log('Emergency-mode activated:\n\tThis is a backdoor system, only to be used for error-connection', 'Warning')
                while True:
                    ask=input('EMERGENY-MODE![]')
                    if ask!='':
                        emerge(ask, data, True)
            else:
                #To prevent re-attempts, it is just to confuse person if he entered wrong authentication(user and host)
                log('Emergency-mode(Fake) activated:\n\tTheir was an attempt to emergency-mode without proper authentication\n\tOr The config file setup had typo', 'Echo')
                while True:
                    ask=input('EMERGENCY-MODE![]')
                    if ask!='':
                        #just so he doesn't remain in oblivion, this is enough
                        print('This is a fakecore enviournment: return 0;', flush=True)
    elif arg[0]=='new-db-->on': #This is kind of complex command, again not in help, it is added in ReadMe.md file instead, it is also for non-technical person but it is not my fault if you ingore basic instructions and believing in help arguement only
        if len(arg)==1:
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
                    cur.execute('Insert into booklib(bk_name, book_status, book_shell) values("Atomic Habits", "1", "A-6")')
                    cur.execute('Insert into booklib(bk_name, book_status, book_shell) values("Matrix-sim", "1", "B-4")')
                    cur.execute('Insert into booklib(bk_name, book_status, book_shell) values("Harry Potters", "1", "B-12")')
                    cur.execute('Insert into booklib(bk_name, book_status, book_shell) values("Fun-day", "0", "A-10")')
                    cur.execute('Insert into booklib(bk_name, book_status, book_shell) values("Eat the Frog", "0", "A-1")')
                    cur.execute('Insert into booklib(bk_name, book_status, book_shell) values("Shadow Slave", "0", "c-9")')
                    db.commit()
                    print('Done! ⸜(｡˃ ᵕ ˂)⸝', flush=True)
                else:
                    print('Cancelling...', flush=True)
            except:
                log('Failed to connect with sql\n\tIf config file or module "mysql-connector" is not the issue then:\n\t\tIt could be sql server is not active\n\t\tOr Something interrupted the new-test protocol')

#Can't have only one libman function, else scancmd won't have a choice, I need to add core, libql, libgui(I will also make GUI, although, conf file creation needs to be done in CLI)
#I will add these in ReadMe.md instead of libman help