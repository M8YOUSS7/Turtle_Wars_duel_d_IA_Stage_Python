#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:19:04 2023

@author: yyouss
"""

from tortue import *
from aim import *

class Joueur:
    def __init__(self, name, x, y, ia):
        self.name   = name
        self.points = 0
        self.trt    = Tortue(x, y)
        #self.trt.ajtArm("FAMAS", 4)
        #self.trt.ajtArm("BROWING M2", 72)
        #self.trt.ajtArm("FN MAG", 13)
        #self.trt.ajtArm("AK-47", 5)
        #self.trt.ajtArm("M16", 3)
        
        if ia=="expert":
            self.aim = IAExpert()
            self.trt.ajtArm("M16", 3)
            
        else:
            self.aim = IA(ia)

    def joue(self, adv, grille):
        while adv.trt.vie>0 and self.trt.endurance>0:
            act = Action(self.aim.prochainCoup(self.trt, adv.trt, grille))
            act.execActDebug(self.trt, adv.trt, grille)

            if (adv.trt.endurance+10)<=100:
                adv.trt.endurance +=10
            else:
                adv.trt.endurance=100
                
        if adv.trt.vie==0:
            adv.trt.endurance=0
            grille[adv.trt.x, adv.trt.y] = "V"
            self.points += 1

    def nouvelleTortue(self, x, y):
        self.trt.iniTortue()
        self.trt.setPos(x, y)