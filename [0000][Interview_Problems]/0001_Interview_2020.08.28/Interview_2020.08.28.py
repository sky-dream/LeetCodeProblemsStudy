'''
Input is a text file. Example of the content in the file:
CompA:CompB,CompC
CompB:CompD

External API: void StartInstallation(string compName)
Note that this API returns immediately when the installation starts, it won't wait for the completion.
'''
# New API needed:IsCompInstalled(string compName)---> return Bool
#                ReadInputFile(FilePath)---> return string

from collections import defaultdict
from collections import deque
import  time
class solution():
    def __init__(self):
        super().__init__()
        self.sorted_comp_list = []
        self.comp_dict = defaultdict(list)
        
    def ReadInputFile(self,inputFile):
        # read infomation from txt into memory
        input_str = "CompA:CompB,CompC\nCompB:CompD\n" # input string in txt also need to be verified
        return input_str
    
    def DecodeInputStr(self,s):
        s_list = s.split('\n')
        #self.comp_dict = defaultdict(list)
        comp_set = set()
        for s in s_list:
            n = len(s)
            key = ''
            i = 0
            while i<n:
                if s[i]!=':':
                    i+=1
                else:
                    key = s[:i]
                    break
            if key not in comp_set:
                comp_set.add(key)
            base_comps = s[i+1:].splist(',')
            self.comp_dict[key] = base_comps
            for comp in base_comps:
                if comp not in comp_set:
                    comp_set.add(comp)
        for comp in comp_set:
            if comp not in comp_set:
                self.comp_dict[comp] = []
        return self.comp_dict
    
    def calcPriority(self,comp_dict): # toplogical sort
        #sorted_comp_list = []
        q = deque()
        for key,base_comps in comp_dict:
            if base_comps==[]:
               self.sorted_comp_list.append(key) 
            else:
                q.append(key)
        while q:
            comp = q.popleft()
            if self.dependecyCheckOK(comp_dict[comp],sorted_comp_list):
               self.sorted_comp_list.append(comp)
            else:
               q.append(comp)      
                
            
    def dependecyCheckOK(self,base_comps,sorted_comp_list):
        for comp in base_comps:
            if comp not in sorted_comp_list:
                return False
        return True   
    def IsBasedCompInstalled(self,comp):
        for basicComp in  self.comp_dict[comp]:
             if  not IsCompInstalled(basicComp):
                 return False
        return True
          
    def IsCompInstalled(self,compName):
        pass
    
    def StartInstallation(self,compName):
        pass
    
    def installComp(self):
        for comp in self.sorted_comp_list:
            while not self.IsBasedCompInstalled:
                 time.sleep(1)
            self.StartInstallation(comp)
               

                
            

        
                
            
        
                
        
                
                
