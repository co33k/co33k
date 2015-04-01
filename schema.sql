DROP TABLE IF EXISTS users;
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

DROP TABLE IF EXISTS tweets;
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

DROP TABLE IF EXISTS issues;
CREATE TABLE issues (
  id                INTEGER PRIMARY KEY,
  subject           TEXT,
  description       TEXT,
  status            INTEGER DEFAULT 0
);

DROP TABLE IF EXISTS thru_words;
CREATE TABLE thru_words (
  id                 INTEGER PRIMARY KEY,
  word               TEXT,
  description        TEXT,
  is_valid           INTEGER DEFAULT 0
);

