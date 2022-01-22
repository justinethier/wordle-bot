import unittest

# Check compares each character in guess to the character in the corresponding position
# in answer and returns an array of 5 integers with one of the following values:
#
#   0 - Letter is in the corresponding position
#   1 - Letter is part of answer but in the wrong position
#   2 - Letter is wrong
#
def check(guess, answer):
  print("check", guess, answer)
  result = []
  remaining = list(answer)
  for i in range(0, 5):
    if guess[i] == answer[i]:
      result.append(0)
      print("guess", guess, "answer", answer, "remaining", remaining, guess[i])
      remaining.remove(guess[i])
    elif guess[i] in remaining:
      result.append(1)
      print("guess", guess, "answer", answer, "remaining(2)", remaining, guess[i])
      remaining.remove(guess[i])
    else:
      result.append(2)
  return result
      
class TestCheck(unittest.TestCase):
  def test_basic(self):
    self.assertEqual(check("audio", "baton"), [1,2,2,2,1])
    self.assertEqual(check("aboot", "robot"), [2,1,1,0,0])
    self.assertEqual(check("toads", "baton"), [1,1,1,2,2])
    self.assertEqual(check("about", "baton"), [1,1,1,2,1])
    self.assertEqual(check("baton", "baton"), [0,0,0,0,0])

  def test_repeated_letters(self):
    self.assertEqual(check("algae", "abbey"), [0,2,2,2,1])
    self.assertEqual(check("keeps", "abbey"), [2,1,2,2,2])
    self.assertEqual(check("orbit", "abbey"), [2,2,0,2,2])
    self.assertEqual(check("abate", "abbey"), [0,0,2,2,1])
    self.assertEqual(check("abbey", "abbey"), [0,0,0,0,0])

if __name__ == '__main__':
  unittest.main()
