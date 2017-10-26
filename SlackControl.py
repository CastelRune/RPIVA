#!/usr/bin/env python3
import os, slackclient, time
import random
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

# delay in seconds before checking for new events 
SOCKET_DELAY = 1
# slackbot environment variables
MA_SLACK_NAME = "MagicAssistant"
MA_SLACK_TOKEN = os.environ.get('MA_SLACK_TOKEN')
MA_SLACK_ID = os.environ.get('MA_SLACK_ID')
MA_slack_client = slackclient.SlackClient(MA_SLACK_TOKEN)
assistant_name="Magic"
def is_for_me(event):
    # TODO Implement later
    return True
def handle_message(message, user, channel):
    # TODO Implement later
    post_message(message='Hello', channel=channel)
def post_message(message, channel):
    MA_slack_client.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)
def run():
    if MA_slack_client.rtm_connect():
        print('[.] MA is ON...')
        aiy.audio.get_recorder().start()
        while True:
            recog = aiy.cloudspeech.get_recognizer()
            recog.expect_phrase(assistant_name)
            text=recog.recognize()
            if text != None:
                print("Understood :",text)
                if "slack" in text:
                    slack = True
                    print("Slack >> True")
            event_list = MA_slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    if event.get('text') != None:
                        print("\n[MESSAGE]",event.get('text'),"\n")
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

def is_private(event):
    """Checks if private slack channel"""
    return event.get('channel').startswith('D')

def get_mention(user):
    return '<@{user}>'.format(user=user)

valet_slack_mention = get_mention(MA_SLACK_ID)
        
def is_for_me(event):
    """Know if the message is dedicated to me"""
    # check if not my own event
    type = event.get('type')
    if type and type == 'message' and not(event.get('user')==MA_SLACK_ID):
        # in case it is a private message return true
        if is_private(event):
            return True
        # in case it is not a private message check mention
        text = event.get('text')
        channel = event.get('channel')
        if MA_slack_mention in text.strip().split():
            return True

def is_hi(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens
               for g in ['hello', 'bonjour', 'hey', 'hi', 'sup', 'morning', 'hola', 'ohai', 'yo'])


def is_bye(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens
               for g in ['bye', 'goodbye', 'revoir', 'adios', 'later', 'cya'])

def is_say(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens
               for g in ['$say'])
def say_hi(user_mention):
    """Say Hi to a user by formatting their mention"""
    response_template = random.choice(['Sup, {mention}...',
                                       'Yo!',
                                       'Hola {mention}',
                                       'Bonjour!'])
    return response_template.format(mention=user_mention)


def say_bye(user_mention):
    """Say Goodbye to a user"""
    response_template = random.choice(['see you later, alligator...',
                                       'adios amigo',
                                       'Bye {mention}!',
                                       'Au revoir!'])
    return response_template.format(mention=user_mention)

def handle_message(message, user, channel):
    if is_hi(message):
        user_mention = get_mention(user)
        post_message(message=say_hi(user_mention), channel=channel)
    elif is_bye(message):
        user_mention = get_mention(user)
        post_message(message=say_bye(user_mention), channel=channel)
    elif is_say(message):
        aiy.audio.say(message[4:])
    elif slack:
        post_message(message=text[len("slack"):], channel=channel)

if __name__=='__main__':
    run()

