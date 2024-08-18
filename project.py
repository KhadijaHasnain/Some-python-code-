def create_partial_matching(id):
    Nmin,Nmax=1300,1500; global seed; seed=id
    def randint(a,b): global seed; seed=(48271*seed)%(2**31-1); return a+seed%(b-a)
    n=randint(Nmin,Nmax+1); pi=[]; [pi.insert(randint(0,i+1),i) for i in range(2*n)]; m=[sorted(_) for _ in zip(pi[::2],pi[1::2])]; m[randint(0,n)]=["*","*"]
    for _ in range(8): m[randint(0,n)][randint(0,2)]="*"
    return [tuple(pair) for pair in m]