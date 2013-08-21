from  osha.hwc2014.testing import OSHA_HWC2014_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=OSHA_HWC2014_FUNCTIONAL_TESTING)
    ])
    return suite