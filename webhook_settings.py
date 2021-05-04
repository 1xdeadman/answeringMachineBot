import telebot
import click


TOKEN = open("token", 'r', encoding='utf-8')

bot = telebot.TeleBot(TOKEN, parse_mode=None)


def set_webhook(server_url: str, server_cert: str):
    bot.set_webhook(url=server_url, certificate=open(server_cert))


def remove_webhook(server_url: str, server_cert: str):
    bot.set_webhook(url=server_url, certificate=open(server_cert))


@click.command()
@click.option('--is_set_web_hook', '-s', required=True, type=bool)
@click.option('--server_url', '-u', required=True, type=str)
@click.option('--server_cert', '-c', required=True, type=str)
def run(is_set_web_hook, server_url, server_cert):
    if is_set_web_hook:
        set_webhook(server_url, server_cert)
    else:
        remove_webhook(server_url, server_cert)


if __name__ == '__main__':
    run()
