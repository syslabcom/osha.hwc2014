import logging

logger = logging.getLogger('osha.hwc2014')


def setupVarious(context):
    """
    @param context: Products.GenericSetup.context.DirectoryImportContext instance
    """

    # We check from our GenericSetup context whether we are running
    # add-on installation for your product or any other proudct
    if context.readDataFile('osha.hwc2014.txt') is None:
        # Not your add-on
        return

    portal = context.getSite()
    acl_users = portal.acl_users
    ps_plugin = acl_users.password_strength_plugin
    ps_plugin.manage_changeProperties(p1_re=".{8}.*", p1_err="Minimum 8 characters.")

    logger.info("PasswordStrength configured.")

    if 'password_policy' in acl_users.objectIds():
        acl_users.manage_delObjects(['password_policy'])
        logger.info("Removed default password policy.")
