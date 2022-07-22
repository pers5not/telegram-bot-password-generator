import telebot
import config
import dbworker
import gen_password
import time

bot = telebot.TeleBot(config.BOT_TOKEN)

# Начало диалога


@bot.message_handler(commands=["start"])
def cmd_start(message):
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_ENTER_NAME.value:
        bot.send_message(
            message.chat.id, "Кажется, кто-то обещал отправить своё имя, но так и не сделал этого :( Жду...")
    elif state == config.States.S_ENTER_LEN_PASS.value:
        bot.send_message(
            message.chat.id, "Кажется, кто-то обещал длину пароля, но так и не сделал этого :( Жду...")
    elif state == config.States.S_SYMBHOLS.value:
        bot.send_message(
            message.chat.id, "Кажется, кто-то обещал из чего генерировать этот пароль, но так и не сделал этого :( Жду...")
    else:  # Под "остальным" понимаем состояние "0" - начало диалога
        bot.send_message(
            message.chat.id, "Привет! Как я могу к тебе обращаться?")
        dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Привет! Как я могу к тебе обращаться?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(
        message.chat.id, "Что ж, начнём по-новой. Как тебя зовут?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
    # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    global name
    name = message.text
    bot.send_message(
        message.chat.id, "Отличное имя, запомню! теперь скажи хочешь ли ты сгенерировать пароль? (Да/Нет) ")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_ANSWER.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_ANSWER.value)
def user_entering_answer(message):
    if message.text.lower() == "да":
        bot.send_message(
            message.chat.id, "Отлично, осталось уточнить какой длины пароль ты хочешь?")
        dbworker.set_state(
            message.chat.id, config.States.S_ENTER_LEN_PASS.value)
    elif message.text.lower() == "нет":
        bot.send_message(
            message.chat.id, "Привет! Как я могу к тебе обращаться?")
        dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)
    else:
        bot.send_message(message.chat.id, "Что-то не так, попробуй ещё раз!")
        return


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_LEN_PASS.value)
def user_entering_len_pass(message):
    if message.text.isdigit() and int(message.text) > 0 and int(message.text) < 999:
        global len_pass
        len_pass = int(message.text)
        bot.send_message(
            message.chat.id, """Отлично, из чего будет состоять твой пароль?
1 - буквы | "abcdefghijklmnopqrstuvwxyz"
2 - БОЛЬШИЕ БУКВЫ | "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
3 - цифры | "0123456789"
4 - специальные симолы | "!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "
5 - все символы введи через
выбор вводить через пример -->  143""")
        dbworker.set_state(message.chat.id, config.States.S_SYMBHOLS.value)
    elif message.text.isdigit() and (int(message.text) < 1 or int(message.text) > 999):
        bot.send_message(
            message.chat.id, "Ты много хочешь мой дорогой друг, диапазон от 1 до 999 до попробуй еще.....")
        return
    else:
        bot.send_message(
            message.chat.id, f"Ты ввел {message.text} я не понимаю что тебе надо уточни...")
        return


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SYMBHOLS.value)
def user_entering_sybbols(message):
    if message.text.isdigit():
        choice_pass = list(message.text)
        add_symb = gen_password.add_symbol(
            gen_password.clean_user_choice(choice_pass))
        passw = gen_password.generator_pas(add_symb, len_pass)
        bot.send_message(
            message.chat.id, f"{name}, твой пароль генерируется жди.....")
        time.sleep(3)
        bot.send_message(
            message.chat.id, f"""{name}, держи свой пароль
{passw}
из {len_pass} сиволов
            
Отлично! Больше от тебя ничего не требуется. 
Если захочешь пообщаться снова - отправь команду /start.""")
        time.sleep(3)
        dbworker.set_state(message.chat.id, config.States.S_START.value)
    else:
        bot.send_message(
            message.chat.id, f"Ты ввел {message.text} я не понимаю что тебе надо уточни...")
        return


if __name__ == "__main__":
    bot.infinity_polling()
