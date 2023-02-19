from dotenv import load_dotenv
import os
import menus
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters


class Communication:
    def __init__(self):
        load_dotenv()
        self.cles = {
            '?': [self.aide, 'displqy commands that are available'],
            '/start': [menus.start, 'select the data you need from the database'],
        }
        self.token = os.environ.get('TOKEN')

    def aide(self):
        self.texteAide = ''
        for k, v in zip(self.cles.keys(),self.cles.values()):
            self.texteAide += k + ' : ' + v[1] + '\n'
        return self.texteAide
        # self.chat.envoi_message(self.texteAide)

    async def action_for_text_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        chat_id = update.effective_chat.id
        for k, v in zip(self.cles.keys(), self.cles.values()):
            if update.message.text.lower() == k:
                message = v[0]()
                await update.message.reply_text(message)

    def lancer(self):
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