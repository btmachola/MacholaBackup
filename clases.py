# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 09:11:00 2025

@author: B MACHOLA
"""

class adv_course:
    
    def __init__(self,subject,dept):
        self.subject=subject
        self.faculty='FEL'
        self.dept=dept
        
    def description(self):
        print('This advance course is of ',self.subject)
        print('This advance course is conducted in',self.faculty)
        
OACT=adv_course('CMPTR','CS DEPT')
OALEC=adv_course('Comn','CE DEPT')
OALER=adv_course('Radar','RC DEPT')

OACT.description()