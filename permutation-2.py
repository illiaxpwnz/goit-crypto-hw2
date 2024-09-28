def create_key_sequence(key):
    key = key.upper()
    sorted_key = sorted(list(key))
    key_sequence = []
    for char in key:
        index = sorted_key.index(char) + 1
        key_sequence.append(index)
        sorted_key[index - 1] = None  # Уникаємо дублювання
    return key_sequence

def simple_permutation_encrypt(text, key):
    key_sequence = create_key_sequence(key)
    key_len = len(key_sequence)
    text_blocks = [text[i:i+key_len] for i in range(0, len(text), key_len)]
    
    encrypted_text = []
    
    for block in text_blocks:
        block = list(block)
        while len(block) < key_len:
            block.append(' ')  # Доповнюємо пробілами для повного блоку
        encrypted_block = [''] * key_len
        for i, k in enumerate(key_sequence):
            encrypted_block[k - 1] = block[i]
        encrypted_text.append(''.join(encrypted_block))
    
    return ''.join(encrypted_text)

def simple_permutation_decrypt(ciphertext, key):
    key_sequence = create_key_sequence(key)
    key_len = len(key_sequence)
    text_blocks = [ciphertext[i:i+key_len] for i in range(0, len(ciphertext), key_len)]
    
    decrypted_text = []
    
    for block in text_blocks:
        block = list(block)
        decrypted_block = [''] * key_len
        for i, k in enumerate(key_sequence):
            if k - 1 < len(block):
                decrypted_block[i] = block[k - 1]
        decrypted_text.append(''.join(decrypted_block))
    
    return ''.join(decrypted_text).rstrip()

def double_permutation_encrypt(text, key1, key2):
    # Спочатку шифруємо за першим ключем
    first_encryption = simple_permutation_encrypt(text, key1)
    
    # Потім шифруємо за другим ключем
    second_encryption = simple_permutation_encrypt(first_encryption, key2)
    
    return second_encryption

def double_permutation_decrypt(ciphertext, key1, key2):
    # Спочатку розшифровуємо за другим ключем
    first_decryption = simple_permutation_decrypt(ciphertext, key2)
    
    # Потім розшифровуємо за першим ключем
    second_decryption = simple_permutation_decrypt(first_decryption, key1)
    
    return second_decryption

# Використання:
key1 = "SECRET"
key2 = "CRYPTO"
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

# Шифрування тексту з подвійною перестановкою
encrypted_double = double_permutation_encrypt(text, key1, key2)
print(f"Зашифрований текст з подвійною перестановкою:\n{encrypted_double}")

# Дешифрування тексту з подвійною перестановкою
decrypted_double = double_permutation_decrypt(encrypted_double, key1, key2)
print(f"Розшифрований текст з подвійною перестановкою:\n{decrypted_double}")
