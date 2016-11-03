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

    # Adds words to trie through recursion. Method 'consumes' the first letter of the
    # input string; creates a key/node pair, if not already present in current node's
    # dict; sets flag and increments count, if entire word is added.
    def addWord(self,w):
        if (w == ''):
            self.isWordEnd = True
            self.count += 1
            return
        if (w[0] not in self.next):
            self.next[w[0]] = MyTrieNode(False)
        self.next[w[0]].addWord(w[1:])


    # Uses recursion, though not necessary for implementation, and likely not optimal.
    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        if (len(w) > 0):
            if (self.next.get(w[0], False)):
                return self.next[w[0]].lookupWord(w[1:])
            else:
                return 0
        else:
            return self.count
    
    
    # 
    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        # Implemented as recursive function with three cases:
        #   1.  Word passed in the initial call is not yet 'consumed', prompting
        #       search for next key:node pair
        #           a.  If next key:node pair doesn't exist, returns empty list
        #   2.  The node is a 'leaf' (i.e. has empty dict), signaling the end
        #       of descent and the return of a tuple with node's count.
        #   3.  The node is in set of potential suffixes.
        #           a.  'Collects' results of recursive calls on children
        #           b.  Returns results, prepended by own tuple if is word end
        # 'Building' of the strings in each tuple is handled on the ascent. That is,
        # after the results of a call are received, each tuple's string is prepended
        # by the appropriate key. This is handled in cases 1 and 3: case 1 prepends
        # all results with the same key, or letter; case 2 prepends results based on
        # which key:node pair they returned from.
        # This method reads and replaces tuples at most c*n times, where n is the number
        # of elements in the final return list and where c is the length of the longest
        # valid autocomplete word. A different approach may have been taken if a helper
        # function (maybe to keep track of current prefix) were implemented.
        # 
        # In retrospect, it may have been more efficient to return lists sans tuples
        # and 'tuplify' once recursion was finished, to avoid reading and changing tuples
        # repeatedly.
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
                tempLst = self.next[key].autoComplete(w[1:])    # w[1:] where w is '' still yields ''
                for i in range(len(tempLst)):
                    tempLst[i] = (key + tempLst[i][0], tempLst[i][1])
                wordLst = wordLst + tempLst
            return wordLst
            

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
 
    
    
     
