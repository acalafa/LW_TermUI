import os
import sys

from menus import dict_menus

def clear_terminal() -> None:
  clearcomm: str = "cls" if os.name == "nt" else "clear"
  os.system(clearcomm)
  return

##########################################################################################

def get_command(menu_key: int) -> int:
  sys.stdout.write("Command: ")
  sys.stdout.flush()

  newcomm: str = input() #read in any input as a string
  try: keyshift: int = int(newcomm) #Try to read the command as an integer
  except: return -1 #return an error code if the command is not an integer
  
  if keyshift == 0: return int((menu_key-(menu_key%10))/10) #remove the last digit of the menu key
  elif keyshift<10: return ((menu_key*10)+keyshift) #single-digit menu entries for now
  elif keyshift<1000: return -1 #reserve 1k+ for functions.
  #if you want more directories, just increase 1k to 10k, etc.
  else: return int(newcomm) #At this point, we're returning a command value. Go ahead and use it as-is.

##########################################################################################

def display_UI(menu_key: int, badcomm: bool = False) -> None:
  menustring: str = dict_menus[menu_key]
  clear_terminal()
  print(menustring)
  if badcomm:
    print("Invalid command")
    badcomm = False
  return

##########################################################################################

def run_program() -> None:
  working: bool = True
  menu_key: int = 1 # 1 is the root menu
  bad_command: bool = False

  while working:
    display_UI(menu_key, bad_command)
    command: int = get_command(menu_key)
    bad_command = False

    if command == 0:
      print("Exiting program...")
      working = False
      continue

    if command in dict_menus: menu_key = command #Update UI if a valid menu key is given
    #elif command in dict_functions: dict_functions[command]() #Run the function if a valid function key is given
    else: bad_command = True #If the command is not a valid menu or function key, set the bad_command flag

  #Clean up loose ends outside of the working loop before exit