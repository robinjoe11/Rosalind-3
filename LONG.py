import sys
import os
sys.path.append(os.getcwd()+'/../')


scratch_handle = open('rosalind_long.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

def combine_strings(superstring, string):
    i = len(string)
    while i > 0:
        
        if string[:i] == superstring[-i:]:
            return superstring + string[i:]
        
        if string[-i:] == superstring[:i]:
            return string[:-i] + superstring
        i -= 1
    return False

def get_shortest_superstring(dataset):
    data = Fasta(dataset).data.values()
    superstring = data.pop()
    while len(data) > 0:
        min_superstring = ''
        min_superstring_index = -1
        i = 0
        while i < len(data):
            new_superstring = combine_strings(superstring, data[i])

            if new_superstring == False:
                i += 1
                continue
            if len(new_superstring) < len(min_superstring) or len(min_superstring) == 0:
                min_superstring = new_superstring
                min_superstring_index = i
            i += 1
        if min_superstring_index != '':
            superstring = min_superstring

            data.pop(min_superstring_index)
        else:
            print ("Can't finish superstring")
    return superstring

superstring = get_shortest_superstring(dataset)
print (superstring)