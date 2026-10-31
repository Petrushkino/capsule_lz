import os
import getpass
import datetime
import uuid
import pandas as pd
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        current_time = datetime.datetime.now()
        log_data = {
            "id": [str(uuid.uuid4())], # генерация уникального ID
            "pc_username": [getpass.getuser()], # получение имени пользователя ПК
            "function_name": [func.__name__], # имя вызванной функции
            "Date in \"date.month.year\"": [current_time.strftime("%d.%m.%Y")], # форматированная дата
            "Time": [current_time.strftime("%H:%M:%S")] # форматированное время
        }
        
        df = pd.DataFrame(log_data)
        file_name = "logs.csv"
        
        if not os.path.exists(file_name):
            df.to_csv(file_name, index=False, mode='w', header=True)
        else:
            df.to_csv(file_name, index=False, mode='a', header=False)
            
        return result
    return wrapper