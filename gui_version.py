from tkinter import *
from base64_encoder_decoder import encode, decode

root = Tk()
root.title("Base64 encoder/decoder")

# Input
input_label = Label(root, text="Input text")
input_label.grid(row=0, column=0)

input_text = Text(root, width=30, height=7, padx=5, pady=5)
input_text.grid(row=1, column=0, padx=10, pady=10)

# Output
output_label = Label(root, text="Output text")
output_label.grid(row=0, column=2)

output_text = Text(root, width=30, height=7)
output_text.grid(row=1, column=2, padx=10, pady=10)

def decrypted_text_output():
    output_text.delete("1.0", END)
    output_text.insert("1.0", encode(input_text.get("1.0", 'end-1c')))
#     end-1c instead of END to avoid adding new line


def encrypted_text_output():
    input_text.delete("1.0", END)
    input_text.insert("1.0", decode(output_text.get("1.0", 'end-1c')))

mainloop()

# Buttons
encrypt_button = Button(root, text="Encrypt", command=decrypted_text_output)
encrypt_button.grid(row=2, column=0)

decrypt_button = Button(root, text="Decrypt", command=encrypted_text_output)
decrypt_button.grid(row=2, column=2)