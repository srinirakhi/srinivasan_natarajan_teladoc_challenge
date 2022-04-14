# srinivasan_natarajan_teladoc_challenge

For automation I have use PyCharm IDE 
Built BDD framework with Behave and Selenium with Python as programming language
Used Allure for reporting

How to run the code:
    1. Download and unzip the project files from GIT into a folder. Folder Structure Framework Folder-->Project Folder
    2. Install Python 3 latest version from python.org on the machine and add Python to PATH (this can be done if used python installation executable file)
    3. By default python virtual environment will be installed if not follow instructions in URL "https://docs.python.org/3/library/venv.html"
    4. Create venv on the framework folder follow instructions in URL "https://docs.python.org/3/library/venv.html". Kindly maintain structure Framework Folder-->venv
    5. Activate virtual env by following instructions in URL "https://docs.python.org/3/library/venv.html"
    6. Use powershell to download scoop refer to "https://scoop.sh/" and and refer to "https://docs.qameta.io/allure/" for allure installation
    7. Open cmd or terminal and navigate to project folder after activating virtual environment.
    8. Run command behave -f allure_behave.formatter:AllureFormatter -o allure_report_out to execute project
    9. Open powershell and navigate to project folde
    10. Run command allure allure serve allure_report_out to generate report on local machine in html format
