class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min=999
        for i in strs:
            if (len(i)<min):
                min=len(i)
        c=0
        b=""
        if min>0:
            for i in range(min):
                a=strs[0][i]
                for j in strs:
                    if j[i]!=a:
                        c+=1
                if c==0:
                    b+=a
                else:
                    break
        return b

        