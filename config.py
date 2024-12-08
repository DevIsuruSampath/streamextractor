#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = ""


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = 
    API_HASH = ""


    USERS = "7865959549 123456789"  

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in USERS.split())

