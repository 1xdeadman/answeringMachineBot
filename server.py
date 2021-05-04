import telebot
import sbercloudAPI
import flask


TOKEN = open("token", 'r', encoding='utf-8').read()


bot = telebot.TeleBot(TOKEN, parse_mode=None)
app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "wake up, the samurai")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "write any text and get answer from THE GOSH!\n/start - launch bot\n/help - get info")


@bot.message_handler(func=lambda x: True)
def send_sber(message):
    # message.text
    res = sbercloudAPI.get_answer(message.text)
    if res is not None:
        bot.reply_to(message, res)
    else:
        bot.reply_to(message, "[Wrong!]")


def run_bot():
    bot.polling()


