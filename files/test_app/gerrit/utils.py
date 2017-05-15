
import re

from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
from urllib.parse import quote_plus


def change_joined_id(project, branch, change_id):
    return "{0}~{1}~{2}".format(quote_plus(project),
                                branch,
                                change_id)

def to_json(items):
    message = '{"' + '", "'.join(['"=>"'.join([key, str(val)]) for key, val in items]) + '"}'
    message = message.replace('"nil"', 'nil')

    return message

def to_xml(dict_obj, custom_root_str):

    xml = dicttoxml(dict_obj, custom_root=custom_root_str, attr_type=False)
    dom = parseString(xml)
    xml_message = dom.toprettyxml(indent='  ')
    xml_message = re.sub('^<\?[\w\s=\"\.]+\?>', '', xml_message)
    xml_message = xml_message.strip()

    return xml_message
