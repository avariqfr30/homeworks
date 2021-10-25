#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
No 1 (Alternate)
Days Calculator
"""

def convert_to_days(hours,minutes,seconds):
    return((hours*3600)+(minutes*60)+seconds)/86400
print ("There are", format(convert_to_days(94,45,36), '.4f'), "days.")


