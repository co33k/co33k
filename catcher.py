#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import twitter
from db.tweet import Tweet
from db.user import User

import co33k
import util


def say(message_uc, in_reply_to_status_id=None, dry_run=False):
    if len(message_uc) > 140:
        message_uc = message_uc[:139] + u'…'

    twitter.tweet(message_uc, in_reply_to_status_id=in_reply_to_status_id, dry_run=dry_run)
    print '!!', message_uc.encode('utf-8')


@click.command()
@click.option('--dry-run/--no-dry-run', default=False)
def main(dry_run=False):
    if dry_run:
        print '<< dry run >>'

    since_id = Tweet.max_id()
    #since_id -= 10000000000000 * 3
    if since_id:
        print since_id
        # 536342886862688258
        # if testmode: since_id -= 10000000000000 * testmag
        statuses = twitter.api.home_timeline(since_id)
    else:
        statuses = twitter.api.home_timeline()

    statuses.reverse()

    is_harahe = False

    for status in statuses:
        if co33k.is_to_ignore(status):
            # print ' <', status.user.screen_name, ':', status.text
            continue

        if dry_run:
            # print user
            # print tweet
            print
            print '%s (%s, %d) <%s> %s:' % (
                status.user.name, status.user.screen_name, status.user.id,
                status.id, status.created_at )
            print '  %s' % (status.text,)

        user = User( (status.user.id,
                      status.user.name,
                      status.user.screen_name,
                      status.user.location,
                      status.user.description,
                      status.user.profile_image_url,
                      status.user.protected,
                      False) ) # is_spam
        if not dry_run: user.save()

        tweet = Tweet( (status.id,
                        util.datetime_to_unixtime(status.created_at),
                        status.text,
                        status.in_reply_to_status_id,
                        status.in_reply_to_user_id,
                        status.user.id,
                        None,
                        None,
                        False) ) # is_mine
        if not dry_run: tweet.save()

        status_text = status.text
        status_text = status_text.replace('&amp;', '&')
        status_text = status_text.replace('&lt;', '<')
        status_text = status_text.replace('&qt;', '>')
        status_text = status_text.replace('&quot;', '"')

        if u'はらへ' in status_text and u'_rin' in status.user.screen_name:
            is_harahe = True

        responses = co33k.responses_for_status(user, status.text, dry_run=dry_run)

        repondu = False
        if responses:
            responses.sort(reverse=True)
            for message, rate in responses:
                rate *= 3
                print '  → %g%%) %s' % (rate, message.encode('utf-8')) #status.id

                if not repondu and util.p(rate):
                    say(message, in_reply_to_status_id=status.id, dry_run=dry_run)
                    repondu = True

    if is_harahe:
        say(u'はらへ', dry_run=dry_run)
        #print '　→ %g%%) %s' % (rate, message.encode('utf-8'))


if __name__ == '__main__':
    main()
