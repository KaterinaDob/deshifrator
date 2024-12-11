# ID - 129672379
def decode_string(encrypted_string: str) -> str:
    """Функция, которая дешифрует инструкции."""
    stack: list[tuple[str, int]] = []
    current_num = current_str = ''
    numbers: set[str] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for char in encrypted_string:
        if char in numbers:
            current_num += char
        elif char == '[':
            stack.append((current_str, int(current_num)))
            current_str = current_num = ''
        elif char == ']':
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            current_str += char

    return current_str


if __name__ == '__main__':
    print(decode_string(input()))
