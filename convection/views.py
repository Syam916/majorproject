from socket import IP_HDRINCL
from django.shortcuts import render
from django.contrib import messages
#import sklearn
import joblib


from joblib import load
data1=load('./MLMODEL/model1.joblib') # model for theoritical data
data2=load('./MLMODEL/model2.joblib') # model for experimental  data
viscosity=load('./MLMODEL/model3.joblib')
prantal_number=load('./MLMODEL/model4.joblib')
thermal_conductivity=load('./MLMODEL/model5.joblib')




from convection.models import  NaturalConvection

# Create your views here.

def temp(request):
    return render(request,'temp.html')
def home(request):
    return render(request,'index.html')

def result(request):
    voltage=float(request.POST['Voltage'])
    current=float(request.POST['Current'])
    temp2=float(request.POST['temp2'])
    temp3=float(request.POST['temp3'])
    temp4=float(request.POST['temp4'])
    temp5=float(request.POST['temp5'])
    temp6=float(request.POST['temp6'])
    temp7=float(request.POST['temp7'])
    room_temp=float(request.POST['temp8'])
    power=voltage*current

    y_pred1=data1.predict([[voltage,current,temp2,temp3,temp4,temp5,temp6,temp7]])
    y_pred2=data2.predict([[voltage,current,temp2,temp3,temp4,temp5,temp6,temp7,room_temp]])

    y_pred1=y_pred1[0]
    y_pred2=y_pred2[0]
    print(y_pred1,y_pred2)
    power=round(power,2)
    y_pred1=round(y_pred1,4)
    y_pred2=round(y_pred2,4)


    # formula calculation part for heat transfer coeffcients 

    power=voltage*current

    avg_temp=(temp2+temp3+temp4+temp5+temp6)/5
    #print(avg_temp)



    # theoritical heat transfer coefficient

    THTC=power/(0.059*(avg_temp-temp7))
    THTC=round(THTC,4)


    #mean temperatrure

    T_mean=(avg_temp+room_temp)/2
    #print(T_mean)


    new=viscosity.predict([[T_mean]])
    prantal=prantal_number.predict([[T_mean]])
    k=thermal_conductivity.predict([[T_mean]])
    '''print(new)
    print(prantal)
    print(k)'''

    beeta=(273+T_mean)
    GR=(9.81*(0.5**3)*(1/beeta)*(avg_temp-T_mean))/(new**2)
    #print("gr is :",GR)

    # experimental heat transfer coefficient 


    valu=0.59*(((GR*10**-2)*prantal)**0.25)
    #print(valu)
    EHTC= (k*valu)/0.5
    EHTC=round(EHTC[0],4)

    print(EHTC,THTC)


    context={
        'voltage':voltage,
        'current':current,
        'power':power,
        'temp2':temp2,
        'temp3':temp3,
        'temp4':temp4,
        'temp5':temp5,
        'temp6':temp6,
        'temp7':temp7,
        'y_pred1':y_pred1,
        'y_pred2':y_pred2,
        'thtc':THTC,
        'ehtc':EHTC


}
    
    ins=NaturalConvection(
        current=current,
        voltage=voltage,
        power=power,

        Temperature_2=temp2,
        Temperature_3=temp3,
        Temperature_4=temp4,
        Temperature_5=temp5,
        Temperature_6=temp6,
        Ambient_Temperature=temp7,
        theoritical_output=y_pred1,
        experimental_output=y_pred2

    )
    ins.save()
    return render(request,'result.html',context)


