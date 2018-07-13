import os


if __name__ == '__main__':
    os.chdir('/home/sourabh/Downloads')
    print(os.getcwd())
    file = open('HungerGames.txt', 'r')
    word_list = file.read().lower().split()
    word_list_copy = []

    for word in word_list:
        word_list_copy.append(word.replace("^a-z", "").strip())
    word_list.clear()

    counter_dict = {}

    for word in word_list_copy:
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1

    for word in counter_dict:
        print("word = {}, freq = {}".format(word, counter_dict[word]))

