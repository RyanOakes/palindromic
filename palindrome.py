import re

def is_palindrome(user_input):


    pattern = '[^A-Za-z]'
    cleansed_user_input = re.sub(pattern, '', user_input)
    cleansed_user_input = cleansed_user_input.lower()

    if len(cleansed_user_input) < 2:
        return True

    if cleansed_user_input[0] != cleansed_user_input[-1]:
        return False

    return is_palindrome(cleansed_user_input[1:-1])


def main():


    user_input = input("Please provide a word or sentence: ")

    #runs the palindrome test
    palindrome_verdict = is_palindrome(user_input)


    if palindrome_verdict:
        print('What a lovely palindrome you have there!')
    else:
        print('Definitely not a palindrome!')


if __name__ == '__main__':
    main()
