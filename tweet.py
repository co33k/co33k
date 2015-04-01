#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
from twitter import tweet
from randmsg import msggen


@click.command()
@click.argument('message', required=False)
@click.argument('pattern_id', type=int, required=False)
@click.option('--in-reply-to-status-id', type=int, required=False, default=None)
@click.option('--destroy-wait', type=int, required=False, default=None)
def main(message=None, pattern_id=None, in_reply_to_status_id=None, destroy_wait=None):
    if not message:
        message = msggen(pattern_id)

    if message:
        tweet(message, in_reply_to_status_id=in_reply_to_status_id, destroy_wait=destroy_wait)
    else:
        print '(no message)'


if __name__ == '__main__':
    main()
