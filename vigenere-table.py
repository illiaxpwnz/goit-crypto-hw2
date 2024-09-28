import math

# Шифр Віженера
def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key.upper()
    key_len = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Пропускаємо неалфавітні символи
    
    return ''.join(encrypted_text)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key = key.upper()
    key_len = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            decrypted_char = chr((ord(char.upper()) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# Табличний шифр
def create_table_key_sequence(key):
    key = key.upper()
    sorted_key = sorted(list(key))
    key_sequence = []
    for char in key:
        index = sorted_key.index(char) + 1
        key_sequence.append(index)
        sorted_key[index - 1] = None  # Уникаємо дублювання
    return key_sequence

def table_encrypt(text, key):
    key_sequence = create_table_key_sequence(key)
    key_len = len(key_sequence)
    
    # Розбиваємо текст на блоки по довжині ключа
    rows = math.ceil(len(text) / key_len)
    table = [['' for _ in range(key_len)] for _ in range(rows)]
    
    # Заповнюємо таблицю по рядках
    index = 0
    for r in range(rows):
        for c in range(key_len):
            if index < len(text):
                table[r][c] = text[index]
                index += 1
            else:
                table[r][c] = ' '  # Заповнюємо порожні місця пробілами

    # Читаємо стовпці у новому порядку, визначеному ключем
    encrypted_text = []
    for k in range(1, key_len + 1):
        col_index = key_sequence.index(k)
        for r in range(rows):
            encrypted_text.append(table[r][col_index])
    
    return ''.join(encrypted_text)

def table_decrypt(ciphertext, key):
    key_sequence = create_table_key_sequence(key)
    key_len = len(key_sequence)
    
    rows = math.ceil(len(ciphertext) / key_len)
    table = [['' for _ in range(key_len)] for _ in range(rows)]
    
    # Заповнюємо таблицю по стовпцях у порядку ключа
    index = 0
    for k in range(1, key_len + 1):
        col_index = key_sequence.index(k)
        for r in range(rows):
            if index < len(ciphertext):
                table[r][col_index] = ciphertext[index]
                index += 1

    # Читаємо таблицю по рядках
    decrypted_text = []
    for r in range(rows):
        for c in range(key_len):
            decrypted_text.append(table[r][c])
    
    return ''.join(decrypted_text).rstrip()

# Використання шифрування Віженера та табличного шифру
vigenere_key = "CRYPTO"
table_key = "MATRIX"

# Текст для шифрування
text = """
The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. 
The critic is he who can translate into another manner or a new material his impression of beautiful things. 
The highest, as the lowest, form of criticism is a mode of autobiography. 
Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. 
Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. 
They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. 
Books are well written, or badly written. That is all. 
The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. 
The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. 
The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. 
No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. 
An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. 
The artist can express everything. Thought and language are to the artist instruments of an art. 
Vice and virtue are to the artist materials for an art. 
From the point of view of form, the type of all the arts is the art of the musician. 
From the point of view of feeling, the actor's craft is the type. 
All art is at once surface and symbol. Those who go beneath the surface do so at their peril. 
Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. 
Diversity of opinion about a work of art shows that the work is new, complex, vital. 
When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. 
The only excuse for making a useless thing is that one admires it intensely. All art is quite useless.
"""

# Спочатку шифруємо текст за допомогою шифру Віженера
vigenere_encrypted = vigenere_encrypt(text, vigenere_key)

# Потім шифруємо результат за допомогою табличного шифру
final_encrypted_text = table_encrypt(vigenere_encrypted, table_key)
print(f"Зашифрований текст з Віженера і табличного шифру:\n{final_encrypted_text}")

# Для дешифрування спочатку застосовуємо табличний шифр
table_decrypted_text = table_decrypt(final_encrypted_text, table_key)

# Потім розшифровуємо результат за допомогою шифру Віженера
final_decrypted_text = vigenere_decrypt(table_decrypted_text, vigenere_key)
print(f"Розшифрований текст: {final_decrypted_text}")
