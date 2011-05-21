from five import grok
from plone.directives import form
from plone.app.textfield import RichText

class IReferenceMaterial(form.Schema):
    
    body = RichText(
            title=u"Reference Material",
            required=False,
        )

