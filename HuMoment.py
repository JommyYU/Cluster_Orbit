import numpy as np
import math

def HuMomnet_calc(x,y):
	if len(x) != len(y):
		print("HuMoment_calc length not equal")
		return

	for i in range(0,len(x)):
        m00 = m00+1
        m10 = m10+x[i]
        m01 = m01+y[i]
'''
    x0 = m10 / float(m00) #计算质量中心
    y0 = m01 / float(m00) 


    for i in range(0,len(x)): 
        dx=x[i]-x0
        dy=y[i]-y0
        m11 += dx * dy
        m20 += math.pow(dx, 2)
        m02 += math.pow(dy, 2)
        m30 += math.pow(dx, 3)
        m03 += math.pow(dy, 3)
        m12 += dx * math.pow(dy, 2)
        m21 += math.pow(dx, 2) * dy


    # 计算规范化后的中心矩: mij/pow(m00,((i+j+2)/2)
    u20 = m20 / math.pow(m00, 2)
    u02 = m02 / math.pow(m00, 2)
    u11 = m11 / math.pow(m00, 2)
    u30 = m30 / math.pow(m00, 2.5)
    u03 = m03 / math.pow(m00, 2.5)
    u12 = m12 / math.pow(m00, 2.5)
    u21 = m21 / math.pow(m00, 2.5)

    //  计算中间变量
    t1=(u20-u02) 
    t2=(u30-3*u12) 
    t3=(3*u21-u03) 
    t4=(u30+u12)
    t5=(u21+u03)

    //  计算不变矩 
    M[0]=u20+u02 
    M[1]=t1*t1+4*u11*u11 
    M[2]=t2*t2+t3*t3 
    M[3]=t4*t4+t5*t5
    M[4]=t2*t4*(t4*t4-3*t5*t5)+t3*t5*(3*t4*t4-t5*t5) 
    M[5]=t1*(t4*t4-t5*t5)+4*u11*t4*t5
    M[6]=t3*t4*(t4*t4-3*t5*t5)-t2*t5*(3*t4*t4-t5*t5)

    return M
'''
