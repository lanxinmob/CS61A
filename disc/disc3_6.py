# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   if front_is_clear():
      move()
   if front_is_clear():
      move()
      main()
      move()
   if front_is_blocked():
      turn_left()
      turn_left()
    