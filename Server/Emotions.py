class Emotions:
    def __init__(self):
        self.average=[]
        self.avg_dif=[]
        self.container=[]
        self.cont=0
    def process_data(self,lista):
        if len(self.average)==0:
            self.average=lista
            for index in range(6):
                self.avg_dif.append(0)
        else:
            self.cont+=1
            self.container=[]
            #print(lista)
            for index in range(len(self.average)):
                self.average[index]=self.average[index]*0.8+((0.2)*lista[index])
                self.avg_dif[index]=self.avg_dif[index]*0.8+((0.2)*(abs(self.average[index]-lista[index])))
                dif=self.average[index]-lista[index]
                if abs(dif)>2.5*abs(self.avg_dif[index]):
                    self.container.append((index,dif,2**index))
                    #print(index,lista[index],abs(dif),self.average[index],2.7*abs(self.avg_dif[index]))
            if len(self.container)!=0 and self.cont>20:
                return self.analyze_anomalies()
            
    def analyze_anomalies(self):
        #self.container=sorted(self.container,key=lambda x:x[0])
        #print(self.container)
        lista=[]
        for elem in self.container:
            if elem[0]==0:
                lista.append("Left mouth corner")
            if elem[0]==1:    
                lista.append("Right mouth corner")
            if elem[0]==2:    
                lista.append("Left eyebrow")
            if elem[0]==3:    
                lista.append("Right eyebrow")
            if elem[0]==4:
                if elem[1]>0:
                    lista.append("Left eye open")
                else:
                    lista.append("Left eye close")
            if elem[0]==5:    
                if elem[1]>0:
                    lista.append("Right eye open")
                else:
                    lista.append("Right eye close")
        #print(lista)
        return lista