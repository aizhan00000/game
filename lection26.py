# alpha = ['a','b','c','d','e','f',
#      'g','h','i','j','k','l',
#      'm','n','o','p','q','r',
#      's','t','u','v','w','x',
#      'y','z']
#
# shift = range(26)
#
# def user_info():
#     info = input("\nPress 'e' to encrypt or 'd' to decrypt: ").lower()
#     if info == 'e' or 'd':
#        return info
#
# def user_message():
#     code = input("What is your message?: ")
#     return code
#
# def user_shift():
#      shift = int(input("What is your shift number?: "))
#      while True:
#          if shift == int(shift):
#              return shift
#
# def True_Message(info, code, shift):
#
#     if info[0] == 'd':     #This encrypts the code
#          shift = -shift
#
#     for letter in code:
#         if letter in alpha:
#             alpha_2 = ord(letter) + shift
#             secret_message = ""
#             if alpha_2 in range (0, len(alpha)):
#                 final_mix = chr(alpha)
#                 secret_message += final_mix
#                 return secret_message
#
# info = user_info()
# code = user_message()
# shift = user_shift()
# print(True_Message(info, code, shift))



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
        for i in self.user_message:  # alex
            el_index = self.alphabet.index(i)
            el_index += self.code_number
            if el_index > 25:
                el_index = el_index - 26
            char = self.alphabet[el_index]
            encode_result += char
        self.saved_encode_message = encode_result
        print(encode_result)

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
