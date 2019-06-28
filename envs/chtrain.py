# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:01:21 2019

@author: SB
"""

import chtrain_ant
import chtrain_pendulum
import chtrain_ComauR3
import chtrain_ant_defsoil
import chtrain_ABB_IRB120

       
def Init(env_name, render):
       if env_name=='ChronoAnt':
              return chtrain_ant.Model(render)
                     
       elif env_name=='ChronoAntDefSoil':
              return chtrain_ant_defsoil.Model(render)

       elif env_name=='ChronoPendulum':
              return chtrain_pendulum.Model(render)
       
       elif env_name=='ChronoRacer3':
              return chtrain_ComauR3.Model(render)
          
       elif env_name=='ABB_IRB120':
              return chtrain_ABB_IRB120.Model(render)
       
       else: 
              print('Unvalid environment name')
                            
       