import xml.etree.ElementTree as ET
import lxml.etree as ett
import xml.etree.ElementPath as EP
tree = ET.parse("zg.xml")   #run this after running 1st file
root = tree.getroot()
def add_new_section_element(branch):
    new_section_element = ET.Element("section")
    branch.insert(1, new_section_element)

def add_new_sub_section_element(branch):
    new_sub_section_element = ET.Element("sub-section1")
    branch.insert(1, new_sub_section_element)
def find_required_new_section_tags():
    for elem in root.iter():
        if elem.tag == "document":
            print("insode document")

            #print(elem[0].tag)
            if elem[1].tag == "paragraph":  # document[1]==paragraph
                # print("no title")
                add_new_section_element(elem)
                new_section_title = ET.Element("title")
                new_section_title.text = "Introduction"
                elem[1].append(new_section_title)
                if elem[2].tag == "paragraph":
                    elem[1].append(elem[2])
                    elem.remove(elem[2])

def find_required_tag():
    for elem in root.iter():
        '''if elem.tag == "document":

            #print(elem[0].tag)
            if elem[1].tag == "paragraph":  # document[1]==paragraph
                # print("no title")
                add_new_section_element(elem)
                new_section_title = ET.Element("title")
                new_section_title.text = "Introduction"
                elem[1].append(new_section_title)
                if elem[2].tag == "paragraph":
                    elem[1].append(elem[2])
                    elem.remove(elem[2])'''


        if elem.tag == "section" :
            i=0
            #print("inside a new section")
            a_list = []
            while i < len(elem):
                a_list.append(elem[i].tag)
                i=i+1
            #print(a_list)
            para_index = []
            bool1=a_list.__contains__("sub-section")
            if bool1==True:
                bool_paragraph1=a_list.__contains__("paragraph")
                if bool_paragraph1==True:
                    print(elem.attrib)
                    for f in a_list:
                        if f=="paragraph":
                            #print("yes equal")
                            para_index.append(1)   #it gets total number of paragraph tags in side section tag
                    #print(len(para_index))
                    len_para_index=len(para_index)
                    new_subsection_element=ET.Element("sub-section")
                    elem.insert(1,new_subsection_element)
                    new_sub_section_title_element=ET.Element("title")
                    new_sub_section_title_element.text="Introduction"
                    elem[1].insert(0,new_sub_section_title_element)
                    i_para=0
                    ii=0
                    '''while i_para<len_para_index:
                        elem[1].append(elem[i_para+2])
                        elem.remove(elem[i_para + 2])
                        i_para += 1  '''
                    #Working for ch1 till here
                    for ii in range(len(elem)):
                        print("in loop")
                        print(elem[ii].attrib)
                        if elem[ii].tag=="paragraph":
                            #print("it is brp")
                            #print(elem.tag)
                            elem[1].append(elem[ii])
                            elem.remove(elem[ii])
                        ii+=1





















def find_req_title_placeholders_section_paragraph():
   ''' for each_section in root.iter("section"): #here we are inserting heading for the paragraph which does not have any sub-section as sibling
        #print('Hi')
        length_k=len(each_section)
        #print("length of each section is :")
        #print(length_k)
        if each_section[1].tag=="paragraph":
            if length_k == 2:
                new_paragraph_title_element = ET.Element("title")
                new_paragraph_title_element.text = "Generally"
                each_section[1].insert(0, new_paragraph_title_element)
            else:
                new_paragraph_title_element = ET.Element("title")
                new_paragraph_title_element.text = "Introduction"
                each_section[1].insert(0, new_paragraph_title_element)'''
   for each_document in root.iter("document"):
       len_each_document=len(each_document)
       #print("len of docu")
       #print(len_each_document)
       for each_document_section in range(len_each_document):
           if each_document[each_document_section].tag=="section":
               each_document_section_holder=each_document[each_document_section]  #This is a variablew which holdes each section tag
               length_k = len(each_document_section_holder)
               print("length of each section is :")
               # print(length_k)
               if each_document_section_holder[1].tag == "paragraph":
                   if length_k == 2:
                       new_paragraph_title_element = ET.Element("title")
                       new_paragraph_title_element.text = "Generally"
                       each_document_section_holder[1].insert(0, new_paragraph_title_element)
                   else:
                       new_paragraph_title_element = ET.Element("title")
                       new_paragraph_title_element.text = "Introduction"
                       each_document_section_holder[1].insert(0, new_paragraph_title_element)
              # print('Hi')




def find_req_title_placeholders_section_sub_section():
    for each_sub_section in root.iter("sub-section"):
        #print("printing length of each subsection")
        length_ = len(each_sub_section)
        #print("printing subsection attrib")
        #print(each_sub_section.attrib)
        #print(length_)
        '''for each_sub_section_1 in each_sub_section.iter("paragraph"):     #here each_sub_section is equal to a sub-section , and each_sub_section_1 is a paragraph/sub-paragraph
            print("printing paragraph attrib")
            print(each_sub_section_1.attrib)
            if each_sub_section_1[0].tag =="para":
                if length_ == 2:       #if this means sub-section has only one paragraph
                    new_paragraph_title_element = ET.Element("title")
                    new_paragraph_title_element.text = "Generally"
                    each_sub_section_1.insert(0, new_paragraph_title_element)
                else:
                    new_paragraph_title_element = ET.Element("title")
                    new_paragraph_title_element.text = "Introduction"
                    each_sub_section_1.insert(0, new_paragraph_title_element)'''

        for a_tag in range(length_):
            a_tag_holder=each_sub_section[a_tag]
            #print(type(a_tag_holder))
            if a_tag_holder.tag=="paragraph":
                if a_tag_holder[0].tag=="para":
                    if length_ == 2:
                        new_paragraph_title_element = ET.Element("title")
                        new_paragraph_title_element.text = "Generally_11"
                        a_tag_holder.insert(0,new_paragraph_title_element)
                        each_sub_section[a_tag]=a_tag_holder
                    else:
                        new_paragraph_title_element = ET.Element("title")
                        new_paragraph_title_element.text = "Introduction_11"
                        a_tag_holder.insert(0, new_paragraph_title_element)
                        each_sub_section[a_tag] = a_tag_holder






























if __name__ == "__main__":
    find_required_new_section_tags()
    find_required_tag()
    find_req_title_placeholders_section_paragraph()
    #find_req_title_placeholder_section_sub_sub_section()
    find_req_title_placeholders_section_sub_section()

    #tree.write('output_ch1_with2nd_pythoncodeQ.xml')
    tree.write('final_Zg.xml')

