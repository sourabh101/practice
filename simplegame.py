import random


def get_guess():
    return int(input("What is you guess?"))


def generate_code():
    digit_list = [i for i in range(10)]
    random.shuffle(digit_list)
    number = 100 * digit_list[0] + 10 * digit_list[1] + digit_list[2]
    return number


def generate_clues(code, guess):
    if guess == code:
        return "correct"
    elif guess < code:
        return "less"
    else:
        return "more"


def main():
    code = generate_code()
    guess = 0
    while guess != code:
        guess = get_guess()
        print(generate_clues(code, guess))


if __name__ == '__main__':
    main()
