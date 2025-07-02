#This is libprocess file for pre-processing of data

from .librr import log #dot

#Replica use of encryption
#This is not a real encrptor but one I made using dictionary, it doesn't really provide actual security and can be reverse-engineered or broken easily unlike real encryption(used just for school project and basic-level security)
d_en={
    'a':'akfht', 'b':'gjtnd', 'c':'khjtn', 'd':'ekfng', 'e':'kgntr', 'f':'lgktr', 'g':'gkrna', 'h':'gjter', 'i':'jghre', 'j':'kfjtr', 'k':'pqmkv', 'l':'tkbpz', 'm':'zmbrg', 'n':'tneam', 'o':'mcnas', 'p':'mzsan', 'q':'tmali', 'r':'maort', 's':'tyrpq', 't':'amlyh', 'u':'tmadf', 'v':'apotr', 'w':'malyh', 'x':'lgtre', 'y':'nhgky', 'z':'rghmf',
    '1':'ktpng', '2':'ngler', '3':'bhrzq', '4':'qaser', '5':'ynapm', '6':'pahtz', '7':'gnegh', '8':'atndi', '9':'grpae', '0':'toage', ' ':'olloo', '.':'llool', '@':'terte', '$':'pwabg', '&':'laqer', '(':'ferte', ')':'etref', '*':'tared', '!':'lform', '#':'kjeqw', '~':'retnj'
}

'''
In this file, I have used raise "Error" which is for debugging only(And to trigger try-except), in actual program, they won't be visible(which is a good thing) and theirfore log serves the purpose of debugging(if using it normally)
'''

#Raw encrypter
def en(inp:str, manual:bool=False):
    ilist=[]
    if manual==True:
        symbol=False
        for i in inp:
            if i not in list(d_en.keys()) and i.lower() not in list(d_en.keys()):
                symbol=True
        if symbol==True:
            symbols=str(ilist)[1:-1]
            log(f'The encrypter was unable to process an unknown symbol: {symbol}\n\tEncryptor recieved an escape or unknown variable that it couldn\'t interpret\n\tTurn off encryption if this issue persists (Not Recommended)')
            raise ValueError(f'libED::"Use of symbol(s):{symbols}"')
        else:
            enp=''
            for ei in inp:
                if ei<='Z' and ei>='A':
                    ei=ei.lower()
                    enp+=d_en[ei].upper()
                else:
                    enp+=d_en[ei]
            return enp
    else:
        log('Their was an issue when trying to access encrypter\n\tThis log shouldn\'t exist if you are using it for third-party reasons, comment log if neccesary')
        raise ModuleNotFoundError('libED::"Using raw libEd function without proper args"')

#Raw decrypter
def ed(inp:str, manual:bool=False):
    if manual==True:
        if inp==None or inp=='':
            log('Decrypter recieved an empty string for some reason\n\tThis may be due to bad procesing or something is wrong with config file\n\tIf the issue persist, turn off encryption(Not Recommended)')
            raise ValueError('libED::"Empty String->NoneType"')
        elif len(inp)%5!=0:
            log('The string recieved by the decrypter had mismatch of length of string:\n\tIt may be due to manual intervention as even one letter matters!')
            raise IndexError('libED::"The string is incomplete or broken"')
        else:
            enp=''
            for i in range(0, len(inp), 5):
                ei=inp[i:i+5]
                if ei[0]<='Z' and ei[0]>='A':
                    ei=ei.lower()
                    for ai in list(d_en.keys()):
                        if d_en[ai]==ei:
                            enp+=ai.upper()
                else:
                    for ai in list(d_en.keys()):
                        if d_en[ai]==ei:
                            enp+=ai
            return enp
    else:
        log('Their was an issue when trying to access decrypter\n\tThis log shouldn\'t exist if you are using it for third-party reasons, comment log if neccesary')
        raise ModuleNotFoundError('libED::"Using raw libEd function without proper args"')

#This function is the main function of the file that handles encrypting and decrypting raw functions
def libcrypt(scanf:str, process:str, add:dict={}, security_level:int=1):
    d_en.update(add)
    if process=='encrypt':
        ec=scanf
        for loop in range(security_level):
            ec=en(ec, True)
    elif process=='decrypt':
        ec=scanf
        for loop in range(security_level):
            ec=ed(ec, True)
    else:
        log('Wrong process was recieved by libcrypt\n\tThis log shouldn\'t exist if you are using it for third-party reasons, comment log if neccesary')
        raise SyntaxError('libED::"Invalid process for libcrypt function"')
    return ec

#Raw compressor
def compresser(inp:str):
    if inp[-1]!='-':
        inp+='-'
    else:
        inp+='+'
    a=inp[0]
    c=0
    comlist=''
    i=0
    while i<len(inp):
        if inp[i]==a:
            c+=1
        else:
            comlist+=f"{c}{a}"
            c=0
            a=inp[i]
            i-=1
        i+=1
    return comlist

#Raw decompresser
def decompresser(inp:str):
    i=0
    num=''
    char=''
    while i<len(inp):
        if inp[i].isdigit():
            num+=inp[i]
        else:
            char+=inp[i]*int(num)
            num=''
        i+=1
    return char

#This file is used in libdata for data-processing. It was the second hardest file after libman, due to logic and thinking required, even if it looks easy than files with more lines but "more lines"!="More Hard"(They are not purpotional, infact, they don't have any connection)