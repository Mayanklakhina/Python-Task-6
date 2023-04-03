# Here is a small program that will be containing three parameters included in dumps function.

import json

dicti = {(1, 2, 3) : 'Mayank', 2 : 'good', 3 : 'to', 4:'see',5:'you', 6 : float('nan')}

json_string = json.dumps(dicti,
                         skipkeys = True, #automatically skip the keys that are not of basic type.
                         allow_nan = True, #If allow_nan is True, their JavaScript equivalents (NaN, Infinity, -Infinity) will be used. 
                         indent = 5,       #if indent parameter is a integer(non-negative ) or string, then JSON object members will be printed in a more readable manner.
                         separators =(". ", " = ")) # If specified, separators should be
                                                    # an (item_separator, key_separator)tuple
                                                    # Items are separated by '.' and key,
                                                    # values are separated by '=' 
 
print('Equivalent json string of dictionary:',
      json_string)