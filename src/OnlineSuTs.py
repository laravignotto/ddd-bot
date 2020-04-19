from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler
import telegram
import requests
import ts3
import re
from emoji import emojize
import json

class OnlineSuTs:
    '''
    Handles /onlinesuts command
    '''
    dp = None
    
    def __init__(self, parent, dispatcher):
        assert(parent.isBot())
        assert(dispatcher!=None)
        self.config = json.load(open("resources/config.json"))
        self.group_id = self.config["group_id"]
        # get a list of TeamSpeak nicknames to ignore
        # !! the names are space-separated in the json file !!
        self.ts_names_to_discard = self.config["ts_names_to_discard"].split()
        self.ts_connection_uri = self.config["ts_connection_uri"]
        self.dp = dispatcher

    def getTsOnlineUsers(self):
        '''
        Returns a list of online users in a TeamSpeak server
        (empty list if noone is online)
        '''
        online_users = []

        with ts3.query.TS3ServerConnection(self.ts_connection_uri) as ts3conn:
            ts3conn.exec_("use", sid=1)

            resp = ts3conn.exec_("clientlist")

            for client in resp.parsed:
                nick = client['client_nickname']
                if nick not in self.ts_names_to_discard:
                    online_users.append(nick)
        
        return online_users
    
    def onlineSuTs(self, update, context):
        '''
        Sends a message with the online users in the TeamSpeak server. 
        This information is available only if the command is launched 
        in a specific Telegram group 
        '''
        chat_id = update.message.chat_id

        # get a list of users connected to the TeamSpeak server
        list_of_users = self.getTsOnlineUsers()

        # the TeamSpeak server is empty
        if len(list_of_users) == 0:
            list_of_users = ['Nessuno :sob:']

        # Send the list of connected users only if the command 
        # is launched from a specific group
        if (chat_id == self.group_id):
            text = ":sound: *Online adesso su TS* :sound:\n" + "\n".join(list_of_users)
            context.bot.send_message(chat_id=chat_id, 
                        text=emojize(text, use_aliases=True),
                        parse_mode=telegram.ParseMode.MARKDOWN,
                        )
        else:
            text = "Non ti è permesso avere questa informazione :rage:"
            context.bot.send_message(chat_id=chat_id, 
                        text=emojize(text, use_aliases=True),
                        parse_mode=telegram.ParseMode.MARKDOWN,
                        )

    def registerToDispatcher(self):
        self.dp.add_handler(CommandHandler('onlinesuts', self.onlineSuTs))
