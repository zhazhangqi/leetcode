def readingArticles(intellectual, pages, p):
    q = [(pages[i], intellectual[i], i) for i in xrange(len(pages))]
   
    sol = -float('inf')
    while q:
        pg, it, idx = q.pop()
        if pg * 2 <= p:
         sol = max(sol, it)
         for i in xrange(idx+1, len(pages)):
            q.append((pg + pages[i], it + intellectual[i], i))
    return sol 