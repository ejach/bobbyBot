# bobbyBot 🤖

[![Twitter Badge](https://img.shields.io/badge/-@bobbyBot17-00acee?style=flat-square&logo=Twitter&logoColor=white)](https://twitter.com/intent/follow?screen_name=bobbyBot17 "Follow on Twitter")
[![Docker](https://img.shields.io/docker/v/ejach/bobbybot?logo=docker&label=version&style=flat-square)](https://hub.docker.com/r/ejach/bobbybot)
[![Docker](https://img.shields.io/docker/cloud/build/ejach/bobbybot?logo=docker&style=flat-square)](https://hub.docker.com/r/ejach/bobbybot/builds)
[![PyPI](https://img.shields.io/pypi/v/tweepy?logo=python&label=tweepy&style=flat-square&color=FFD43B)](https://pypi.org/project/tweepy/)


A simple Twitter bot that tweets every 24 hours the amount of time Bobby Shmurda has been released from prison and has **not** released a song.

## How to install

### With Docker

`sudo docker run -it -e consumer_key=<YOUR_KEY> -e consumer_secret=<YOUR_KEY> -e access_token=<YOUR_KEY> -e access_token_secret=<YOUR_KEY> ghcr.io/ejach/bobbybot:latest`

### Manually

- Clone the repository
- Install the requirements using `pip3 install -r requirements.txt`
- Edit the `.env` file with your twitter tokens and API keys ([reference](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api))
- Start the program by running `python3 main.py`
- Go crazy

## ⚠ NOTICE ⚠
This is intended as a joke, please do not take it seriously.
