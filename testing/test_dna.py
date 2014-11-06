#Filename: test_dna.py

def test_dna_starts_with_simple():
    from dna import dna_starts_with
    
    assert dna_starts_with('actttgcacgt','a') == True

def test_dna_starts_with_systematic():
    from dna import dna_starts_with
    
    #sequence    prefix   expected
    Tests = [
    ['act',       'a',     True],  # Test 0
    ['act',       't',     False], # Test 1
    ['act',      'at',     False], # Test 2
    ['act',      'AC',     True],  # Test 3
    ]
     
    #Run and report
    passes = 0
    for (i, (seq, prefix, expected)) in enumerate(Tests):
        if dna_starts_with(seq, prefix) == expected:
            passes += 1
        else:
            print 'test %d failed' % i
    print '%d/%d tests passed' % (passes, len(Tests))
    assert passes == len(Tests)

def test_incorrect_input():
    from dna import dna_starts_with
    try:
        dna_starts_with('actttgcacgt','h')      
    except Exception, error:
        pass        
    else:
        assert False
        
    try:
        dna_starts_with('actttgcacgt','a')      
    except Exception, error:
        assert False       
    else:
        pass
