import xml.etree.ElementTree as ET 
from xml.dom import minidom
'''
Basic XLIFF structure is as follows
Root element is "xliff" which can have multiple "file" elements as 
children nodes (although in this class single "file" element is being used for simplicity)
Each file have "header" and "body" elements as its children. 
Each body can have multiple children elements by the name "trans-unit"
Each "trans-unit" can have multiple children by the name "source" and "target" (former
for source language and latter for target languege

In this library, this XLIFF heirarchy has been used to create XLIFF files.
'''

class XLIFF:    
    def __init__(self, file_name, source, target, approved=False):
        self.xliff = ET.Element("xliff")
        self.file = ET.SubElement(self.xliff,"file")
        self.header = ET.SubElement(self.file,"header")
        self.body = ET.SubElement(self.file,"body")
        self.trans_unit_ind = 0
        self.source = source
        self.target = target
        self.approved = approved

        self.set_xliff()
        self.set_file(file_name)
        self.set_header(file_name)
        
    def set_xliff(self):
        self.xliff.set("version", "1.2")
        self.xliff.set("xmlns", "urn:oasis:names:tc:xliff:document:1.2")
        self.xliff.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.xliff.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.xliff.set("xsi:schemaLocation", "urn:oasis:names:tc:xliff:document:1.2 xliff-core-1.2-transitional.xsd")
        
    def set_file(self, file_name):
        self.file.set("original", file_name)
        self.file.set("source-language", self.source)
        self.file.set("tool-id","custom")
        self.file.set("datatype","plaintext")
        
    def set_header(self,file_name):
        skl = ET.SubElement(self.header,"skl")
        ext_file = ET.SubElement(skl,"external-file")
        ext_file.set("href", file_name+".skl")
        
    def add_trans_unit(self, s, t):
        trans_unit = ET.SubElement(self.body,"trans-unit")
        trans_unit.set("id", str(self.trans_unit_ind))
        trans_unit.set("xml:space", "preserve")
        if(self.approved):
            trans_unit.set("approved", "yes")
        else:
            trans_unit.set("approved", "no")
        self.trans_unit_ind = self.trans_unit_ind + 1
        
        source = ET.SubElement(trans_unit, "source")
        source.set("xml:lang", self.source)
        source.text = s 
        
        target = ET.SubElement(trans_unit, "target")
        target.set("xml:lang", self.target)
        target.text = t
        
        
    def get_str(self):
        s = ET.tostring(self.xliff)
        s = minidom.parseString(s).toprettyxml(indent="   ")
        return s