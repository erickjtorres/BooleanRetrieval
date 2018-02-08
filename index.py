#Python 2.7.3
import re
import os
import collections
import time



class index:

    def __init__(self,path):
        self.path = path
        self.list_of_files = os.listdir(path)
        self.index = self.build_index()


    def build_index(self):
        start_time = time.time()
        # create the index
        index = {}
        # create an id to keep track of the list
        id = 0
        # create a place to keep track of the location of the file
        position = 0
        # we want to get the name of each file in an array
        list_of_files = self.list_of_files

        # loop through the list_of_files
        for file in list_of_files:
            # open the file at the location
            f = open(self.path + file, "r")

            # turn the file opened into a string and lower case everything
            stringify = f.read()
            stringify = stringify.lower()

            # use regular expression to only get words
            arrayOfWords = re.split('[0-9\W]', stringify)

            # removing repeated words -> does not take into account uppercase vs lowercase
            arrayOfWords = list(set(arrayOfWords))

            # remove any words that are less than or equal to one -> single letters should be removed
            # we can also use this to remove stop words
            for i in arrayOfWords:
                if len(i) <= 1:
                    arrayOfWords.remove(i)

            # go through every term in the array
            for term in arrayOfWords:
                # find every position of the term in the document by
                position = [m.start() for m in re.finditer(term, stringify)]
                # if the term is not already in the index add it and add an ID
                if term not in index:
                    index[term] = [('ID' + str(id), position)]
                # if the term is in the index and the IDNumber is not associated with the index then append the ID
                elif ('ID' + str(id)) not in index[term]:
                    index[term].append(('ID' + str(id), position))
            id += 1
        end_time = time.time() - start_time
        print("Index built in" + ' ' + str(end_time))
        return index



        # function to read documents from collection, tokenize and build the index with tokens
# use unique document IDs

    def and_query(self, query_terms):
        #starting timer
        start_time = time.time()
        #getting the index
        index = self.index
        #creating posting array to hold all ID
        postings = []
        #append the document id to the posting list
        postings.append([docs[0] for term in query_terms for docs in index[term]])
        #count the times each ID is shown
        counter = collections.Counter(postings[0])
        #if the ID is seen the same number of times as the len of the query_terms then its a match
        same_docs = [k for k, v in counter.iteritems() if v == len(query_terms)]
        #end the clock we found the documents!
        end_time = time.time() - start_time
        print('Total docs retrieved' + ':' + str(len(same_docs)))
        for i in same_docs:
            print(i)
        print('Retrieved in' + ' ' + str(end_time))







    # function for identifying relevant docs using the index


    def print_dict(self):
        print(self.index)
# function to print the terms and posting list in the index

    def print_doc_list(self):
        id = 0
        for doc in self.list_of_files:
            print('Doc' + str(id) + '==>' + doc)
            id += 1

# function to print the documents and their document id

a = index('collection/')
# x = a.and_query(['me'])
a.print_dict()
# a.print_doc_list()
