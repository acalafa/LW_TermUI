#include <iostream>
#include <string>
#include <map>

#include "menus.hh"

int get_command(int menu_key);
void display_UI(int menu_key, bool badcomm);
void run_program();

int get_command(int menu_key) {
  std::cout << "\nCommand: "; std::flush(std::cout);
  std::string newcomm; std::cin >> newcomm; //read in any input as a string
  try {std::stoi(newcomm);} //Try to read the command as an integer
  catch (...) {return -1;} //return an error code if the command is not an integer

  int keyshift = std::stoi(newcomm); //Try to read the command as an integer
  if (keyshift == 0) return (menu_key - (menu_key % 10)) / 10; //remove the last digit of the menu key
  else if (keyshift < 10) return (menu_key * 10) + keyshift; //single-digit menu entries for now
  else return std::stoi(newcomm); //At this point, we're returning a command value. Go ahead and use it as-is.
}

void display_UI(int menu_key, bool badcomm) {
  std::string menustring = dict_menus[menu_key];
  std::system("clear"); //change to "cls" on Windows
  std::cout << menustring;
  if (badcomm) {
    std::cout << "\nInvalid command";
    badcomm = false;
  }
  std::flush(std::cout);
  return;
}

void run_program() {
  bool working = true;
  int menu_key = 1; // 1 is the root menu
  bool bad_command = false;

  while (working) {
    display_UI(menu_key, bad_command);
    int command = get_command(menu_key);
    bad_command = false;

    if (command == 0) {
      std::cout << "Exiting program...\n"; std::flush(std::cout);
      working = false;
      continue;
    }

    if (dict_menus.find(command) != dict_menus.end()) menu_key = command;
    else bad_command = true; //If the command is not a valid menu or function key, set the bad_command flag
  }
  return;
}