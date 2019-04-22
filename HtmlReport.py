import unittest
import HTMLTestRunner
import os
from InstPersonLogin import InstPersonLoginTest

dir = os.getcwd()
login_test = unittest.TestLoader().loadTestsFromTestCase(InstPersonLoginTest)

smoke_tests = unittest.TestSuite([login_test])

outfile = open(dir + "\SmokeTestReport.html", "wb")

runner = HTMLTestRunner.HTMLTestRunner(
	stream=outfile,
	title="Test Report",
	description="Smoke Tests"
)

runner.run(smoke_tests)
