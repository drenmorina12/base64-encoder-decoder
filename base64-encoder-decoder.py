
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