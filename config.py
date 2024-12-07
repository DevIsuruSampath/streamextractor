#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = "6390472117:AAEzwXUxskUwVE91F8NVBRDiPn2ePyV-eOs"


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = 27185969
    API_HASH = "e367a91377a91e665cc182a5ad2af99e"


    USERS = "956022686 5443081541 1226841901 1671626669 866649963 5160169373 1958851206 778988294 947859478 1157557110 1772988300 2135072465 1363236962 1178035103 1363236962 1840565374 1619444244 1837756549 1457595674 1457595674 1958464691 1958464691 1356300848 1984136592 5450200086 1178035103"  

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in USERS.split())

