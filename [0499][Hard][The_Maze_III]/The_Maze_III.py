# -*- coding: utf-8 -*-  
# leetcode time     cost : time exceeded
# leetcode memory   cost : time exceeded
# solution 1, BFS
import collections
class Solution:
    def findShortestWay(self, maze: [[int]], ball: [int], hole: [int]) -> str:   
        m = len(maze)
        n = len(maze[0])
        queue = collections.deque()
        stepPathDict = {}
        directions = [(-1,0,'u'),(0,1,'r'),(0,-1,'l'),(1,0,'d')]  
        def isValid(x,y,maze):
            if 0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y]== 0:
                return True
            else:
                return False    
        def BFS(maze,ball,hole):
            path = ""
            step = 0
            minStep = float('inf') 
            queue.append([ball[0],ball[1],step,path]) 
  
            while queue:
                x,y,step,path = queue.popleft()
                print("poped out: [",x,",",y,",",step,",",path,"]",",after poped,queue:",queue)

                # due to need lexicographically smallest way, start with the order d,l,r,u,
                # make the high priority direction update the stepPathDict last, using last win.
                temStep = step
                for i in range(x-1,-2,-1):                    
                    if i == hole[0] and y == hole[1]:
                        temStep += 1
                        stepPathDict[temStep] = path+"r"
                        minStep = min(minStep,temStep)
                        print("hole is reached, step and solution is ",stepPathDict)
                        break
                                             
                    if isValid(i,y,maze):
                        temStep += 1  
                    elif not isValid(i,y,maze) and i<x-1:
                        queue.append([i+1,y,temStep,path+"u"])                        
                        break
                    else: 
                        break

                temStep = step
                for i in range(y+1,n):                    
                    if x == hole[0] and i == hole[1]:
                        temStep += 1
                        stepPathDict[temStep] = path+"r"
                        minStep = min(minStep,temStep)
                        print("hole is reached, step and solution is ",stepPathDict)
                        break
                                            
                    if isValid(x,i,maze):
                        temStep += 1   
                    elif not isValid(x,i,maze) and i>y+1:
                        queue.append([x,i-1,temStep,path+"r"])                        
                        break
                    else: 
                        break

                temStep = step
                for i in range(y-1,-2,-1):                  
                    if x == hole[0] and i == hole[1]:
                        temStep += 1
                        stepPathDict[temStep] = path+"l"
                        minStep = min(minStep,temStep)
                        print("hole is reached, step and solution is ",stepPathDict)
                        break
                                             
                    if isValid(x,i,maze):
                        temStep += 1 
                    elif not isValid(x,i,maze) and i<y-1:
                        queue.append([x,i+1,temStep,path+"l"])
                        break
                    else: 
                        break

                temStep = step
                for i in range(x+1,m):
                    if i == hole[0] and y == hole[1]:
                        temStep += 1                        
                        stepPathDict[temStep] = path+"d"
                        minStep = min(minStep,temStep)
                        print("hole is reached, step and solution is ",stepPathDict)
                        break
                                           
                    if isValid(i,y,maze):
                        temStep += 1  
                    elif not isValid(i,y,maze) and i>x+1:
                        queue.append([i-1,y,temStep,path+"d"])
                        break
                    else: 
                        break     

                #print("current layer is finished,step is ",step)
            stepPathDict[0] = "impossible"
            return minStep 

        minStep = BFS(maze,ball,hole)

        # check whether stepPathDict.keys() has elements except 0
        return stepPathDict[minStep] if  len(stepPathDict.keys())>1 else "impossible"

