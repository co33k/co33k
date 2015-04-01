#!/usr/bin/python
# -*- coding: utf-8 -*-
from database import Database

class User(Database):
    columns = ('id', 'name', 'screenname', 'location', 'description', 'profile_image_url', 'protected', 'is_spam')

    @staticmethod
    def get_create_table_sql():
        return """
CREATE TABLE users (
  id                 INTEGER PRIMARY KEY, /* twitter の user idをそのまま */
  name               TEXT,
  screenname         TEXT,
  location           TEXT,
  description        TEXT,
  profile_image_url  BLOB,
  protected          INTEGER DEFAULT 0,
  is_spam            INTEGER DEFAULT 0
);
        """


if __name__ == '__main__':
    user = User()
    print User.max_id()

    for user in User.find():
        print user
