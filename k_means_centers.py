#!/usr/bin/python3.5
#
# File: k_means_Centers.py
import copy
import math

initial_centers = []
clusters = []
actual_center = []
actual_clusters = []

class k_means_centers:

#------------------------------------------------------------------------------
    #constructor
    #parameters created
    def __init__(self, matrix, numCenters):
        self.__matrix = matrix
        self.__numCenters = numCenters
        initial_centers[:] = []
        clusters[:] = []
        actual_center[:] = []
        actual_clusters[:] = []

#------------------------------------------------------------------------------
    def __findInitialCenters(self, matrix, numC):
        for i in range(0, numC):
            initial_centers.append([])
            initial_centers[i] = matrix[i]
            
#------------------------------------------------------------------------------
    def __distance(self, centerW, centerX, centerY, centerZ, pointW, pointX, pointY, pointZ):

        return math.sqrt(math.pow((centerW - pointW), 2)+ math.pow((centerX - pointX), 2) + \
                math.pow((centerY - pointY), 2) + math.pow((centerZ - pointZ), 2))

#------------------------------------------------------------------------------
    #clustering
    #m is the initial cluster, c is the center point,
    
    def __clustering(self, m, c, clstrs):

        cntM = 0


        for i in range(0,len(c)):
            clstrs.append([])
            clstrs[i] = []

        for row in m:
            cntC = 0
            
            shdi = math.pow(10,10) #shortest difference
            temp_shdi = math.pow(10,10)
            tC = math.pow(10,10)
            tM = math.pow(10,10)
            
            for i in range(0,len(c)):

                temp_shdi = self.__distance(c[cntC][0], c[cntC][1], c[cntC][2], c[cntC][3],
			m[cntM][0], m[cntM][1], m[cntM][2], m[cntM][3])

                if (temp_shdi <= shdi):
                    shdi = temp_shdi
                    tC = cntC
                    tM = cntM

                cntC+=1
            
            clstrs[tC].append(m[tM][:])
            cntM+=1
#------------------------------------------------------------------------------
    def true_center (self, cpOld, clstr):

        temp_cp = []
        
        for i in range(0, len(cpOld)):
            cW = 0
            cX = 0
            cY = 0
            cZ = 0
            for j in range(0, len(clstr[i]) ):
                cW+=clstr[i][j][0]
                cX+=clstr[i][j][1]
                cY+=clstr[i][j][2]
                cZ+=clstr[i][j][3]
            if(len(clstr[i]) != 0):
                cW/=len(clstr[i])
                cX/=len(clstr[i])
                cY/=len(clstr[i])
                cZ/=len(clstr[i])

            actual_center.append([cW,cX,cY,cZ])
            temp_cp.append([cW,cX,cY,cZ])

        return temp_cp

                
#------------------------------------------------------------------------------
    def __print_cluster_by_center(self, cenp, clust):

        for i in range(0, len(cenp)):
            print("Cluster #",i+1)
            print("Center Point: ", cenp[i])
            print("Data Points: ",clust[i])

#------------------------------------------------------------------------------
    def solution(self):
        
        ##this arbitrarily assigns the first n entries as the initial centers (n corresponds to __numCenters)
        self.__findInitialCenters(self.__matrix,self.__numCenters)

        #This contains the initial cluster based on the given center points
        #stored in 'clusters'
        self.__clustering(self.__matrix, initial_centers, clusters)

        #This finds the true center of of each cluster
        #stored in 'actual_center'
        actual_center=self.true_center(initial_centers, clusters)

        #This contains the true clusters based on the true centers
        #stored in 'actual_clusters'
        self.__clustering(self.__matrix, actual_center, actual_clusters)


        #final answer
        cpOLD = []
        count = 0
        while(1):
            t_aclu = actual_clusters
            actual_center=self.true_center(actual_center, t_aclu)
            self.__clustering(self.__matrix, actual_center, actual_clusters)

            if(actual_center==cpOLD):
                break
            cpOLD = actual_center
            
        return actual_center,actual_clusters


#------------------------------------------------------------------------------





                
