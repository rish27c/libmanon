from .uf_var import le
lmvr={}

def compile():
    global le
    try:
        with open('lib.menu', 'r') as file:
            data=file.read()
        data=data.split('\n')
    except:
        print('Unable to load menu :(\n \'lib.menu\' file not found.\n', flush=True)
        #i will create a mini compiler for script handling
    try:
        for od in range(len(data)):
            try:
                inst=data[od]
                if inst.strip()!='' or inst[0]!='#' or inst[0]!='/' or inst[0]!='?' or inst[0]==';':
                    if inst[0]=='!':
                        inst=inst[1:]
                        if inst[0:8]=='DISPLAY ':
                            try:
                                dis=inst[8:]
                                prt=''
                                for nd in dis.split():
                                    if nd[0:5]=='load[' and nd[-1]==']':
                                        st=nd[5:-1]
                                        prt+=str(lmvr[st])
                                    else:
                                        prt+=nd+' '
                                print(prt, flush=True)
                            except:
                                print('Failed echoing at line', od+1)
                        elif inst[0:4]=='GET ':
                            try:
                                get=input(inst[4:])
                                try:
                                    if float(get)==int(get):
                                        get=int(get)
                                    else:
                                        get=float(get)
                                except:
                                    pass
                            except:
                                print('Failed user-input at line', od+1)
                        elif inst[0:5]=='SAVE ':
                            try:
                                if inst[5:].split()[-2:]==['as', '&GET']:
                                    if inst[5:].split()[-3]==inst[5:].split()[0]:
                                        var=inst[5:].split()[-3]
                                        lmvr.update({var:get})
                                    else:
                                        print('Invalid variable assignment at line', od+1)
                                elif inst[5:].split()[-2:]==['as', '&GET2']:
                                    if inst[5:].split()[-3]==inst[5:].split()[0]:
                                        var=inst[5:].split()[-3]
                                        lmvr.update({var:f'[{get}]'})
                                    else:
                                        print('Invalid variable assignment at line', od+1)
                                elif inst[5:].split()[-2:]==['as', '&GET3']:
                                    if inst[5:].split()[-3]==inst[5:].split()[0]:
                                        var=inst[5:].split()[-3]
                                        lmvr.update({var:f'%[{get}]%'})
                                    else:
                                        print('Invalid variable assignment at line', od+1)
                                else:
                                    sit=inst.split()
                                    if sit[3]!='as' or len(sit)>5:
                                        print('Invalid syntax at line', od+1)
                                    else:
                                        if sit[1]=='pnum':
                                            var=sit[2]; val=int(sit[4])
                                            lmvr.update(var, val)
                                        elif sit[1]=='fnum':
                                            var=sit[2]; val=float(sit[4])
                                            lmvr.update(var, val)
                                        elif sit[1]=='chars':
                                            var=sit[2]; val=' '.join(sit[4:])
                                            lmvr.update({var:val})
                                        else:
                                            print('Datatype not defined in sdaving value at line', od+1)
                            except:
                                print('Failed to save value at line', od+1)
                        elif inst[0:3]=='IF ':
                            try:
                                prt=''
                                for nf in inst[3:].split():
                                    if nf[0:5]=='load[' and nf[-1]==']':
                                        nv=nf[5:-1]
                                        nv=str(lmvr[nv])
                                    else:
                                        nv=nf
                                    prt+=nv
                                if prt[-1]!=':':
                                    print('Invalid conditionl syntax at line', od+1)
                                else:
                                    if not eval(str(prt[0:-1])):
                                        sn=od
                                        while True:
                                            if data[sn]!='#!FI':
                                                data[sn]=''
                                                sn+=1
                                            else:
                                                data[sn]=''
                                                break
                            except:
                                try:
                                    sn=od
                                    while True:
                                        if data[sn]!='#!FI':
                                            data[sn]=''
                                            sn+=1
                                        else:
                                            data[sn]=''
                                            break
                                except:
                                    pass
                        else:
                            print('Unknown line at line', od+1)
                    elif inst[0]=='$':
                        if inst[1:]=='STOP':
                            return 'exit'
                        elif inst[1:8]=='PROMPT ':
                            pt=''
                            for i in inst[8:].split():
                                if i[0:5]=='load[' and i[-1]==']':
                                    v=i[5:-1]
                                    v=str(lmvr[v])
                                else:
                                    v=i
                                pt+=v+' '
                            pmt=pt.split()
                            return pmt
                        else:
                            print('Unknown line at line', od+1)
                    elif inst[0]=='?':
                        try:
                            eval(str(inst[1:]))
                        except:
                            print('Failed to run line', od+1)
                    elif inst[0]==';':
                        if inst[1:]!='EXE':
                            le.append(inst[1:])
                        else:
                            exe='\n'.join(le)
                            le=[]
                            try:
                                exec(str(exe))
                            except:
                                print('ExecutionError occured :(')
            except:
                pass
    except:
        pass

def precompile():
    global le
    try:
        with open('lib.menu', 'r') as file:
            data=file.read()
        data=data.split('\n')
    except:
        print('Unable to load menu :(\n \'lib.menu\' file not found.\n', flush=True)
        #i will create a mini compiler for script handling
    try:
        for od in range(len(data)):
            try:
                if data[od][0]=='/':
                    inst=data[od][1:]
                    if inst.strip()!='' or inst[0]!='#' or inst[0]!='/' or inst[0]!='?' or inst[0]==';':
                        if inst[0]=='!':
                            inst=inst[1:]
                            if inst[0:8]=='DISPLAY ':
                                try:
                                    dis=inst[8:]
                                    prt=''
                                    for nd in dis.split():
                                        if nd[0:5]=='load[' and nd[-1]==']':
                                            st=nd[5:-1]
                                            prt+=str(lmvr[st])
                                        else:
                                            prt+=nd+' '
                                    print(prt, flush=True)
                                except:
                                    print('Failed echoing at line', od+1)
                            elif inst[0:4]=='GET ':
                                try:
                                    get=input(inst[4:])
                                    try:
                                        if float(get)==int(get):
                                            get=int(get)
                                        else:
                                            get=float(get)
                                    except:
                                        pass
                                except:
                                    print('Failed user-input at line', od+1)
                            elif inst[0:5]=='SAVE ':
                                try:
                                    if inst[5:].split()[-2:]==['as', '&GET']:
                                        if inst[5:].split()[-3]==inst[5:].split()[0]:
                                            var=inst[5:].split()[-3]
                                            lmvr.update({var:get})
                                        else:
                                            print('Invalid variable assignment at line', od+1)
                                    else:
                                        sit=inst.split()
                                        if sit[3]!='as' or len(sit)>4:
                                            print('Invalid syntax at line', od+1)
                                        else:
                                            if sit[1]=='pnum':
                                                var=sit[2]; val=int(sit[4])
                                                lmvr.update({var:val})
                                            elif sit[1]=='fnum':
                                                var=sit[2]; val=float(sit[4])
                                                lmvr.update({var:val})
                                            elif sit[1]=='chars':
                                                var=sit[2]; val=' '.join(sit[4:])
                                                lmvr.update({var:val})
                                            else:
                                                print('Datatype not defined in sdaving value at line', od+1)
                                except:
                                    print('Failed to save value at line', od+1)
                            elif inst[0:3]=='IF ':
                                try:
                                    prt=''
                                    for nf in inst[3:].split():
                                        if nf[0:5]=='load[' and nf[-1]==']':
                                            nv=nf[5:-1]
                                            nv=str(lmvr[nv])
                                        else:
                                            nv=nf
                                        prt+=nv
                                    if prt[-1]!=':':
                                        print('Invalid conditionl syntax at line', od+1)
                                    else:
                                        if not eval(str(prt[0:-1])):
                                            data[od+1]=''
                                except:
                                    print('Condition failure at line', od+1)
                            else:
                                print('Unknown line at line', od+1)
                        elif inst[0]=='$':
                            if inst[1:]=='STOP':
                                return 'exit'
                            elif inst[1:8]=='PROMPT ':
                                pt=''
                                for i in inst[8:].split():
                                    if i[0:5]=='load[' and i[-1]==']':
                                        v=i[5:-1]
                                        v=str(lmvr[v])
                                    else:
                                        v=i
                                    pt+=v+' '
                                pmt=pt.split()
                                return pmt
                            else:
                                print('Unknown line at line', od+1)
                        elif inst[0]=='?':
                            try:
                                eval(str(inst[1:]))
                            except:
                                print('Failed to run line', od+1)
                        elif inst[0]==';':
                            if inst[1:]!='EXE':
                                le.append(inst[1:])
                            else:
                                exe='\n'.join(le)
                                le=[]
                                try:
                                    exec(str(exe))
                                except:
                                    print('ExecutionError occured :(')
            except:
                pass
    except:
        pass