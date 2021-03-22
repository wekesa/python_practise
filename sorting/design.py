"""

- Designing a Google search type head suggestion

Requirements:
 - A lot of data being pulled constantly
 - Need speed and a lot of data happening at the same time
 - Techniques to deal with this problem
 -

 Requirements:
 - Functional Requirements:
    - suggestions for top 5 search suggestions
    - How many phrases to be shown
    -
 - Non Functional Requirements:
    - Highly available (< 200ms)
    - Can lag in the most updated information (Compromise)

Capacity Estimation:
- Assumptions:
  - 500 b daily searches - 60K per second
  - 20% duplicates
  - 100 million uniquie terms
- Capacity calculations
  - average word has 5 characters = 15 characters
  - average query has 3 words
  - 100 * 2bytes per character * 15 characters = 3GB
  - 1 year storage 3GB (300%) ~ 21GB

APIs:
- Get Search API:
GET https://www.myservice.com/customsearch/v1
   Response of
{
   "kind" : "customerSearch",
   "url" : " ",
   "queries" : " "
}

   Trie Data structure: Is used to search in a big text

Basic Design:


Advanced design:


Further enhancements
"""