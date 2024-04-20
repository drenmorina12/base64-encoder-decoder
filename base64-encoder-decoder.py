
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
