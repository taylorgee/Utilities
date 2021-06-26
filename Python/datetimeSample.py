import datetime

def timestamp():
    today = datetime.datetime.now()
    current = today.strftime('%m/%d/%Y %H:%M:%S')
    return current

today = timestamp() 
print(str(today))

print(f'---{today}')




