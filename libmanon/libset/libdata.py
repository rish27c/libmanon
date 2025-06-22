from librr import log #dot
import getpass
from libprocess import libcrypt as lib #dot
from os import path

#conf processing
def conf():
    #Well, if it returns None, the module recieving it's value will assume that it created conf file and will call it again, if it returns None twice then that's an issue
    try:
        with open('config.blib', 'r') as rec:
            data=rec.read()
        return old_conf(data)
    except:
        new_conf()

#This is conf writer while also processing data
#If their is an error or issue in conf file gneration then it may be due to this logic, although, the function has been tested to be working, so it is unlikely
#But if their is an error, then it may be due to string being too large for python to process, which is possbile, although the limits have not been tested, it is estimated to unable to encrypt/decrypt 250,000 length of string by default
def new_conf():
    print('\nIt looks like you are missing config file data.\n\n\tNo Issue! We got you covered! (｡•̀ᴗ-)✧\n', flush=True)
    log('Missing conf file\n\tThis is not an issue and can be ignored unless their already is a config file', 'Warning')
    user=input('Enter value: user=')
    host=input('Enter value: host=')
    try:
        password=getpass.getpass('\n(Input won\'t be visible) Enter value: password=')
    except:
        log('ModuleError: getpass failed to hide password\n\tThis common cause could be that terminal doesn\'t allow UI manipulation', 'Warning')
        print('\n!!<InputError> Failed to hide input (ó﹏ò｡)', flush=True)
        #I mean, it is bad but user's choice
        password=input('\n(Unable to hide password![vulnerable!]) Enter value: password=')
    if password=='':
        password='#None*~' #This is because libprocess encryptor throws error on empty strings, so I made this tranforming value and these symbols are to make sure that it is not a legit mysql password, if someone does, change it (Your password)
        #Don't think of changing the above string value because it is connected with other files so you would break things, it would be easier to change your password and config file then diving into chaos of errors
    print('All Done!', flush=True)
    ask=input('\n\nDo you want secure save? (Encrypts your data!) [Y/n](Default=Y)')
    #If encryption fails, this logic block will degrade security-level step by step and no encryption is final measure if everything fails
    if ask.lower()!='n':
        from libprocess import compresser #dot
        try:
            nuser=lib(user, 'encrypt', security_level=3)
            nuser=compresser(nuser)
            nhost=lib(host, 'encrypt', security_level=3)
            nhost=compresser(nhost)
            npassword=lib(password, 'encrypt', security_level=4)
            npassword=compresser(npassword)
            lock=4
        except:
            print('\nIt seems like something went wrong while encrypting your data (◞‸◟,)\nCheck Error_logs for more information.', flush=True)
            try:
                print('Retrying...', flush=True)
                nuser=lib(nuser, 'encrypt', security_level=2)
                nuser=compresser(nuser)
                nhost=lib(nhost, 'encrypt', security_level=2)
                nhost=compresser(nhost)
                npassword=lib(npassword, 'encrypt', security_level=3)
                npassword=compresser(npassword)
                lock=3
            except:
                print('\n\nSorry, we failed again (っ◞‸◟ c)', flush=True)
                reask=input('Do you want to save info without encryption?[Y/n]')
                if reask.lower()!='n':
                    try:
                        nuser=lib(nuser, 'encrypt', security_level=1)
                        nuser=compresser(nuser)
                        nhost=lib(nhost, 'encrypt', security_level=1)
                        nhost=compresser(nhost)
                        npassword=lib(npassword, 'encrypt', security_level=2)
                        npassword=compresser(npassword)
                        lock=2
                    except:
                        #We skipped lcok=1 because of my own principle of degrading security, although, it would be easy to see how the pattern is following and security-level 0 means no security so what's the point of only encrypting password only? (If you are wondering why, it is because emergency mode protocol authentication)
                        print('\n\nUnfortunately, we failed once more ૮꒰◞ ˕ ◟ ྀི꒱ა', flush=True)
                        print('\n\nWe will disable encryption', flush=True)
                        log('libdata had an issue in processing input, it returned bad vlue\n\tEncryption failed, it may be due to long string or use of escape symbols\n\t(This will not affect the functioning of libmanon but may cause security vulnerablity)', 'Bad')
                        lock=0
                else:
                    lock=0
    else:
        #We don't give user a choice of level of encryption because if it works then best level encryption must be followed, we believe that user
        #Although, the choice of no encryption is only for the reason if encrypting and decrypting throws error everytime (And freewill, although, why if not for errors, why would someone not use encryption?)
        print('Ok! We will not use encryption then.', flush=True)
        lock=0
    if lock==0:
        lock=lib(str(lock), 'encrypt', security_level=2)
        with open('config.blib', 'w') as file:
            file.write(f"lkvl:{lock}\nuser:{user}\nhost:{host}\npassword:{password}")
    else:
        lock=lib(str(lock), 'encrypt', security_level=2)
        #lock is like a key that tells the encryption level to the old_conf() function, it is best to not touch it. It is also the reason it is also the reason it is consistent, although with lowest level encryption so deecrypting it won't be time consuming
        with open('config.blib', 'w') as file:
            file.write(f"lkvl:{lock}\nuser:{nuser}\nhost:{nhost}\npassword:{npassword}")

#This function is for sole purpose of reading file and interpreting it, in case you found any errors in interpretetion, it may be due to logic flaw in this file
#Although, not certain as all these functions have been tested to be working, unless manually touched
#In any case, if their is an error, check if the conf file was created first
def old_conf(data):
    from libprocess import decompresser
    usr, hst, pss, lvl=False, False, False, False #To make sure someone don't override the actual config file, although the person still can if he directly gets access to it and so this would be useless(although, that's why lock is also in encrypted form for that reason)
    data=data.split('\n')
    for info in data:
        if info[0:5]=='lkvl:':
            if lvl==False:
                lock=int(lib(info[5:], 'decrypt', security_level=2))
                lvl=True
            else:
                log('Config file has two or more same variables: lkvl')
        elif info[0:5]=='user:':
            if usr==False:
                if lock!=0:
                    user=decompresser(info[5:])
                    user=lib(user, 'decrypt', security_level=lock-1) #As I have already mentioned, following the pattern
                else:
                    user=info[5:]
                usr=True
            else:
                log('Config file has two or more same variable: user')
        elif info[0:5]=='host:':
            if hst==False:
                if lock!=0:
                    host=decompresser(info[5:])
                    host=lib(host, 'decrypt', security_level=lock-1)
                else:
                    host=info[5:]
                hst=True
            else:
                log('Config file has two or more same variable: host')
        elif info[0:9]=='password:':
            if pss==False:
                if lock!=0:
                    password=decompresser(info[9:])
                    password=lib(password, 'decrypt', security_level=lock)
                else:
                    password=info[9:]
                pss=True
            else:
                log('Conf file has two or more same variable: password')
        else:
            log('An unknown statement was detected in config file\n\tIf the file is working then this issue can be safely ignored\n\tIt may be caused due to use of unknown varaible\n\t\tThis means that config file has been manually tampered', 'Warning')
    #returns a list for further processing, this list gets bullied by many functions that calls its values for every now and then(for building connection)
    return [user, host, password]

#Any issue here will be handeled by external error-handler, easier to maintain. (File:librr) [Currently; underdeveloped by alot]