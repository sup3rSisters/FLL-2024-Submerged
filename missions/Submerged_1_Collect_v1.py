# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":638,"y":-179,"deletable":false,"next":{"block":{"type":"variables_set_prime_hub","id":"eErG~11dD.Ey32{G{9WP","extraState":{"optionLevel":1},"fields":{"VAR":{"id":"fEhq)iedyzg5lK1##D=s"}},"inputs":{"AXIS_TOP":{"shadow":{"type":"blockParametersAxis","id":"bUi#;t2U[z7$gC`s~_@a","fields":{"VALUE":"z"}}},"AXIS_FRONT":{"shadow":{"type":"blockParametersAxis","id":"*1]BBMr|F7![n2woisOw","fields":{"VALUE":"x"}}}},"next":{"block":{"type":"variables_set_motor","id":"$0:iV)zv3MMIM^RzxY:.","fields":{"VAR":{"id":"u%E,Y!H;hn8[F;isp,m4"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"hs}@.J/*@1.sVI7;@~-N","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"x#Rugq-w#fisoC9XJe~j","fields":{"SELECTION":"Direction.COUNTERCLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"(:SYI1OhgUzDGN]L;EmJ","fields":{"VAR":{"id":"]dX^t^dQ8Yj)v3+e^]}1"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"P?,R1xG#6iXnRdMhY}b6","fields":{"NAME":"B"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":",S~j9Ou|Yp-^tLB])F._","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_drive_base","id":"O.;pP9[{}rC2-OH/otuX","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1"}},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"]@Z?d*_:qM7!90V7fAM#","fields":{"VAR":{"id":"u%E,Y!H;hn8[F;isp,m4","name":"left","type":"Motor"}}}},"VAR2":{"shadow":{"type":"variables_get_motor_device","id":"Tzp%Ge9ZGYV_.$%3*als","fields":{"VAR":{"id":"]dX^t^dQ8Yj)v3+e^]}1","name":"right","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_distance","id":"QK`^[W2_kGI[GM=OU$Nj","fields":{"VALUE0":88}}},"VALUE1":{"shadow":{"type":"unit_distance","id":"koYte!aNs,z_b7+;#ymU","fields":{"VALUE0":97}}}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":-159,"y":87,"deletable":false,"next":{"block":{"type":"blockFunctionCallerStatement","id":"!$qPBd|NJb$rAN*jtOnS","extraState":{"optionLevel":0},"fields":{"ICON":"TASK","VAR":{"id":"=!LihrfB68WooWqZT^-H"}},"next":{"block":{"type":"blockDriveBaseDrive","id":"kNnBVqT3|5}dn~O;Wn8w","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"yOBev:TrK,Pev:|4*SlV","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"6(VdJa?.k3Dm3r5]!s$x","fields":{"VALUE0":-420}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"jlJUEn[#ro$,JnfYNx|2","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"AcW6m|VF.Bp4~Ly=pD=f","extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_DRIVE_TURN"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"6.[XZXT=?nMq!JL,-uLQ","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angle","id":"GYpzBVkw.7n_oc:(fs=D","fields":{"VALUE0":105}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"jn}oaim:e$H%=^ZyB+WW","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"m:KxMl5YLEQCyjCwA5IR","extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_DRIVE_CURVE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"kT/o.]y7xa0))`|dc]=;","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"Oy-a1!|:sjUnu,`0(lHO","fields":{"VALUE0":-4000}}},"ARG1":{"shadow":{"type":"unit_angle","id":"@*)[{3#bWwT]:y;kW!AR","fields":{"VALUE0":-9}}},"ARG2":{"shadow":{"type":"parameters_stop_4","id":"ymJB6a|%AQEzi-{rQJHz","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"{j)g0UF]hM!CT{#)jv@.","extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_DRIVE_TURN"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"O(4[3Tdmz3_j2M=m?$jt","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angle","id":"9a|)]f3g!^A0KfJF)U%T","fields":{"VALUE0":-115}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"fMweF5swjF=/LJza]Tx]","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockWaitTime","id":"2LLA/N%/#VY*st;S9(tD","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"T=cEM+t,TUyuAtJt[gtt","fields":{"VALUE0":500}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"=lzU@X{Abe%zg~^nO.6@","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"RIh%h@N$a}vqEF#Zp1Wq","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"n@xie0|AS6:f=|5rnTti","fields":{"VALUE0":-950}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"buT.xAO3Ymk`qF}y^G43","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"Gc1sn!2*RE}9$w3vz[Hy","extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_DRIVE_CURVE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"[3t#bRQ2,]@noEg%uER$","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"!!5=E/amYs;5VxJ(^Y33","fields":{"VALUE0":-450}}},"ARG1":{"shadow":{"type":"unit_angle","id":"+KwVv%+n;Y1u{.n=49S,","fields":{"VALUE0":35}}},"ARG2":{"shadow":{"type":"parameters_stop_4","id":"TDf5JNB`rEAp0MycuD{L","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"dQ8mNu(dc#AribS?//0~","extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_DRIVE_TURN"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"^^;@sMgY8^GVtAVo)GAR","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angle","id":"_69Oz~4-c!6V[Z-Fg+(~","fields":{"VALUE0":-25}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"2i/XW:#]zdRWmz=kUAd|","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"^eZV[sW57=~xW7(W,$ty","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"?6sJ3G^AFYD$`%V6t$]M","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"-/FjyIyp=8OG:kD}LF=l","fields":{"VALUE0":-550}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"^d3RI]{`63pl++y*:J26","fields":{"VALUE":"Stop.HOLD"}}}}}}}}}}}}}}}}}}}}}}}}},{"type":"variables_setup_function","id":"Ow#c8IS[WwV5`vbnpC?C","x":631,"y":86,"extraState":{"optionLevel":0},"fields":{"ICON":"TASK","VAR":{"id":"=!LihrfB68WooWqZT^-H"}},"inputs":{"STACK":{"block":{"type":"blockDriveBaseUseGyro","id":"i0[2xP(hbS4rUm6[_$.e","fields":{"METHOD":"DRIVEBASE_USE_GYRO_TRUE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"3HF:j/bD/Z_iOCXlMg5x","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"8#!kA^qYtEuh58AO`r2r","extraState":{"optionLevel":1},"fields":{"METHOD":"DRIVEBASE_STRAIGHT_SPEED"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"e]S)v;s9S$%-xOHr,Pw{","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_speed","id":"uHK$b#c`$w=7V:`8h|~t","fields":{"VALUE0":400}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"}Ep$}GA+P@KY(2XuOb6F","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_STRAIGHT_ACCELERATION"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"vC7(y/b`H=g+N{CDd!AQ","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_acceleration","id":":EA9kS5$Lmnl[IC~B=cr","fields":{"VALUE0":100}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"P,pN2WYCrXr/qM4gcoTg","extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_TURN_RATE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"tznWYotxGLvb!UY5(t,U","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angularVelocity","id":"k_^ho7xab._v|nKDybIR","fields":{"VALUE0":150}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"0A.YEf:04?!x^%~{TZd;","extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_TURN_ACCELERATION"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"pNxH1g686:UQi~n$?`E?","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angularAcceleration","id":"V:/F?riw,QO+!J$v;,n5","fields":{"VALUE0":750}}}}}}}}}}}}}}}},{"type":"variables_setup_function","id":"fSf9p?d!XjY$(zO~Cfc.","x":641,"y":435,"extraState":{"optionLevel":0},"fields":{"ICON":"TASK","VAR":{"id":"WUSH@2B%z{S|~exs8=^u"}},"inputs":{"STACK":{"block":{"type":"blockDriveBaseUseGyro","id":"~Sf1q*JCnz){]|#73vsw","fields":{"METHOD":"DRIVEBASE_USE_GYRO_TRUE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"Vr(^gadiYu6$Np0-E``b","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":".g_3P7f`sB*Y/,uzY{Ct","extraState":{"optionLevel":1},"fields":{"METHOD":"DRIVEBASE_STRAIGHT_SPEED"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"b|TJC,#QWo=rj6#20lQ:","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_speed","id":"pnmSk1Xv%Eva$Khi-uKl","fields":{"VALUE0":400}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"8nG{=-x1_p)sb/3-wKl0","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_STRAIGHT_ACCELERATION"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"FR}q0o(Iq,DwLns)6Z=(","fields":{"VAR":{"id":"=Z?niE;VLs]q[|2Qb:`1","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_acceleration","id":"L[aC@ua+d-i2%5L$0gA?","fields":{"VALUE0":1000}}}}}}}}}}}}]},"variables":[{"name":"red","id":"k2z)d[K8+v_S_/=_n?bL","type":"ColorDef"},{"name":"orange","id":"R?7~hpLM(qVLUs);?-+F","type":"ColorDef"},{"name":"yellow","id":"`V3hi$kX!!A:mVwq`BNU","type":"ColorDef"},{"name":"green","id":"-HrtFAEu.T!!Q8}/boU0","type":"ColorDef"},{"name":"cyan","id":"^+mxhXS=G5!cR4Cb3L69","type":"ColorDef"},{"name":"blue","id":"D1v!bspE~Ck+W,A=9Sk#","type":"ColorDef"},{"name":"violet","id":"L((8;%uOT/J1W(ttWa-T","type":"ColorDef"},{"name":"magenta","id":"NHU{NSy!V1.NTXfzY4Np","type":"ColorDef"},{"name":"white","id":"`qq1L=C?`_g=|Hpj,/Q%","type":"ColorDef"},{"name":"none","id":"qo6|0csK5d;}z#86.1^t","type":"ColorDef"},{"name":"prime hub","id":"fEhq)iedyzg5lK1##D=s","type":"PrimeHub"},{"name":"left","id":"u%E,Y!H;hn8[F;isp,m4","type":"Motor"},{"name":"right","id":"]dX^t^dQ8Yj)v3+e^]}1","type":"Motor"},{"name":"mediumSpeed","id":"=!LihrfB68WooWqZT^-H","type":"Function"},{"name":"fastSpeed","id":"WUSH@2B%z{S|~exs8=^u","type":"Function"},{"name":"robot","id":"=Z?niE;VLs]q[|2Qb:`1","type":"DriveBase"},{"name":"drive base","id":"]p$3L,J9a,^?lJeV$Q4_","type":"DriveBase"}],"info":{"type":"pybricks","version":"1.2.3"}}
from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
robot = DriveBase(left, right, 88, 97)

def mediumSpeed():
    robot.use_gyro(True)
    robot.settings(straight_speed=400)
    robot.settings(straight_acceleration=100)
    robot.settings(turn_rate=150)
    robot.settings(turn_acceleration=750)

def fastSpeed():
    robot.use_gyro(True)
    robot.settings(straight_speed=400)
    robot.settings(straight_acceleration=1000)


# The main program starts here.
mediumSpeed()
robot.straight(-420)
robot.turn(105) # flick the crab traps
robot.curve(-4000, -9) # pick up the krill and coral
robot.turn(-115) # turn to face the correct side to go across
wait(500)
robot.straight(-950) # go across
robot.curve(-450, 35) # pick up more hings
robot.turn(-25) # turn to pick up the last thing
robot.straight(-550) # go home
