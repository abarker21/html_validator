ction performs a limited version of html validation by checking whether every opening tag $
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    phrase = _extract_tags(html);
    i = 0
    while i < len(phrase)-1:
        tag = phrase[i]
        nexttag = "<" + "/" + tag[1:]
        if phrase[i+1] != nexttag:
            tag = phrase[i+1]
            nexttag = "<" + "/" + tag[1:]
            i+=1
            if tag[1:2] == '/':
                return False
        else:
            phrase.remove(tag)
            phrase.remove(nexttag)
            i = 0
        print(phrase)
    print(phrase)
    if (len(phrase) != 0):
        return False
    else:
        return True


    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep tra$
    # but arbitrary text located between the html tags



def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are p$
    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    phrase = list(html)
    output = []
    i = 0
    while i < len(phrase):
        character = phrase[i]
        if character == '<':
            word = ""
            while phrase[i] != '>':
                word = word + phrase[i]
                i = i+1
            word = word + phrase[i]
            output.append(word)
        i = i + 1
    return output
