# ddd-bot
Joke Telegram bot I use in a friends group chat

## How to use
1. Clone the repository with `git clone`.
2. Enter in the `ddd-bot` folder and create two folders:
   * `resources`: inside this folder create a json file named `config.json`. It must contain the bot token, and other infos for the `/onlinesuts` command (a group id, some TeamSpeak nicknames, and a Teamspeak connection URI) e.g.:

      ```
      {
         "token": "XXXXXXXXX:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
         "group_id" : "-XXXXXXXXX",
         "ts_names_to_discard" : "nickname1 nickname2 nickname3",
         "ts_connection_uri" : "telnet://serveradmin:password@localhost:10011"
      }
      ```
      For more infos look at the `/onlinesuts` command in the **Commands** section.
   * `images`: here you have to put pictures used by the bot. E.g.: for the command `/dancanize`, put a picture named `base.jpg`.
3. in the `src` folder create a file named `dancan_msgs.txt`. It must contain lines of ''text messages'', since those are needed to generate fake text with the `/dancantext` command. More text messages mean better results!
4. Type `pipenv shell`
5. In the shell, install the dependencies with either `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
6. Run the bot by giving the command `python main.py` or `python3 main.py`.

## Commands
* `/start`: starts the bot.
* `/help`: gives info about the bot.
* `/dancanize`: reply to a text message with this command to get a picture with the replied text in it.
* `/dancantext`: generates and sends a fake text message. The command uses Markov chains to build a message that looks like it's written by the person who wrote the texts in the `dancan_msgs.txt` file.
* `/onlinesuts`: sends a message with the list of online users on the server. You must specify sensitive data in `config.json`: the command can only be used in the group specified in `"group_id"`, ignores users specified in `"ts_names_to_discard"`, and the server connection must be specified in `"ts_connection_uri"`. For more informations look at the `OnlineSuTs` class in `src` and visit [the ts3 package manual](https://py-ts3.readthedocs.io/en/v2/api/query.html?highlight=query#ts3.query.TS3ServerConnection)

## Other actions
* `AutoRespond`: when messages contain certain words, the bot will respond accordingly.
