class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        neg=1
        Ntime=3
        count=[0]*32
        NoOfNeg=0
        for i in xrange(len(A)):
            t=A[i]
            j=0
            if t<0:
                NoOfNeg=NoOfNeg+1
                t=t*-1
            while(t!=0 and j<len(count)):
                if(t&1==1):
                    count[j]+=1
                j=j+1
                t=t>>1
        if NoOfNeg%Ntime!=0:
            neg=neg*-1
        for i in xrange(len(count)):
            count[i]=count[i]%Ntime
        #print count
        count="".join(map(str,reversed(count)))
        result=int(count,2)*neg
        return result