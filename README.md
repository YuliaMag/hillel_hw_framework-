## README File

##### Project Overview: 
Training on creating separate test project from scratch.

##### Installation: 
- Please install required dependencies: pip install -r requirements.txt
- Entity under test: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Tests are supposed to be run for Chrome browser only. 
- Please install chromedriver according to base instructions (https://katekuehl.medium.com/installation-guide-for-google-chrome-chromedriver-and-selenium-in-a-python-virtual-environment-e1875220be2f)

##### Running Tests: 
Please make sure you are in correct directory: ./hillel_hw_framework-
- Commands to run tests with pytest:
- pytest tests  -- to  run all tests at once
- pytest -k <test_name>.py -- to run particular test by key
- pytest tests/<test_name>.py --  to run test from particular path
- pytest tests/t<test_name>.py::def_test_name -- to run particular test inside test file

##### Test Structure: 
- Please refer to visualizations/project_structure.txt for project structure and organization details. 
- Please refer to visualizations/scenarios.txt for test scenarios description. 

