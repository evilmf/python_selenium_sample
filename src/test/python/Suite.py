import unittest
from BookTour import BookTour
from NewCustomerAccount import NewCustomerAccount
from NewTour import NewTour
from xmlrunner import XMLTestRunner

if __name__ == '__main__':
    testClassesToRun = [BookTour, NewCustomerAccount, NewTour]

    loader = unittest.TestLoader()

    suitesList = []
    for testClass in testClassesToRun:
        suite = loader.loadTestsFromTestCase(testClass)
        suitesList.append(suite)

    bigSuite = unittest.TestSuite(suitesList)

    runner = XMLTestRunner(output='test-reports')
    results = runner.run(bigSuite)