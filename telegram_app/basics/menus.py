from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from database.api.utils import get_query_related_to_telegram_choice

############################ MENUS #########################################

########### Starting menu ###########


async def start(bot, update):
    await bot.message.reply_text(generic_message('main'),
                                 reply_markup=main_menu_keyboard())


async def main_menu(bot, update):
    await bot.callback_query.message.edit_text(generic_message('main'),
                                               reply_markup=main_menu_keyboard())


########### Administrative menus ###########


async def administrative(bot, update):
    path = 'main > administrative'
    await bot.callback_query.message.edit_text(generic_message(path),
                                               reply_markup=administrative_keyboard())


async def document(bot, update):
    path = 'main > administrative > document'
    await bot.callback_query.message.edit_text(generic_message(path),
                                               reply_markup=document_keyboard())


async def id_card(bot, update):
    path = 'main > administrative > document > ID card'
    await bot.callback_query.message.edit_text(generic_message(path),
                                               reply_markup=id_card_keyboard())


async def os_id_card(bot, update):
    get_query_related_to_telegram_choice(
        bot['callback_query']['message']['reply_markup']['inline_keyboard'][0][0]['callback_data']
    )


############################ Keyboards #########################################


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Administative > document / insurances', callback_data='administrative')],
                [InlineKeyboardButton('Finance > Bank accounts', callback_data='finance')],
                [InlineKeyboardButton('Assets > Mortgage / Tenants / insurances / Copro...', callback_data='assets')],
                [InlineKeyboardButton('Taxes', callback_data='taxes')]]
    return InlineKeyboardMarkup(keyboard)


def administrative_keyboard():
    keyboard = [[InlineKeyboardButton('Documents', callback_data='document')],
                [InlineKeyboardButton('Insurance_companies', callback_data='insurance_companies')],
                [InlineKeyboardButton('Insurance_contracts', callback_data='insurance_contracts')],
                [InlineKeyboardButton('<<< back to previous menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def document_keyboard():
    keyboard = [[InlineKeyboardButton('ID card', callback_data='id_card')],
                [InlineKeyboardButton('Passport', callback_data='passport')],
                [InlineKeyboardButton('Driving Licence', callback_data='driving_licence')],
                [InlineKeyboardButton('Tickets', callback_data='tickets')],
                [InlineKeyboardButton('Other', callback_data='other')],
                [InlineKeyboardButton('<<< back to previous menu', callback_data='administrative')]
                ]
    return InlineKeyboardMarkup(keyboard)


def id_card_keyboard():
    keyboard = [[InlineKeyboardButton('Olivier', callback_data='os_id_card')],
                # [InlineKeyboardButton('Paula', callback_data='id_card_os')],
                # [InlineKeyboardButton('Gabrielle', callback_data='id_card_os')],
                [InlineKeyboardButton('<<< back to previous menu', callback_data='document')]
                ]
    return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################
def generic_message(path):
    return '{}\nWhat data do you need?'.format(path)
