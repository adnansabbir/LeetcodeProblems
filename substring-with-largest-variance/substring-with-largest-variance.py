class Solution:
    def largestVariance(self, s: str) -> int:
        res=0
        Combinations=[]
        Unique=[]
        for i in s:
            if i not in Unique:
                Unique.append(i)
        for i in range(len(Unique)):
            for j in range(i+1,len(Unique)):
                Combinations.append([Unique[i],Unique[j]])
                Combinations.append([Unique[j],Unique[i]])
        #Till now we have just found all the possible pair of two chars.
        for i in range(len(Combinations)):
            first=Combinations[i][0]
            second=Combinations[i][1]
            currSum=0
            ans=0
            start=0
            isSecond=0
            for j in range(len(s)):
                if s[j]!=first and s[j]!=second:
                    start+=1
                    continue
                if s[j]==first:
                    currSum+=1
                elif s[j]==second:
                    isSecond+=1
                    currSum-=1
                if currSum>ans and isSecond>0:
                    ans=max(currSum,ans)
                else:
                    ans=max(currSum-1,ans)
                while currSum<0 and start<=j:
                    if s[start]==first:
                        currSum-=1
                    elif s[start]==second:
                        currSum+=1
                        isSecond-=1
                    start+=1
            res=max(res,ans)

        return res