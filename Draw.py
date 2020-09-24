#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import main

if __name__ == '__main__':
    main.run_main("forward_selection", ["pearson", "fisher", "greedy"], "auc")