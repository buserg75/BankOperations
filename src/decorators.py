from typing import Any, Callable


def log(filename=None):
    """Декоратор для логирования функции и вывода результата в файл или в консоль"""
    def wrapper(fnc: Callable) -> Any:
        def inner(*args, **kwargs) -> Any:
            try:
                result = fnc(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{fnc.__name__} ok\n")
                else:
                    print(f"{fnc.__name__} ok\n")
                return result

            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{fnc.__name__} error: Делить на ноль нельзя! Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{fnc.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                return 'Делить на ноль нельзя!'

        return inner
    return wrapper


@log(filename="mylog.txt")
def add(x, y):
    return x + y


add(5, 3)


@log(filename="mylog.txt")
def divide(x, y):
    return x / y


divide(2, 0)

if __name__ == "__main__":  # pragma: no cover
    print(add(5, 3))  # 8
    print(divide(2, 0))  # Ошибка деления на ноль
