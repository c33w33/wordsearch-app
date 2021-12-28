import re

# file location
doc_path = './wordsearch-app/static/doc/Test File.txt'

"""
search_doc () : function to search a string from a named document
parameters:
keyword = string to search
matchcase = boolean, TRUE:case-sensitive search
onlywhole = boolean, TRUE:exact word/phrase search, word/phrase is preceded and followed by spaces
doc_path = path to document

returns:
- list of dictionaries containing: 
		- line number, 
		- column number
		- line where string was found, with the string in bold

dictionaries suffice for now because of the size of the data. it would be
economical to however store the results in a db if there were more data.
"""


def search_doc(keyword, matchcase, onlywhole, doc_path):
    doc = open(doc_path, 'r')  # read the file only
    cnt = 0
    str_cnt = 0
    result = []
    for num, line in enumerate(doc):
        if matchcase == False:
            keyword = keyword.casefold()
            line = line.casefold()
        if onlywhole == True:
            keyword = " {keyword} ".format(keyword=keyword)

        # store all details in dictionary
        if keyword in line:
            details = {}
            details['Line'] = num + 1
            details['Column/s'] = [i.start() + 1 for i in re.finditer('(?={key})'.format(key=re.escape(keyword)), line)]  # find all occurences of string
            details['Text'] = line.replace(keyword, "<b>{text}</b>".format(text=keyword))
            result.append(details)
            cnt += 1  # count line matches
            str_cnt += line.count(keyword)  # count string matches
    doc.close()
    return result, cnt, str_cnt
