import sys

def encrypt(message: str, date: tuple[int, int, int]) -> str:
    new_message = ""
    i = 0
    
    message = message.lower()
    
    for char in message:
        if 'a' <= char <= 'z':
            char_code = ord(char) - ord('a')
            
            shift = date[i]
            new_code = (char_code + shift) % 26
            
            new_message += chr(new_code + ord('a'))
            
            i = (i + 1) % 3
        else:
            new_message += char
            
    return new_message

def decrypt(message: str, date: tuple[int, int, int]) -> str:
    new_message = ""
    i = 0
    
    message = message.lower()
    
    for char in message:
        if 'a' <= char <= 'z':
            char_code = ord(char) - ord('a')
            
            shift = date[i]
            new_code = (char_code - shift) % 26
            
            new_message += chr(new_code + ord('a'))
            
            i = (i + 1) % 3
        else:
            new_message += char
            
    return new_message

def main():
    if(len(sys.argv) != 4 or (sys.argv[1] != "-e" and sys.argv[1] != "-d")):
        print("Use: python3 romantik_schema.py [OPTION] [MESSAGE] [DATE]")
        print("[OPTIONS]:")
        print("     -e : encrypt" \
              "     -d : decrypt")
        return -1
    if(sys.argv[1] == "-e"):
        cypher = encrypt(sys.argv[2], sys.argv[3])
        print(cypher)
    if(sys.argv[1] == "-d"):
        message = decrypt(sys.argv[2], sys.argv[3])
        print(message)
    return 0


if __name__ == "__main__":
    fecha_aniv = (2, 5, 18)
    cypher = encrypt("te amo mucho!", fecha_aniv)
    print(cypher)
    print(decrypt(cypher, fecha_aniv))