from five import grok
from zope import schema

from z3c.relationfield.schema import RelationChoice

from plone.formwidget.autocomplete import AutocompleteFieldWidget
from plone.formwidget.contenttree import ObjPathSourceBinder, \
    ContentTreeFieldWidget
from plone.directives import form, dexterity
from plone.app.textfield import RichText

from fullmarks.assessmentitem import _
from fullmarks.assessmentitem.referencematerial import IReferenceMaterial

class IAssessmentItem(form.Schema):
    """Assessment Item
    """
    
    form.widget(referenceMaterial=ContentTreeFieldWidget)
    referenceMaterial = RelationChoice(
            title=_(u"Reference Material"),
            source=ObjPathSourceBinder(
                object_provides=IReferenceMaterial.__identifier__),
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

    answerMarkedCorrect = schema.Int(
            title=_(u"Answer Marked Correct"),
            description=_(u"The number of times other members have "
                           "confirmed the answer as correct"),
        )

    answerMarkedIncorrect = schema.Int(
            title=_(u"Answer Marked Incorrect"),
            description=_(u"The number of times other members have "
                           "marked the answer as incorrect"),
        )

    dateLastUsed = schema.Datetime(
            title=_(u"Date Last Used"),
            description=_(u"The last time this item was used in a test"),
            required=False,
        )

    learnerResponseTime = schema.Int(
            title=_(u"Learner Response Time"),
            required=False,
        )


