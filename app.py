import json
from difflib import get_close_matches

# Get the data needed for operations
data = json.load(open("data.json"))


# Returns the meaning of the given word
#w = the give word
def translate(w):
    # convert to lower case to accomodate all cases
    w = w.lower()
    # 1. Check if word exsist
    if w in data:
        # if so return the meaning of the word
        values = data[w]
        return {
            'values':values,
            'search_word': {'instead':False, 'matched':True}
        }
    # 2. Check for close match proximity(word that are close to the given)
    elif len(get_close_matches(w, data.keys())) > 0:
        # Get the close value to the word.
        close_match = get_close_matches(w, data.keys(),cutoff=0.8)[0]
        # return
        return {
            'search_word':{'instead': True, 'close_match': close_match}, 'values':data[close_match]
        }
    # Word does not exist, return an custome error messesge
    else:
        return {'search_word': {'unmatched':True},'values':["The word doesn't exist. Please double check it."]}