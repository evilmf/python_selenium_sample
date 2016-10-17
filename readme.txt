Installation:
1. install python 2.7.x
2. pip install selenium
3. pip install unittest-xml-reporting 
4. install JDK 1.7
5. install maven 2+

Running the whole test suite with Maven: (This requires Maven, jdk 1.7 and unittest-xml-reporting Python module)
cd into the project root folder where pom.xml locates and run one of the following commands: 
For windows: mvn clean -Denv=chrome_win32 test
For mac osx: mvn clean -Denv=chrome_mac64 test

Running individual test script: (This doesn't require Maven, jdk 1.7 and unittest-xml-reporting Python module)
cd into ./src/test/python
set environment variable WEBDRIVER=chrome_win32 or WEBDRIVER=chrome_mac64 then
python NewCustomerAccount.py
python NewTour.py
python BookTour.py

Note: 
1. Tested in Windows 10 with Chrome Version 53.0.2785.143 m only.  
2. Test XML report can be found at src/test/python/test-reports if you run with Maven