Installation:
1. install python 2.7.x
2. pip install selenium
2. pip install unittest-xml-reporting
4. install JDK 1.7
5. install maven

Running the Test:
For windows: clean -Denv=chrome_win32 test

For mac osx: clean -Denv=chrome_mac64 test

Note: 
1. Tested in Windows 10 with Chrome Version 53.0.2785.143 m only.  
2. Test XML report can be found at src/test/python/test-reports