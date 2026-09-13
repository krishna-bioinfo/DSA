class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        count=0
        shortest= min(strs, key=len)
        maincount= len(shortest)
            
        for i in range(0,len(strs)):
            for j in range(0,len(shortest)):
               if(shortest[j])!= (strs[i][j]):
                  break
               else:
                    count+=1
  
            if count<maincount:
                maincount=count
            count=0
        
        for i in range(0,maincount):
            s=s+shortest[i]
        if len(strs)>1:
            return s
        else:
            return strs[0]
                 
            


            


        