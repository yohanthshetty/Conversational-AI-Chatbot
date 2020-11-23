from xml.dom.minidom import parse
import xml.dom.minidom
import json

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("covid_topics.xml")
collection = DOMTree.documentElement

# Get all the topics in the collection
covid_topics = collection.getElementsByTagName("topic")

my_dict = {}
main_list = []

# Save all topics to json.
for topic in covid_topics:
   my_dict = {}
   my_dict['topic_number'] = topic.getAttribute("number")
   query = topic.getElementsByTagName('query')[0]
   my_dict['query'] = query.childNodes[0].data
   question = topic.getElementsByTagName('question')[0]
   my_dict['question'] = question.childNodes[0].data
   narrative = topic.getElementsByTagName('narrative')[0]
   my_dict['narrative'] = narrative.childNodes[0].data
   main_list.append(my_dict)

# write topics to json
with open("topics_json_file.json", 'w') as fout:
   json.dump(main_list, fout)

print("Parsing of XML Complete")