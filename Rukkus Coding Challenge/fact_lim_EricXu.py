def fact_lim(n, lim):
    if (lim<1 or n<1) or (lim>n) or ((n%1)!=0 or (lim%1)!=0):
        print 'error: parameters invalid'
        print 'parameters must be integers greater than 1'
        print 'first parameter >= second parameter'
    else:
        result=0
        for i in range(0,n):
            addResult=1
            for k in range((n-i+1)-lim,n-i+1):
                if k<1:
                    k=1
                addResult=addResult*k
            result=result+addResult
        return result
