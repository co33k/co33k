#!/usr/bin/python
# -*- coding: utf-8 -*-
from database import Database

class Issue(Database):
    columns = ('id', 'subject', 'description', 'status')

    @staticmethod
    def get_create_table_sql():
        return """
CREATE TABLE issues (
  id           INTEGER PRIMARY KEY,
  subject      TEXT,
  description  TEXT,
  status       INTEGER DEFAULT 0
);
        """
