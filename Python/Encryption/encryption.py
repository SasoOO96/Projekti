import random

def generate_random_numbers(length, seed):
    random.seed(seed)
    return [random.randint(0, 255) for _ in range(length)]

def encrypt_text(text, key):
    random_numbers = generate_random_numbers(len(text), key)
    encrypted_text = ''
    for char, rand_num in zip(text, random_numbers):
        encrypted_text += chr(ord(char) ^ rand_num)
    return encrypted_text

def decrypt_text(text, key):
    random_numbers = generate_random_numbers(len(text), key)
    decrypted_text = ''
    for char, rand_num in zip(text, random_numbers):
        decrypted_text += chr(ord(char) ^ rand_num)
    return decrypted_text
