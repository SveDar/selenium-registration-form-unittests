import unittest
from fail_testregistrationform import FailTestRegistrationForm
from pass_testregistrationform import PassTestRegistrationForm

def run_tests():
    # Create a test suite
    test_suite_pass = unittest.TestLoader().loadTestsFromTestCase(PassTestRegistrationForm)
    test_suite_fail = unittest.TestLoader().loadTestsFromTestCase(FailTestRegistrationForm)
    suite = unittest.TestSuite([test_suite_pass,test_suite_fail])

    # Run the tests
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Check if the test run was successful
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")

if __name__ == '__main__':
    run_tests()
