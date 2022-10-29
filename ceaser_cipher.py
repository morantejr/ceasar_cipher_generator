alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction.lower() == "decode":
        shift_amount *= -1
        for char in start_text:
            end_text += alphabet[alphabet.index(char)+shift_amount]
    elif cipher_direction.lower() == "encrypt":
        for char in start_text:
            end_text += alphabet[alphabet.index(char)+shift_amount]
    else:
        print("Incorrect")
    print(end_text)
cesar("hello",5,"encrypt")
