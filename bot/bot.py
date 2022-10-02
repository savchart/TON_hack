import telebot
from token_key import get_token

TOKEN = get_token()
bot = telebot.TeleBot(TOKEN)


def main_menu_markup(markup):
    item_0 = telebot.types.KeyboardButton('Subscribe')
    item_1 = telebot.types.KeyboardButton('NFT Manager')
    item_2 = telebot.types.KeyboardButton('DAO Info')
    item_3 = telebot.types.KeyboardButton('Active proposals')
    item_4 = telebot.types.KeyboardButton('Create DAO(only for admins)')
    markup.add(item_0, item_1, item_2, item_3, item_4)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = main_menu_markup(markup)

    bot.send_message(message.chat.id, 'Hi, {0.first_name}, welcome to newDAO'.format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Subscribe':
            # TODO call mint function from contract
            bot.send_message(message.chat.id, 'Success, you are in DAO!')
        elif message.text == 'NFT Manager':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            # TODO: call stake/unstake function from contract
            item_0 = telebot.types.KeyboardButton('Stake')
            item_2 = telebot.types.KeyboardButton('Unstake')
            item_1 = telebot.types.KeyboardButton('Your NFTs')
            item_3 = telebot.types.KeyboardButton('Back')
            markup.add(item_0, item_1, item_2, item_3)
            bot.send_message(message.chat.id, 'NFTs info', reply_markup=markup)
        elif message.text == 'DAO Info':
            bot.send_message(message.chat.id, 'Treasure  248255 TONs')
            bot.send_message(message.chat.id, 'Your voting power - 2566')
        elif message.text == 'Active proposals':
            bot.send_message(message.chat.id, 'Proposal 229')
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_0 = telebot.types.KeyboardButton('YES 83%')
            item_1 = telebot.types.KeyboardButton('NO 17%')
            item_2 = telebot.types.KeyboardButton('Back')
            markup.add(item_0, item_1, item_2)
            bot.send_message(message.chat.id, 'Use your voices', reply_markup=markup)
        elif message.text == 'Back':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = main_menu_markup(markup)
            bot.send_message(message.chat.id, 'Main menu', reply_markup=markup)


bot.polling(none_stop=True)
