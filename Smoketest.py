import unittest
from InstPersonLogin import InstPersonLoginTest

login_test = unittest.TestLoader().loadTestsFromTestCase(InstPersonLoginTest)

smoke_tests = unittest.TestSuite([login_test])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)
