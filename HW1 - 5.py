#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
No.5 - Temprature Converter
"""
def convert_temp():
    def temprature_in_f():
        tempf = float(input("The temprature in Fahrenheit is : "))
        return tempf
    def temprature_in_c(tf):
        return (5/9)*(tf-32)
    def temprature_in_k(tc):
        return tc + 273.15
    
    tf = temprature_in_f()
    tc = temprature_in_c(tf)
    tk = temprature_in_k(tc)
    
    print("The temprature in Celcius is : ", format(tc, '.4f'))
    print("The temprature in Kelvin is : ", format(tk, '.4f'))
convert_temp()
    

    

    
    
    

 