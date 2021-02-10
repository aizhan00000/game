class CesarCipher:
    def __init__(self):
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'
        ]
        self.user_message = ''
        self.saved_encode_message = ''
        self.code_number = 0
        self.saved_encode_number = 0

    def encode(self):
        self.user_message = input("Enter a word: ").lower()
        self.code_number = int(input("Enter number to encode(1-25): "))
        while self.code_number > 25 or self.code_number == 0:
            self.code_number = int(input("Enter number to encode(1-25): "))
        self.saved_encode_number = self.code_number

        encode_result = ""
        file = open("file.txt", 'w')
        for i in self.user_message:
            el_index = self.alphabet.index(i)
            el_index += self.code_number
            if el_index > 25:
                el_index = el_index - 26
            char = self.alphabet[el_index]
            encode_result += char
        self.saved_encode_message = encode_result
        print(encode_result)
        file.write(self.user_message)
        file.close()

    def decode(self):
        self.user_message = input("Enter a word: ").lower()
        self.code_number = int(input("Enter number to decode(1-25): "))
        while self.code_number > 25 or self.code_number == 0:
            self.code_number = int(input("Enter number to decode(1-25): "))

        decode_result = ""
        if self.code_number == self.saved_encode_number:
            for i in self.user_message:  # fqjc
                el_index = self.alphabet.index(i)
                el_index -= self.code_number
                if el_index < 0:
                    el_index += 26
                char = self.alphabet[el_index]
                decode_result += char
        print(decode_result)


def main():
    cesar = CesarCipher()
    user_choice = int(input(
        "1) Encode message.\n"
        "2) Decode message.\n"
        "3) Quit.\n"
        "Choose an action: "
    ))
    if user_choice == 1:
        cesar.encode()
        print(cesar.code_number)
        print(cesar.saved_encode_number)
        return main()
    elif user_choice == 2:
        cesar.decode()
        print(cesar.code_number)
        print(cesar.saved_encode_number)
        return main()
    else:
        return True


if __name__ == '__main__':
    main()