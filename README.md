# Selenium Python scripts for automating test cases.

## Contains scrips to automate test cases of "Anki" web-based application. Foth tests generated manually and with the help of CIT.

## Contents:
* excel_files: excel table with tests cases data generated with the help of CIT;
* utilities: supporting functions, namely get_data_fromExcel.py and login_anki_profile.py;
* test_anki: scripts of the tests. Each file corresponds to one test scenario and runs multiple tests with various parameters;

## Setup:
a .zip folder is prepared for download. It containes all the elements of a Python project as well as the 3 packages mentioned above.
After download, Selenium must be installed on the used machine.

## Notes:
1) ankiweb account login:
My personal ankiweb account was used to perform the tests. Thus, in order to use the scrips present in this repository, a brand new account must be created. Then your own password and username must be used in login_anki_profile.py utility function instead of values "your_password" and "your_username" respectively.

2) test scenarious preconditions:
   





