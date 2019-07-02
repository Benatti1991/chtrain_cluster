# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: D:\files\Ajeje_Brazorf\Comau_R3.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'ABB_IRB120_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Racer3_p03-1')
body_1.SetPos(chrono.ChVectorD(9.5973672982106e-13,0.559999999999997,0.0577499999999558))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(10.3728089874946)
body_1.SetInertiaXX(chrono.ChVectorD(0.135351163523564,0.176351507859371,0.0662572827719947))
body_1.SetInertiaXY(chrono.ChVectorD(6.67046202009325e-05,4.53808512459234e-05,0.00356008428611989))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.000779225680825848,-0.168753274058432,-0.0558835115362147),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Collision shapes 
body_1.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=-1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=-1 
body_1.GetCollisionModel().AddBox(0.0395,0.036,0.0587499999999994,chrono.ChVectorD(0.00574444444444444,-0.15,-0.0587499999999994),mr)
body_1.GetCollisionModel().BuildModel()
body_1.SetCollide(True)

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Racer3_p06-2')
body_2.SetPos(chrono.ChVectorD(8.37885316684606e-13,-2.4980018054066e-15,-0.00974999999995417))
body_2.SetRot(chrono.ChQuaternionD(1.17961196366423e-16,-2.77555756156289e-17,1,-6.22460558025955e-30))
body_2.SetMass(2.10059663848927)
body_2.SetInertiaXX(chrono.ChVectorD(0.00108999246895887,0.00212848592492114,0.0020609403503579))
body_2.SetInertiaXY(chrono.ChVectorD(-2.14165623203743e-06,3.2224257157417e-06,2.2813841512309e-08))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.300905163754392,0.630062216798406,-3.68522501256792e-05),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_2.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Racer3_p05-1')
body_3.SetPos(chrono.ChVectorD(-0.301999999999166,0.629999999999998,-0.00974999999995427))
body_3.SetRot(chrono.ChQuaternionD(5.71683110376037e-17,-5.55111512312578e-17,1,-1.23259516440783e-32))
body_3.SetMass(4.23269774636928)
body_3.SetInertiaXX(chrono.ChVectorD(0.00874186762217474,0.0294932955860917,0.0293132947008589))
body_3.SetInertiaXY(chrono.ChVectorD(0.000146905448408953,-0.00243433071013402,1.62260275620461e-05))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0757866568886516,0.000371805945289896,0.00456599373754589),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_3.GetAssets().push_back(body_3_1_level) 

# Collision shapes 
body_3.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=0; mr[1,0]=-1; mr[2,0]=0 
mr[0,1]=1.88044606100651E-14; mr[1,1]=0; mr[2,1]=1 
mr[0,2]=-1; mr[1,2]=0; mr[2,2]=1.88044606100651E-14 
body_3.GetCollisionModel().AddCylinder(0.041,0.041,0.062,chrono.ChVectorD(-9.42688781739109E-29,0,-5.01682029252493E-15),mr)
body_3.GetCollisionModel().BuildModel()
body_3.SetCollide(True)

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Racer3_p02-1')
body_4.SetPos(chrono.ChVectorD(0,0,0))
body_4.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_4.SetMass(5.77385036241004)
body_4.SetInertiaXX(chrono.ChVectorD(0.0471845023648761,0.0597079756999918,0.0355427324035167))
body_4.SetInertiaXY(chrono.ChVectorD(-7.32011280324341e-05,0.000796161627242262,-0.000114203138023589))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(6.83088781192802e-05,0.253925907979441,-0.000142127456334174),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_4.GetAssets().push_back(body_4_1_level) 

# Collision shapes 
body_4.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=0; mr[1,0]=1; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=0; mr[2,1]=-1 
mr[0,2]=-1; mr[1,2]=0; mr[2,2]=0 
body_4.GetCollisionModel().AddCylinder(0.064,0.064,0.05875,chrono.ChVectorD(-6.14352493113471E-14,0.29,-0.000750000000025369),mr)
body_4.GetCollisionModel().BuildModel()
body_4.SetCollide(True)

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('HAND_e_finger-1-3')
body_5.SetPos(chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428))
body_5.SetRot(chrono.ChQuaternionD(0.707106781186548,1.74315279842105e-32,-1.37140828284124e-16,0.707106781186547))
body_5.SetMass(0.0938874355859725)
body_5.SetInertiaXX(chrono.ChVectorD(3.31466514037026e-05,2.45304814291191e-05,3.68005499125014e-05))
body_5.SetInertiaXY(chrono.ChVectorD(4.73448371552155e-06,-1.6596537866072e-06,7.80573433834422e-06))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.00724735083156416,0.020647536888227,-0.022421500455029),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_5.GetAssets().push_back(body_5_1_level) 

# Collision shapes 
body_5.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=6.24500451352433E-15 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=2.77555756156289E-15 
mr[0,2]=-6.24500451352433E-15; mr[1,2]=-2.77555756156289E-15; mr[2,2]=1 
body_5.GetCollisionModel().AddBox(0.00999999999998747,0.01,0.00300000000000004,chrono.ChVectorD(-0.000489999999987308,0.0501000000000003,-0.0279999999999992),mr)
body_5.GetCollisionModel().BuildModel()
body_5.SetCollide(True)

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('Racer3_p04-1')
body_6.SetPos(chrono.ChVectorD(-0.0719528449808596,0.493846097658507,-0.00974999999991879))
body_6.SetRot(chrono.ChQuaternionD(-9.0430643194969e-15,-1.11937572411186e-30,1,-1.2195235893339e-16))
body_6.SetMass(2.57881604056105)
body_6.SetInertiaXX(chrono.ChVectorD(0.00515580278191959,0.00582192778397179,0.00711907986386555))
body_6.SetInertiaXY(chrono.ChVectorD(-0.000218981016479624,-1.36278778686613e-05,-5.84114046893191e-05))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0491519964799016,0.124047265613641,-0.00106523411880757),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

# Collision shapes 
body_6.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=0; mr[1,0]=-1; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=0; mr[2,1]=1 
mr[0,2]=-1; mr[1,2]=0; mr[2,2]=0 
body_6.GetCollisionModel().AddCylinder(0.049,0.049,0.053,chrono.ChVectorD(-0.071952844981693,0.0661539023414395,-0.00400000000000006),mr)
body_6.GetCollisionModel().BuildModel()
body_6.SetCollide(True)

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('Hand_base_and_p07-3')
body_7.SetPos(chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428))
body_7.SetRot(chrono.ChQuaternionD(-6.8570414142062e-17,0.707106781186548,-0.707106781186547,6.8570414142062e-17))
body_7.SetMass(0.303832889881202)
body_7.SetInertiaXX(chrono.ChVectorD(0.000170332854701716,0.000356987850207563,0.000354717958269458))
body_7.SetInertiaXY(chrono.ChVectorD(2.55390720647526e-09,7.99598465940156e-07,9.67154883446795e-10))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.94524691596611e-07,-0.0397662836717129,7.28693415284112e-05),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_7.GetAssets().push_back(body_7_1_level) 

# Collision shapes 
body_7.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=0; mr[1,0]=0; mr[2,0]=-1 
mr[0,1]=0; mr[1,1]=-1; mr[2,1]=0 
mr[0,2]=-1; mr[1,2]=0; mr[2,2]=0 
body_7.GetCollisionModel().AddCylinder(0.0375,0.0375,0.04940000094,chrono.ChVectorD(0,-0.03630000094,0),mr)
body_7.GetCollisionModel().BuildModel()
body_7.SetCollide(True)

exported_items.append(body_7)



# Rigid body part
body_8= chrono.ChBodyAuxRef()
body_8.SetName('HAND_e_finger-2-1')
body_8.SetPos(chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428))
body_8.SetRot(chrono.ChQuaternionD(0.707106781186548,-1.37140828284124e-16,-8.71576399210525e-33,0.707106781186547))
body_8.SetMass(0.0938874355859725)
body_8.SetInertiaXX(chrono.ChVectorD(3.31467659305197e-05,2.45303153855084e-05,3.6800601429295e-05))
body_8.SetInertiaXY(chrono.ChVectorD(-4.73444367209372e-06,-1.65947246859143e-06,-7.80569347513243e-06))
body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00724737975140957,0.0206478134281555,0.0224215440569809),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_8.GetAssets().push_back(body_8_1_level) 

# Collision shapes 
body_8.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=-1; mr[1,0]=3.30423519234954E-16; mr[2,0]=8.26058798087386E-16 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=5.20417042793042E-16 
mr[0,2]=-8.26058798087386E-16; mr[1,2]=5.20417042793042E-16; mr[2,2]=-1 
body_8.GetCollisionModel().AddBox(0.0104999999999594,0.01,0.003,chrono.ChVectorD(-1.00000000174933E-05,0.0501000000000003,0.0279999999999993),mr)
body_8.GetCollisionModel().BuildModel()
body_8.SetCollide(True)

exported_items.append(body_8)



# Rigid body part
body_9= chrono.ChBodyAuxRef()
body_9.SetName('Racer3_p01-1')
body_9.SetPos(chrono.ChVectorD(0,0,0))
body_9.SetRot(chrono.ChQuaternionD(0,0,1,0))
body_9.SetMass(2)
body_9.SetInertiaXX(chrono.ChVectorD(0.0178574312658815,0.0139838889253173,0.0215331449032541))
body_9.SetInertiaXY(chrono.ChVectorD(0.00022534490771271,-1.13074017366894e-05,-1.46417309442246e-05))
body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.042007179851563,0.0796401008011628,-8.00702571762052e-05),chrono.ChQuaternionD(1,0,0,0)))
body_9.SetBodyFixed(True)

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_9.GetAssets().push_back(body_9_1_level) 

# Collision shapes 
body_9.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=0; mr[1,0]=0; mr[2,0]=1 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=-1; mr[1,2]=0; mr[2,2]=0 
body_9.GetCollisionModel().AddCylinder(0.091,0.091,0.083,chrono.ChVectorD(0,0.083,0),mr)
body_9.GetCollisionModel().BuildModel()
body_9.SetCollide(True)

exported_items.append(body_9)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_9 , SW name: Racer3_p01-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Racer3_p02-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0.1765,0)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(-6.14409169281283e-14,0.166,-2.48666584593661e-14)
dB = chrono.ChVectorD(0,1,0)
link_1.Initialize(body_9,body_4,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0,0.1765,0)
cB = chrono.ChVectorD(-6.14409169281283e-14,0.166,-2.48666584593661e-14)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_2.Initialize(body_9,body_4,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Racer3_p01-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Racer3_p02-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0.166,0)
cB = chrono.ChVectorD(-6.14409169281283e-14,0.166,-2.48666584593661e-14)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,-1,0)
link_3.Initialize(body_9,body_4,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0.166,0)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(-6.14409169281283e-14,0.166,-2.48666584593661e-14)
dB = chrono.ChVectorD(0,-1,0)
link_4.SetFlipped(True)
link_4.Initialize(body_9,body_4,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_4 , SW name: Racer3_p02-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Racer3_p03-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-6.14352493113471e-14,0.29,-0.240519335983782)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(9.59150439600569e-13,0.289999999999998,0.0597499999999644)
dB = chrono.ChVectorD(1.82243807002376e-14,4.89069225964583e-17,1)
link_5.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-6.14352493113471e-14,0.29,-0.240519335983782)
cB = chrono.ChVectorD(9.59150439600569e-13,0.289999999999998,0.0597499999999644)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(1.82243807002376e-14,4.89069225964583e-17,1)
link_6.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Racer3_p02-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_1 , SW name: Racer3_p03-1 ,  SW ref.type:4 (4)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(9.59210500828341e-13,0.559999999999997,-3.90174004216703e-14)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(-9.11219035011878e-15,-2.44534612982291e-17,-1)
link_7.Initialize(body_4,body_1,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(9.59210500828341e-13,0.559999999999997,-3.90174004216703e-14)
dB = chrono.ChVectorD(-9.11219035011878e-15,-2.44534612982291e-17,-1)
link_8.SetFlipped(True)
link_8.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Racer3_p03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Racer3_p04-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(9.58953721958393e-13,0.559999999999998,0.0597499999999639)
dA = chrono.ChVectorD(1.82243807002376e-14,4.89069225964583e-17,1)
cB = chrono.ChVectorD(8.29933344270728e-13,0.559999999999947,-0.197342929112483)
dB = chrono.ChVectorD(1.80861286389938e-14,2.43904717866781e-16,1)
link_9.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(9.58953721958393e-13,0.559999999999998,0.0597499999999639)
cB = chrono.ChVectorD(8.29933344270728e-13,0.559999999999947,-0.197342929112483)
dA = chrono.ChVectorD(1.82243807002376e-14,4.89069225964583e-17,1)
dB = chrono.ChVectorD(1.80861286389938e-14,2.43904717866781e-16,1)
link_10.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Racer3_p03-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Racer3_p04-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0572530248465861,0.357253820140855,-0.0597500000000431)
cB = chrono.ChVectorD(8.32417468288327e-13,0.559999999999947,-0.0597499999999201)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(-1.80861286389938e-14,-2.43904717866781e-16,-1)
link_11.Initialize(body_1,body_6,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0572530248465861,0.357253820140855,-0.0597500000000431)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(8.32417468288327e-13,0.559999999999947,-0.0597499999999201)
dB = chrono.ChVectorD(-1.80861286389938e-14,-2.43904717866781e-16,-1)
link_12.SetFlipped(True)
link_12.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
exported_items.append(link_12)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: Racer3_p04-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Racer3_p05-1 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(500.000000000001,0.629999999999947,-0.00975000000896313)
dA = chrono.ChVectorD(-1,-3.31053967256856e-32,1.80861286389938e-14)
cB = chrono.ChVectorD(-0.233072414976564,0.629999999999998,-0.00974999999995426)
dB = chrono.ChVectorD(1,1.11022302462516e-16,1.14336622075207e-16)
link_13.SetFlipped(True)
link_13.Initialize(body_6,body_3,False,cA,cB,dA,dB)
link_13.SetName("Concentric4")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(500.000000000001,0.629999999999947,-0.00975000000896313)
cB = chrono.ChVectorD(-0.233072414976564,0.629999999999998,-0.00974999999995426)
dA = chrono.ChVectorD(-1,-3.31053967256856e-32,1.80861286389938e-14)
dB = chrono.ChVectorD(1,1.11022302462516e-16,1.14336622075207e-16)
link_14.Initialize(body_6,body_3,False,cA,cB,dA,dB)
link_14.SetName("Concentric4")
exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: Racer3_p04-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Racer3_p05-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.149599999999167,0.629999999999947,-0.00974999999997883)
cB = chrono.ChVectorD(-0.149599999999165,0.629999999999998,-0.00975000000001565)
dA = chrono.ChVectorD(-1,3.46873373136055e-32,1.80861286389935e-14)
dB = chrono.ChVectorD(1,1.11022302462516e-16,1.14336622075486e-16)
link_15.Initialize(body_6,body_3,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.149599999999167,0.629999999999947,-0.00974999999997883)
dA = chrono.ChVectorD(-1,3.46873373136055e-32,1.80861286389935e-14)
cB = chrono.ChVectorD(-0.149599999999165,0.629999999999998,-0.00975000000001565)
dB = chrono.ChVectorD(1,1.11022302462516e-16,1.14336622075486e-16)
link_16.SetFlipped(True)
link_16.Initialize(body_6,body_3,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
exported_items.append(link_16)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Racer3_p05-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Racer3_p06-2 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.301999999999166,0.629999999999998,0.0292500000000461)
dA = chrono.ChVectorD(1.14336622075208e-16,-2.46519032881566e-32,-1)
cB = chrono.ChVectorD(-0.301999999999166,0.629999999999998,-0.0447499999999543)
dB = chrono.ChVectorD(-2.35922392732846e-16,1.24492111605191e-29,1)
link_17.SetFlipped(True)
link_17.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_17.SetName("Concentric5")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.301999999999166,0.629999999999998,0.0292500000000461)
cB = chrono.ChVectorD(-0.301999999999166,0.629999999999998,-0.0447499999999543)
dA = chrono.ChVectorD(1.14336622075208e-16,-2.46519032881566e-32,-1)
dB = chrono.ChVectorD(-2.35922392732846e-16,1.24492111605191e-29,1)
link_18.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_18.SetName("Concentric5")
exported_items.append(link_18)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Racer3_p05-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Racer3_p06-2 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.301999999999166,0.629999999999998,-0.0407499999999543)
cB = chrono.ChVectorD(-0.301999999999166,0.629999999999998,-0.0407499999999543)
dA = chrono.ChVectorD(-1.14336622075208e-16,2.46519032881566e-32,1)
dB = chrono.ChVectorD(2.35922392732846e-16,-1.24492111605191e-29,-1)
link_19.Initialize(body_3,body_2,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident5")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.301999999999166,0.629999999999998,-0.0407499999999543)
dA = chrono.ChVectorD(-1.14336622075208e-16,2.46519032881566e-32,1)
cB = chrono.ChVectorD(-0.301999999999166,0.629999999999998,-0.0407499999999543)
dB = chrono.ChVectorD(2.35922392732846e-16,-1.24492111605191e-29,-1)
link_20.SetFlipped(True)
link_20.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_20.SetName("Coincident5")
exported_items.append(link_20)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Racer3_p06-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.344999999999166,0.629999999999998,-0.00974999999995427)
dA = chrono.ChVectorD(1,5.55111512312578e-17,1.80411241501588e-16)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dB = chrono.ChVectorD(1,6.15242222082669e-17,1.93946419314488e-16)
link_21.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_21.SetName("Concentric6")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateGeneric()
link_22.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.344999999999166,0.629999999999998,-0.00974999999995427)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(1,5.55111512312578e-17,1.80411241501588e-16)
dB = chrono.ChVectorD(1,6.15242222082669e-17,1.93946419314488e-16)
link_22.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_22.SetName("Concentric6")
exported_items.append(link_22)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Racer3_p06-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.363999999999166,0.629999999999998,0.0252500000000457)
cB = chrono.ChVectorD(-0.363999999999166,0.629999999999998,-0.00974999999995427)
dA = chrono.ChVectorD(-1,-5.55111512312578e-17,-1.80411241501588e-16)
dB = chrono.ChVectorD(1,4.50102280827071e-16,1.11375342349619e-15)
link_23.Initialize(body_2,body_7,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Coincident6")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.363999999999166,0.629999999999998,0.0252500000000457)
dA = chrono.ChVectorD(-1,-5.55111512312578e-17,-1.80411241501588e-16)
cB = chrono.ChVectorD(-0.363999999999166,0.629999999999998,-0.00974999999995427)
dB = chrono.ChVectorD(1,4.50102280827071e-16,1.11375342349619e-15)
link_24.SetFlipped(True)
link_24.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_24.SetName("Coincident6")
exported_items.append(link_24)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_5 , SW name: HAND_e_finger-1-3 ,  SW ref.type:4 (4)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(1.93946419314488e-16,0,-1)
dB = chrono.ChVectorD(-1.93946419314488e-16,-1.93946419314488e-16,1)
link_25.Initialize(body_7,body_5,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Coincident7")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(1.93946419314488e-16,0,-1)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dB = chrono.ChVectorD(-1.93946419314488e-16,-1.93946419314488e-16,1)
link_26.SetFlipped(True)
link_26.Initialize(body_7,body_5,False,cA,cB,dA,dB)
link_26.SetName("Coincident7")
exported_items.append(link_26)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_5 , SW name: HAND_e_finger-1-3 ,  SW ref.type:4 (4)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
dB = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
link_27.Initialize(body_7,body_5,False,cA,cB,dB)
link_27.SetDistance(0)
link_27.SetName("Coincident8")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dB = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
link_28.Initialize(body_7,body_5,False,cA,cB,dA,dB)
link_28.SetName("Coincident8")
exported_items.append(link_28)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_5 , SW name: HAND_e_finger-1-3 ,  SW ref.type:4 (4)

link_29 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(6.15242222082669e-17,-1,0)
dB = chrono.ChVectorD(-6.1524222208267e-17,1,1.93946419314488e-16)
link_29.Initialize(body_7,body_5,False,cA,cB,dB)
link_29.SetDistance(0)
link_29.SetName("Coincident9")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(6.15242222082669e-17,-1,0)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dB = chrono.ChVectorD(-6.1524222208267e-17,1,1.93946419314488e-16)
link_30.SetFlipped(True)
link_30.Initialize(body_7,body_5,False,cA,cB,dA,dB)
link_30.SetName("Coincident9")
exported_items.append(link_30)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_8 , SW name: HAND_e_finger-2-1 ,  SW ref.type:4 (4)

link_31 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(1.93946419314488e-16,0,-1)
dB = chrono.ChVectorD(-1.93946419314488e-16,1.93946419314488e-16,1)
link_31.Initialize(body_7,body_8,False,cA,cB,dB)
link_31.SetDistance(0)
link_31.SetName("Coincident10")
exported_items.append(link_31)

link_32 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(1.93946419314488e-16,0,-1)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dB = chrono.ChVectorD(-1.93946419314488e-16,1.93946419314488e-16,1)
link_32.SetFlipped(True)
link_32.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_32.SetName("Coincident10")
exported_items.append(link_32)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_8 , SW name: HAND_e_finger-2-1 ,  SW ref.type:4 (4)

link_33 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
dB = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
link_33.Initialize(body_7,body_8,False,cA,cB,dB)
link_33.SetDistance(0)
link_33.SetName("Coincident11")
exported_items.append(link_33)

link_34 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dB = chrono.ChVectorD(-1,-6.15242222082669e-17,-1.93946419314488e-16)
link_34.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_34.SetName("Coincident11")
exported_items.append(link_34)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_8 , SW name: HAND_e_finger-2-1 ,  SW ref.type:4 (4)

link_35 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(6.15242222082669e-17,-1,0)
dB = chrono.ChVectorD(-6.15242222082669e-17,1,-1.93946419314488e-16)
link_35.Initialize(body_7,body_8,False,cA,cB,dB)
link_35.SetDistance(0)
link_35.SetName("Coincident12")
exported_items.append(link_35)

link_36 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dA = chrono.ChVectorD(6.15242222082669e-17,-1,0)
cB = chrono.ChVectorD(-0.449700001879166,0.629999999999998,-0.00974999999995428)
dB = chrono.ChVectorD(-6.15242222082669e-17,1,-1.93946419314488e-16)
link_36.SetFlipped(True)
link_36.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_36.SetName("Coincident12")
exported_items.append(link_36)


# Mate constraint: Angle1 [MatePlanarAngleDim] type:6 align:0 flip:False
#   Entity 0: C::E name: body_4 , SW name: Racer3_p02-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name:  , SW name: Comau_R3 ,  SW ref.type:4 (4)


# Mate constraint: Angle2 [MatePlanarAngleDim] type:6 align:0 flip:True
#   Entity 0: C::E name: body_1 , SW name: Racer3_p03-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_4 , SW name: Racer3_p02-1 ,  SW ref.type:4 (4)


# Mate constraint: Angle3 [MatePlanarAngleDim] type:6 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: Racer3_p04-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_1 , SW name: Racer3_p03-1 ,  SW ref.type:4 (4)


# Mate constraint: Angle4 [MatePlanarAngleDim] type:6 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: Racer3_p04-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_3 , SW name: Racer3_p05-1 ,  SW ref.type:4 (4)


# Mate constraint: Angle5 [MatePlanarAngleDim] type:6 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Racer3_p06-2 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_3 , SW name: Racer3_p05-1 ,  SW ref.type:4 (4)


# Mate constraint: Angle6 [MatePlanarAngleDim] type:6 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Racer3_p06-2 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_7 , SW name: Hand_base_and_p07-3 ,  SW ref.type:4 (4)

