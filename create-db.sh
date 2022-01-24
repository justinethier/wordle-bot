#!/bin/bash

function csv_to_sqlite() {
  local database_file_name="$1"
  local table_name="$2"
  sqlite3 -csv $database_file_name ".import '|cat -' $table_name"
}

#database_file_name=$1
#table_name=$2

database_file_name=test.db
table_name=words

rm -f $database_file_name
sqlite3 $database_file_name "create table words (\"word\" text);"
sqlite3 $database_file_name "create table word_counts (\"word\" text, \"first\" text, \"second\" text, \"third \" text, \"fourth\" text, \"fifth\" text);"
cat wordle*.txt | csv_to_sqlite "$database_file_name" "$table_name"
sqlite3 $database_file_name "insert into word_counts select word, substr(word, 1, 1), substr(word, 2, 1), substr(word, 3, 1), substr(word, 4, 1), substr(word, 5, 1) from words;"


