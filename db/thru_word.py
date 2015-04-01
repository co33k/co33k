#!/usr/bin/python
# -*- coding: utf-8 -*-
from database import Database, _execute

class ThruWord(Database):
    columns = ('id', 'word', 'description', 'is_valid')

    @staticmethod
    def get_create_table_sql():
        return """
CREATE TABLE thru_words (
  id           INTEGER PRIMARY KEY,
  word         TEXT UNIQUE,
  description  TEXT,
  is_valid     INTEGER DEFAULT 0
);
        """

    @staticmethod
    def register(word):
        thru_word = ThruWord({ 'word': word, 'is_valid': 1 })
        thru_word.save()

    @staticmethod
    def invalidate(word):
        thru_word = ThruWord({ 'word': word, 'is_valid': 0 })
        thru_word.save()

    @staticmethod
    def words():
        return [thru_word.word for thru_word in ThruWord.find('is_valid=1')]


if __name__ == '__main__':
    print ThruWord.max_id()
    ThruWord.register('momomo')
    ThruWord.invalidate('momomo')
    print ThruWord.words()
