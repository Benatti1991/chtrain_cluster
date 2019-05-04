#-------------------------------------------------------------------------------
# Name:        modulo1
# Purpose:
#
# Author:      tasora
#
# Created:     1/1/2019
# Copyright:   (c) tasora 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()


import os
import math
import numpy as np
#import sys, getopt
import pychrono as chrono
try:
   from pychrono import irrlicht as chronoirr
except:
   print('Could not import ChronoIrrlicht')

# ---------------------------------------------------------------------
#
# Parse command-line parameters
class Model(object):
       def __init__(self, render):
              self.animate = render
              self.observation_space = np.empty([18,])
              self.action_space = np.zeros([6,])
              #TODO: check if targ is reachable
              self.targ_init_pos = [-0.25,0.015,-0.25]
              self.fingerdist = chrono.ChVectorD(0,0.1117,0)
              #self.d_old = np.linalg.norm(self.Xtarg + self.Ytarg)
              self.robosystem = chrono.ChSystemNSC()
              chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.001)
              chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.001)
              #robosystem.SetSolverType(chrono.ChSolver.Type_BARZILAIBORWEIN) # precise, more slow
              self.timestep = 0.01

              self.info =  {}
       
              m_filename = "ComauR3"
              self.timestep = 0.001
              m_length = 1.0
              self.my_material = chrono.ChMaterialSurfaceNSC()
              self.my_material.SetFriction(0.5)
              self.my_material.SetDampingF(0.2)
              self.my_material.SetCompliance (0.0000001)
              self.my_material.SetComplianceT(0.0000001)
              #m_visualization = "irrlicht"
              self.m_datapath = "../../../../../../codes/Chrono/Chrono_Source/data"
              chrono.SetChronoDataPath(self.m_datapath)       
              print ("  file to load is ", m_filename)
              print ("  timestep is ", self.timestep)
              print ("  length is ", m_length)
              print ("  data path for fonts etc.: ", self.m_datapath)
              # ---------------------------------------------------------------------
              #
              #  load the file generated by the SolidWorks CAD plugin
              #  and add it to the ChSystem.
              # Remove the trailing .py and add / in case of file without ./
              #m_absfilename = os.path.abspath(m_filename)
              #m_modulename = os.path.splitext(m_absfilename)[0]

              print ("Loading C::E scene...");
              dir_path = os.path.dirname(os.path.realpath(__file__))
              self.fpath = os.path.join(dir_path, m_filename)
              #exported_items = chrono.ImportSolidWorksSystem(self.fpath)
              #self.exported_items = chrono.ImportSolidWorksSystem(m_modulename)
              
              print ("...loading done!");
              # Print exported items
              #for my_item in exported_items:
              	#print (my_item.GetName())		
              # Optionally set some solver parameters.
              #self.robosystem.SetMaxPenetrationRecoverySpeed(1.00)
              self.robosystem.SetSolverType(chrono.ChSolver.Type_BARZILAIBORWEIN);
              self.robosystem.SetMaxItersSolverSpeed(600);
              self.robosystem.SetSolverWarmStarting(True);
              self.robosystem.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
              """
              $$$$$$$$ FIND THE SW DEFINED CONSTRAINTS, GET THEIR self.frames AND GET RID OF EM $$$$$$$$ 
              """
              
              self.con_link = ["Concentric1", "Concentric2", "Concentric3", "Concentric4", "Concentric5", "Concentric6"]
              self.coi_link = ["Coincident1", "Coincident2", "Coincident3", "Coincident4", "Coincident5", "Coincident6"]
              self.bodiesNames = ["Racer3_p01-3", "Racer3_p02-1", "Racer3_p03-1", "Racer3_p04-1", "Racer3_p05-1", "Racer3_p06-1", "Hand_base_and_p07-2"]
              self.maxSpeed = [430, 450, 500, 600, 600, 900] #°/s
              # TODO: convert to rads (converted in every operation)
              
              #self.limits:
              # TODO: check signs
              # TODO: peridodicity ignored
              # REAL self.limits
              #self.maxRot = [170, 135, 90, 200, 125, 2700] # °
              #self.minRot = [-170, -95, -155, -200, -125, -2700] # °
              # MODIFIED self.limits
              self.maxRot = [170, 135, 90, 179, 125, 179] # °
              self.minRot = [-170, -95, -155, -179, -125, -179] # °
              #self.maxT = np.asarray([28, 28, 28, 7.36, 7.36, 4.41])
              self.maxT = np.asarray([100, 100, 50, 7.36, 7.36, 4.41])

              if (self.animate) :
                     self.myapplication = chronoirr.ChIrrApp(self.robosystem, 'Test', chronoirr.dimension2du(1280,720))
                     self.myapplication.AddShadowAll()
                     self.myapplication.SetStepManage(True)
                     self.myapplication.SetTimestep(self.timestep)
                     self.myapplication.AddTypicalSky(chrono.GetChronoDataPath() + 'skybox/')
                     self.myapplication.AddTypicalLogo(chrono.GetChronoDataPath() + 'logo_pychrono_alpha.png')
                     self.myapplication.AddTypicalCamera(chronoirr.vector3df(1,1,1),chronoirr.vector3df(0.0,0.0,0.0))
                     self.myapplication.AddTypicalLights()               # angle of FOV

       def reset(self):
    
              self.isdone = False
              self.robosystem.Clear()              
              #action = (np.random.rand(6,)-0.5)*2
              #torques = np.multiply(action, self.maxT)
              self.exported_items = chrono.ImportSolidWorksSystem(self.fpath)
              self.csys = []
              self.frames = []
              self.revs = []
              self.motors = []
              self.limits = []

              for con, coi in zip(self.con_link, self.coi_link):
                     indices = []
                     for i in range(len(self.exported_items)):
                            if con==self.exported_items[i].GetName() or coi==self.exported_items[i].GetName() : 
                                   indices.append(i) 
                     rev = self.exported_items[indices[0]]
                     af0 = rev.GetAssetsFrame()
                     # Revolute joints and ChLinkMotorRotation are z oriented, while parallel is x oriented. 
                     # Event though this Frame won't be used anymore is good practice to create a copy before editing its value.
                     af = chrono.ChFrameD(af0)
                     af.SetRot(af0.GetRot() % chrono.Q_ROTATE_X_TO_Z)
                     self.frames.append(af)
                     for i in indices: del self.exported_items[i]

              # ADD IMPORTED ITEMS TO THE SYSTEM
              for my_item in self.exported_items:
              	self.robosystem.Add(my_item)
              
              #TODO: some links not found (and not deleted)
              #ll = self.robosystem.Get_linklist()
              #print('link rimasti:')
              #for l in ll: print(l.GetName())
              
              """
              $$$$$$$$ FIND THE SW DEFINED CONSTRAINTS, GET THEIR MARKERS AND GET RID OF EM $$$$$$$$ 
              """
              self.bodies = [self.robosystem.SearchBody(name) for name in self.bodiesNames]
              self.hand = self.robosystem.SearchBody('Hand_base_and_p07-2')
              self.base  = self.robosystem.SearchBody('Racer3_p01-3')
              self.biceps  = self.robosystem.SearchBody('Racer3_p03-1')
              self.forearm  = self.robosystem.SearchBody('Racer3_p05-1')
              self.finger1 = self.robosystem.SearchBody('HAND_e_finger-1')
              self.finger2 = self.robosystem.SearchBody('HAND_e_finger-2')
              
              for i in range(len(self.con_link)):
                     revolute = chrono.ChLinkLockRevolute() 
                     cs = chrono.ChCoordsysD(self.frames[i].GetPos(), self.frames[i].GetRot())
                     self.csys.append(cs)
                     revolute.Initialize(self.bodies[i], self.bodies[i+1], self.csys[i])
                     self.revs.append(revolute)
                     self.robosystem.Add(self.revs[i])
                     lim = self.revs[i].GetLimit_Rz()
                     self.limits.append(lim)
                     self.limits[i].SetActive(True)
                     self.limits[i].SetMin(self.minRot[i]*(math.pi/180))
                     self.limits[i].SetMax(self.maxRot[i]*(math.pi/180))
                     
                     m = chrono.ChLinkMotorRotationTorque() 
                     m.Initialize(self.bodies[i], self.bodies[i+1], self.frames[i])
                     #self.robosystem.Add(m2)
                     #m2.SetTorqueFunction(chrono.ChFunction_Const(5))
                     self.motors.append(m)
                     #self.motors[i].SetTorqueFunction(chrono.ChFunction_Const(float(torques[i])))
                     self.robosystem.Add(self.motors[i])

              self.body_floor = chrono.ChBody()
              self.body_floor.SetBodyFixed(True)
              self.body_floor.SetPos(chrono.ChVectorD(0, -1, 0 ))
              self.body_floor.SetMaterialSurface(self.my_material)
              
              # Floor Collision.
              self.body_floor.SetMaterialSurface(self.my_material)
              self.body_floor.GetCollisionModel().ClearModel()
              self.body_floor.GetCollisionModel().AddBox(5, 1, 5, chrono.ChVectorD(0, 0, 0 ))
              self.body_floor.GetCollisionModel().BuildModel()
              self.body_floor.SetCollide(True)
              
              # Visualization shape
              body_floor_shape = chrono.ChBoxShape()
              body_floor_shape.GetBoxGeometry().Size = chrono.ChVectorD(5, 1, 5)
              body_floor_shape.SetColor(chrono.ChColor(0.4,0.4,0.5))
              self.body_floor.GetAssets().push_back(body_floor_shape)
              body_floor_texture = chrono.ChTexture()
              texpath = os.path.join(self.m_datapath, 'concrete.jpg')
              body_floor_texture.SetTextureFilename(texpath)
              self.body_floor.GetAssets().push_back(body_floor_texture)     
              self.robosystem.Add(self.body_floor)

              self.targ_box = chrono.ChBody()
              # UNset to grasp
              self.targ_box.SetBodyFixed(True)
              self.targ_box.SetPos(chrono.ChVectorD(self.targ_init_pos[0], self.targ_init_pos[1], self.targ_init_pos[2]))
              self.targ_box.SetMaterialSurface(self.my_material)    
              # Floor Collision.
              self.targ_box.SetMaterialSurface(self.my_material)
              self.targ_box.GetCollisionModel().ClearModel()
              self.targ_box.GetCollisionModel().AddBox(0.015, 0.015, 0.015, chrono.ChVectorD(0, 0, 0 ))
              self.targ_box.GetCollisionModel().BuildModel()
              self.targ_box.SetCollide(True)    
              # Visualization shape
              targ_box_shape = chrono.ChBoxShape()
              targ_box_shape.GetBoxGeometry().Size = chrono.ChVectorD(0.015, 0.015, 0.015)
              col = chrono.ChColorAsset()
              col.SetColor(chrono.ChColor(1.0,0,0))
              self.targ_box.GetAssets().push_back(targ_box_shape)
              self.targ_box.GetAssets().push_back(col)
              self.robosystem.Add(self.targ_box)
              
              self.numsteps= 0

              if (self.animate):
                     self.myapplication.AssetBindAll()
                     self.myapplication.AssetUpdateAll()	
              return self.get_ob()

       def step(self, ac):
              #posbefore = self.body_abdomen.GetPos().x
              self.numsteps += 1
              self.ac = ac.reshape((-1,))
              #TODO: do not control each timestep. Frequency not reachable by real world contorllers
              torques = np.multiply(self.ac, self.maxT)
              for i, t in enumerate(torques):
                            if self.revs[i].GetRelWvel().z > self.maxSpeed[i]*(math.pi/180) and torques[i] > 0: 
                                   torques[i] = 0
                            if self.revs[i].GetRelWvel().z < -self.maxSpeed[i]*(math.pi/180) and torques[i] < 0: 
                                   torques[i] = 0
              for m, t in zip(self.motors, torques): m.SetTorqueFunction(chrono.ChFunction_Const(float(t)))
              
              if (self.animate):
                     self.myapplication.GetDevice().run()
                     self.myapplication.BeginScene()
                     self.myapplication.DrawAll()
                     self.myapplication.DoStep()
                     self.myapplication.EndScene()
              else:
                     self.robosystem.DoStepDynamics(self.timestep)
              
              obs= self.get_ob()
              rew = self.calc_rew()    
              
              self.is_done()
              return obs, rew, self.isdone, self.info



              
       
       
       def get_ob(self):
       
              self.q_mot   = np.zeros([6,])
              self.q_dot_mot   = np.zeros([6,])
              for i, r in enumerate(self.revs): 
                     self.q_mot[i] = r.GetRelAngle()
                     self.q_dot_mot[i] = r.GetRelWvel().z
              gripV = self.hand.GetPos() + self.hand.GetRot().Rotate(self.fingerdist)
              self.grip = np.asarray([gripV.x, gripV.y, gripV.z])
              tarpos = self.targ_box.GetPos()
              self.targ = np.asarray([tarpos.x, tarpos.y, tarpos.z])
              return np.concatenate ([self.q_mot,  self.q_dot_mot, self.targ, self.grip])
       
       def calc_rew(self):
       
              electricity_cost     = 0.001    # cost for using self.motors -- this parameter should be carefully tuned against reward for making progress, other values less improtant
              #stall_torque_cost    = -0.1    # cost for running electric current through a motor even at zero rotational speed, small
              dist_coeff = 1
              #joints_at_limit_cost = -0.2    # discourage stuck joints
              
              #power_cost  = electricity_cost  * float(np.abs(self.ac*self.q_dot_mot).mean())  # let's assume we have DC motor with controller, and reverse current braking. BTW this is the formula of motor power
              #Reduced stall cost to avoid joints at limit
              #joints_limit = joints_at_limit_cost * self.joint_at_limit
              self.self_coll =  0 if self.base.GetContactForce().Length()+ self.biceps.GetContactForce().Length() + self.forearm.GetContactForce().Length() == 0 else -1000
              fing_con = - (self.finger1.GetContactForce().Length() + self.finger2.GetContactForce().Length())
              #progress = self.calc_progress()
              self.dist = np.linalg.norm([self.grip-self.targ])
              rew = ( dist_coeff/(self.dist+0.0001)) + self.self_coll - electricity_cost*np.linalg.norm(self.ac) + fing_con
              return rew

       """
       WE DO NOT USE APPROACHING SPEED BUT IT COULD BE USED IN FUTURE
       def calc_progress(self):
              d = np.linalg.norm( [self.Ytarg - self.body_abdomen.GetPos().y, self.Xtarg - self.body_abdomen.GetPos().x] )
              progress = -(d - self.d_old )/self.timestep
              self.d_old = d
              return progress      """               
       def is_done(self):
       
              if (self.self_coll < -1 or self.numsteps *self.timestep>3):
                            self.isdone = True
       def get_prog(self):
          
              return np.array([[self.numsteps *self.timestep], [self.dist]])

                                     
       def __del__(self):
              if (self.animate):
                     self.myapplication.GetDevice().closeDevice()
                     print('Destructor called, Device deleted.')
              else:
                     print('Destructor called, No device to delete.')
       
       def ScreenCapture(self, interval):
              try: 
                     self.myapplication.SetVideoframeSave(True)
                     self.myapplication.SetVideoframeSaveInterval(interval)
              except:
                     print('No ChIrrApp found. Cannot save video self.frames.')
                     
              
              
              
       """"grip.SetRot(bdy_hand.GetRot())
       # to place the center of the box at the same distance as the finger tip consider the distance between the hand origin and the finger tip plus the distance between the hand origin and the han COG (SetFrame_COG_to_REF in imported model)
       grip.SetPos(bdy_hand.GetPos() + bdy_hand.GetRot().Rotate(chrono.ChVectorD(0,0.1117,0)) )"""
