#!/usr/bin/python3

# TODO: using sqlite3 DB -
# select * from word_counts where first = 'a' and word like '%e%' and word like '%b';
#
# for correct letters (0) - use first, second, etc
# for wrong position (1) - use 'like' clause
#
# TODO: how to pick a word from the list. brute force with first one, for now???

import check
import sqlite3

def solve(guess, answer):
  guesses = []
  known = [False] * 5
  badpos = []
  wrong = []
  return iter(guess, answer, guesses, known, badpos, wrong)

def iter(guess, answer, guesses, known, badpos, wrong):
  guesses.append(guess)
  status = check.check(guess, answer)

  #print("Guess", guess, "Status", status)
  if status == [0,0,0,0,0]:
    return True, guesses

  # for now, give up after so many iterations
  if len(guesses) > 6:
    return False, guesses
  
  # Collect correct letters
  for i in range(5):
    if not known[i] and status[i] == 0:
      known[i] = guess[i]

  # Collect letters in wrong position
  known_chars = []
  for i in range(5):
    if status[i] == 1:
      known_chars.append(guess[i])

  # Collect wrong letters from this iteration
# TODO: how to reconcile this and handling of duplicate letters?
  w = [False] * 5
  for i in range(5):
    if status[i] == 2:
      w[i] = guess[i]
  wrong.append(w)

  sql = build_known(known)
  sql = sql_add(sql, build_known_chars(known_chars))
  sql = sql_add(sql, build_wrong_chars(wrong))
  #print("known", known, "known chars", known_chars, "sql", sql)

  # Find candidates
  con = sqlite3.connect("words.db")
  cur = con.cursor()
  sql = "select * from word_counts where " + sql
  for row in cur.execute(sql):
    if row[0] != guess:
      guess = row[0]
      break

  return iter(guess, answer, guesses, known, known_chars, wrong)

def build_known(known):
  sql = ""
  if known[0]: sql = sql_add(sql, " first = '"  + known[0] + "'")
  if known[1]: sql = sql_add(sql, " second = '" + known[1] + "'")
  if known[2]: sql = sql_add(sql, " third = '"  + known[2] + "'")
  if known[3]: sql = sql_add(sql, " fourth = '" + known[3] + "'")
  if known[4]: sql = sql_add(sql, " fifth = '"  + known[4] + "'")
  return sql

def build_known_chars(lis):
  sql = ""
  for c in lis:
    sql = sql_add(sql, " word like '%" + c + "%'")
  return sql

# Build contrains for wrong characters in each iteration of our solver
# Given parameter is an array of arrays.
# Each leaf array contains a list either wrong characters by position or false
def build_wrong_chars(wrong_chars_by_iter):
  sql = ""
  for wchars in wrong_chars_by_iter:
    if wchars[0]: sql = sql_add(sql, " first <> '"  + wchars[0] + "'")
    if wchars[1]: sql = sql_add(sql, " second <> '" + wchars[1] + "'")
    if wchars[2]: sql = sql_add(sql, " third <> '"  + wchars[2] + "'")
    if wchars[3]: sql = sql_add(sql, " fourth <> '" + wchars[3] + "'")
    if wchars[4]: sql = sql_add(sql, " fifth <> '"  + wchars[4] + "'")
  return sql

def sql_add(sql, clause):
  if len(sql) > 0 and len(clause) > 0:
    sql = sql + " and "
  return sql + clause

#guess = "adieu" # TODO: smarter way to do this
#answer = "print" # TODO: prompt for this
#status, guesses = solve("adieu", "print")
#print(status, guesses)

print(solve("adieu", "print"))
print(solve("adieu", "vicua"))
print(solve("adieu", "strad"))
print(solve("adieu", "metus"))
print(solve("adieu", "lofts"))
print(solve("adieu", "foppy"))
print(solve("adieu", "munch"))
print(solve("adieu", "waged"))
print(solve("adieu", "assis"))
print(solve("adieu", "abdom"))
print(solve("adieu", "golet"))
print(solve("adieu", "gorer"))
print(solve("adieu", "skite"))
print(solve("adieu", "joola"))
print(solve("adieu", "secre"))
print(solve("adieu", "flunk"))
print(solve("adieu", "creel"))
print(solve("adieu", "zamia"))
print(solve("adieu", "snows"))
print(solve("adieu", "lushy"))
print(solve("adieu", "knees"))
print(solve("adieu", "krans"))
print(solve("adieu", "ruvid"))
print(solve("adieu", "geoid"))
print(solve("adieu", "griot"))
print(solve("adieu", "apium"))

