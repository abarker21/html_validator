#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag $
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    list_storage = _extract_tags(html);

    i = 0

    while i < len(list_storage)-1:   
        tag0 = list_storage[i]
        tag1 = "<" + "/" + tag0[1:]

        if list_storage[i+1] != tag1:
            tag0 = list_storage[i+1]
            tag1 = "<" + "/" + tag0[1:]
            i+=1
            if tag0[1:2] == '/':
                return False
            
        else:
            list_storage.remove(tag0)
            list_storage.remove(tag1)
            i = 0

        print(list_storage)
        


    print(list_storage)
    if (len(list_storage) != 0):
        return False
    else:
        return True
        
def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are p$
    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    list_storage = list(html)
    p_out = []
    i = 0
    while i < len(list_storage):

        char7 = list_storage[i]
        
        if char7 == '<':
  
            word1 = ""     
            while list_storage[i] != '>':
                word1 = word1 + list_storage[i]
                
                i = i+1
            word1 = word1 + list_storage[i]
            
            p_out.append(word1)
            
            
        i = i + 1

    return p_out
