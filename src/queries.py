def get_repos(cursor):
    query = """query($first: Int!, $query: String!, $type: SearchType!, $after: String)
    {search(first:$first ,query:$query, type:$type, after:$after){
                edges {
                  node {
                    ... on Repository {
                    
                      owner{
                        login
                      }
                      
                      name
                      
                      stargazers {
                        totalCount
                      }
                      
                      forkCount
                      
                      defaultBranchRef{
                        target{
                          ... on Commit{
                            history(first:0){
                              totalCount
                              edges{
                                node{
                                  ... on Commit{
                                    committedDate
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                      
                      pullRequests(states: OPEN){
                        totalCount
                      }
                    }
                  }
                }
                pageInfo{
                    hasPreviousPage
                    startCursor
                    hasNextPage
                    endCursor
                }
              }
            }"""

    if cursor is None:
        variables = """{
                  "first": 50,
                  "query": "language:javascript stars:>1600",
                  "type": "REPOSITORY",
                  "after": null
                }"""
    else:
        variables = """{
                  "first": 50,
                  "query": "language:javascript stars:>1600",
                  "type": "REPOSITORY",
                  "after": "%s"
                }""" % cursor

    return query, variables


def rate_limit():
    query = """
{
  viewer {
    login
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""
    return query


