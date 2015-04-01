#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import config
import time

DEBUG = False

def certificate():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.oauth_token, config.oauth_token_secret)
    return tweepy.API(auth_handler=auth, api_root='/1.1', secure=True)

api = certificate()


def tweet(msg, in_reply_to_status_id=None, destroy_wait=None, dry_run=False):

    if isinstance(msg, str):
        msg = msg.decode('utf-8')

    if DEBUG:
        destroy_wait = 15
        msg = '[TEST]' + msg.replace('@', '$')

    if dry_run:
        msg = '[dry-run]' + msg

    print '(tweet)', msg.encode('utf-8')

    if dry_run: return

    try:
        if in_reply_to_status_id:
            status = api.update_status(msg, in_reply_to_status_id)
        else:
            status = api.update_status(msg)
        if destroy_wait and isinstance(destroy_wait, int):
            print '(tweeted but this will be destroyed after %d sec)' % destroy_wait
            time.sleep(destroy_wait)
            api.destroy_status(status.id)
            print '(status has been destroyed)'
    except tweepy.error.TweepError, e:
        print 'An error occurred:', e.args[0]
