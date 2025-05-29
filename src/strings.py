welcome_message = "Welcome to the CrowdStrike Python demo!"

def print_welcome_message(message):
    print(message)


def make_string_uppercase(message):
    return message.upper()


def make_string_lowercase(message):
    return message.lower()


def split_string_into_list(message):
    return message.split()


def print_string_length(message):
    print(f"Length of the message: {len(message)}")


def iterate_though_list(message_list):
    count = 0
    for item in message_list:
        count += 1
        print(f"word {count}: {item}")


def is_string_palindrome(message):
    if message == message[::-1]:
        print(f"{message} is a palindrome")
        return True
    else:   
        print(f"{message} is not a palindrome")
        return False


 
if __name__ == "__main__":
    print_welcome_message(welcome_message)
    print_string_length(welcome_message)
    uppercase_message = make_string_uppercase(welcome_message)
    print(f"Uppercase message: {uppercase_message}")
    lowercase_message = make_string_lowercase(welcome_message)
    print(f"Lowercase message: {lowercase_message}")
    split_message = split_string_into_list(welcome_message)
    print(f"Split message: {split_message}")
    iterate_though_list(split_message)
    is_string_palindrome(welcome_message)

    

