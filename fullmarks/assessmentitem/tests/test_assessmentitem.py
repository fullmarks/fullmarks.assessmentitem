import unittest
from xml.dom.minidom import parseString

from plone.dexterity.interfaces import IDexterityFTI
from Products.PloneTestCase.ptc import PloneTestCase

from fullmarks.assessmentitem.tests.layer import Layer

from fullmarks.assessmentitem.assessmentitem import IAssessmentItem

class TestAssessmentItem(PloneTestCase):
    """Unit tests for assesment items"""
    layer = Layer
    def test_qti(self):
        
        new_id = self.folder.invokeFactory('fullmarks.assessmentitem.assessmentitem','test_item')
        new_item = self.folder[new_id]
        new_item.title = "My Title"
        new_item.question = "How much cheese is there on the moon?"
        new_item.answer = "A lot, Grommit"
        new_item.marks = 10
        
        #Must get status
        #Something with Portal Workflow tools
        
        view = new_item.restrictedTraverse('@@qti')
        doc = parseString(view())

        items_dom = doc.getElementsByTagName("item")
        self.assertEquals(len(items_dom),1)
        item_dom = items_dom[0]
        self.assertEquals(item_dom.getAttribute("title"),new_item.title)
        self.assertEquals(item_dom.getAttribute("ident"),new_item.id)
        
        item_mds = item_dom.getElementsByTagName("itemmetadata")
        self.assertEquals(len(item_mds),1)
        item_md = item_mds[0]
        #Check qmd_itemtype
        #Check qmd_status
        #Check qmd_topic

        pres_doms = item_dom.getElementsByTagName("presentation")
        self.assertEquals(len(pres_doms),1)
        pres_dom = pres_doms[0]
        material_doms = pres_dom.getElementsByTagName("material")
        self.assertEquals(len(material_doms),1)
        material_dom = material_doms[0]

        mattext_doms = material_dom.getElementsByTagName("mattext")
        self.assertEquals(len(mattext_doms),1)
        mattext_dom = mattext_doms[0]
        
        #We dont really know how to represent this in a standard way
        #self.assertEqual(mattext_dom.firstChild.data,??)

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
