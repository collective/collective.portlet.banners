from zope.i18nmessageid import MessageFactory
BannerPortletMessageFactory = MessageFactory('collective.portlet.banners')

from Products.Archetypes import atapi
from Products.CMFCore import utils as cmfutils
from collective.portlet.banners import config

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)
        
    # Now initialize all these content types. The initialization process takes
    # care of registering low-level Zope 2 factories, including the relevant
    # add-permission. These are listed in config.py. We use different
    # permissions for each content type to allow maximum flexibility of who
    # can add which content types, where. The roles are set up in rolemap.xml
    # in the GenericSetup profile.
    
    for atype, constructor in zip(content_types, constructors):
        cmfutils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types      = (atype,),
            permission         = config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)
