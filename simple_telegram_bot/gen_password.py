import random

def clean_user_choice(user_list):
    user_choice = []
    for choice in user_list:
        if choice.isdigit():
            choice = int(choice)
            if choice not in user_choice and choice > 0 and choice <= 5:
                user_choice.append(int(choice))
            else:
                continue
    return user_choice


def add_symbol(list_sumbol):
    user_symbol_list = ''
    if 1 in list_sumbol:
        user_symbol_list += "abcdefghijklmnopqrstuvwxyz"
    if 2 in list_sumbol:
        user_symbol_list += "abcdefghijklmnopqrstuvwxyz".upper()
    if 3 in list_sumbol:
        user_symbol_list += "0123456789"
    if 4 in list_sumbol:
        user_symbol_list += "!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "
    if 5 in list_sumbol:
        user_symbol_list = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "
    return user_symbol_list


def generator_pas(add_symbol, pass_len):
    pas = ''
    for i in range(int(pass_len)):
        pas += random.choice(add_symbol)
    return pas
    