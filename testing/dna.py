#Filename: dna.py

def dna_starts_with(dna_string,fragment):
    # Thanks go out to Tom Couch!
    
    valid_characters = ['a','c','g','t']
    wrong_character_found = False
    for character in fragment.lower():
        #Write code to check characters in fragment against valid characters
        assert character in valid_characters            
            
    
    dna_string = dna_string.lower()
    fragment = fragment.lower()
    
    match = True
    for i,j in enumerate(fragment):
        if fragment[i] != dna_string[i]:
            match = False
    return match