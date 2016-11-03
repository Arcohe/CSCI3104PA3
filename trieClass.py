#LastName:  Trieu
#FirstName: Thomas
#Email:     thomas.trieu@colorado.edu
#Comments:  CSCI-3104 Fall 2016

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        if (w == ''):
            self.isWordEnd = True
            self.count += 1
            return
        if (w[0] not in self.next):
            self.next[w[0]] = MyTrieNode(False)
        self.next[w[0]].addWord(w[1:])

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        
        # If not on last node, call lookupWord on next node with w[1:].
        if (len(w) > 0):
            # Checks if self.next contains next prefix.
            if (self.next.get(w[0], False)):
                return self.next[w[0]].lookupWord(w[1:])
            else:
                return 0
        else:
            return self.count
    

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
        
        # Grossly unoptimized, but oh well.

        if (len(w) > 0):
            if (w[0] not in self.next):
                return []
            Lst = self.next[w[0]].autoComplete(w[1:])
            if (not Lst):
                return []
            for n in range(len(Lst)):
                Lst[n] = (w[0] + Lst[n][0], Lst[n][1])
            return Lst
        elif (not self.next):
            return [('', self.count)]
        else:
            wordLst = []
            if (self.isWordEnd):
                wordLst.append(('', self.count))
            for key in self.next:
                tempLst = self.next[key].autoComplete(w[1:])
                # Prepends key to self.next to appropriate children words.
                for i in range(len(tempLst)):
                    tempLst[i] = (key + tempLst[i][0], tempLst[i][1])
                wordLst = wordLst + tempLst
            return wordLst
            
        #return [('Walter',1),('Mitty',2),('Went',3),('To',4),('Greenland',2)] #TODO: change this line, please
    
    
            

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     
