'''
Valid Parentheses

Link: https://leetcode.com/problems/valid-parentheses
----------------------------------------------

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
----------
Input: s = "()"
Output: true

Example 2:
----------
Input: s = "()[]{}"
Output: true

Example 3:
----------
Input: s = "(]"
Output: false
 

Constraints:
------------
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def isValid(s):

  if s[0] in {")","]","}"} or s[-1] in {"(","[","{"}:
      return False
  
  def search(parens, cache, loop=True):
  
      matched = True
      done = False
  
      for j in range(len(parens)):
          if parens[j] == "(" or parens[j] == "[" or parens[j] == "{":
            result = search(parens[j + 1:], parens[j])
            matched = result['matched']
            cache = result['cache']
            done = result['done']
            
            if matched is False or done is True:
              break

          elif cache == "(":
              if parens[j] == "]" or parens[j] == "}":
                  matched = False
                  break
              elif parens[j] == ")" and j < len(parens)-1:
                  cache = parens[j + 1]
  
          elif cache == "[":
              if parens[j] == ")" or parens[j] == "}":
                  matched = False
                  break
              elif parens[j] == "]" and j < len(parens)-1:
                  cache = parens[j + 1]
  
          elif cache == "{":
              if parens[j] == ")" or parens[j] == "]":
                  matched = False
                  break
              elif parens[j] == "}" and j < len(parens)-1:
                  cache = parens[j + 1]

          if j == len(parens) -1:
            done = True
            
      if loop is True:
        return {'matched': matched, 'cache': cache, 'done': done}
      else:
        return matched
  
  return search(s, s[0], False)

print("This file is a work in progress, please check back later!")