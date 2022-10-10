from datetime import datetime
import os


def decorator_logger(file_name):
    file_path = os.path.abspath(file_name)

    def decorator_it_self(some_function):
        time = datetime.now().strftime("%d %B %Y  time %H:%M:%S")

        def new_function(*args, **kwargs):
            result = some_function(*args, **kwargs)
            text = f'''Дата и время вызова функции: {time};
Имя функции: {some_function.__name__};
Аргументы: {args};
Результат: {result}\n\n'''
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(text)
            return result
        return new_function
    return decorator_it_self
