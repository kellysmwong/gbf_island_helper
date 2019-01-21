import pyautogui
import sys

def execute_skill(char_idx, skills):
  pyautogui.click(char_loc[char_idx][0], char_loc[char_idx][1])

  for skill_no in commands[1:]:
    skill_idx = int(skill_no)  - 1
    pyautogui.click(skill_loc[skill_idx][0], skill_loc[skill_idx][1])
  
  pyautogui.click(back[0], back[1])


def execute_attack():
  pyautogui.click(attack[0], attack[1])


def execute_summon(summon_idx):
  pyautogui.click(summon_menu[0], summon_menu[1])
  pyautogui.click(summon[summon_idx][0], summon[summon_idx][1])
  pyautogui.click(summon_confirm[0], summon_confirm[1])
  
##############################################
# Button position
char_loc = [
[67, 560],
[148, 560],
[225, 560],
[299, 560]]
skill_loc = [
  [176, 594],
  [251, 594],
  [334, 594],
  [416, 594]
]
attack = [388, 429]
back = [64, 433]
summon_menu = [402, 561]
summon_confirm = [358, 563]
summon = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[434, 560]]
##############################################

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

if len(sys.argv) > 1:
  config_file = sys.argv[1]
else:
  config_file = 'sample.txt'

f = open(config_file, "r")
for line in f:
  commands = line.split(',')
  if commands[0] == 'A':
    execute_attack()
  elif commands[0] == 'S':
    execute_summon(int(commands[1]) - 1)
  else:
    execute_skill(int(commands[0]) - 1, commands[1:])
