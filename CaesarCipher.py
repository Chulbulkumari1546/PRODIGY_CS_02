#IMPLEMENT CAESAR CIPHER
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
#For Encryption
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
      if char in Alphabet:
       position=Alphabet.index(char)
       new_position=(position+shift_key)%26
       cipher_text +=Alphabet[new_position]
      else:
        cipher_text += char
    print(f"Here is the text after encryption: {cipher_text}")

#For Decryption
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
      if char in Alphabet:
       position=Alphabet.index(char)
       new_position=(position-shift_key)%26
       plain_text +=Alphabet[new_position]
      else:
        plain_text += char 
    print(f"Here is the text after decryption: {plain_text}")

#For looping
end_program=False
while not end_program:
  what_to_do=input("Type 'encrypt' for encryption,type 'decrypt' for decryption:\n")
  text=input("Type your message:\n").lower()  #for lower case conversion
  shift=int(input("Enter shift key:\n"))
  if what_to_do=="encrypt":
    encryption(plain_text=text,shift_key=shift)
  elif what_to_do=="decrypt":
     decryption(cipher_text=text,shift_key=shift)
  continue_again=input("Type 'yes' to continue, type 'no' to exit: \n")
  if continue_again=='no':
   end_program=True
   print("Thank You for using this  !")
 
