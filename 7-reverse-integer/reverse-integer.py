class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=str(x)
        b=0
        if a[0]!="-":
            a=a[::-1]
            b=int(a)
            
        else:
            s=a[1:]
            s=s[::-1]
            b=int(s)
            b=-b
        if b<-2147483648 or b>2147483647:
            return 0
        return b
        