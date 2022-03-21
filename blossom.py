""" Декоратор `blossom` повторяет укананную функцию до `max_retries` раз - пока не равершится без исключений,
 либо пока не превысит число `max_retries` и форматирует результат исполнения."""

from typing import Callable, Any
import requests as requests


class ConfigurationError(Exception):
    def __init__(self, message: str):
        super().__init__(self)
        self.message = message

    def __str__(self) -> str:
        return "Некорретные данные"


def blossom(max_retries: int = 1) -> Callable:
    """один необязательный параметр `max_retries` - максимальное количество запусков функции
     Если значение параметра - не целое число или целое число но меньшее 1 - выбросить ConfigurationError"""
    if max_retries < 1 or not isinstance(max_retries, int):
        raise ConfigurationError("Число не целое или меньше 1")

    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            excep_list = list()
            isSussess = False
            result = None
            for i in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    isSussess = True
                    str = (f" \"exception\": {None},"
                           f" \"return\": {result}")
                    excep_list.append(str)
                    break
                except Exception as excep:
                    isSussess = False
                    str = (f" \"exception\": {excep.__class__.__name__}, "
                           f" \"return\": {result}")
                    excep_list.append(str)
            msg = (f" \"{func.__name__}\": \n \"is_success\" : {isSussess} \n"
                   f" \"run\" : {excep_list}")
            return msg

        return wrapper

    return decoration


@blossom(2)
def get_page_content(url: str) -> Any:
    """Получение содержимого страницы по url"""
    resp = requests.get(url)
    return resp.content


content_with_retry = get_page_content("http://very_fake_address.com")
print(content_with_retry)

# content = get_page_content("https://httpbin.org")
# print(content)

# content_with_no_retry = get_page_content("https://httpbin.org/get")
# print(content_with_no_retry)
