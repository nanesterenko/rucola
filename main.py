"""декоратор `blossom` будет повторять укананную функцию до `max_retries` раз - пока не равершится без исключений,
 либо пока не превысит число `max_retries`
  + форматирует результат исполнения"""

from typing import Callable, Any

import requests as requests


class ConfigurationError(Exception):
    def __init__(self, message: str):
        super().__init__(self)
        self.message = message

    def __str__(self) -> str:
        return "Некорретные данные"


def blossom(max_retries=1):
    """один необязательный параметр `max_retries` - максимальное количество запусков функции
     Если значение параметра - не целое число или целое число но меньшее 1 - выбросить ConfigurationError"""
    if max_retries < 1 and not isinstance(max_retries, int):
        raise ConfigurationError("Число не целое или меньше 1")

    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            excep_list = list()
            result = None
            for i in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                except Exception as excep:
                    str = f" \"exception\": {excep.__class__.__name__},\n \"return\": {result} \n"
                    excep_list.append(str)
            msg = (f" \"{func.__name__}\": \n \"is_success\" : {bool(result)} \n"
                   f" \"run\" : {excep_list}")
            return msg
        return wrapper
    return decoration


@blossom(3)  # Сохраняет все отловленные исключения, прогоняя функцию до трёх раз
def get_page_content(url):
    resp = requests.get(url)
    return resp.content


# content_with_retry = get_page_content("http://very_fake_address.com")
# print(content_with_retry)

content_with_no_retry = get_page_content("https://httpbin.org/get")
print(content_with_no_retry)
# if __name__ == "__main__":
