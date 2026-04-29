from datetime import date

'''
Romantik Cypher.
by Juan Pedro Basualdo.

This cryptogram is based on the Vignere cryptogram. A message M is encrypted into a cypher C with a three step shift. Given
a date formatted as the tuple of integers (DD,MM,YY) a letter m_i of M is encrypted into a letter c_i of C as follows:
    c_1 = m_1 + DD
    c_2 = m_2 + MM
    c_3 = m_3 + YY
    c_4 = m_4 + DD
        ...
So on and so forth.

A cypher C is encrypted into a message M as follows:
    m_1 = c_1 - DD
    m_2 = c_2 - MM
    m_3 = c_3 - YY
    m_4 = c_4 - DD
        ...
So on and so forth.

The name of this cryptogram is based on the fact that can be used to encrypt a romantic letter to give to a partner as an
anniversary gift. (The k means key)

!!! This cryptogram is not secure at all as it is meant to be cracked in a short period of time with pen and paper. !!!
'''

def encrypt(message: str, anniversary_date: tuple[int, int, int]) -> str:
    '''
    Given a message M and a tuple representing a date, this method encrypts M into a cypher C as follows:
        c_1 = m_1 + DD
        c_2 = m_2 + MM
        c_3 = m_3 + YY
        c_4 = m_4 + DD
            ...
    So on and so forth.
    '''
    cypher = ""
    i = 0
    message = message.lower()

    for char in message:
        if 'a' <= char <= 'z':
            char_code = ord(char) - ord('a')
            shift = anniversary_date[i]

            new_code = (char_code + shift) % 26
            cypher += chr(new_code + ord('a'))

            i = (i + 1) % 3
        else:
            cypher += char
            
    return cypher

def decrypt(cypher: str, anniversary_date: tuple[int, int, int]) -> str:
    '''
    Given a cypher C and a tuple representing a date, this method decrypts C into a message M as follows:
        m_1 = c_1 - DD
        m_2 = c_2 - MM
        m_3 = c_3 - YY
        m_4 = c_4 - DD
            ...
    So on and so forth.
    '''
    message = ""
    i = 0
    
    cypher = cypher.lower()
    
    for char in cypher:
        if 'a' <= char <= 'z':
            char_code = ord(char) - ord('a')
            
            shift = anniversary_date[i]
            new_code = (char_code - shift) % 26
            
            message += chr(new_code + ord('a'))
            
            i = (i + 1) % 3
        else:
            message += char
            
    return message

# ADDONS: Optional fun use cases 

def decrypt_today(cypher: str) -> str:
    '''
    Given a cypher, this method decrypts said cypher with the romantik cryptogram applying today's date.
    (Fun if used on days before or after the key date)
    '''
    today = date.today()
    aniversary_date = (today.day, today.month + 1, today.year)
    return decrypt(cypher, aniversary_date)

def encrypt_from_file(path: str, anniversary_date: tuple[int, int, int]) -> str:
    '''
    Given a path to an existing file, this method encrypts that file's content with the romantik cryptogram. 
    '''
    with open(path, 'r') as file:
        message = file.read()
    return encrypt(message, anniversary_date)

def decrypt_into_file(cypher: str, anniversary_date: tuple[int, int, int], path: str) -> None:
    '''
    Given a path to an existing file, this method decrypts a cypher with the romantik cryptogram into said path.
    '''
    message = decrypt(cypher, anniversary_date)
    with open(path, 'w') as file:
        file.write(message)
    return

def encrypt_in_caesar(message: str) -> str:
    '''
    Encrypts a string with the Caesar cryptogram. 
    Given a message M, each letter c from the cypher C is encrypted from a letter m of M as follows:
        c = m + 3
    '''
    return encrypt(message, (3, 3, 3))

def decrypt_in_caesar(cypher: str) -> str:
    '''
    Decrypts a string with the Caesar cryptogram.
    Given a cypher C, each letter from the message M is decrypted from a letter c of C as follows:
        m = c - 3
    '''
    return decrypt(cypher, (3, 3, 3))

# MAIN METHOD (used for testing)

if __name__ == "__main__":
    fecha_aniv = (2, 5, 18)
    cypher = encrypt("te amo mucho!", fecha_aniv)
    print(cypher)
    print(decrypt_today(cypher))