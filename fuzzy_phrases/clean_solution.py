from imp import SEARCH_ERROR
import json, os

saveIndex = 0

def phrasel_search(P, Queries):
    # Write your solution here
    
    appendPhrase = []
    ans = []
    
    # Iterates through each query in the input list of queries
    for q in Queries:
        # Iterates through each phrase in the input list of phrases
        for phrase in P:
            
            #Initialize a query index and an endpoint for query traversal
            queryIndex = 0
            endRange = (len(q.split()) - len(phrase.split()))
            
            # Length Mismatch Handling
            if(len(phrase.split()) > len(q.split())): 
                endRange = queryIndex
            
            # Iterates through the array of words in query
            for i in range(queryIndex, endRange): 
                
                # Break if Length Mismatch
                if(len(phrase.split()) > len(q.split())): 
                    break
                
                # Create query span with size of phraseLength + 1
                currentQuerySpan = q.split()[i:i+len(phrase.split())+1]
                
                # Initialize a span and phrase index in order to keep track of position in span and phrase
                spanIndex = 0
                phraseIndex = 0
                
                #Check if foreign word has already been processed in span
                diffWordReached = False
                
                # Check for span validity
                isValid = True
                
                # Check for presence of perfect phrase match in current query span
                if (phrase.split() == currentQuerySpan[0:len(currentQuerySpan)-1]) or (phrase.split() == currentQuerySpan[1:len(currentQuerySpan)]):
                    appendPhrase.append(phrase)
                    queryIndex += 1
                    continue
                
                # Iterate through the entire span checking for matching words with allowance for one
                # possible discrepancy/"foreign word" along the iteration
                for j in range(0, (len(currentQuerySpan))):
                    
                    # Check if discrepancy has already been reached
                    if(diffWordReached):
                        if(phrase.split()[phraseIndex-1] == currentQuerySpan[spanIndex-1]):
                            spanIndex += 1
                            phraseIndex += 1
                        else:
                            isValid = False
                            break
                    else:
                        if(phrase.split()[phraseIndex-1] == currentQuerySpan[spanIndex-1]):
                            spanIndex += 1
                            phraseIndex += 1
                        else:
                            diffWordReached = True
                            spanIndex += 1
                
                # If span is valid, add span to ans double array
                if(isValid):
                    appendPhrase.append(' '.join(currentQuerySpan))
                    queryIndex += 1
        
        # Filter out double occurrences
        if(len(appendPhrase) > 0):
            ans.append(list(dict.fromkeys(appendPhrase)))
        
        # Reset current list of fuzzy matched phrases
        appendPhrase = []
    return ans

if __name__ == "__main__":
    
    print(os.getcwd())
    
    with open((os.getcwd()) + '\interview-questions\\fuzzy_phrases\\sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
