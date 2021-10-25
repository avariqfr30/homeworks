#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
No.5 - Temprature Converter
"""
def convert_temp(tempf):
    return tempf, (5/9)*(tempf-32), ((5/9)*(tempf-32)+273.15)
print ("The temprature after converted is : ", convert_temp(120))
    
    
    

 