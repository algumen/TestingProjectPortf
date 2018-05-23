# README #


This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Automation of testing 

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests


********To run tests in threads:
pytest -n <NUM>  (where <NUM> is q-ty of threads. Example: pytest -n 4)

********To run tests with allure:
pytest -n 4 --alluredir=reports    - to run
allure serve reports               - to make report after

pytest -n 2 tests/test_pages.py::test_check_webpage_markup --alluredir=reports

********To run tests many times(bad idea now:)):
py.test --count=10 test_file.py      - repeat for 10 times
pytest --count=2 tests/ -n 4         - run all tests in folder tests 2 times in 4 threads
pytest --count=6 tests/test_pages.py::test_sign_up_with_valid_user --alluredir=reports     - run chosen tests only

pytest --count=20 tests/test_pages.py::test_check_bets_system -s -v   - repeat N times + extended print + verbouse
pytest --count=10 tests/pause_test_pages.py::test_sign_up_with_valid_user -s   - repeat 10 times + extended print

pytest tests/test_pages.py::test_check_single_bet tests/test_pages.py::test_check_multi_bet --alluredir=reports

* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
