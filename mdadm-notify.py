#!/usr/bin/python3

# General Libraries
import sys
import socket
import logging
import telebot
import os
from config import setupEnv

# Gets the directory path where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Reading configuration variables
cfg_name = script_dir + "/config/user.cfg"
confBot = setupEnv.botConfig(cfg_name)

# Configure logging
logging.basicConfig(format='[ %(asctime)s ]  %(message)s', filename='logBot.log', encoding='utf-8', level=confBot.loggingLevel)

MDSTAT = confBot.mdstat
TELEBOT_KEY = confBot.telebotKey
TELEGRAM_USER_ID = confBot.telegramUserId

def run():
    status = open(MDSTAT).read()

    # Information provided by mdadm
    event = sys.argv[1]
    device = sys.argv[2]

    # Compose message
    message = "Device: %s\nEvent: %s\n\n%s:\n%s" % (device, event, MDSTAT, status)

    # Send message
    send_telegram_message(message)

def send_telegram_message(message):
    bot = telebot.TeleBot(token=TELEBOT_KEY)
    bot.send_message(chat_id=TELEGRAM_USER_ID, text=message)

if __name__ == "__main__":
    run()