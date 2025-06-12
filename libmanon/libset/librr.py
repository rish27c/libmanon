#This is error-handler for libmanon, log function is for recording errors in Error_logs.txt for tracebag

#Function to record errors
def log(words:any, type:str='Error'):
    try:
        with open('Error_logs.txt', 'r') as report:
            logs=report.read()
        c=logs.count('Log#')+1
        logs=logs.split('\n')
    except:
        c=1
        logs=[]
    record=f'[{type} Log#{c}] {words}'
    logs.append(record)
    record='\n'.join(logs)
    with open('Error_logs.txt', 'w') as crash:
        crash.write(record)

#Sorry, bro, Emrgency-mode stole your one of the functions but I will add some, the project is far from done, not until I also have GUI in it for user while unix mode for technical people(which would naturally have more control)