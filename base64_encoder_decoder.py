# import base64

# my_text = "Hello World"


# def encode(text):
#     text = text.encode("ascii")
#     text_b64 = base64.b64encode(text)
#     return text_b64

# def decode(text_b64):
#     text = base64.b64decode(text_b64)
#     return text

base64_table = {
    '000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D',
    '000100': 'E', '000101': 'F', '000110': 'G', '000111': 'H',
    '001000': 'I', '001001': 'J', '001010': 'K', '001011': 'L',
    '001100': 'M', '001101': 'N', '001110': 'O', '001111': 'P',
    '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T',
    '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X',
    '011000': 'Y', '011001': 'Z', '011010': 'a', '011011': 'b',
    '011100': 'c', '011101': 'd', '011110': 'e', '011111': 'f',
    '100000': 'g', '100001': 'h', '100010': 'i', '100011': 'j',
    '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n',
    '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r',
    '101100': 's', '101101': 't', '101110': 'u', '101111': 'v',
    '110000': 'w', '110001': 'x', '110010': 'y', '110011': 'z',
    '110100': '0', '110101': '1', '110110': '2', '110111': '3',
    '111000': '4', '111001': '5', '111010': '6', '111011': '7',
    '111100': '8', '111101': '9', '111110': '+', '111111': '/'
}

inverse_base64_table = {value: key for key, value in base64_table.items()}

my_text1 = "MUGIWARaaaaaaaaa"

#konvertimi i tekstit ne ASCII-vlere, konvertimi ne blloqe binare 8-biteshe
def text_to_binary(text):
    binary_text = ''.join('{0:08b}'.format(ord(x), 'b') for x in text)
    return binary_text

#ndarja e string-ut binare ne blloqe 6-biteshe
def chunk_binary_for_encoding(binary_string):
    chunks = []
    chunk_size = 6
    for i in range(0, len(binary_string), chunk_size):
        chunk = binary_string[i:i+chunk_size].ljust(chunk_size, '0')
        chunks.append(chunk)

    return chunks

def binary_to_text(binary_text):
    # Ndani tekstin binar në pjesë të vogla prej 8 bitësh
    chunks = []
    for i in range(0, len(binary_text), 8):
        chunks.append(binary_text[i:i + 8])
    # chunks = [binary_text[i:i + 8] for i in range(0, len(binary_text), 8)]

    # Konvertoni çdo pjesë 8-bitësh në paraqitjen e saj të karaktereve ASCII
    text = ''.join(chr(int(chunk, 2)) for chunk in chunks)

    return text

def chunk_binary_for_decoding(binary_string):
    # Lista për të ruajtur blloqet e 8 bitësh
    chunks = []
    chunk_size = 8
    # Iterimi përmes vargut të dhënë binar
    for i in range(0, len(binary_string), chunk_size):
        chunk = binary_string[i:i+chunk_size].ljust(chunk_size, '0')
        chunks.append(chunk)
        
    return chunks

def encode(text):
    base64_text = ""
    binary_text = text_to_binary(text)
    chunks = chunk_binary_for_encoding(binary_text)

    for chunk in chunks:
        base64_text += base64_table[chunk]

    if len(binary_text) % 3 == 1:
        base64_text += "="
    elif len(binary_text) % 3 == 2:
        base64_text += "=="

    return base64_text

def decode(base65_text):
    normal_text = ""
    binary_values = []

    for i in base65_text:
        # print(i)
        if i == '=':
            continue
        binary_values.append(inverse_base64_table[i])

    binary_text = ''.join(binary_values)
    # print(binary_text)
    chunks = chunk_binary_for_decoding(binary_text)

    for chunk in chunks:

        normal_text += binary_to_text(chunk)

    return normal_text
