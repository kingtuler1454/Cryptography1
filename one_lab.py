table=[
    ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W'],
    ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A'],
    ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B'],
    ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C'],
    ['E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D'],
    ['F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E'],
    ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F'],
    ['H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G'],
    ['I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H'],
    ['J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I'],
    ['K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J'],
    ['L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K'],
    ['M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L'],
    ['N','O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M'],
    ['O','P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N'],
    ['P','Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'],
    ['Q','R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
    ['R','S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
    ['S','T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'],
    ['T','U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'],
    ['U','V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'],
    ['V','X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'],
    ['X','Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'],
    ['Y','Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X'],
    ['Z','W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y'],
    ['W','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z'],
    ]


def cipher(symbol, key_char):
    number_string = table[0].index(symbol)  # вычисляем насколь вниз нам опуститься по значению символа
    number_column = table[0].index(key_char)  # вычисляем насколько вправо двигаться по ключу
    
    return table[number_string][number_column]    # вернем шифр значение по данным координатам


def decipher(symbol, key_char):
    number_column = table[0].index(key_char)   # в дешифровке номер столбца это по символу ключу
    for i in range(len(table)):  # смотрим в какой строке у нас совпадет символ с зашифрованным
        if table[i][number_column] == symbol:
            return str(table[0][i])  # когда символ совпал, вернем расшифрованный символ


def main():
    print('Encryption..')
    with open('start_message.txt') as file:  # открываем файл для чтения
        text = file.read()
    key_char = str('A')  #изначальный ключ шифрования A, ибо
    cipher_text = '' # шифр текст строка в которую будем добавлять символы
    for symbol in text.upper():  # поднимем все символы в верхний регистр и для каждого такого символа
        if symbol in table[0]:  # если символ есть в таблице, то можем его зашифровать
            symbol_cipher = cipher(symbol, key_char) #  отправляем изначальный символ и сивол ключ, получаем зашифрованный символ
            cipher_text += symbol_cipher  # добавляем шифрсимвол к строке
            key_char = symbol  # меняем ключ символ на исходный символ, так у нас последующий ключ это будет предыдущий символ
        else:
            cipher_text += symbol  # если вдруг попадяется например запятая, просто запишем ее
    cipher_text = cipher_text.lower()  # понизим все уродство к нижнему регистру для красоты
    with open("cipher.txt", "w") as file:  # запишем шифртекст в файл
        file.write(cipher_text)
        
    print('Decryption..')    
    with open('cipher.txt') as file:  # откроем файлик для дешифровки
        text = file.read()
    key_char = str('A')  # начальный ключ снова A
    decipher_text = ''
    for symbol in text.upper():  # ch
        if symbol in table[0]:
            symbol_decipher = decipher(symbol, key_char)  # отправляемся в  функцию дешифровки
            decipher_text += symbol_decipher
            key_char = symbol_decipher  # ДЛЯ ДЕШИФРОВКИ ТУТ ЗАПИСЫВАЕМ РАСШИФРОВАННЫЙ СИМВОЛ
        else:
            decipher_text += symbol
    decipher_text = decipher_text.lower()
    with open("decipher.txt", "w") as file:  # запись файла дешифровки
        file.write(decipher_text)
    print('Successfully')
    
if __name__ == "__main__":
    main()
