# This lab was made by Ryan with Day as a collaborator on 3/7/23

def encoder(password):
    encoded = ""
    for char in password:
        encoded += str(int(char) + 3)
    return encoded


def decoder(password):
    decoded = ""
    for char in password:
        decoded += str(int(char) - 3)
    return decoded


def main():
    orig_pass = ""
    encoded_pass = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        selection = int(input("Please enter an option: "))
        if selection == 1:
            orig_pass = input("Please enter your password to encode: ")
            encoded_pass = encoder(orig_pass)
            print("Your password has been encoded and stored!")
        if selection == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {orig_pass}")
        if selection == 3:
            break


if __name__ == "__main__":
    main()
