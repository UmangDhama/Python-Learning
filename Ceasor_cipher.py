alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def encrypt(original_text,shift_amount):
    encrypted_text = ""
    for char in original_text:
        if ord(char)<97 or ord(char)>122:
            encrypted_text = encrypted_text +char
        elif ord(char)+shift_amount>122:
            encrypted_text=encrypted_text+chr((shift_amount-(122-ord(char)))+96)
        else:

            encrypted_text = encrypted_text+chr(ord(char)+shift_amount)

    print(f"Here's the encoded result: {encrypted_text}")


def decrypt(encrypted_text,shift_amount):
    decrypted_text=""
    for char in encrypted_text:
        if ord(char)<97 or ord(char)>122:
            decrypted_text = decrypted_text +char
        elif ord(char)-shift_amount<97:
            decrypted_text=decrypted_text+chr(123-(shift_amount-(ord(char)-97)))
        else:
            decrypted_text=decrypted_text+chr(ord(char)-shift_amount)
    print(f"Here's the decoded result: {decrypted_text}")
ans="yes"

while ans=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction=='encode':
         encrypt(text, shift)
         print("Type 'yes' if you want to go again.Otherwise type 'no")
         ans=input()
    elif direction=='decode':
        decrypt(text,shift)
        print("Type 'yes' if you want to go again.Otherwise type 'no'")
        ans = input()



