#!/usr/bin/python
# -*- coding: utf-8 -*-
from database import Database

class Tweet(Database):
    columns = ('id', 'created_at', 'text', 'in_reply_to_status_id', 'in_reply_to_user_id', 'user_id', 'issue_id', 'status', 'is_mine')

    @staticmethod
    def get_create_table_sql():
        return """
CREATE TABLE tweets (
  id                     INTEGER PRIMARY KEY, /* twitterのtweet idをそのまま */
  created_at             INTEGER DEFAULT NULL, /* unix time */
  text                   TEXT NOT NULL,
  in_reply_to_status_id  INTEGER DEFAULT NULL,
  in_reply_to_user_id    INTEGER DEFAULT NULL,
  user_id                INTEGER DEFAULT NULL,
  issue_id               INTEGER DEFAULT NULL,
  status                 INTEGER DEFAULT 0, /* 要返答とか */
  is_mine                INTEGER DEFAULT 0  /* bool */
);
        """

    def set_issue_id(self, issue_id):
        self.issue_id = issue_id
        self.save()


if __name__ == '__main__':
    print Tweet.max_id(), Tweet.count()

    tw = Tweet()
    tw.id = Tweet.max_id() + 1
    tw.text = 'TEST'
    tw.save()
    print "tw:", tw
    print Tweet.max_id()

    for tweet in Tweet.find('id=26527699897'):
        print tweet
