# Selenium Python scripts for automating test cases.

## Contains scrips to automate test cases of "Anki" web-based application. Both tests generated manually and with the help of CIT.

## Contents:
* excel_files: excel tables with test cases data generated with the help of CIT;
* utilities: supporting functions, namely get_data_fromExcel.py and login_anki_profile.py;
* test_anki: scripts of the tests. Each file corresponds to one test scenario and runs multiple tests with various parameters;

## Setup:
a .zip folder is prepared for download. It contains all the elements of a Python project as well as the 3 packages mentioned above.
After download, Selenium must be installed on the used machine.

## Notes:
1) ankiweb account login:
My personal ankiweb account was used to perform the tests. Thus, in order to use the scrips present in this repository, a brand new account must be created. Then your own password and username must be used in login_anki_profile.py utility function instead of values "your_password" and "your_username" respectively.

2) excel tables location:
all scripts use absolute paths to locate the excel tables with data on a used machine.
After downloading, it is necessary to specify the locations where those excel files from excel_files folder are stored.
Then your own locations must be used as a parameter passed to get_data_fromExcel.py utility function instead of value present at the moment.

3) test scenarios preconditions:
All the tests will work correctly only if all the test preconditions are met. All the preconditions for each test case can be found in manual_tests.xlxs file.





