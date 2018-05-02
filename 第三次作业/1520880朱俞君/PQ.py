def     PQ(n,start,buffer,end):

    if(n==1):

        print("from",start,"move",n,"to",end)

    else:

        PQ(n-1,start,end,buffer)

        PQ(1,start,buffer,end)

        PQ(n-1,buffer,start,end)
