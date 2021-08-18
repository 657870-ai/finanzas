#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:48:09 2021

@author: andresbarbudorodriguez
"""

import pulp

WindowsPhone = pulp.LpVariable("WindowsPhone", lowBound=0)
iPhone = pulp.LpVariable("iPhone", lowBound=0)

problem = pulp.LpProblem("A simple maximization objective", pulp.LpMaximize)
problem += 3*WindowsPhone + 2*iPhone, "The objective function"
problem += 2*WindowsPhone + iPhone <= 77706920, "1st constraint"
problem += WindowsPhone + iPhone <= 22269554, "2nd constraint"
problem += WindowsPhone <= 2452, "3rd constraint"
problem.solve() 