# mdadm-notify

A simple notification script for `mdadm` that allows notifications to Telegram

## Configuration

Edit the user.cfg script to set the following variables

- `LOGGING_LEVEL`: Log level
- `TELEBOT_KEY`: Your Telegram Bot's access token
- `TELEGRAM_USER_ID`: Your chat id where you will receive messages

Optional:

- `MDSTAT`: The location of `mdadm`'s status file. Should usually be `/proc/mdstat`

## Installation

To install, run

    sudo ./setup.sh

as root to install mdadm-notify to /usr/bin

Edit your `mdadm` configuration file (e.g. `/etc/mdadm/mdadm.conf`) and change the `PROGRAM` variable to match witch the script

    PROGRAM /home/user/mdadm-notify

## Test

Verify that installation and configuration have worked by running the following as root

    mdadm --monitor --test --oneshot /dev/mdX --program /home/user/mdadm-notify

where X is replaced by an `mdadm` device
