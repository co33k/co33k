#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import re
#from collections import namedtuple

_conn = sqlite3.connect('/home/naoyat/twitter/co33k_python/tweets.db')


def uncamelize(camelname):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelname)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def plural_form(name):
    return name + 's'


def _execute(sql, bind_values=None, do_fetch=True, do_commit=False):
    cur = _conn.cursor()
    try:
        if bind_values:
            cur.execute(sql, bind_values)
        else:
            cur.execute(sql)
    except sqlite3.Error, e:
        print 'An error occurred:', e.args[0]

    if do_commit:
        _conn.commit()

    if do_fetch:
        result = cur.fetchall()
        cur.close()
        return result
    else:
        cur.close()
        return []


class Database():
    has_record = False

    def __init__(self, args=None):
        if isinstance(args, tuple) or isinstance(args, list):
            for column, value in zip(self.columns, args):
                setattr(self, column, value)
        elif isinstance(args, dict):
            for column in self.columns:
                setattr(self, column, args.get(column, None))
        else:
            for column, value in zip(self.columns, args):
                setattr(self, column, None)

    def __repr__(self):
        return repr(self.values())

    def exists(self):
        if not self.id:
            return False
        else:
            result = self.execute('SELECT count(*) FROM :this WHERE id=:id')
            return len(result) == 1

    def values(self):
        return dict([(column, getattr(self, column)) for column in self.columns])

    def execute(self, sql, do_commit=False):
        sql = sql.replace(':this', self.get_table_name())
        # print 'execute> SQL:', sql
        # print 'execute> values:', self.values()
        return _execute(sql, self.values(), do_commit=do_commit)

    def save(self):
        self.execute(self.get_upsert_sql(), do_commit=True)
        self.has_record = True

    @classmethod
    def find(cls, where=None, limit=10):
        sql = ' '.join([
            'SELECT *',
            'FROM %s' % cls.get_table_name(),
            ('WHERE %s' % where) if where else '',
            'LIMIT %d' % limit
        ])
        return [cls(record) for record in _execute(sql)]

    @classmethod
    def truncate(cls):
        self.execute('DELETE FROM :this')

    @classmethod
    def max_id(cls):
        table_name = cls.get_table_name()
        result = _execute('SELECT max(id) FROM %s' % table_name)
        if len(result) == 0:
            return None

        assert len(result) == 1
        max_id, = result[0]
        assert isinstance(max_id, int)
        return max_id

    @classmethod
    def count(cls, where=None):
        sql = 'SELECT count(*) FROM ' + cls.get_table_name()
        if where: sql += ' WHERE ' + where

        result = _execute(sql)
        if len(result) == 0:
            return None

        assert len(result) == 1
        max_id, = result[0]
        assert isinstance(max_id, int)
        return max_id

    def get_upsert_sql(self):
        return 'INSERT OR REPLACE INTO :this VALUES (:%s)' % ',:'.join(self.columns)
        # raise NotImplementedError()

    @classmethod
    def get_table_name(cls):
        return plural_form(uncamelize(cls.__name__))

