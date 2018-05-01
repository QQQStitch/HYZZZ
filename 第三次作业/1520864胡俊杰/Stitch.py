def Stitch(n,start,buffer,end):
    if(n==1):
        print("from",start,"move",n,"to",end)
    else:
        Stitch(n-1,start,end,buffer)
        Stitch(1,start,buffer,end)
        Stitch(n-1,buffer,start,end)
