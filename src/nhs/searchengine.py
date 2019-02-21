import string

def _extract_words(text):
    """
    Extract the words from a text ignoring the punctuation. Words are all converted to lowercase.
    Duplicate words are discarded.

    :param text: text to extract the words from
    :return: a set of unique lower case words
    """

    # we create a translator for removing punctuation
    translator = str.maketrans('', '', string.punctuation)

    # we return the list of unique words (converted to lowercase)
    return set(text.translate(translator).lower().split())


def search(datafile, query, bool_operator):
    """
    Queries on a set of documents.

    :param datafile: The location of the datafile as a pathlib.Path
    :param query: the query text
    :param bool_operator: the operator. Must be one of [OR, AND]
    :return: the list of indexes matching the search criteria
    """

    # we normalize to uinique lowercase words the query string and split by space
    query = _extract_words(query)

    # we read the datafile
    data = datafile.readlines()

    # calculating results
    results = [str(i) for i, text in enumerate(data)
               if (query.issubset(_extract_words(text))
                   if bool_operator == 'AND'
                   else bool(query.intersection(_extract_words(text))))]

    return results