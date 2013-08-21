from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class Oshahwc2014Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import osha.hwc2014
        xmlconfig.file(
            'configure.zcml',
            osha.hwc2014,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'osha.hwc2014:default')

OSHA_HWC2014_FIXTURE = Oshahwc2014Layer()
OSHA_HWC2014_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OSHA_HWC2014_FIXTURE,),
    name="Oshahwc2014Layer:Integration"
)
OSHA_HWC2014_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OSHA_HWC2014_FIXTURE, z2.ZSERVER_FIXTURE),
    name="Oshahwc2014Layer:Functional"
)
