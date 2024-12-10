# ID - 129613266
def decode_string(s: str) -> str:
    """Функция, которая дешифрует инструкции."""
    stack: list[tuple[str, int]] = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            # Получаем число
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Сохраняем текущую строку и число в стек
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            # Извлекаем строку и число из стека
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            # Просто добавляем символ к текущей строке
            current_str += char

    return current_str


if __name__ == '__main__':
    print(decode_string(input()))
