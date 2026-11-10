from functools import wraps # This is for the Task 3

# Task 1

import re

class User:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not isinstance(email, str) or not re.match(pattern, email):
            raise ValueError(f"Invalid email: {email}")
        
        return True


user1 = User("alex@example.com")
print(user1.email)

# user2 = User("alex-example.com")  # error check

# Task 2

class Boss:

    def __init__(self, id_: int, name: str, company: str):

        self.id = id_

        self.name = name

        self.company = company

        self._workers = []
        
    @property
    def workers(self):
        return self._workers.copy()
        
    def add_worker(self, worker):
        if isinstance(worker, Worker):
            if worker not in self._workers:
                self._workers.append(worker)
        else:
            raise ValueError("Wrong type of value")
        
    def remove_worker(self, worker):
        if isinstance(worker, Worker):
            if worker in self._workers:
                self._workers.remove(worker)
        else:
            raise ValueError("Wrong type of value")
        
 

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):

        self.id = id_

        self.name = name

        self.company = company
        
        self._boss = None

        self.boss = boss
        
    @property
    def boss(self):
        return self._boss
        
    @boss.setter
    def boss(self, value: Boss):
        if isinstance(value, Boss):
            if self._boss and self._boss != value:
                self._boss.remove_worker(self)
            self._boss = value
            value.add_worker(self)
        else:
            raise ValueError("Wrong type of value")
        
# Task 3

class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                return int(res)
            except (ValueError, TypeError):
                return res
        return wrapper 

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                return str(res)
            except (ValueError, TypeError):
                return res
        return wrapper 

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, str):
                if res.strip().lower() == 'true' or res.strip().lower() == '1':
                    return True
                elif res.strip().lower() == 'false' or res.strip().lower() == '0':
                    return False
                else:
                    return res
            else:
                return bool(res)
        return wrapper 

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                return float(res)
            except (ValueError, TypeError):
                return res
        return wrapper 
 
@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

 

assert do_nothing('25') == 25
assert do_something('True') is True