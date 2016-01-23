directions = ['north', 'south', 'east', 'west']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of']
nouns = ['bear', 'princess']

def scan(words):
    words = words.split()
    result = [ ]
    
    for i in words:
            if i in directions:
                result.append(('direction', i))
             
            elif i in verbs:
                result.append(('verb', i))
            
            elif i in stops:
                result.append(('stop', i))
        
            elif i in nouns:
                result.append(('noun', i))
        
            elif i.isdigit():
                result.append(('number', convert_number(i)))
            else:
                result.append(('error', i))
            
    return result
    
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
        
print scan('north')
