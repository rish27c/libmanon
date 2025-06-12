#Rishabh here, making comments for easy navigation across this project, hope this helps. Please ignore any grammar or spelling mistakes that went unnoticed in pile of words

#This is focused on user-friendly enviournment with less print(clutter...bla, bla, bla)

#importing custom and built-in modules
from librr import log #dot
import os
from libdata import conf #dot

#Everytime I mention mysql-connector, I mean mysql-connector-python and not mysql-connector, confusing, right? But that is the case to not trouble the user much

#Here, the main program is made, libman connects all files
def main():
    #this block checks for crashes(If the program was not existed correctly)
    try:
        with open('Error_logs.txt', 'r') as file:
            None
        print('\n\nIt seems like you forgot to properly close the application ( ˶°ㅁ°) !!\n\n', flush=True) #Clumsy way to check for crashes
        os.remove('Error_logs.txt')
    except:
        pass
    #Checking for mysql-connector to not cause import issue
    try:
        import mysql.connector
    except:
        #This is self-recovery, I mean, users are unreliable(not always)
        log('mysql.connector didn\'t respond: Import file seems to be missing or not accessible\n')
        print('It seems like you are missing mysql-connector\n\n\tWe can try patch for you!\nIt will only work is pip is added to enviournment path or is accessible externally(without admin privileges or sudo)\n', flush=True)
        ask=input('Do you want the libmanon to try patching>[y/N]')
        if ask.lower()=='y':
            print('\nLet us fix it by pip installation if possible! (ง•̀ᗝ•́)ง', flush=True)
            os.system('pip install mysql-connector-python==8.0.31') #os.system(command)-->This injects command directly in system of the OS (Also, installs stable sql version)
            try:
                #Re-attempt after correction
                import mysql.connector
                print('\nThe patch worked. Wohoo! ◝(ᵔᗜᵔ)◜', flush=True)
            except:
                #Second time fail? It means things are actually bad and not to be taken lightly, although, can't tell that to user
                log('Failed execution of pip/pip3 installation of mysql-connector')
                ask2=input('It seems we failed to resolve the issue ( ◡̀_◡́)ᕤ\nWe want to follow patch#2 protocol but it may delete/uninstall modules.\nShall we try patch#2 for you?[y/n]') #asking for consent, can't take risks
                if ask2.lower()=='y':
                    #These are all common things that causes issues, I mean, what is the best solution then reinstalling everything?
                    os.system('pip uninstall mysql-connector-python')
                    os.system('pip uninstall mysql-connector')
                    os.system('pip uninstall mysql-client')
                    os.system('pip uninstall mysqlclient')
                    os.system('pip install mysql-connector-python==8.0.31')
                    try:
                        #Second Re-attempt
                        import mysql.connector
                        print('\nWo! It seems we fixes the issue for you! ٩(^ᗜ^ )و', flush=True)
                    except:
                        #This is not something that can be fixed without going to root cause but this is not a recovery system, we have done enough
                        log('\'mysql-connector\' module is missing and libmanon failed to patch it\n\tPip is also not accessible')
                else:
                    print('\n\nOk! Cancelling...\nIt is advisable to manually install mysql-connector', flush=True)
        else:
            print('\n\nSkipping...\nIt is advisable to manually install mysql-connector', flush=True)
            log('mysql-connector installation was skipped\n\tWe believe user to do it manually\n\tUse "pip install mysql-connector" or check server status', 'Warning')
    try:
        data=conf()
        if data==None: #If this fails then that means that file didn't existed and it exists none after creating file (already mentioned un libdata)
            data=conf()
            if data==None:
                log('Config file or lobdata has an issue; Null value is returned after data processing', 'ConfigBugReport')
        user=data[0]
        host=data[1]
        password=data[2]
        if password=='#None*~':
            password='' #This is reversing libdata transformation, don't ask, don't touch
    except:
        log('Unable to interpret config file\n\tThe main cause could be decryption failed(if conf file exists)\n\tOr Conf file was tampered with manually!')
    try:
        #Attempting mysql connection
        db=mysql.connector.connect(host=host, user=user, password=password, database='libgo')
        db.close()
    except:
        log('Unable to build connection with sql server:\n\tMaybe libgo database doesn\'t exist\n\tOr bad config file', 'Warning')
        try:
            #Re-attempting connection building
            db=mysql.connector.connect(user=user, host=host, password=password)
            cur=db.cursor()
            cur.execute('Create database libgo')
            db.commit()
            db.close()
            db=mysql.connector.connect(host=host, user=user, password=password, database='libgo')
            db.close()
        except:
            #This is assuming that mysql.connector worked but the version is unstable so the best solution would be rolling back to the stable one
            log('Unble to build connection with sql server(Second time):\n\tReason could be bad config or server is off\n\tOr the mysql-connector is not stable(This has been reported by oracle, [date: 2025-06-11])\n\t\t(The time is given when this issue was known, if the issue had gotten patched up then check it on official oracle community)', 'CriticalError')
            ask=input('\n\nWe might uninstall/deleted moduled. Can we try to fix the issue? (๑•́ -•̀) [y/N]') #Asking for consent again
            if ask.lower()=='y':
                #Proceeding, this is same steps as before, because we are assuming that the issue is mysql module, if it's not then it is config issue where connection fails because of incorrect config value (That's not our fault but users in that case)
                print('\nPlease be patient while we do things for you( ＾◡＾)っ\n\n', flush=True)
                os.system('pip uninstall mysql-connector')
                os.system('pip uninstall mysql-connector-python')
                os.system('pip uninstall mysql-client')
                os.system('pip uninstall mysqlclient')
                print('\n\nJust a little while longer(づ˶•༝•˶)づ\n', flush=True)
                os.system('pip install mysql-connector-python==8.0.31')
                print('\n\nPlease restart to see changes\n\n', flush=True)
    try:
        import liber #dot
    except:
        log('Missing file: \'liber\' which is responsible for handling commands.', 'CriticalError')
    print('\n')
    #liber command handler
    cr=False
    while True:
        scan=input('libcmd#>>')
        if scan!='':
            scancmd=scan.split() #parsing
            if scancmd[0].lower() in ['stop', 'exit', 'quit', 'bye', 'end', 'terminate', 'goodbye']:
                if len(scancmd)==1:
                    print('\nBYE! ヾ(˃ᴗ˂)◞ • *✰', flush=True)
                    try:
                        os.remove('Error_logs.txt')
                    except:
                        pass
                    break
                else:
                    try:
                        os.remove('Error_logs.txt')
                    except:
                        pass
                    print('\nNo need for extra arguement. Bye! ヾ(˃ᴗ˂)◞', flush=True)
            try:
                if '(' in scancmd[0] or ')' in scancmd[0] or ',' in scancmd[0] or '=' in scancmd[0] or '#' in scan:
                    raise Exception #This is to protect any attempt to exploit eval, like eval-injection(if that is even a word, like sql-injection)
                if scancmd[0]=='core' and cr==False and password!='':
                    #core is like sudo, my expierence as ex-linux user(wine error in running school meeting related application pulled me back to windows[not important])
                    import getpass
                    try:
                        ask=getpass.win_getpass('\n(Not visible) [Authentication]Password:')
                    except:
                        try:
                            ask=get.unix_getpass('\n(Not visible) [Authentication]Password:')
                        except:
                            log('\nUnable to hide password input\n\tThis could be the terminal not allowing UI manipulation\n\n', 'Warning')
                            ask=input('(Visible) [Authentication]Password:') #I tested in IDLE and getpass failed but it showed fallback warning so I used raw functionality instead of getpass function
                    if ask==password:
                        cr=True
                    else:
                        print('Authentication failed! ꒰๑•̥﹏•̥๑꒱\n\n', flush=True)
                    liber.core(scancmd[1:], data)
                elif scancmd[0]!='core':
                    eval('liber.'+scancmd[0])(scancmd[1:], data)  #eval converts the input to function and call it in liber, makes it easy to create and handle commands
                elif cr==True:
                    eval('liber.'+scancmd[0])(scancmd[1:], data) #I found it annoying that it asked for password everytime, so I just stopped the redundancy
                else:
                    raise Exception #To trigger the print statement given below
            except:
                print('\nUnknown command or mistype or not known by libman ¯\\_(ツ)_/¯\n', flush=True)
        else:
            continue #Thinking why I didn't use if scan=='' then continue but instead put everything inside the above if block? I planned the block to be small but with time, it grew

main()