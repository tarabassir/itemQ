#!/usr/bin/python3
import numpy as np
import math
from numpy.linalg import inv
import k_means_Centers
import random

class RBFN:
#------------------------------------------------------------------------------
    # Constructor
    def __init__(self,inputs,center_num,neighboring_center_num):
        self.__inputs = inputs
        self.__train_inputs=[]
        self.__train_outputs = []
        self.output=[]
        self.__weights_hidden_to_output=[]
        self.__hidden_layer = []
        self.__hidden_layer_predict = []
        self.__center_num=center_num
        self.neighboring_center_num=neighboring_center_num
        

#------------------------------------------------------------------------------
    """find all the clusters and center points and store them"""
    def find_centers(self,x):
        #use K-means to find centers and store it in nxk matrix
        #where n is number of input nodes and k is number of centers
        k_means_object_1 = k_means_Centers.k_means_Centers(x, self.__center_num)
        self.__centers,self.__clusters=k_means_object_1.solution()
        
        
#------------------------------------------------------------------------------
    """given an input return the corresponding center"""
    def find_c(self,x):
        for i in range(len(self.__centers)):
            for j in range(len(self.__clusters[i])):
                if (self.__clusters[i][j]==x):
                    return self.__centers[i]

#------------------------------------------------------------------------------        
    def center_exist(self,x):
        i=False
        for i in range(len(self.__centers)):
            for j in range(len(self.__clusters[i])):
                if (self.__clusters[i][j]==x):
                    i=True
                    break
        return i
                
#------------------------------------------------------------------------------
    def find_closest_c(self,x):
        a=[]
        b=[]
        
        #calculate distance between input to all centers
        for i in range(len(self.__centers)):
            a.append(np.sum( ( np.asarray(x) - np.asarray(self.__centers[i]) )**2 ) )
        a.sort()
        return a[0]
    
#------------------------------------------------------------------------------    
    """find r which is root mean square distance between current cluster
       center and k number of neighboring cluster centers."""
    def find_r(self,c):
        a=[]
        #calculate distance between current center to all centers
        for i in range(len(self.__centers)):
            a.append(np.sum( ( np.asarray(c) - np.asarray(self.__centers[i]) )**2 ) )
        a.sort()
        b=[]
        for j in range(self.neighboring_center_num):
            b.append(a[j+1]) #a[0] is distance of current center to itself so start with a[1]
        r=math.sqrt((sum(b)**2)/self.neighboring_center_num)
        
        a.clear()
        b.clear()
        return r
            

#------------------------------------------------------------------------------ 
    """radial basis function
     x is one input
     c is the center for that input
     x and c are vectors"""
    def RBF(self,x,c):
        a= np.sum( (np.asarray(x) - np.asarray(c)) **2)
        c_current=self.find_c(x)
        b=self.find_r(c_current)
        return (math.exp(-1 * a /( b**2 ) ))

    def RBF_predict(self,x,c):
        a= np.sum( (np.asarray(x) - np.asarray(c)) **2)
        c_current=self.find_closest_c(x)
        b=self.find_r(c_current)
        return (math.exp(-1 * a /( b**2 ) ))
       
        
#------------------------------------------------------------------------------
    def calculate_hidden_layer(self,in1):
        # N by K matrix
        # N is number of inputs and k is number of centers (# of hidden layer)
        temp_hidden=[]
        self.__hidden_layer.clear()
        for i in range(len(in1)):
            for j in range(len(self.__centers)):
            # c is center for the input
                a=self.RBF(in1[i],self.__centers[j])
                temp_hidden.append(a)
            self.__hidden_layer.append([n for n in temp_hidden])
            temp_hidden.clear()
#------------------------------------------------------------------------------

    def calculate_hidden_layer_predict(self,in1):
        # N by K matrix
        # N is number of inputs and k is number of centers (# of hidden layer)
        temp_hidden=[]
        self.__hidden_layer_predict.clear()
        for i in range(len(in1)):
            for j in range(len(self.__centers)):
            # c is center for the input
                a=self.RBF_predict(in1[i],self.__centers[j])
                temp_hidden.append(a)
            self.__hidden_layer_predict.append([n for n in temp_hidden])
            temp_hidden.clear()
#------------------------------------------------------------------------------
            
    def predict(self):
        self.calculate_hidden_layer_predict(self.__inputs)
        H=np.asarray(self.__hidden_layer_predict)
        W_np=np.asarray(self.__weights_hidden_to_output)
        y=np.dot(H,W_np)
        round_output=np.rint(y)
        print("output")
        self.__predicted_output=round_output.tolist()
        for i in range (0, len(self.__predicted_output)):
            if (self.__predicted_output[i][0] < 1):
                self.__predicted_output[i][0] = 1

        print(self.__predicted_output)
        
#------------------------------------------------------------------------------

    """Calculates hidden to output wieghts using matrix operations"""
    def cal_wieghts(self):
        H_np=np.asarray(self.__hidden_layer)
        H_tanspose=np.transpose(H_np)
        Y=np.asarray(self.__train_outputs)
        mul=np.dot(H_tanspose,H_np)
        Inv=inv(mul)
        a=np.dot(Inv,H_tanspose)
        b=np.dot(a,Y)
        self.__weights_hidden_to_output=b.tolist()
        print("predicted output")
        round_num=np.rint(np.dot(H_np,b))
        round_num=round_num.tolist()
        for i in range (0, len(round_num)):
            if (round_num[i][0] < 1):
                round_num[i][0] = 1
        print(round_num)
      
#------------------------------------------------------------------------------        

    def train(self):       
        NUMBER_OF_DATAPOINTS = 200
        for i in range(0, 4):
            for j in range(0, NUMBER_OF_DATAPOINTS):
                consumers = random.randint(1, 7)
                date = random.randint(1, 366)
                amount = random.randint(1, 3)
    
                if i == 0:
                    if date in range(1, 101) or range(300, 366):
                        temp = random.randint(5, 11)
                        time = temp / (consumers / amount)
                    else:
                        temp = random.randint(7, 15)
                        time = temp / (consumers / amount)
                elif i == 1:
                    if date in range(1, 101) or range(300, 366):
                        temp = random.randint(2, 5)
                        time = temp / (consumers / amount)
                    else:
                        temp = random.randint(5, 9)
                        time = temp / (consumers / amount)
                elif i == 2:
                    if date in range(1, 101) or range(300, 366):
                        temp = random.randint(5, 11)
                        time = temp / (consumers / amount)
                    else:
                        temp = random.randint(2, 5)
                        time = temp / (consumers / amount)
                elif i == 3:
                    if date in range(1, 101) or range(300, 366):
                        temp = random.randint(3, 11)
                        time = temp / (consumers / amount)
                    else:
                        temp = random.randint(5, 15)
                        time = temp / (consumers / amount)
                
                self.__train_inputs.append([i, amount, consumers, date])
                self.__train_outputs.append([time])
        print("target output")
        print(self.__train_outputs)
        rfn_instance.find_centers(self.__train_inputs)
        rfn_instance.calculate_hidden_layer(self.__train_inputs)
        rfn_instance.cal_wieghts()



#------------------------------------------------------------------------------    
        
if __name__ == "__main__":
    
    inputs=[[0,1,2,50]]
    rfn_instance = RBFN(inputs,195,2)
    rfn_instance.train()
    rfn_instance.predict()
