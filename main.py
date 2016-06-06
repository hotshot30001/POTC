import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from pandac.PandaModules import CardMaker
from pandac.PandaModules import NodePath
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
import time

class ObjectServer(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ObjectServer')
    
    def __init__(Cat, cr):
        DistributedObject.DistributedObject.__init__(Cat, cr)

 
loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_tortuga.jpg', pos = (0, 20, .3), parent=render2d)
loadingImage1.setScale(.7)
loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
loadingImage.reparentTo(aspect2d)      
loadingImage.setPos(0, 0, 0.0)
loadingImage.setScale(.21)
base.graphicsEngine.renderFrame()
base.graphicsEngine.renderFrame()


from direct.task import Task
from direct.actor.Actor import Actor
from direct.showbase import DirectObject
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker

from panda3d.core import *

from panda3d.ode import *
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
import random
from direct.directtools.DirectGeometry import LineNodePath
#Print that version info!
print("This version is as of May 24th, 2014 at 11:41AM.")

#Load That Sky!

sky = loader.loadModel("phase_2/models/sky/PiratesSkyDome.bam")
sky.reparentTo(render)
"""
cloudcover = loader.loadModel("cloudOverlay.bam")
cloudcover.ls()
cloudcover.reparentTo(sky)
"""
LightClouds = loader.loadTexture("phase_2/maps/clouds_light.jpg")
MediumClouds = loader.loadTexture("phase_2/maps/clouds_medium.jpg")
Stars = loader.loadTexture("phase_2/maps/stars.jpg")

sky.findAllMatches("**/CloudsTop").show()
sky.findAllMatches("**/Top").hide()
sky.findAllMatches("**/Horizon").show()
sky.findAllMatches("**/Sides").show()

sky.setColor(0.25,0.5,1.5,1)
sky.setTexture(MediumClouds,1)


####################################################################

#moon = loader.loadModel("stars.bam")
#moon.reparentTo(sky)

#moon.place()

####################################################################

select = loader.loadModel("phase_2/models/gui/avatar_chooser_rope.bam")

cavernson = False
cavernsoff = False
SmashoOn = False
Cat = Actor("phase_2/models/char/mp_2000.bam",
											{"running-jump-idle":"phase_2/models/char/mp_jump.bam",
											"walk":"phase_2/models/char/mp_walk.bam",
											"turnLeft1":"phase_2/models/char/mp_spin_left.bam",
											"turnRight2":"phase_2/models/char/mp_spin_right.bam",
											"neutral":"phase_2/models/char/mp_idle_centered.bam",
											"run":"phase_2/models/char/mp_run.bam",
                                                                                        "sweep":"phase_3/models/char/mp_cutlass_sweep.bam"})


Cat.reparentTo(render)
sweepLen=Cat.getNumFrames('sweep')
print(sweepLen)
Cat.findAllMatches("**/clothing_layer1*").hide() 
Cat.findAllMatches("**/clothing_layer2*").hide() 
Cat.findAllMatches("**/clothing_layer3*").hide() 
Cat.findAllMatches("**/hair*").hide()
Cat.findAllMatches("**/acc*").hide() 
Cat.findAllMatches("**/beard*").hide() 
Cat.findAllMatches("**/mustache*").hide() 
Cat.findAllMatches("**/gh_master_face*").hide()
Cat.findAllMatches("**/body_armpit*").hide()
Cat.findAllMatches("**/body_forearm*").hide()
Cat.findAllMatches("**/body_foot*").hide()
Cat.findAllMatches("**/body_shoulder*").hide()
Cat.findAllMatches("**/body_torso*").hide()
Cat.findAllMatches("**/body_waist*").hide()
Cat.findAllMatches("**/body_knee*").hide()
Cat.findAllMatches('**/body_belt').hide()

Cat.findAllMatches('**/clothing_layer1_hat_barbossa').show()
Cat.findAllMatches('**/clothing_layer1_hat_barbossa_feather').show()
Cat.findAllMatches('**/clothing_layer2_vest_long_closed_legs_front').show()
Cat.findAllMatches('**/clothing_layer2_vest_long_closed_torso_front').show()
Cat.findAllMatches('**/clothing_layer3_coat_long_torso').show()
Cat.findAllMatches('**/clothing_layer3_coat_long_legs').show()
Cat.findAllMatches('**/clothing_layer1_pant_tucked_base').show()
Cat.findAllMatches('**/clothing_layer2_belt_square').show()
Cat.findAllMatches('**/clothing_layer2_belt_buckle_square').show()
Cat.findAllMatches('**/clothing_layer1_shoe_boot_tall_left').show()
Cat.findAllMatches('**/clothing_layer1_shoe_boot_tall_right').show()

hat = loader.loadTexture('phase_2/maps/PM_hat_barbossa.jpg')
Cat.find('**/clothing_layer1_hat_barbossa').setTexture(hat, 1)

coat = loader.loadTexture('phase_2/maps/PM_coat_long_zombie.jpg')
Cat.find('**/clothing_layer3_coat_long_torso').setTexture(coat, 1)
Cat.find('**/clothing_layer3_coat_long_legs').setTexture(coat, 1)

pants = loader.loadTexture('phase_2/maps/PM_pant_long_pants_tucked_brown_sidebuttons.jpg')
Cat.find('**/clothing_layer1_pant_tucked_base').setTexture(pants, 1)

CatrightHand1 = Cat.exposeJoint(None, 'modelRoot', 'weapon_left')
Sword1 = Actor("phase_3/models/handheld/musket_bayonet.bam")
Sword1.reparentTo(CatrightHand1)
Sword1.setHpr(Cat.getHpr())
Cat.sweep=False
Veteran1 = Actor("phase_2/models/char/mp_2000.bam",
											{"drill":"phase_4/models/char/mp_bayonet_drill.bam",
											"walk":"phase_4/models/char/mp_bayonet_attack_walk.bam",
                                                                                        "GuardDeath":"phase_3/models/char/mp_death.bam"})
Veteran2 = Actor("phase_2/models/char/mp_2000.bam",
											{"drill":"phase_4/models/char/mp_bayonet_drill.bam",
											"walk":"phase_4/models/char/mp_bayonet_attack_walk.bam",
                                                                                        "GuardDeath":"phase_3/models/char/mp_death.bam"})
Veteran3 = Actor("phase_2/models/char/mp_2000.bam",
											{"drill":"phase_4/models/char/mp_bayonet_drill.bam",
											"walk":"phase_4/models/char/mp_bayonet_attack_walk.bam",
                                                                                        "GuardDeath":"phase_3/models/char/mp_death.bam"})
Veteran4 = Actor("phase_2/models/char/mp_2000.bam",
											{"drill":"phase_4/models/char/mp_bayonet_drill.bam",
											"walk":"phase_4/models/char/mp_bayonet_attack_walk.bam",
                                                                                        "GuardDeath":"phase_3/models/char/mp_death.bam"})
Veteran5 = Actor("phase_2/models/char/mp_2000.bam",
											{"drill":"phase_4/models/char/mp_bayonet_drill.bam",
											"walk":"phase_4/models/char/mp_bayonet_attack_walk.bam",
                                                                                        "GuardDeath":"phase_3/models/char/mp_death.bam"})
Veteran6 = Actor("phase_2/models/char/mp_2000.bam",
											{"drill":"phase_4/models/char/mp_bayonet_drill.bam",
											"walk":"phase_4/models/char/mp_bayonet_attack_walk.bam",
                                                                                        "GuardDeath":"phase_3/models/char/mp_death.bam"})
Veteran = [Veteran1, Veteran2, Veteran3, Veteran4, Veteran5, Veteran6]
Guard1 = Actor("phase_2/models/char/mp_2000.bam",{"GuardDeath":"phase_3/models/char/mp_death.bam"})
Guard2 = Actor("phase_2/models/char/mp_2000.bam",{"GuardDeath":"phase_3/models/char/mp_death.bam"})
Guards = [Guard1, Guard2]
for i in Veteran:
    i.health=100
    i.dead=False
for i in Guards:
    i.health=75
    i.dead=False
Enemies = [Veteran1, Veteran2, Veteran3, Veteran4, Veteran5, Veteran6, Guard1, Guard2]

Remington = Actor("phase_2/models/char/mp_2000.bam")

CutlassSweep = base.loader.loadSfx("phase_3/audio/sfx_cutlass_sweep.mp3")

def tortugaTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_tortuga.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,-817.23,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].reparentTo(render)
		Guards[i].findAllMatches("**/clothing_layer1*").hide() 
		Guards[i].findAllMatches("**/clothing_layer2*").hide() 
		Guards[i].findAllMatches("**/clothing_layer3*").hide() 
		Guards[i].findAllMatches("**/hair*").hide()
		Guards[i].findAllMatches("**/acc*").hide() 
		Guards[i].findAllMatches("**/beard*").hide() 
		Guards[i].findAllMatches("**/mustache*").hide() 
		Guards[i].findAllMatches("**/gh_master_face*").hide()
		Guards[i].findAllMatches("**/body_armpit*").hide()
		Guards[i].findAllMatches("**/body_forearm*").hide()
		Guards[i].findAllMatches("**/body_foot*").hide()
		Guards[i].findAllMatches("**/body_shoulder*").hide()
		Guards[i].findAllMatches("**/body_torso*").hide()
		Guards[i].findAllMatches("**/body_waist*").hide()
		Guards[i].findAllMatches("**/body_knee*").hide()
		Guards[i].findAllMatches("**/body_belt*").hide()
		Guards[i].findAllMatches("**/clothing_layer3_coat_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_pant_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_shoe_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_shoe__india_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_hat_navy*").show()
		gua = TextNode('node name')
		gua.setText("Sergeant Lv 12")
		textNodePath = aspect2d.attachNewNode(gua)
		textNodePath.setScale(.5)
		textNodePath.reparentTo(Guards[i])
		textNodePath.setPos(-1.5, 0, 7.1)
		CatrightHand = Guards[i].exposeJoint(None, 'modelRoot', 'weapon_right')
		Sword = Actor("phase_3/models/handheld/pir_m_hnd_swd_davyJones_j.bam")
		Sword.reparentTo(CatrightHand)
		Sword.setHpr(Cat.getHpr())
	###############################
	#Tortuga
	TortugaModel.reparentTo(render)
	TortugaOcean.reparentTo(render)
	TortugaBuildings.reparentTo(render)
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	spawnpos = random.randint(1,2)
	if spawnpos == 1:
		Cat.setY(-597.64)
		Cat.setX(23.68)
		Cat.setZ(4.21)
		Cat.setH(368.84)
		Guards[1].setY(-597.64)
		Guards[1].setX(23.68)
		Guards[1].setZ(4.21)
		Guards[1].setH(368.84)
	elif spawnpos == 2:
		Cat.setY(-152.03)
		Cat.setX(325.4)
		Cat.setZ(1.6)
		Cat.setH(442.16)
		Guards[1].setY(-152.03)
		Guards[1].setX(325.4)
		Guards[1].setZ(1.6)
		Guards[1].setH(221.16)
	for i in range(len(audio)):
		audio[i].stop()
	audio[1].setLoop(True)
	audio[1].play()	
	audio[1].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()

	
tortugabutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
							         select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=tortugaTeleport)
tortugabutton.setPos(1.54,0,-0.25)	

textPlayer1 = TextNode('node name')
textPlayer1.setText("Tortuga")
textNodePathPlayer1 = aspect2d.attachNewNode(textPlayer1)
textNodePathPlayer1.setScale(.16)
textNodePathPlayer1.reparentTo(tortugabutton)
textPlayer1.setTextColor(1,1,1,1)
textNodePathPlayer1.setPos(-0.28,0,.1)


def devilsTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_anvil.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = True
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.reparentTo(render)
	DevilsBuildings.reparentTo(render)
	DevilsOcean.reparentTo(render)
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-521.49)
	Cat.setX(-5.04)
	Cat.setZ(3.93)
	Cat.setH(343.1)
	for i in range(len(audio)):
		audio[i].stop()
	audio[0].setLoop(True)
	audio[0].play()
	audio[0].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
devilsbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
							   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=devilsTeleport)
devilsbutton.setPos(1.54,0,0)

textPlayer2 = TextNode('node name')
textPlayer2.setText("Devil's Anvil")
textNodePathPlayer2 = aspect2d.attachNewNode(textPlayer2)
textNodePathPlayer2.setScale(.16)
textNodePathPlayer2.reparentTo(devilsbutton)
textPlayer2.setTextColor(1,1,1,1)
textNodePathPlayer2.setPos(-0.40,0,.1)


def cubaTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_cuba.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.reparentTo(render)
	CubaBuildings.reparentTo(render)
	CubaOcean.reparentTo(render)
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-772.75)
	Cat.setX(-128.39)
	Cat.setZ(2.04)
	Cat.setH(426.83)
	for i in range(len(audio)):
		audio[i].stop()
	audio[3].setLoop(True)
	audio[3].play()
	audio[3].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
cubabutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
								  select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=cubaTeleport)
cubabutton.setPos(1.54,0,-0.125)


textPlayer3 = TextNode('node name')
textPlayer3.setText("Cuba")
textNodePathPlayer3 = aspect2d.attachNewNode(textPlayer3)
textNodePathPlayer3.setScale(.16)
textNodePathPlayer3.reparentTo(cubabutton)
textPlayer3.setTextColor(1,1,1,1)
textNodePathPlayer3.setPos(-0.20,0,.1)


def delFuegoTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_del_fuego.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = True
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = True
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.reparentTo(render)
	delFuegoBuildings.reparentTo(render)
	delFuegoOcean.reparentTo(render)
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(288.05)
	Cat.setX(-1369.14)
	Cat.setZ(8.69)
	Cat.setH(-674.71)
	for i in range(len(audio)):
		audio[i].stop()
	audio[4].setLoop(True)
	audio[4].play()
	audio[4].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
delFuegobutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									  select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=delFuegoTeleport)
delFuegobutton.setPos(1.54,0,-0.375)


textPlayer5 = TextNode('node name')
textPlayer5.setText("Padres Del Fuego")
textNodePathPlayer5 = aspect2d.attachNewNode(textPlayer5)
textNodePathPlayer5.setScale(.16)
textNodePathPlayer5.reparentTo(delFuegobutton)
textPlayer5.setTextColor(1,1,1,1)
textNodePathPlayer5.setPos(-0.5,0,.1)



def cangrejosTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_cangrejos.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.reparentTo(render)
	CangrejosBuildings.reparentTo(render)
	CangrejosOcean.reparentTo(render)
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-147.48)
	Cat.setX(-17.43)
	Cat.setZ(2.75)
	Cat.setH(-31.22)
	for i in range(len(audio)):
		audio[i].stop()
	audio[2].setLoop(True)
	audio[2].play()
	audio[2].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
cangrejosbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=cangrejosTeleport)
cangrejosbutton.setPos(1.54,0,-0.5)



textPlayer4 = TextNode('node name')
textPlayer4.setText("Isla Cangrejos")
textNodePathPlayer4 = aspect2d.attachNewNode(textPlayer4)
textNodePathPlayer4.setScale(.16)
textNodePathPlayer4.reparentTo(cangrejosbutton)
textPlayer4.setTextColor(1,1,1,1)
textNodePathPlayer4.setPos(-0.41,0,.1)



def driftwoodTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_driftwood.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.reparentTo(render)
	DriftwoodBuildings.reparentTo(render)
	DriftwoodOcean.reparentTo(render)
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-125.1)
	Cat.setX(-114.20)
	Cat.setZ(1.43)
	Cat.setH(-343.39)
	for i in range(len(audio)):
		audio[i].stop()
	audio[5].setLoop(True)
	audio[5].play()
	audio[5].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()

driftwoodbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=driftwoodTeleport)
driftwoodbutton.setPos(1.54,0,-0.625)


textPlayer6 = TextNode('node name')
textPlayer6.setText("Driftwood Island")
textNodePathPlayer6 = aspect2d.attachNewNode(textPlayer6)
textNodePathPlayer6.setScale(.16)
textNodePathPlayer6.reparentTo(driftwoodbutton)
textPlayer4.setTextColor(1,1,1,1)
textNodePathPlayer6.setPos(-0.5,0,.1)

def kingsheadTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_kingshead.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.reparentTo(render)
	KingsheadBuildings.reparentTo(render)
	KingsheadOcean.reparentTo(render)
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(437.59)
	Cat.setX(-943.02)
	Cat.setZ(21.06)
	Cat.setH(-799.58)
	for i in range(len(audio)):
		audio[i].stop()
	audio[6].setLoop(True)
	audio[6].play()
	audio[6].setVolume(0.25)
	for i in range(0,6):
		Veteran[i].reparentTo(render)
		Veteran[i].findAllMatches("**/clothing_layer1*").hide() 
		Veteran[i].findAllMatches("**/clothing_layer2*").hide() 
		Veteran[i].findAllMatches("**/clothing_layer3*").hide() 
		Veteran[i].findAllMatches("**/hair*").hide()
		Veteran[i].findAllMatches("**/acc*").hide() 
		Veteran[i].findAllMatches("**/beard*").hide() 
		Veteran[i].findAllMatches("**/mustache*").hide() 
		Veteran[i].findAllMatches("**/gh_master_face*").hide()
		Veteran[i].findAllMatches("**/body_armpit*").hide()
		Veteran[i].findAllMatches("**/body_forearm*").hide()
		Veteran[i].findAllMatches("**/body_foot*").hide()
		Veteran[i].findAllMatches("**/body_shoulder*").hide()
		Veteran[i].findAllMatches("**/body_torso*").hide()
		Veteran[i].findAllMatches("**/body_waist*").hide()
		Veteran[i].findAllMatches("**/body_knee*").hide()
		Veteran[i].findAllMatches("**/body_belt*").hide()
		Veteran[i].findAllMatches("**/clothing_layer3_coat_navy*").show()
		Veteran[i].findAllMatches("**/clothing_layer1_pant_navy*").show()
		Veteran[i].findAllMatches("**/clothing_layer1_shoe_navy*").show()
		Veteran[i].findAllMatches("**/clothing_layer1_shoe__india_navy*").show()
		Veteran[i].findAllMatches("**/clothing_layer1_hat_navy*").show()
		Veteran[i].loop("drill")
		rightHand = Veteran[i].exposeJoint(None, 'modelRoot', 'weapon_right')
		bayonet = Actor("phase_3/models/handheld/musket_bayonet.bam")
		bayonet.reparentTo(rightHand)
		vet = TextNode('node name')
		vet.setText("Veteran Lv 18")
		textNodePath = aspect2d.attachNewNode(vet)
		textNodePath.setScale(.5)
		textNodePath.reparentTo(Veteran[i])
		textNodePath.setPos(-1.5, 0, 7.1)
	for i in range(0,2):
		Guards[i].reparentTo(render)
		Guards[i].findAllMatches("**/clothing_layer1*").hide() 
		Guards[i].findAllMatches("**/clothing_layer2*").hide() 
		Guards[i].findAllMatches("**/clothing_layer3*").hide() 
		Guards[i].findAllMatches("**/hair*").hide()
		Guards[i].findAllMatches("**/acc*").hide() 
		Guards[i].findAllMatches("**/beard*").hide() 
		Guards[i].findAllMatches("**/mustache*").hide() 
		Guards[i].findAllMatches("**/gh_master_face*").hide()
		Guards[i].findAllMatches("**/body_armpit*").hide()
		Guards[i].findAllMatches("**/body_forearm*").hide()
		Guards[i].findAllMatches("**/body_foot*").hide()
		Guards[i].findAllMatches("**/body_shoulder*").hide()
		Guards[i].findAllMatches("**/body_torso*").hide()
		Guards[i].findAllMatches("**/body_waist*").hide()
		Guards[i].findAllMatches("**/body_knee*").hide()
		Guards[i].findAllMatches("**/body_belt*").hide()
		Guards[i].findAllMatches("**/clothing_layer3_coat_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_pant_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_shoe_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_shoe__india_navy*").show()
		Guards[i].findAllMatches("**/clothing_layer1_hat_navy*").show()
		gua = TextNode('node name')
		gua.setText("Sergeant Lv 12")
		textNodePath = aspect2d.attachNewNode(gua)
		textNodePath.setScale(.5)
		textNodePath.reparentTo(Guards[i])
		textNodePath.setPos(-1.5, 0, 7.1)
		CatrightHand = Guards[i].exposeJoint(None, 'modelRoot', 'weapon_right')
		Sword = Actor("phase_3/models/handheld/pir_m_hnd_swd_davyJones_j.bam")
		Sword.reparentTo(CatrightHand)
		Sword.setHpr(Cat.getHpr())
	Remington.reparentTo(render)
	Remington.findAllMatches("**/clothing_layer1*").hide()	
	Remington.findAllMatches("**/clothing_layer2*").hide() 
	Remington.findAllMatches("**/clothing_layer3*").hide() 
	Remington.findAllMatches("**/hair*").hide()
	Remington.findAllMatches("**/acc*").hide() 
	Remington.findAllMatches("**/beard*").hide() 
	Remington.findAllMatches("**/mustache*").hide() 
	Remington.findAllMatches("**/gh_master_face*").hide()
	Remington.findAllMatches("**/body_armpit*").hide()
	Remington.findAllMatches("**/body_forearm*").hide()
	Remington.findAllMatches("**/body_foot*").hide()
	Remington.findAllMatches("**/body_shoulder*").hide()
	Remington.findAllMatches("**/body_torso*").hide()
	Remington.findAllMatches("**/body_waist*").hide()
	Remington.findAllMatches("**/body_knee*").hide()
	Remington.findAllMatches("**/body_belt*").hide()
	Remington.findAllMatches("**/clothing_layer3_coat_eitc*").show()
	Remington.findAllMatches("**/clothing_layer1_pant_eitc*").show()
	Remington.find("**/hair_a1").show()
	Remington.setY(-694.25)
	Remington.setX(209.96)
	Remington.setZ(222.9)
	Remington.setH(881.13)
	Veteran1.setY(656.31)
	Veteran1.setX(-281.65)
	Veteran1.setZ(67.98)
	Veteran1.setH(630.4)
	Veteran2.setY(656.31)
	Veteran2.setX(-291.65)
	Veteran2.setZ(67.98)
	Veteran2.setH(630.4)
	Veteran3.setY(646.31)
	Veteran3.setX(-281.65)
	Veteran3.setZ(67.98)
	Veteran3.setH(630.4)
	Veteran4.setY(646.31)
	Veteran4.setX(-291.65)
	Veteran4.setZ(67.98)
	Veteran4.setH(630.4)
	Veteran5.setY(636.31)
	Veteran5.setX(-281.65)
	Veteran5.setZ(67.98)
	Veteran5.setH(630.4)
	Veteran6.setY(636.31)
	Veteran6.setX(-291.65)
	Veteran6.setZ(67.98)
	Veteran6.setH(630.4)
	Guard1.setY(504)
	Guard1.setX(-536.92)
	Guard1.setZ(59.71)
	Guard1.setH(-1345.72)
	Guard2.setY(531.25)
	Guard2.setX(-536.92)
	Guard2.setZ(59.71)
	Guard2.setH(-1345.72)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
kingsheadbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=kingsheadTeleport)
kingsheadbutton.setPos(1.54,0,-0.75)


textPlayer7 = TextNode('node name')
textPlayer7.setText("Kingshead")
textNodePathPlayer7 = aspect2d.attachNewNode(textPlayer7)
textNodePathPlayer7.setScale(.16)
textNodePathPlayer7.reparentTo(kingsheadbutton)
textPlayer4.setTextColor(1,1,1,1)
textNodePathPlayer7.setPos(-0.35,0,.1)


def pvpSpanishTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_avaricia.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.reparentTo(render)
	pvpSpanishBuildings.reparentTo(render)
	pvpSpanishOcean.reparentTo(render)
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(130.79)
	Cat.setX(234.70)
	Cat.setZ(1.18)
	Cat.setH(-152)
	for i in range(len(audio)):
		audio[i].stop()
	audio[8].setLoop(True)
	audio[8].play()
	audio[8].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
pvpSpanishbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=pvpSpanishTeleport)
pvpSpanishbutton.setPos(1.54,0,0.125)

textPlayer8 = TextNode('node name')
textPlayer8.setText("Isla de la Avaricia")
textNodePathPlayer8 = aspect2d.attachNewNode(textPlayer8)
textNodePathPlayer8.setScale(.16)
textNodePathPlayer8.reparentTo(pvpSpanishbutton)
textPlayer4.setTextColor(1,1,1,1)
textNodePathPlayer8.setPos(-0.50,0,.1)

def portRoyalTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_portroyal.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.reparentTo(render)
	PRBuildings.reparentTo(render)
	PROcean.reparentTo(render)
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-327.19)
	Cat.setX(-101.33)
	Cat.setZ(11.77)
	Cat.setH(351.15)
	for i in range(len(audio)):
		audio[i].stop()
	audio[7].setLoop(True)
	audio[7].play()
	audio[7].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()


portRoyalbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=portRoyalTeleport)
portRoyalbutton.setPos(1.54,0,0.375)

textPlayer9 = TextNode('node name')
textPlayer9.setText("Port Royal")
textNodePathPlayer9 = aspect2d.attachNewNode(textPlayer9)
textNodePathPlayer9.setScale(.16)
textNodePathPlayer9.reparentTo(portRoyalbutton)
textPlayer9.setTextColor(1,1,1,1)
textNodePathPlayer9.setPos(-0.35,0,.1)

def ravensCoveTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_ravensCove.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = True
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.reparentTo(render)
	RavensBuildings.reparentTo(render)
	RavensOcean.reparentTo(render)
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#Smasho Cave
	SmashoCave.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-18.34)
	Cat.setX(371.03)
	Cat.setZ(6.64)
	Cat.setH(-198.33)
	for i in range(len(audio)):
		audio[i].stop()
	audio[9].setLoop(True)
	audio[9].play()
	audio[9].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
ravensCovebutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=ravensCoveTeleport)
ravensCovebutton.setPos(1.54,0,0.25)

textPlayer10 = TextNode('node name')
textPlayer10.setText("Raven's Cove")
textNodePathPlayer10 = aspect2d.attachNewNode(textPlayer10)
textNodePathPlayer10.setScale(.16)
textNodePathPlayer10.reparentTo(ravensCovebutton)
textPlayer10.setTextColor(1,1,1,1)
textNodePathPlayer10.setPos(-0.40,0,.1)

def outcastTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_tormenta.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.reparentTo(render)
	OutcastBuildings.reparentTo(render)
	OutcastOcean.reparentTo(render)
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(152.33)
	Cat.setX(73.95)
	Cat.setZ(3.54)
	Cat.setH(-363.87)
	for i in range(len(audio)):
		audio[i].stop()
	audio[10].setLoop(True)
	audio[10].play()
	audio[10].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
outcastbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=outcastTeleport)
outcastbutton.setPos(1.54,0,0.5)


textPlayer11 = TextNode('node name')
textPlayer11.setText("Outcast Isle")
textNodePathPlayer11 = aspect2d.attachNewNode(textPlayer11)
textNodePathPlayer11.setScale(.16)
textNodePathPlayer11.reparentTo(outcastbutton)
textPlayer11.setTextColor(1,1,1,1)
textNodePathPlayer11.setPos(-0.38,0,.1)

def cutthroatTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_cutthroat.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.reparentTo(render)
	CutthroatBuildings.reparentTo(render)
	CutthroatOcean.reparentTo(render)
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(151.28)
	Cat.setX(504.49)
	Cat.setZ(13.72)
	Cat.setH(114.24)
	for i in range(len(audio)):
		audio[i].stop()
	audio[11].setLoop(True)
	audio[11].play()
	audio[11].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
cutthroatbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=cutthroatTeleport)
cutthroatbutton.setPos(1.54,0,0.625)


textPlayer12 = TextNode('node name')
textPlayer12.setText("Cutthroat Isle")
textNodePathPlayer12 = aspect2d.attachNewNode(textPlayer12)
textNodePathPlayer12.setScale(.16)
textNodePathPlayer12.reparentTo(cutthroatbutton)
textPlayer12.setTextColor(1,1,1,1)
textNodePathPlayer12.setPos(-0.43,0,.1)

def rumRunnerTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_rum_runners.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.reparentTo(render)
	RumrunnerBuildings.reparentTo(render)
	RumrunnerOcean.reparentTo(render)
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(183.48)
	Cat.setX(-25.21)
	Cat.setZ(2.49)
	Cat.setH(11.61)
	for i in range(len(audio)):
		audio[i].stop()
	audio[12].setLoop(True)
	audio[12].play()
	audio[12].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
rumRunnerbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=rumRunnerTeleport)
rumRunnerbutton.setPos(1.54,0,0.75)

textPlayer13 = TextNode('node name')
textPlayer13.setText("Rumrunner's Island")
textNodePathPlayer13 = aspect2d.attachNewNode(textPlayer13)
textNodePathPlayer13.setScale(.16)
textNodePathPlayer13.reparentTo(rumRunnerbutton)
textPlayer13.setTextColor(1,1,1,1)
textNodePathPlayer13.setPos(-0.60,0,.1)

def tormentaTeleport():
	pvpfrenchbutton.hide()
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	tormentabutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_outcast_island.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = True
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.reparentTo(render)
	TormentaBuildings.reparentTo(render)
	TormentaOcean.reparentTo(render)
	#pvpFrench
	pvpFrenchModel.detachNode()
	pvpFrenchBuildings.detachNode()
	pvpFrenchOcean.detachNode()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-134.57)
	Cat.setX(401.8)
	Cat.setZ(3.67)
	Cat.setH(437.23)
	for i in range(len(audio)):
		audio[i].stop()
	audio[13].setLoop(True)
	audio[13].play()
	audio[13].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
tormentabutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=tormentaTeleport)
tormentabutton.setPos(1.54,0,-0.88)


textPlayer14 = TextNode('node name')
textPlayer14.setText("Isla Tormenta")
textNodePathPlayer14 = aspect2d.attachNewNode(textPlayer14)
textNodePathPlayer14.setScale(.16)
textNodePathPlayer14.reparentTo(tormentabutton)
textPlayer14.setTextColor(1,1,1,1)
textNodePathPlayer14.setPos(-0.40,0,.1)

def pvpFrenchTeleport():
	tortugabutton.hide()
	devilsbutton.hide()
	cubabutton.hide()
	delFuegobutton.hide()
	cangrejosbutton.hide()
	driftwoodbutton.hide()
	kingsheadbutton.hide()
	pvpSpanishbutton.hide()
	portRoyalbutton.hide()
	ravensCovebutton.hide()
	outcastbutton.hide()
	cutthroatbutton.hide()
	rumRunnerbutton.hide()
	pvpfrenchbutton.hide()
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_porc.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	sky.setPos(0,0,0)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	Remington.detachNode()
	for i in range(0,6):
		Veteran[i].detachNode()
	for i in range(0,2):
		Guards[i].detachNode()
	###############################
	#Tortuga
	TortugaModel.detachNode()
	TortugaOcean.detachNode()
	TortugaBuildings.detachNode()
	#PortRoyal
	PRModel.detachNode()
	PRBuildings.detachNode()
	PROcean.detachNode()
	#Devils
	DevilsModel.detachNode()
	DevilsBuildings.detachNode()
	DevilsOcean.detachNode()
	#Cuba
	CubaModel.detachNode()
	CubaBuildings.detachNode()
	CubaOcean.detachNode()
	#DelFuego
	delFuegoModel.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	#Cangrejos
	CangrejosModel.detachNode()
	CangrejosBuildings.detachNode()
	CangrejosOcean.detachNode()
	#Driftwood
	DriftwoodModel.detachNode()
	DriftwoodBuildings.detachNode()
	DriftwoodOcean.detachNode()
	#Kingshead
	KingsheadModel.detachNode()
	KingsheadBuildings.detachNode()
	KingsheadOcean.detachNode()
	#pvpSpanish
	pvpSpanishModel.detachNode()
	pvpSpanishBuildings.detachNode()
	pvpSpanishOcean.detachNode()
	#RavensCove
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	RavensOcean.detachNode()
	#Outcast
	OutcastModel.detachNode()
	OutcastBuildings.detachNode()
	OutcastOcean.detachNode()
	#Cutthroat
	CutthroatModel.detachNode()
	CutthroatBuildings.detachNode()
	CutthroatOcean.detachNode()
	#Rumrunners
	RumrunnerModel.detachNode()
	RumrunnerBuildings.detachNode()
	RumrunnerOcean.detachNode()
	#Tormenta
	TormentaModel.detachNode()
	TormentaBuildings.detachNode()
	TormentaOcean.detachNode()
	#pvpFrench
	pvpFrenchModel.reparentTo(render)
	pvpFrenchBuildings.reparentTo(render)
	pvpFrenchOcean.reparentTo(render)
	#pvpFrench
	pvpFrenchModel.show()
	pvpFrenchBuildings.show()
	pvpFrenchOcean.show()
	#CursedCaverns
	cursed_caverns.detachNode()
	#Grotto
	GrottoModel.detachNode()
	GrottoBuildings.detachNode()
	#BeckettsQuarry
	BeckettsQuarry.detachNode()
	#TheCatacombs
	TheCatacombs.detachNode()
	###############################
	Cat.setY(-210.90)
	Cat.setX(-66.77)
	Cat.setZ(1.47)
	Cat.setH(1083.39)
	for i in range(len(audio)):
		audio[i].stop()
	audio[14].setLoop(True)
	audio[14].play()
	audio[14].setVolume(0.25)
	loadingImage1.removeNode()
	loadingImage.removeNode()
	tortugabutton.show()
	devilsbutton.show()
	cubabutton.show()
	delFuegobutton.show()
	cangrejosbutton.show()
	driftwoodbutton.show()
	kingsheadbutton.show()
	pvpSpanishbutton.show()
	portRoyalbutton.show()
	ravensCovebutton.show()
	outcastbutton.show()
	cutthroatbutton.show()
	rumRunnerbutton.show()
	tormentabutton.show()
	pvpfrenchbutton.show()
	
pvpfrenchbutton = DirectButton(geom = (select.find("**/avatar_c_A_bottom"),
									   select.find("**/avatar_c_A_bottom_over")),relief=None, scale=.4, command=pvpFrenchTeleport)
pvpfrenchbutton.setPos(1.54,0,-1.01)


textPlayer15 = TextNode('node name')
textPlayer15.setText("Ile d'Etable de Porc")
textNodePathPlayer15 = aspect2d.attachNewNode(textPlayer15)
textNodePathPlayer15.setScale(.16)
textNodePathPlayer15.reparentTo(pvpfrenchbutton)
textPlayer15.setTextColor(1,1,1,1)
textNodePathPlayer15.setPos(-0.40,0,.1)

def CursedCaverns():
	sky.setPos(0,0,0)
	global cavernsoff
	cavernsoff = True
	global cavernson
	cavernson = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	cursed_caverns.reparentTo(render)
	for i in range(0,3):
		TormentaModel.detachNode()
		TormentaBuildings.detachNode()
		TormentaOcean.detachNode()
		BeckettsQuarry.detachNode()
		TheCatacombs.detachNode()
	Cat.setY(888.52)
	Cat.setX(24.29)
	Cat.setZ(325.37)
	Cat.setH(-542.63)

def BackToTormenta1():
	sky.setPos(0,0,0)
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = True
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	cursed_caverns.detachNode()
	for i in range(0,3):
		TormentaModel.reparentTo(render)
		TormentaBuildings.reparentTo(render)
		TormentaOcean.reparentTo(render)
		BeckettsQuarry.detachNode()
		TheCatacombs.detachNode()
	Cat.setY(-220.56)
	Cat.setX(-280.93)
	Cat.setZ(12.58)
	Cat.setH(508.07)
	
def BackToTormenta2():
	sky.setPos(0,0,0)
	global cavernsoff
	cavernsoff = False
	global cavernson
	cavernson = True
	global grottooff
	grottooff = False
	global grottoon
	grottoon = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	cursed_caverns.detachNode()
	for i in range(0,3):
		TormentaModel.reparentTo(render)
		TormentaBuildings.reparentTo(render)
		TormentaOcean.reparentTo(render)
		BeckettsQuarry.detachNode()
		TheCatacombs.detachNode()
	Cat.setY(-18.9)
	Cat.setX(152.14)
	Cat.setZ(13.48)
	Cat.setH(248.54)

def BarbossasGrotto():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = False
	global grottooff
	grottooff = True
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	GrottoModel.reparentTo(render)
	GrottoBuildings.reparentTo(render)
	for i in range(0,3):
		DevilsModel.detachNode()
		DevilsBuildings.detachNode()
		BeckettsQuarry.detachNode()
		TheCatacombs.detachNode()
	Cat.setY(-141.89)
	Cat.setX(71.11)
	Cat.setZ(23.19)
	Cat.setH(30.26)

def BackToDevils():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = True
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	DevilsModel.reparentTo(render)
	DevilsBuildings.reparentTo(render)
	for i in range(0,3):
		GrottoModel.detachNode()
		GrottoBuildings.detachNode()
		BeckettsQuarry.detachNode()
		TheCatacombs.detachNode()
	Cat.setY(234.25)
	Cat.setX(153.54)
	Cat.setZ(26.13)
	Cat.setH(335.64)

def beckettsQuarry():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = True
	global bOfPadresOn
	bOfPadresOn = True
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	delFuegoBuildings.detachNode()
	delFuegoOcean.detachNode()
	delFuegoModel.detachNode()
	TheCatacombs.detachNode()
	for i in range(0,3):
		BeckettsQuarry.reparentTo(render)
	Cat.setX(-600.80)
	Cat.setY(140.17)
	Cat.setZ(198.97)
	Cat.setH(268.12)

def BackToPadres1():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = True
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = True
	global CatacombsOff
	CatacombsOff = False
	BeckettsQuarry.detachNode()
	TheCatacombs.detachNode()
	for i in range(0,3):
		delFuegoBuildings.reparentTo(render)
		delFuegoOcean.reparentTo(render)
		delFuegoModel.reparentTo(render)
	Cat.setX(-943.23)
	Cat.setY(-350.32)
	Cat.setZ(6.08)
	Cat.setH(14.19)

def BackOfPadres():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = True
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	BeckettsQuarry.detachNode
	TheCatacombs.detachNode()
	for i in range(0,3):
		delFuegoBuildings.reparentTo(render)
		delFuegoOcean.reparentTo(render)
		delFuegoModel.reparentTo(render)
	Cat.setX(-292.30)
	Cat.setY(-625.25)
	Cat.setZ(37.27)
	Cat.setH(76.64)

def FoulbertoCave():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = True
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = False
	RavensOcean.detachNode()
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	SmashoCave.reparentTo(render)
	TheCatacombs.detachNode()
	Cat.setX(13.69)
	Cat.setY(-17.54)
	Cat.setZ(100.05)
	Cat.setH(19.25)

def CatacombsTeleport():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = False
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = False
	global CatacombsOff
	CatacombsOff = True
	RavensOcean.detachNode()
	RavensModel.detachNode()
	RavensBuildings.detachNode()
	SmashoCave.detachNode()
	delFuegoOcean.detachNode()
	delFuegoBuildings.detachNode()
	delFuegoModel.detachNode()
	TheCatacombs.reparentTo(render)
	Cat.setX(-227.4562)
	Cat.setY(426.0312)
	Cat.setZ(-42.1891)
	Cat.setH(-96.7632)

def BackToPadres1():
	sky.setPos(0,0,0)
	global grottoon
	grottoon = False
	global grottooff
	grottooff = False
	global bQuarryOn
	bQuarryOn = True
	global bQuarryOff
	bQuarryOff = False
	global bOfPadresOn
	bOfPadresOn = False
	global SmashoOn
	SmashoOn = False
	global CatacombsOn
	CatacombsOn = True
	BeckettsQuarry.detachNode()
	TheCatacombs.detachNode()
	for i in range(0,3):
		delFuegoBuildings.reparentTo(render)
		delFuegoOcean.reparentTo(render)
		delFuegoModel.reparentTo(render)
	Cat.setX(-712.737)
	Cat.setY(247.7662)
	Cat.setZ(18.2899)
	Cat.setH(-694.690)

text = TextNode('node name')
text.setText("Hector FireMorgan")
textNodePath = aspect2d.attachNewNode(text)
textNodePath.setScale(.5)
textNodePath.reparentTo(Cat)
textNodePath.setPos(-1.5, 0, 7.1)
Impress = loader.loadFont('phase_2/models/fonts/BriosoPro_chipped_outline.bam')
text.setTextColor(0.9, 0.3, 0.9, 1)
text.setCardColor(0.8, 0.8, 0.8, 0.001)
text.setCardAsMargin(.1, .2, .2, .1)
text.setCardDecal(True)

GM = loader.loadModel("phase_2/models/gui/gmLogo_tflip.bam")
GM.reparentTo(Cat)
GM.setScale(1)
GM.setPos(0, 0, 8.15)

founder = loader.loadModel("phase_2/models/gui/toplevel_gui_founder.bam")
founder.reparentTo(aspect2d)
switch = founder.find("**/+SwitchNode")
switch.node().setVisibleChild(70)
founder.reparentTo(Cat)
founder.setScale(1.5)
founder.setPos(-1.75, 0, 7.25)

fswalk = loader.loadSfx('phase_2/audio/sfx_avatar_run_sandx2.ogg')
 
geom = Cat.getGeomNode()
geom.getChild(0).setSx(1.0)
geom.getChild(0).setSy(1.0)
geom.getChild(0).setSz(1.0)
geom.getChild(0).setH(180)

offset = 3.2375
 
base.camera.reparentTo(Cat)
base.camera.setPos(0, -12.0 - offset, offset)
base.disableMouse()
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()

def getAirborneHeight():
    return offset + 0.025000000000000001
walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(30.0, 30.0, 15.0, 80.0)
walkControls.initializeCollisions(base.cTrav, Cat, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
Cat.physControls = walkControls
 
def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        if active == True:
            inputState.set(input, True)
            keyMap[keyMapName] = 1
        else:
            inputState.set(input, False)
            keyMap[keyMapName] = 0
    base.accept(key, watchKey, [True])
    base.accept(key+'-up', watchKey, [False])
 
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'space':0, 'z':0}

setWatchKey('z','sweep','z') 
setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('space', 'jump', 'space')
 
movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False

def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral
    global movingForward
    global movingRotation
    global movingBackward
    global movingJumping
    if 'jump' in loopName:
        movingJumping = True
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'run':
        movingJumping = False
        movingForward = True
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'walk':
        movingJumping = False
        movingForward = False
        movingNeutral = False
        if playRate == -1.0:
            movingBackward = True
            movingRotation = False
    elif loopName == 'turnLeft1':
	    movingJumping = False
	    movingForward = False
	    movingNeutral = False
	    movingRotation = True
	    movingBackward = False
    elif loopName == 'turnRight2':
	    movingJumping = False
	    movingForward = False
	    movingNeutral = False
	    movingRotation = True
	    movingBackward = False
    elif loopName == 'neutral':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    elif loopName == 'sweep':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    else:
        movingJumping = False
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    ActorInterval(Cat, loopName, playRate=playRate).loop()
sweep=False 

def handleMovement(task):
	global BackToTormenta1
	global BackToTormenta2
	global cavernsoff
	global cavernson
	global grottooff
	global grottoon
	global bQuarryOn
	global bQuarryOff
	global bOfPadresOn
	global CatacombsOn
	global CatacombsOff
	global BackToPadres2
	global CursedCaverns
	global SmashoOn
	global CutlassSweep
	global sweep
	Sword1.setHpr(Cat.getHpr())
	if SmashoOn == True:
		if Cat.getY() < 495.19 and Cat.getY() > 486.17 and Cat.getX() < -98.66 and Cat.getX() > -108.04:
			FoulbertoCave()
	if cavernson == True:
		if Cat.getY() > -27 and Cat.getY() < 3 and Cat.getX() < 133 and Cat.getX() > 124:
			CursedCaverns()
		if Cat.getY() < -187 and Cat.getY() > -212 and Cat.getX() > -270 and Cat.getX() < -259:
			CursedCaverns()
	if cavernsoff == True:
		if Cat.getY() > 896 and Cat.getY() < 930  and Cat.getX() > 12 and Cat.getX() < 37:
			BackToTormenta1()
		if Cat.getY() < -784 and Cat.getY() > -824 and Cat.getX() < 311 and Cat.getX() > 278:
			BackToTormenta2()
	global barbossasGrotto
	if grottoon == True:
		if Cat.getY() < 228.56 and Cat.getY() > 218 and Cat.getX() > 131.67 and Cat.getX() < 164.49:
			BarbossasGrotto()
	if grottooff == True:
		if Cat.getY() < -155 and Cat.getY() >  -174 and Cat.getX() > 72.83 and Cat.getX() < 100:
			BackToDevils()
	global PadresCaves
	if bQuarryOn == True:
		if Cat.getY() < -351.63 and Cat.getY() > -366.14 and Cat.getX() > -950.75 and Cat.getX() < -924.17:
			beckettsQuarry()
	if bQuarryOff == True:
		if Cat.getY() < 148.54 and Cat.getY() > 120.14 and Cat.getX() > -622 and Cat.getX() < -611.81:
			BackToPadres1()
	if bOfPadresOn == True:
		if Cat.getY() < 532.58 and Cat.getY() > 531.55 and Cat.getX() > 37.07 and Cat.getX() < 49.10:
			BackOfPadres()
	if CatacombsOn == True:
		if Cat.getY() <  239.2859 and Cat.getY() > 228.5411 and Cat.getX() > -720.2208 and Cat.getX() < -691.6280:
			CatacombsTeleport()
	if CatacombsOff == True:
		if Cat.getY < 441.411 and Cat.getY > 430.9685 and Cat.getX > -239.598 and Cat.getX <  -229.6136:
			BackToPadres2()
	for i in range(0,6):
		if (Cat.getY()) < Veteran[i].getY()+10 and (Cat.getY()) > Veteran[i].getY()-10 and (Cat.getX()) < Veteran[i].getX()+10 and (Cat.getX()) > Veteran[i].getX()-10 and (Cat.getZ()) < Veteran[i].getZ()+10 and (Cat.getZ()) > Veteran[i].getZ()-10:
			Veteran[i].setPos(Cat.getPos())
			Veteran[i].loop("walk")
	if (Cat.getY()) < 220 and (Cat.getY()) > 210 and (Cat.getX()) < 260 and (Cat.getX()) > 250 and (Cat.getZ()) < 35 and (Cat.getZ()) > 25:
		print("Jail!")
	global movingNeutral, movingForward
	global movingRotation, movingBackward, movingJumping
	if keyMap['z'] == 1:
            if Cat.sweep==False:
                setMovementAnimation('sweep')
                CutlassSweep.play()
                sweep=True
                Cat.sweep=True
        if sweep:
            if Cat.getCurrentFrame('sweep')>=sweepLen-10:
                setMovementAnimation('neutral')
                sweep=False
                Cat.sweep=False
        if sweep==False:
            if keyMap['space'] == 1:
                    if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
                            if movingJumping == False:
                                    if Cat.physControls.isAirborne:
                                            setMovementAnimation('running-jump-idle')
                                    else:
                                            if keyMap['forward']:
                                                    if movingForward == False:
                                                            setMovementAnimation('run')
                                            elif keyMap['backward']:
                                                    if movingBackward == False:
                                                            setMovementAnimation('walk', playRate=-1.0)
                                            elif keyMap['left']:
                                                    if movingRotation == False:
                                                            setMovementAnimation('turnLeft1', playRate=1.0)
                                            elif keyMap['right']:
                                                    if movingRotation == False:
                                                            setMovementAnimation('turnRight2', playRate=1.0)
                            else:
                                    if not Cat.physControls.isAirborne:
                                            if keyMap['forward']:
                                                    if movingForward == False:
                                                            setMovementAnimation('run')
                                            elif keyMap['backward']:
                                                    if movingBackward == False:
                                                            setMovementAnimation('walk', playRate=-1.0)
                                            elif keyMap['left']:
                                                    if movingRotation == False:
                                                            setMovementAnimation('turnLeft1', playRate=1.0)
                                            elif keyMap['right']:
                                                    if movingRotation == False:
                                                            setMovementAnimation('turnRight2', playRate=1.0)
                    else:
                            if movingJumping == False:
                                    if Cat.physControls.isAirborne:
                                            setMovementAnimation('running-jump-idle')
                                    else:
                                            if movingNeutral == False:
                                                    setMovementAnimation('neutral')
                            else:
                                    if not Cat.physControls.isAirborne:
                                            if movingNeutral == False:
                                                    setMovementAnimation('neutral')
            elif keyMap['forward'] == 1:
                    if movingForward == False:
                            if not Cat.physControls.isAirborne:
                                    setMovementAnimation('run')
                                    fswalk.setLoop(True)
                                    fswalk.play()
                                    fswalk.setVolume(0.125)
                                    
            elif keyMap['backward'] == 1:
                    if movingBackward == False:
                            if not Cat.physControls.isAirborne:
                                    setMovementAnimation('walk', playRate=-1.0)
            elif keyMap['left']: 
                    if movingRotation == False:
                            if not Cat.physControls.isAirborne:
                                    setMovementAnimation('turnLeft1', playRate=1.0)
            elif keyMap['right']:
                    if movingRotation == False:
                            if not Cat.physControls.isAirborne:
                                    setMovementAnimation('turnRight2', playRate=1.0)
            else:
                    if not Cat.physControls.isAirborne:
                            if movingNeutral == False:
                                    setMovementAnimation('neutral')
                                    fswalk.stop()
	return Task.cont

base.taskMgr.add(handleMovement, 'controlManager')
def combat(task):
    for i in Enemies:
        if Cat.getDistance(i)<=5:
            if sweep:
                i.health-=50
        if i.health<=0:
            if i.dead==False:
                i.play('GuardDeath')
                i.dead=True
    return Task.cont
base.taskMgr.add(combat, 'combat')
                
def collisionsOn():
    Cat.physControls.setCollisionsActive(True)
    Cat.physControls.isAirborne = True
def collisionsOff():
    Cat.physControls.setCollisionsActive(False)
    Cat.physControls.isAirborne = True
def toggleCollisions():
    if Cat.physControls.getCollisionsActive():
        Cat.physControls.setCollisionsActive(False)
        Cat.physControls.isAirborne = True
    else:
        Cat.physControls.setCollisionsActive(True)
        Cat.physControls.isAirborne = True
Cat.collisionsOn = collisionsOn
Cat.collisionsOff = collisionsOff
Cat.toggleCollisions = toggleCollisions



localAvatar = Cat
base.localAvatar = localAvatar
localAvatar.physControls.placeOnFloor()

onScreenDebug.enabled = False

def updateOnScreenDebug(task):
 
    onScreenDebug.add('Avatar Position', localAvatar.getPos())
    onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
 
    return Task.cont


class EnvironmentTTC():

    def __init__(self):
        #Create the dictionary for all the models
        self.modeldict = {}


offset = 3.2375


base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')

def StartOfCords():
	print("Starting Prints")
	def Cordinates1(task):
		print(Cat.getX(),Cat.getY(),Cat.getZ(),Cat.getH())
		return task.again
	myTask = taskMgr.doMethodLater(0.00000001, Cordinates1, 'print pos')


#Tortuga
TortugaOcean = loader.loadModel("phase_5/models/islands/pir_m_are_isl_tortuga_ocean.bam")
TortugaModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_tortuga.bam')
TortugaBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_tortuga.bam')

#DevilsAnvil
DevilsOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_devilsAnvil_ocean.bam')
DevilsModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_devilsAnvil.bam')
DevilsBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_devilsAnvil.bam')

#Cuba
CubaModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_cuba.bam')
CubaBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_cuba.bam')
CubaOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_cuba_ocean.bam')

#DelFuego
delFuegoModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_delFuego.bam')
delFuegoBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_delFuego.bam')
delFuegoOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_delFuego_ocean.bam')

#Cangrejos
CangrejosModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_cangrejos.bam')
CangrejosBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_cangrejos.bam')
CangrejosOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_cangrejos_ocean.bam')

#Driftwood
DriftwoodModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_driftwood.bam')
DriftwoodBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_driftwood.bam')
DriftwoodOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_driftwood_ocean.bam')

#Kinghead
KingsheadModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_kingshead.bam')
KingsheadBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_kingshead.bam')
KingsheadOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_kingshead_ocean.bam')

#Spanish PVP
pvpSpanishModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_pvpSpanish.bam')
pvpSpanishBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_pvpSpanish.bam')
pvpSpanishOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_pvpSpanish_ocean.bam')

#Port Royal
PRModel = loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal.bam')
PRBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_portRoyal.bam')
PROcean = loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal_ocean.bam')

#Ravens Cove
RavensModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_ravensCove.bam')
RavensBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_ravensCove.bam')
RavensOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_ravensCove_ocean.bam')

#Outcast
OutcastModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_outcast.bam')
OutcastBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_outcast.bam')
OutcastOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_outcast_ocean.bam')

#Cutthroat
CutthroatModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_cutthroat.bam')
CutthroatBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_cutthroat.bam')
CutthroatOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_cutthroat_ocean.bam')

#Rumrunner
RumrunnerModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_rumRunner.bam')
RumrunnerBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_rumRunner.bam')
RumrunnerOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_rumRunner_ocean.bam')

#Tormenta
TormentaModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_tormenta.bam')
TormentaBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_tormenta.bam')
TormentaOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_tormenta_ocean.bam')

#Ile d'Etable de Porc
pvpFrenchModel = loader.loadModel('phase_5/models/islands/pir_m_are_isl_pvpFrench.bam')
pvpFrenchBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_pvpFrench.bam')
pvpFrenchOcean = loader.loadModel('phase_5/models/islands/pir_m_are_isl_pvpFrench_ocean.bam')

#Cursed Caverns
cursed_caverns = loader.loadModel('phase_4/models/caves/pir_m_are_cav_cursed_caverns.bam')
#Barbossas Grotto
GrottoModel = loader.loadModel('phase_4/models/caves/pir_m_are_cav_barbossa.bam')
GrottoBuildings = loader.loadModel('phase_4/models/caves/pir_m_are_cav_barbossa_bui.bam')
#BeckettsQuarry
BeckettsQuarry = loader.loadModel("phase_4/models/caves/pir_m_are_cav_quarry.bam")
#FoulbertoCave
SmashoCave = loader.loadModel('phase_4/models/caves/pir_m_are_cav_smasho.bam')
#The Catacombs
TheCatacombs = loader.loadModel('phase_4/models/caves/pir_m_are_cav_catacombs.bam')
########################################################################################################
#Fix that water
#Tormenta Water
TormOColor = loader.loadTexture("phase_3/maps/pir_t_are_isl_tormenta_ocean.jpg")
TormentaOcean.findAllMatches("**/water_color").setTexture(TormOColor,1)
TormentaOcean.findAllMatches("**/water_alpha").hide()
#Port Royal Water
PROColor = loader.loadTexture("phase_4/maps/pir_t_are_isl_portRoyal_ocean.jpg")
PROcean.findAllMatches("**/water_color").setTexture(PROColor,1)
PROcean.findAllMatches("**/water_alpha").hide()
PROcean.findAllMatches("**/sandfloor").hide()
PRModel.findAllMatches("**/minimap_0").hide()
#Ravens Cove Water
RCOColor = loader.loadTexture("phase_3/maps/pir_t_are_isl_ravensCove_ocean.jpg")
RavensOcean.findAllMatches("**/water_color").setTexture(RCOColor,1)
RavensOcean.findAllMatches("**/water_alpha").hide()
RavensOcean.findAllMatches("**/sandfloor").hide()
RavensModel.findAllMatches("**/minimap_0").hide()
#Rumrunner Water
RROColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_rumRunner_ocean.jpg")
RumrunnerOcean.findAllMatches("**/water_color").setTexture(RROColor,1)
RumrunnerOcean.findAllMatches("**/water_alpha").hide()
RumrunnerOcean.findAllMatches("**/sandfloor").hide()
#Kingshead Water
KOColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_kingshead_ocean.jpg")
KingsheadOcean.findAllMatches("**/water_color").setTexture(KOColor,1)
KingsheadOcean.findAllMatches("**/water_alpha").hide()
KingsheadOcean.findAllMatches("**/sandfloor").hide()
#Cuba Water
COColor = loader.loadTexture("phase_3/maps/pir_t_are_isl_cuba_ocean.jpg")
CubaOcean.findAllMatches("**/water_color").setTexture(COColor,1)
CubaOcean.findAllMatches("**/water_alpha").hide()
CubaOcean.findAllMatches("**/sandfloor").hide()
CubaOcean.findAllMatches("**/water_alpha_swamp").hide()
CubaOcean.findAllMatches("**/water_color_swamp").hide()
CubaOcean.findAllMatches("**/water_swamp_ns").hide()
CubaModel.findAllMatches("**/minimap_0").hide()
#Devils Anvil Water
DAOColor = loader.loadTexture("phase_3/maps/pir_t_are_isl_devilsAnvil_ocean.jpg")
DevilsOcean.findAllMatches("**/water_color").setTexture(DAOColor,1)
DevilsOcean.findAllMatches("**/water_alpha").hide()
DevilsOcean.findAllMatches("**/sandfloor").hide()
#Spanish Water
SOColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_pvpSpanish_ocean.jpg")
pvpSpanishOcean.findAllMatches("**/water_color").setTexture(SOColor,1)
pvpSpanishOcean.findAllMatches("**/water_alpha").hide()
pvpSpanishOcean.findAllMatches("**/sandfloor").hide()
#Cutthroat Water
CTOColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_cutthroat_ocean.jpg")
CutthroatOcean.findAllMatches("**/water_color").setTexture(CTOColor,1)
CutthroatOcean.findAllMatches("**/water_alpha").hide()
CutthroatOcean.findAllMatches("**/sandfloor").hide()
#Driftwood Water
DWOColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_driftwood_ocean.jpg")
DriftwoodOcean.findAllMatches("**/water_color").setTexture(DWOColor,1)
DriftwoodOcean.findAllMatches("**/water_alpha").hide()
DriftwoodOcean.findAllMatches("**/sandfloor").hide()
#Outcast Water
OOColor = loader.loadTexture("phase_3/maps/pir_t_are_isl_outcast_ocean.jpg")
OutcastOcean.findAllMatches("**/water_color").setTexture(OOColor,1)
OutcastOcean.findAllMatches("**/water_alpha").hide()
OutcastOcean.findAllMatches("**/sandfloor").hide()
#Cangrejos Water
CangreOColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_driftwood_ocean.jpg")
CangrejosOcean.findAllMatches("**/water_color").setTexture(CangreOColor,1)
CangrejosOcean.findAllMatches("**/water_alpha").hide()
CangrejosOcean.findAllMatches("**/sandfloor").hide()
#Padres Water
PadOColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_delFuego_ocean.jpg")
delFuegoOcean.findAllMatches("**/water_color").setTexture(PadOColor)
delFuegoOcean.findAllMatches("**/water_alpha").hide()
delFuegoOcean.findAllMatches("**/sandfloor").hide()
#Ile d'Etable de Porc Water
IleColor = loader.loadTexture("phase_5/maps/pir_t_are_isl_pvpFrench_ocean.jpg")
pvpFrenchOcean.findAllMatches("**/water_color").setTexture(IleColor)
pvpFrenchOcean.findAllMatches("**/water_alpha").hide()
pvpFrenchOcean.findAllMatches("**/sandfloor").hide()
####################################################################
#Remove those decorations!
#Tortuga
TortugaBuildings.findAllMatches("**/holiday").hide()
TortugaBuildings.findAllMatches("**/extraData").hide()
TortugaBuildings.findAllMatches("**/WinterFestival").hide()
#TortugaBuildings.findAllMatches("**/Section-beach_05/high/lod_low/").hide()
#Port Royal
PRBuildings.findAllMatches("**/holiday").hide()
PRBuildings.findAllMatches("**/extraData").hide()
PRBuildings.findAllMatches("**/WinterFestival").hide()

########################################################################################################

devilsaudio = base.loader.loadSfx("phase_5/audio/music_devils_anvil_alt.mp3")
tortugaaudio = base.loader.loadSfx("phase_5/audio/music_tortuga.mp3")
cangrejosaudio = base.loader.loadSfx("phase_5/audio/music_cangrejos.mp3")
cubaaudio = base.loader.loadSfx("phase_5/audio/music_cuba.mp3")
padresaudio = base.loader.loadSfx("phase_5/audio/music_madre_del_fuego.mp3")
driftwoodaudio = base.loader.loadSfx("phase_5/audio/music_driftwood.mp3")
kingsheadaudio = base.loader.loadSfx("phase_5/audio/music_kingshead.mp3")
portroyalaudio = base.loader.loadSfx("phase_4/audio/music_port_royal.mp3")
spanishaudio = base.loader.loadSfx("phase_5/audio/music_isla_de_porc.mp3")
ravensaudio = base.loader.loadSfx("phase_5/audio/music_ravens_cove_night.mp3")
outcastaudio = base.loader.loadSfx("phase_5/audio/music_outcast.mp3")
cutthroataudio = base.loader.loadSfx("phase_5/audio/music_cutthroat.mp3")
rumrunneraudio = base.loader.loadSfx("phase_5/audio/music_rumrunner.mp3")
tormentaaudio = base.loader.loadSfx("phase_5/audio/music_tormenta.mp3")
frenchaudio = base.loader.loadSfx("phase_5/audio/music_ile_detable.mp3")

audio = [devilsaudio, tortugaaudio, cangrejosaudio, cubaaudio, padresaudio, driftwoodaudio, kingsheadaudio, portroyalaudio, spanishaudio, ravensaudio, outcastaudio, cutthroataudio, rumrunneraudio, tormentaaudio, frenchaudio]

textPlayer15.setFont(Impress)
textPlayer14.setFont(Impress)
textPlayer13.setFont(Impress)
textPlayer12.setFont(Impress)
textPlayer11.setFont(Impress)
textPlayer10.setFont(Impress)
textPlayer9.setFont(Impress)
textPlayer8.setFont(Impress)
textPlayer7.setFont(Impress)
textPlayer6.setFont(Impress)
textPlayer5.setFont(Impress)
textPlayer4.setFont(Impress)
textPlayer3.setFont(Impress)
textPlayer2.setFont(Impress)
textPlayer1.setFont(Impress)
#text1.setFont(Impress)
text.setFont(Impress)
camera.hide()
base.oobe()
tortugaTeleport()
loadingImage.removeNode()
loadingImage1.removeNode()
#StartOfCords()
#TortugaModel.place()
#Cat.place()
base.run()
