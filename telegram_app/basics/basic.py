from dotenv import load_dotenv
import os
import menus
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters


class Communication:
    def __init__(self):
        load_dotenv()
        self.file_path = os.environ.get('ATTRIBUTES_FILE_PATH')
        self.cles = {
            '?': [self.aide, 'display commands that are available'],
            '/start': [menus.start, 'select the data you need from the database'],
        }
        self.token = os.environ.get('TOKEN')

    def aide(self):
        self.texteAide = ''
        for k, v in zip(self.cles.keys(),self.cles.values()):
            self.texteAide += k + ' : ' + v[1] + '\n'
        return self.texteAide

    def get_model_details(self):
        with open(self.file_path, 'r') as file:
            data = file.readline()
        data = data.split('|')
        print('data = ', data)
        results = [item.split(',') for item in data]
        print(results)
        final = []
        for item in results:
            final.append({'module': item[0][item[0].find(':')+ 2:], 'model': item[1][item[1].find(':')+ 2:], 'attributes': item[2][item[2].find(':')+ 2:]})
        return final

    async def action_for_text_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        chat_id = update.effective_chat.id
        for k, v in zip(self.cles.keys(), self.cles.values()):
            if update.message.text.lower() == k:
                message = v[0]()
                await update.message.reply_text(message)

    def lancer(self):
        data = self.get_model_details()
        application = Application.builder().token(self.token).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.action_for_text_message))
        ####### Menus for API ############
        application.add_handler(CommandHandler('start', menus.start))
        application.add_handler(CallbackQueryHandler(menus.main_menu, pattern='main'))
        application.add_handler(CallbackQueryHandler(menus.administrative, pattern='administrative'))
        application.add_handler(CallbackQueryHandler(menus.document, pattern='document'))
        application.add_handler(CallbackQueryHandler(menus.id_card, pattern='id_card'))
        application.add_handler(CallbackQueryHandler(menus.os_id_card, pattern='os_id_card'))
        ##################################
        application.run_polling()

Communication().lancer()