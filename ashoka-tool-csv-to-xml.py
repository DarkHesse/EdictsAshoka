import pandas as pd
import json as js
import xmltodict as xtd

def convert_info(info_source, info_num, info_place):
    return_string = """
        <head>
            <source>%s</source>
            <num>%s</num>
            <place>%s</place>
        </head>
    """ % (info_source, info_num, info_place)
    return return_string

def convert_sentence(sentence_number, sentence_text):
    return_string = """
        <sentence>
            <number>%s</number>
            <text>%s</text>
        </sentence>
    """ % (sentence_number, sentence_text)
    return return_string

xml_head = """<?xml version="1.1" encoding="UTF-8"?>
<!DOCTYPE edicts SYSTEM "ashoka_edicts.dtd">
<edicts>
"""

xml_start = """<edict>"""

xml_end = """
</edict>
"""

df = pd.read_csv("ashoka_foreign_relations.csv")

xml_output = xml_head

for index, row in df.iterrows():
    xml_output += xml_start
    xml_output += convert_info(row["source"], row["num"], row["place"])
   
    for index_column in range(1, 28):
        index_string = str(index_column)
        #print (row[index_string])
        xml_output += convert_sentence(index_string, row[index_string])
    xml_output += xml_end
xml_output += """</edicts>"""
            
with open("ashoka_edicts_foreign_relations.xml", "w") as text_file:
    text_file.write(xml_output)
    
with open("ashoka_edicts_foreign_relations.xml") as xml_file:
    data_dict = xtd.parse(xml_file.read())
    
json_data = js.dumps(data_dict)

with open("ashoka_edicts_foreign_relations.json", "w") as json_file:
    json_file.write(json_data)