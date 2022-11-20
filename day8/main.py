alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
if direction == 'encode':
  def encrypt(text1, shift1):
    cipher_text = []
    for letter in text:
      position = alphabet.index(letter)
      cipher_text.append(alphabet[position+shift])
    print(f'Your encrypted message is {"".join(cipher_text)}')
  encrypt(text1=text,shift1=shift)

if direction == 'decode':
  def encrypt(text1, shift1):
    cipher_text = []
    for letter in text:
      position = alphabet.index(letter)
      cipher_text.append(alphabet[position-shift])
    print(f'Your dencrypted message is {"".join(cipher_text)}')
  encrypt(text1=text,shift1=shift)
    
