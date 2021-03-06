import xml.dom.minidom

from five import grok
from zope import schema

from z3c.relationfield.schema import RelationChoice

from plone.formwidget.autocomplete import AutocompleteFieldWidget
from plone.formwidget.contenttree import ObjPathSourceBinder, \
    ContentTreeFieldWidget
from plone.directives import form
from plone.app.textfield import RichText

from Products.ATContentTypes.interfaces.interfaces import ITextContent

from fullmarks.assessmentitem import _


class IAssessmentItem(form.Schema):
    """Assessment Item
    """
    
    form.widget(referenceMaterial=ContentTreeFieldWidget)
    referenceMaterial = RelationChoice(
            title=_(u"Reference Material"),
            source=ObjPathSourceBinder(
                object_provides=ITextContent.__identifier__),
            required=False,
        )

    question = RichText(
            title=_(u"Question"),
            required=True
        )
    
    answer = RichText(
            title=_(u"Answer"),
            required=False,
        )

    marks = schema.Int(
            title=_(u"Marks"),
            required=False,
            default=0,
        )

    form.omitted('answerMarkedCorrect')
    answerMarkedCorrect = schema.Int(
            title=_(u"Answer Marked Correct"),
            description=_(u"The number of times other members have "
                           "confirmed the answer as correct"),
            required=False,
            default=0,
        )

    form.omitted('answerMarkedIncorrect')
    answerMarkedIncorrect = schema.Int(
            title=_(u"Answer Marked Incorrect"),
            description=_(u"The number of times other members have "
                           "marked the answer as incorrect"),
            required=False,
            default=0,
        )

    form.omitted('dateLastUsed')
    dateLastUsed = schema.Datetime(
            title=_(u"Date Last Used"),
            description=_(u"The last time this item was used in a test"),
            required=False,
        )

    learnerResponseTime = schema.Int(
            title=_(u"Learner Response Time"),
            required=False,
        )


class View(form.DisplayForm):
    grok.context(IAssessmentItem)
    grok.require('zope2.View')

class QTI(grok.View):
    grok.context(IAssessmentItem)
    grok.require('zope2.View')
    
    def render(self):
       self.request.response.setHeader('Content-Type', 'text/xml')
       doc = xml.dom.minidom.Document()
       
       item = doc.createElement("item")
       doc.appendChild(item)
       item.setAttribute("title",self.context.title)
       item.setAttribute("ident",self.context.id)

       item_md = doc.createElement("itemmetadata")
       item.appendChild(item_md)

       pres = doc.createElement("presentation")
       item.appendChild(pres)

       material = doc.createElement("material")
       pres.appendChild(material)

       mattext = doc.createElement("mattext")
       material.appendChild(mattext)

       return doc.toprettyxml()

