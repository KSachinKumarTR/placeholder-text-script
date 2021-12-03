import xml.etree.ElementTree as ET
import lxml.etree as ett
import xml.etree.ElementPath as EP

tree = ET.parse("lbp_formatted.xml")   #1st run this file
root = tree.getroot()


def add_new_section_element(branch):
    new_section_element = ET.Element("section")
    branch.insert(1, new_section_element)


def add_new_sub_section_element(branch):
    new_sub_section_element = ET.Element("sub-section1")
    branch.insert(1, new_sub_section_element)




def find_required_child_sub_section_tags():
    a = ["section/sub-section","section/sub-section/sub-section","section/sub-section/sub-section/sub-section","section/sub-section/sub-section/sub-section"]
    for i_a in a:
        #print(i_a)
        #print(type(a[0]))
        for elem in root.findall(i_a):
            if elem.tag == "sub-section":
                i = 0
                # print("inside a new section")
                a_list = []
                while i < len(elem):
                    a_list.append(elem[i].tag)
                    i = i + 1
                #print(a_list)
                para_index = []
                bool1 = a_list.__contains__("sub-section")
                #print("it contains child sub-section")
                if bool1 == True:
                    bool_paragraph1 = a_list.__contains__("paragraph")

                    if bool_paragraph1 == True:
                        print("child subsection conmtains paragrapht")
                        #print("yes")
                        for f in a_list:
                            if f == "paragraph":
                                # print("yes equal")
                                para_index.append(1)  # it gets total number of paragraph tags in side section tag
                        #print(len(para_index))
                        len_para_index = len(para_index)
                        new_subsection_element = ET.Element("sub-section")
                        elem.insert(1, new_subsection_element)
                        new_sub_section_title_element = ET.Element("title")
                        new_sub_section_title_element.text = "Introduction"
                        elem[1].insert(0, new_sub_section_title_element)

                        i_para = 0
                        while i_para < len_para_index:
                            elem[1].append(elem[i_para + 2])
                            #elem.remove(elem[i_para + 2])
                            i_para += 1  # Working for ch1 till here
                        for ss in range(50):
                            for r_i in range(len(elem)):
                                if elem[r_i].tag == "paragraph":
                                    print("hbhbybybnn     " + elem[r_i].tag)
                                    elem.remove(elem[r_i])
                                    r_i = r_i + 1
                                    break




def find_req_title_placeholders_section_sub_section_sub_section():
    a=["section/sub-section/sub-section","section/sub-section/sub-section/sub-section","section/sub-section/sub-section/sub-section/sub-section"]
    i=""
    for i in range(len(a)):
        for each_sub_section in root.findall(a[i]):

            length_k = len(each_sub_section)
            '''#print("hi brbrbrbrbr")
            #print(each_sub_section)
            
            for each_sub_section_tag in range(len(each_sub_section)):
            #for each_sub_section_1 in each_sub_section.iter("paragraph"):  # here each_sub_section is equal to a sub-section , and each_sub_section_1 is a paragraph/sub-paragraph
                #print(each_sub_section_1.tag)
                if each_sub_section_1[0].tag == "para":
                    if length_k == 2:  # if this means sub-section has only one paragraph
                        new_paragraph_title_element = ET.Element("title")
                        new_paragraph_title_element.text = "Generally"
                        each_sub_section_1.insert(0, new_paragraph_title_element)
                    else:
                        new_paragraph_title_element = ET.Element("title")
                        new_paragraph_title_element.text = "Introduction"
                        each_sub_section_1.insert(0, new_paragraph_title_element)
            if each_sub_section[each_sub_section_tag].tag == "para":
                if length_k == 2:  # if this means sub-section has only one paragraph
                    new_paragraph_title_element = ET.Element("title")
                    new_paragraph_title_element.text = "Generally"
                    each_sub_section[each_sub_section_tag].insert(0, new_paragraph_title_element)
                else:
                    new_paragraph_title_element = ET.Element("title")
                    new_paragraph_title_element.text = "Introduction"
                    each_sub_section[each_sub_section_tag].insert(0, new_paragraph_title_element)'''

            for a_tag in range(length_k):
                a_tag_holder = each_sub_section[a_tag]
                print(type(a_tag_holder))
                if a_tag_holder.tag == "paragraph":
                    if a_tag_holder[0].tag == "para":
                        if length_k == 2:
                            new_paragraph_title_element = ET.Element("title")
                            new_paragraph_title_element.text = "Generally_11"
                            a_tag_holder.insert(0, new_paragraph_title_element)
                            each_sub_section[a_tag] = a_tag_holder
                        else:
                            new_paragraph_title_element = ET.Element("title")
                            new_paragraph_title_element.text = "Introduction_11"
                            a_tag_holder.insert(0, new_paragraph_title_element)
                            each_sub_section[a_tag] = a_tag_holder




if __name__ == "__main__":

    find_required_child_sub_section_tags()
    #find_req_title_placeholders_section_sub_section_sub_section()
    tree.write('zg.xml')    #1st run this file

