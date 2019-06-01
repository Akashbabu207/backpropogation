import math
a=float(input("enter the input1 value:"))
b=float(input("enter the input2 value:"))
c=float(input("Enter the input3 value:"))
d=float(input("enter the input4 value:"))
f=float(input("enter the input5 value:"))
e=0;oo1=0
targeto1=float(input("enter the tarhet output 1:"))
targeto2=float(input("enter the target output 2:"))
targeto3=float(input("enter the target output 3:"))
targeto4=float(input("enter the target output 4:"))
targeto5=float(input("enter the target output 5:"))
w1=0.10;w2=0.15;w3=0.20;w4=0.25;w5=0.30;w6=0.35;w7=0.40
w8=0.45;w9=0.50;w10=0.55;w11=0.60;w12=0.65
w13=0.70;w14=0.75;w15=0.80;w16=0.85
w17=0.90;w18=0.95;w19=1.0;w20=1.10;w21=1.15;w22=1.20;w23=1.25;w24=1.30
w25=1.35;w26=1.40;w27=1.45;w28=1.50;w29=1.55;w30=1.60
b1=0.35;b2=0.60
i=0
h1=(((w1)*a)+((w2)*b)+(w3*c)+(w4*d)+(w5*f)+b1*1)
oh1=1/(1+(2.718281)**-h1)
#print("The Hidden1 Value is:",h1) 
#print("\nThe hidden output is:",oh1)
h2=(((w6)*a)+((w7)*b)+(w8*c)+(w9*d)+(w10*f)+(b1*1))
#print("\nThe Hidden2 Value is:",h2)
oh2=1/(1+(2.718281)**-h2)
#print("\nThe Hidden2 Output is:",oh2)
h3=((w11*a)+(w12*b)+(w13*c)+(w14*d)+(w15*f)+(b1*1))
oh3=1/(1+(2.718281)**-h3)
o1=((oh1*(w16))+(oh2*(w17))+(oh3*w18)+(b2*1))
#print("The Output1 value is:",o1)
oo1=1/(1+(2.718281)**-o1)
print("The output1 is:",oo1)
o2=((oh1*(w19))+(oh2*(w20))+(oh3*w21)+(b2*1))
#print("The Output2 value is:",o2)
oo2=1/(1+(2.718281)**-o2)
#(∂Etotal/ ∂outh1)* (∂outh1/ ∂neth1)* (∂neth1/ ∂w1)
print("The output2 is:",oo2)
o3=((oh1*(w22))+(oh2*(w23))+(oh3*w24)+(b2*1))
oo3=1/(1+(2.718281)**-o3)
o4=((oh1*w25)+(oh2*w26)+(oh3*w27)+(b2*1))
oo4=1/(1+(2.718281)**-o4)
o5=((oh1*w28)+(oh2*w29)+(oh3*w30)+(b2*1))
oo5=1/(1+(2.718281)**-o5)
#e=(oo1+oo2)
#print(e)
#w1=0.15-i;w2=0.2-i;w3=0.25-i;w4=0.30-i;w5=0.40-i;w6=0.45-i;w7=0.50-i;w8=0.55-i
#i=i+0.01
t1=(0.5*(targeto1-oo1)**2)
t2=(0.5*(targeto2-oo2)**2)
t3=(0.5*(targeto3-oo3)**2)
t4=(0.5*(targeto4-oo4)**2)
t5=(0.5*(targeto5-oo5)**2)
#print("Eo1",t1,"\nEo2",t2)
etotal=t1+t2+t3+t4+t5

while(etotal!=0.00):
    
    i=i+1
    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh1*(1-oh1)
    dif3=a
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w1=w1-0.5*Q
    #print(Q)
    #print("the w1 is:",w1)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh1*(1-oh1)
    dif3=b
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w2=w2-0.5*Q
    #print(Q)
    #print("the w2 is:",w2)

    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh1*(1-oh1)
    dif3=c
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w3=w3-0.5*Q
    #print(Q)
    #print("the w3 is:",w3)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh1*(1-oh1)
    dif3=d
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w4=w4-0.5*Q
    #print(Q)
    #print("the w4 is:",w4)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh1*(1-oh1)
    dif3=e
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w5=w5-0.5*Q
    #print(Q)
    #print("the w5 is:",w5)      

    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh2*(1-oh2)
    dif3=a
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w6=w6-0.5*Q
    #print(Q)
    #print("the w6 is:",w6)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh2*(1-oh2)
    dif3=b
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w72=w7-0.5*Q
    #print(Q)
    #print("the w7 is:",w7)



    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh2*(1-oh2)
    dif3=c
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w8=w8-0.5*Q
    #print(Q)
    #print("the w8 is:",w8)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh2*(1-oh2)
    dif3=d
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w9=w9-0.5*Q
    #print(Q)
    #print("the w9 is:",w9)      


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh2*(1-oh2)
    dif3=e
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w10=w10-0.5*Q
    #print(Q)
    #print("the w10 is:",w10)

    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh3*(1-oh3)
    dif3=a
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w11=w11-0.5*Q
    #print(Q)
    #print("the w11 is:",w11)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5))
    dif2=oh3*(1-oh3)
    dif3=b
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w12=w12-0.5*Q
    #print(Q)
    #print("the w12 is:",w12)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5)) 
    dif2=oh3*(1-oh3)
    dif3=c
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w13=w13-0.5*Q
    #print(Q)
    #print("the w13 is:",w13)


    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5)) 
    dif2=oh3*(1-oh3)
    dif3=d
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w14=w14-0.5*Q
    #print(Q)
    #print("the w14 is:",w14)



    dif1=(-(targeto1-oo1)*oo1*(1-oo1))+(-(targeto2-oo2)*oo2*(1-oo2))+(-(targeto3-oo3)*oo3*(1-oo3))+(-(targeto4-oo4)*oo4*(1-oo4))+(-(targeto5-oo5)*oo5*(1-oo5)) 
    dif2=oh3*(1-oh3)
    dif3=e
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w15=w15-0.5*Q
    #print(Q)
    #print("the w15 is:",w15)


        
    dif1=-(targeto1-oo1)
    dif2=oo1*(1-oo1)
    dif3=1*oh1*w16**(1-1)+0+0
    #print(dif1,dif2,dif3)
    Q=dif1*dif2*dif3
    w16=w16-0.5*Q
    #print(Q)
    #print("the w16 is:",w16)
        
    dif11=-(targeto1-oo1)
    dif21=oo1*(1-oo1)
    dif31=1*oh1*w17**(1-1)+0+0
    #print(dif11,dif21,dif31)
    Q1=dif11*dif21*dif31
    w17=w17-0.5*Q1
    #print(Q1)
    #print("the w17 is:",w17)


    dif12=-(targeto1-oo1)
    dif22=oo1*(1-oo1)
    dif32=1*oh1*w18**(1-1)+0+0
    #print(dif12,dif22,dif32)
    Q2=dif12*dif22*dif32
    w18=w18-0.5*Q2
    #print(Q2)
    #print("the w18 is:",w18)

    
    dif13=-(targeto2-oo2)
    dif23=oo2*(1-oo2)
    dif33=1*oh1*w19**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w19=w19-0.5*Q3
    #print(Q3)
    #print("the w19 is:",w19)


    dif13=-(targeto2-oo2)
    dif23=oo2*(1-oo2)
    dif33=1*oh2*w20**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w20=w20-0.5*Q3
    #print(Q3)
    #print("the w20 is:",w20)


    dif13=-(targeto2-oo2)
    dif23=oo2*(1-oo2)
    dif33=1*oh2*w21**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w21=w21-0.5*Q3
    #print(Q3)
    #print("the w21 is:",w21)


    dif13=-(targeto3-oo3)
    dif23=oo3*(1-oo3)
    dif33=1*oh2*w22**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w22=w22-0.5*Q3
    #print(Q3)
    #print("the w22 is:",w22)


    dif13=-(targeto3-oo3)
    dif23=oo3*(1-oo3)
    dif33=1*oh2*w23**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w23=w23-0.5*Q3
    #print(Q3)
    #print("the w23 is:",w23)


    dif13=-(targeto3-oo3)
    dif23=oo3*(1-oo3)
    dif33=1*oh2*w24**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w24=w24-0.5*Q3
    #print(Q3)
    #print("the w24 is:",w24)


    dif13=-(targeto4-oo4)
    dif23=oo4*(1-oo4)
    dif33=1*oh2*w25**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w25=w25-0.5*Q3
    #print(Q3)
    #print("the w25 is:",w25)
      
    dif13=-(targeto4-oo4)
    dif23=oo4*(1-oo4)
    dif33=1*oh3*w26**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w26=w26-0.5*Q3
    #print(Q3)
    #print("the w26 is:",w26)
      
    dif13=-(targeto4-oo4)
    dif23=oo4*(1-oo4)
    dif33=1*oh3*w27**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w27=w27-0.5*Q3
    #print(Q3)
    #print("the w27 is:",w27)
      
    dif13=-(targeto5-oo5)
    dif23=oo5*(1-oo5)
    dif33=1*oh3*w28**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w28=w28-0.5*Q3
    #print(Q3)
    #print("the w28 is:",w28)

    dif13=-(targeto5-oo5)
    dif23=oo5*(1-oo5)
    dif33=1*oh3*w29**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w29=w29-0.5*Q3
    #print(Q3)
    #print("the w29 is:",w29)
      
    dif13=-(targeto5-oo5)
    dif23=oo5*(1-oo5)
    dif33=1*oh3*w30**(1-1)+0+0
    #print(dif13,dif23,dif33)
    Q3=dif13*dif23*dif33
    w30=w30-0.5*Q3
    #print(Q3)
    #print("the w30 is:",w30) 


    h1=(((w1)*a)+((w2)*b)+(w3*c)+(w4*d)+(w5*f)+b1*1)
    oh1=1/(1+(2.718281)**-h1)
    #print("The Hidden1 Value is:",h1) 
    #print("\nThe hidden output is:",oh1)
    h2=(((w6)*a)+((w7)*b)+(w8*c)+(w9*d)+(w10*f)+(b1*1))
    #print("\nThe Hidden2 Value is:",h2)
    oh2=1/(1+(2.718281)**-h2)
    #print("\nThe Hidden2 Output is:",oh2)
    h3=((w11*a)+(w12*b)+(w13*c)+(w14*d)+(w15*f)+(b1*1))
    oh3=1/(1+(2.718281)**-h3)
    o1=((oh1*(w16))+(oh2*(w17))+(oh3*w18)+(b2*1))
    #print("The Output1 value is:",o1)
    oo1=1/(1+(2.718281)**-o1)
    print("The output1 is:",oo1)
    o2=((oh1*(w19))+(oh2*(w20))+(oh3*w21)+(b2*1))
    #print("The Output2 value is:",o2)
    oo2=1/(1+(2.718281)**-o2)
    #(∂Etotal/ ∂outh1)* (∂outh1/ ∂neth1)* (∂neth1/ ∂w1)
    print("The output2 is:",oo2)
    o3=((oh1*(w22))+(oh2*(w23))+(oh3*w24)+(b2*1))
    oo3=1/(1+(2.718281)**-o3)
    o4=((oh1*w25)+(oh2*w26)+(oh3*w27)+(b2*1))
    oo4=1/(1+(2.718281)**-o4)
    o5=((oh1*w28)+(oh2*w29)+(oh3*w30)+(b2*1))
    oo5=1/(1+(2.718281)**-o5)
    #e=(oo1+oo2)
    #print(e)
    #w1=0.15-i;w2=0.2-i;w3=0.25-i;w4=0.30-i;w5=0.40-i;w6=0.45-i;w7=0.50-i;w8=0.55-i
    #i=i+0.01
    t1=(0.5*(targeto1-oo1)**2)
    t2=(0.5*(targeto2-oo2)**2)
    t3=(0.5*(targeto3-oo3)**2)
    t4=(0.5*(targeto4-oo4)**2)
    t5=(0.5*(targeto5-oo5)**2)
    #print("Eo1",t1,"\nEo2",t2)
    etotal=t1+t2+t3+t4+t5

print(oo1)
print(oo2)
print(oo3)
    
