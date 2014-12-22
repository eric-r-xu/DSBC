%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.covariance import EllipticEnvelope
import math

SectionData=pd.read_csv('section_data.csv') # pandas DataFrame
SectionData['X']=None
SectionData['Y']=None
SectionData['newX']=None
SectionData['newY']=None
SectionData['newAngle']=None
SectionData['OUTLIER']=None
SectionData['angle']=None
SectionData['Distance']=None

#parsing X and Y coordinates from center for plotting
for i in range(0,len(SectionData)):
    coordinates=SectionData['center'][i]
    coordinates=coordinates.replace(',','').replace('(','').replace(')','')
    x_coordinate=[]
    y_coordinate = []
    row = coordinates.split()
    x_coordinate.append(row[0])
    y_coordinate.append(row[1])
    x_coordinate=str(x_coordinate)
    y_coordinate=str(y_coordinate)
    x_coordinate=x_coordinate.replace('[','').replace(']','').replace("'",'')
    y_coordinate=y_coordinate.replace('[','').replace(']','').replace("'",'')
    x_coordinate=float(x_coordinate)
    y_coordinate=float(y_coordinate)
    
    
    #centering coordinates
    #approximate center coordinate: 272, 190
    SectionData['X'][i]=x_coordinate-272
    SectionData['Y'][i]=y_coordinate-190
    
    #collapsing points to one quadrant (90-180 deg.)
    if SectionData['X'][i]<0:
        SectionData['newX'][i]=abs(SectionData['X'][i])
        SectionData['newY'][i]=abs(SectionData['Y'][i])
        if ((SectionData['Y'][i])*-1)<0:
            SectionData['newAngle'][i]=180-SectionData['gradient_angle'][i]
        else:
            SectionData['newAngle'][i]=SectionData['gradient_angle'][i]
    else:
        SectionData['newX'][i]=SectionData['X'][i]
        if (SectionData['Y'][i])<0:
            SectionData['newY'][i]=abs(SectionData['Y'][i])
            SectionData['newAngle'][i]=180-SectionData['gradient_angle'][i]
        else:
            SectionData['newY'][i]=SectionData['Y'][i]
            SectionData['newAngle'][i]=SectionData['gradient_angle'][i]
            
#changing 0's to 180's, add Distance via Pythagorean Theorem
for i in range(0,len(SectionData)):
    if SectionData['newAngle'][i]==0:
        SectionData['angle'][i]=180
    else:
        SectionData['angle'][i]=SectionData['newAngle'][i]
    x=SectionData['newX'][i]
    y=SectionData['newY'][i]
    SectionData['Distance'][i]=math.sqrt((x*x)+(y*y))
        



#fit the outlier detector to the data and predict
X=SectionData[['angle','newX','newY']]
outlier_detector = EllipticEnvelope(contamination=0.14).fit(X.values)
outliers = outlier_detector.predict(X.values)

#finds outliers
for i in range(0,len(outliers)):
    SectionData['OUTLIER'][i]=outliers[i]
    if outliers[i]==-1:
        print 'outlier at: ',SectionData['center'][i]
        
        
fig = plt.figure(figsize=(20,20))
#plotting the section map 
#outliers indicated on map with larger circles
for i in range(0,len(SectionData)):
    if SectionData['OUTLIER'][i]==-1:
        plt.scatter(SectionData['X'][i],SectionData['Y'][i],s=40)
        plt.annotate(str(int(round(SectionData['gradient_angle'][i],0))),(SectionData['X'][i],SectionData['Y'][i]+5))
    else:
        plt.scatter(SectionData['X'][i],SectionData['Y'][i],s=10)
plt.title('Section Map with gradient angle sections')
plt.axis([-260, 260, -240, 240])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
