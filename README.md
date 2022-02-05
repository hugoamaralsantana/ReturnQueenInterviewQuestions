## Instructions
- Clone the repository and use it to create a *public* repository in your GitHub account.
- The problem statement is described in the `problem_statement.pdf` file.
- Write the solution into the `fuzzy_phrases/solution.py`. Please do not change the input and output contract of the `def phrasel_search(P, Queries) -> [[string]]` function as the testing of the code correctness will be done programmatically.
- Note - You can only use standard python libraries. ex - json, random, etc

## Solution Documentation
- Solution consisted of creating an iterator over the split query sentence where a check would be performed inside the span to check for similarity between the current phrase and the current ```(phrase length + 1)``` query elements being analyzed. The split array of words would then be put into a holder/placement array where the fuzzy search matches were put back into complete strings and sorted in order to match the solution formatting.
- Development Requirement: I solved this problem on VSCode and Windows 10. I ended up requiring an import of Python's ```os``` library in order to properly access the 20, 30, and 50 point input json files on my personal computer, but it could be just a personal accessing problem on my end.
