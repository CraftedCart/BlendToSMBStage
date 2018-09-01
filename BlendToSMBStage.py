import bpy
import bgl
from sys import platform
import math
import threading
import os
import random
import webbrowser

if platform == "linux" or platform == "linux2":
    from lxml import etree
else:
    import xml.etree.ElementTree as etree

bl_info = {
    "name": "BlendToSMBStage",
    "author": "CraftedCart",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "description": "Create Super Monkey Ball stages within Blender",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

def setItemGroupProperties(ig, animated = False):
    ig["collisionStartX"] = -256
    ig["collisionStartY"] = -256
    ig["collisionStepX"] = 32
    ig["collisionStepY"] = 32
    ig["collisionStepCountX"] = 16
    ig["collisionStepCountY"] = 16

    ig["posXAnim"] = animated
    ig["posYAnim"] = animated
    ig["posZAnim"] = animated
    ig["rotXAnim"] = animated
    ig["rotYAnim"] = animated
    ig["rotZAnim"] = animated

    ig["animId"] = 0;
    ig["initPlaying"] = 1;
    ig["loopAnim"] = 1;

def isItemGroupAnimated(ig):
    if "posXAnim" in ig and ig["posXAnim"] == 1: return True
    if "posYAnim" in ig and ig["posYAnim"] == 1: return True
    if "posZAnim" in ig and ig["posZAnim"] == 1: return True
    if "rotXAnim" in ig and ig["rotXAnim"] == 1: return True
    if "rotYAnim" in ig and ig["rotYAnim"] == 1: return True
    if "rotZAnim" in ig and ig["rotZAnim"] == 1: return True

    return False

def addPosXAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)

    hitLast = False

    for i in range(startFrame, endFrame, bpy.context.scene.timeStepProp):
        if i == endFrame:
            hitLast = True

        bpy.context.scene.frame_set(i)
        seconds = round(i / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(bpy.context.scene.objects.active.location.x, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

    if not hitLast:
        bpy.context.scene.frame_set(endFrame)
        seconds = round(endFrame / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(bpy.context.scene.objects.active.location.x, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addPosYAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    hitLast = False

    bpy.context.scene.frame_set(0)

    for i in range(startFrame, endFrame, bpy.context.scene.timeStepProp):
        if i == endFrame:
            hitLast = True

        bpy.context.scene.frame_set(i)
        seconds = round(i / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(-bpy.context.scene.objects.active.location.y, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

    if not hitLast:
        bpy.context.scene.frame_set(endFrame)
        seconds = round(endFrame / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(-bpy.context.scene.objects.active.location.y, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);


def addPosZAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)

    hitLast = False;

    for i in range(startFrame, endFrame, bpy.context.scene.timeStepProp):
        if i == endFrame:
            hitLast = True

        bpy.context.scene.frame_set(i)
        seconds = round(i / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(bpy.context.scene.objects.active.location.z, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

    if not hitLast:
        bpy.context.scene.frame_set(endFrame)
        seconds = round(endFrame / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(bpy.context.scene.objects.active.location.z, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addRotXAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)

    hitLast = False

    for i in range(startFrame, endFrame, bpy.context.scene.timeStepProp):
        if 1 == endFrame:
            hitLast = True

        bpy.context.scene.frame_set(i)
        seconds = round(i / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(math.degrees(bpy.context.scene.objects.active.rotation_euler.x), bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

    if not hitLast:
        bpy.context.scene.frame_set(endFrame)
        seconds = round(endFrame / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(math.degrees(bpy.context.scene.objects.active.rotation_euler.x), bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addRotYAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)

    hitLast = False

    for i in range(startFrame, endFrame, bpy.context.scene.timeStepProp):
        if 1 == endFrame:
            hitLast = True

        bpy.context.scene.frame_set(i)
        seconds = round(i / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(math.degrees(-bpy.context.scene.objects.active.rotation_euler.y), bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

    if not hitLast:
        bpy.context.scene.frame_set(endFrame)
        seconds = round(endFrame / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round(math.degrees(-bpy.context.scene.objects.active.rotation_euler.y), bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addRotZAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)

    hitLast = False

    for i in range(startFrame, endFrame, bpy.context.scene.timeStepProp):
        if 1 == endFrame:
            hitLast = True

        bpy.context.scene.frame_set(i)
        seconds = round(i / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round((bpy.context.scene.objects.active.rotation_euler.z) / (2 * math.pi) * 360.0, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

    if not hitLast:
        bpy.context.scene.frame_set(endFrame)
        seconds = round(endFrame / bpy.context.scene.render.fps, bpy.context.scene.roundTimeProp)

        val = round((bpy.context.scene.objects.active.rotation_euler.z) / (2 * math.pi) * 360.0, bpy.context.scene.roundValueProp)

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

#Operation
class NewItemGroup(bpy.types.Operator):
    bl_idname = "object.new_item_group"
    bl_label = "New item group"
    bl_description = "Creates an empty with various custom properties\nParent your object to the empty to add it to the item group"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[IG] New item group", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        setItemGroupProperties(ig)
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class NewAnimatedItemGroup(bpy.types.Operator):
    bl_idname = "object.new_animated_item_group"
    bl_label = "New animated item group"
    bl_description = "Creates an empty with various custom properties\nParent your object to the empty to add it to the item group"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[IG] New item group", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        setItemGroupProperties(ig, True)
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class ConvertToGroup(bpy.types.Operator):
    bl_idname = "object.convert_to_group"
    bl_label = "Convert selected to non-animated item group(s)"
    bl_description = "Converts the selected objects to item groups"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            setItemGroupProperties(obj, False)
            obj.name = "[IG] " + obj.name

        return {'FINISHED'}

#Operation
class ConvertToAnimtedGroup(bpy.types.Operator):
    bl_idname = "object.convert_to_animated_group"
    bl_label = "Convert selected to animated item group(s)"
    bl_description = "Converts the selected objects to item groups"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            setItemGroupProperties(obj, True)
            obj.name = "[IG] " + obj.name

        return {'FINISHED'}

#Operation
class ConvertToBackground(bpy.types.Operator):
    bl_idname = "object.convert_to_background"
    bl_label = "Convert selected to background object(s)"
    bl_description = "Converts the selected objects to item groups"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            setItemGroupProperties(obj, False)
            obj.name = "[BG] " + obj.name

        return {'FINISHED'}

#Operation
class NewStart(bpy.types.Operator):
    bl_idname = "object.new_start"
    bl_label = "New start"
    bl_description = "Creates a start object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[START]", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class NewGoalB(bpy.types.Operator):
    bl_idname = "object.new_goal_b"
    bl_label = "New goal blue"
    bl_description = "Creates a goal object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[GOAL_B] New goal", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class NewGoalG(bpy.types.Operator):
    bl_idname = "object.new_goal_g"
    bl_label = "New goal green"
    bl_description = "Creates a goal object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[GOAL_G] New goal", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class NewGoalR(bpy.types.Operator):
    bl_idname = "object.new_goal_r"
    bl_label = "New goal red"
    bl_description = "Creates a goal object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[GOAL_R] New goal", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class NewBananaS(bpy.types.Operator):
    bl_idname = "object.new_banana_s"
    bl_label = "New banana single"
    bl_description = "Creates a banana object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[BANANA_S] New banana", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class NewBananaB(bpy.types.Operator):
    bl_idname = "object.new_banana_b"
    bl_label = "New banana bunch"
    bl_description = "Creates a banana object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[BANANA_B] New banana", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

#Operation
class NewBumper(bpy.types.Operator):
    bl_idname = "object.new_bumper"
    bl_label = "New bumper"
    bl_description = "Creates a bumper object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[BUMPER] New bumper", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig

        return {'FINISHED'}

class NewWormhole(bpy.types.Operator):
    bl_idname = "object.new_wormhole"
    bl_label = "New wormhole"
    bl_description = "Creates a wormhole object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[WH] New wormhole", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig
        ig["id"] = random.randint(1, 100000001);
        ig["linkedId"] = 0

        return {'FINISHED'}

class NewSwitchPlay(bpy.types.Operator):
    bl_idname = "object.new_switch_play"
    bl_label = "New switch play"
    bl_description = "Creates a switch object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[SW_PLAY] New switch", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig
        ig["animId"] = random.randint(1, 65535);

        return {'FINISHED'}

class NewSwitchPause(bpy.types.Operator):
    bl_idname = "object.new_switch_pause"
    bl_label = "New switch pause"
    bl_description = "Creates a switch object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[SW_PAUSE] New switch", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig
        ig["animId"] = random.randint(1, 65535);

        return {'FINISHED'}

class NewSwitchPlayBackwards(bpy.types.Operator):
    bl_idname = "object.new_switch_play_backwards"
    bl_label = "New switch play backwards"
    bl_description = "Creates a switch object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[SW_PLAY_BACKWARDS] New switch", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig
        ig["animId"] = random.randint(1, 65535);

        return {'FINISHED'}

class NewSwitchPlayFf(bpy.types.Operator):
    bl_idname = "object.new_switch_ff"
    bl_label = "New switch FF"
    bl_description = "Creates a switch object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[SW_FF] New switch", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig
        ig["animId"] = random.randint(1, 65535);

        return {'FINISHED'}

class NewSwitchPlayRw(bpy.types.Operator):
    bl_idname = "object.new_switch_rw"
    bl_label = "New switch RW"
    bl_description = "Creates a switch object"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        ig = bpy.data.objects.new("[SW_RW] New switch", None)
        bpy.context.scene.objects.link(ig)
        ig.empty_draw_type = "ARROWS"
        bpy.ops.object.select_all(action='DESELECT')
        ig.select = True
        bpy.context.scene.objects.active = ig
        ig["animId"] = random.randint(1, 65535);

        return {'FINISHED'}

#Operation
class MakeNocoli(bpy.types.Operator):
    bl_idname = "object.make_nocoli"
    bl_label = "Disable collision for selected"
    bl_description = "Will not generate collision for NOCOLI objects"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.name = "[NOCOLI] " + obj.name

        return {'FINISHED'}

#Operation
class MakeNodisp(bpy.types.Operator):
    bl_idname = "object.make_nodisp"
    bl_label = "Disable visibility for selected"
    bl_description = "Will not mark NODISP objects as visible"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.name = "[NODISP] " + obj.name

        return {'FINISHED'}

#Operation
class CopyAnimXML(bpy.types.Operator):
    bl_idname = "object.copy_anim_xml"
    bl_label = "Copy animation XML for active object to clipboard"
    bl_description = "Generates animation keyframe data in XML and copies it to the clipboard"
    # bl_options = {'REGISTER', 'UNDO'} #Cannot undo a copy

    #Execute function
    def execute(self, context):
        #Generate the XML
        kf = etree.Element("animKeyframes")

        if context.scene.genPosXKeyframesProp:
            posX = etree.Element("posX")
            addPosXAnim(posX)
            kf.append(posX)
        if context.scene.genPosYKeyframesProp:
            posY = etree.Element("posY")
            addPosZAnim(posY)
            kf.append(posY)
        if context.scene.genPosZKeyframesProp:
            posZ = etree.Element("posZ")
            addPosYAnim(posZ)
            kf.append(posZ)
        if context.scene.genRotXKeyframesProp:
            rotX = etree.Element("rotX")
            addRotXAnim(rotX)
            kf.append(rotX)
        if context.scene.genRotYKeyframesProp:
            rotZ = etree.Element("rotZ")
            addRotYAnim(rotZ)
            kf.append(rotY)
        if context.scene.genRotZKeyframesProp:
            rotY = etree.Element("rotY")
            addRotZAnim(rotY)
            kf.append(rotY)

        #Copy the XML to the clipboard
        if platform == "linux" or platform == "linux2":
            bpy.context.window_manager.clipboard = str(etree.tostring(kf, pretty_print = True, encoding = "unicode"))
        else:
            bpy.context.window_manager.clipboard = str(etree.tostring(kf, encoding = "unicode"))

        return {'FINISHED'}

#Operation
class GenerateConfig(bpy.types.Operator):
    bl_idname = "object.generate_config"
    bl_label = "Generate config"
    bl_description = "Generates a config from this scene"
    bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        root = etree.Element("superMonkeyBallStage", version="1.1.0")
        modelImport = etree.SubElement(root, "modelImport")
        # modelImport.text = "//PUT A PATH TO YOUR OBJ HERE"
        modelImport.text = context.scene.modelImportProp

        startPosX = 0.0
        startPosY = 0.0
        startPosZ = 0.0
        startRotX = 0.0
        startRotY = 0.0
        startRotZ = 0.0

        children = [ob_child for ob_child in bpy.context.scene.objects]
        for child in children:
            if "[START]" in child.name:
                startPosX = child.location.x
                startPosY = child.location.z
                startPosZ = -child.location.y
                startRotX = math.degrees(child.rotation_euler.x)
                startRotY = math.degrees(child.rotation_euler.z)
                startRotZ = math.degrees(-child.rotation_euler.y)

        start = etree.SubElement(root, "start")
        etree.SubElement(start, "position", x = str(startPosX), y = str(startPosY), z = str(startPosZ))
        etree.SubElement(start, "rotation", x = str(startRotX), y = str(startRotY), z = str(startRotZ))

        etree.SubElement(root, "falloutPlane", y = str(context.scene.falloutProp))

        #Find and export backgrounds
        backgrounds = [obj for obj in bpy.context.scene.objects if obj.name.startswith("[BG]")]
        for ig in backgrounds:
            print("Processing background: " + ig.name)

            xig = etree.SubElement(root, "backgroundModel")

            if ig.data == None or ig.name == ig.data.name:
                model = etree.SubElement(xig, "name")
                model.text = ig.name.replace(" ", "_")
            else:
                model = etree.SubElement(xig, "name")
                model.text = (ig.name + "_" + ig.data.name).replace(" ", "_")

        #Find and export item groups
        itemGroups = [obj for obj in bpy.context.scene.objects if obj.name.startswith("[IG]")]

        dummyIg = etree.SubElement(root, "itemGroup") #TODO: This is kind-of a hack to work around stuff being funky with the first item group
        grid = etree.SubElement(dummyIg, "collisionGrid")

        etree.SubElement(grid, "start", x = "-256", z = "-256")
        etree.SubElement(grid, "step", x = "32", z = "32")
        etree.SubElement(grid, "count", x = "16", z = "16")

        for ig in itemGroups:
            print("Processing item group: " + ig.name)

            #XML Item Group
            xig = etree.SubElement(root, "itemGroup")

            igName = etree.SubElement(xig, "name")
            igName.text = ig.name

            bpy.context.scene.frame_set(0)
            etree.SubElement(xig, "rotationCenter", x = str(ig.location.x), y = str(ig.location.z), z = str(-ig.location.y))
            print(">>>")
            print(str(ig.location.y))
            print(str(ig.name))
            etree.SubElement(xig, "initialRotation", x = str(math.degrees(ig.rotation_euler.x)), y = str(math.degrees(ig.rotation_euler.z)), z = str(math.degrees(-ig.rotation_euler.y)))
            animLoopTime = etree.SubElement(xig, "animLoopTime") #TODO: Allow different loop times per item group
            animLoopTime.text = str(bpy.context.scene.frame_end / 60.0)

            animId = 0
            initPlaying = "PLAY"
            loop = "LOOPING_ANIMATION"
            if "animId" in ig:
                animId = ig["animId"]
            if "initPlaying" in ig:
                if ig["initPlaying"] == 0:
                    initPlaying = "PAUSE"
            if "loopAnim" in ig:
                if ig["loopAnim"] == 0:
                    loop = "PLAY_ONCE_ANIMATION"

            animIdE = etree.SubElement(xig, "animGroupId")
            animIdE.text = str(animId)

            animInitlayE = etree.SubElement(xig, "animInitialState")
            animInitlayE.text = initPlaying

            animLoopE = etree.SubElement(xig, "animSeesawType")
            animLoopE.text = loop

            grid = etree.SubElement(xig, "collisionGrid")

            collisionStartX = ig["collisionStartX"]
            collisionStartY = ig["collisionStartY"]
            collisionStepX = ig["collisionStepX"]
            collisionStepY = ig["collisionStepY"]
            collisionStepCountX = ig["collisionStepCountX"]
            collisionStepCountY = ig["collisionStepCountY"]

            etree.SubElement(grid, "start", x = str(collisionStartX), z = str(collisionStartY))
            etree.SubElement(grid, "step", x = str(collisionStepX), z = str(collisionStepY))
            etree.SubElement(grid, "count", x = str(collisionStepCountX), z = str(collisionStepCountY))

            #Find all level models who are children of this item group
            children = [ob_child for ob_child in bpy.context.scene.objects if ob_child.parent == ig]

            children.append(ig)

            for child in children:
                loc = child.matrix_world.to_translation()
                rot = child.matrix_world.to_euler("XZY")

                if "[GOAL_B]" in child.name:
                    print("    goal: " + child.name)
                    goal = etree.SubElement(xig, "goal")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    type = etree.SubElement(goal, "type")
                    type.text = "BLUE"
                    continue

                elif "[GOAL_G]" in child.name:
                    print("    goal: " + child.name)
                    goal = etree.SubElement(xig, "goal")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    type = etree.SubElement(goal, "type")
                    type.text = "GREEN"
                    continue

                elif "[GOAL_R]" in child.name:
                    print("    goal: " + child.name)
                    goal = etree.SubElement(xig, "goal")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    type = etree.SubElement(goal, "type")
                    type.text = "RED"
                    continue

                elif "[BANANA_S]" in child.name:
                    print("    banana: " + child.name)
                    goal = etree.SubElement(xig, "banana")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    type = etree.SubElement(goal, "type")
                    type.text = "SINGLE"
                    continue

                elif "[BANANA_B]" in child.name:
                    print("    banana: " + child.name)
                    goal = etree.SubElement(xig, "banana")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    type = etree.SubElement(goal, "type")
                    type.text = "BUNCH"
                    continue

                elif "[BUMPER]" in child.name:
                    print("    bumper: " + child.name)
                    goal = etree.SubElement(xig, "bumper")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    etree.SubElement(goal, "scale", x = str(child.scale.x), y = str(child.scale.z), z = str(child.scale.y))
                    continue

                elif "[WH]" in child.name:
                    print("    wormhole: " + child.name)
                    goal = etree.SubElement(xig, "wormhole")
                    name = etree.SubElement(goal, "name")
                    name.text = "WH" + str(child["id"])
                    name = etree.SubElement(goal, "destinationName")
                    name.text = "WH" + str(child["linkedId"])
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    etree.SubElement(goal, "scale", x = str(child.scale.x), y = str(child.scale.z), z = str(child.scale.y))
                    continue

                elif "[SW_RW]" in child.name:
                    print("    switch: " + child.name)
                    goal = etree.SubElement(xig, "switch")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    gType = etree.SubElement(goal, "type")
                    gType.text = "REWIND"
                    group = etree.SubElement(goal, "animGroupId")
                    group.text = str(child["animId"])
                    continue

                elif "[SW_PLAY_BACKWARDS]" in child.name:
                    print("    switch: " + child.name)
                    goal = etree.SubElement(xig, "switch")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    gType = etree.SubElement(goal, "type")
                    gType.text = "PLAY_BACKWARDS"
                    group = etree.SubElement(goal, "animGroupId")
                    group.text = str(child["animId"])
                    continue

                elif "[SW_PAUSE]" in child.name:
                    print("    switch: " + child.name)
                    goal = etree.SubElement(xig, "switch")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    gType = etree.SubElement(goal, "type")
                    gType.text = "PAUSE"
                    group = etree.SubElement(goal, "animGroupId")
                    group.text = str(child["animId"])
                    continue

                elif "[SW_PLAY]" in child.name:
                    print("    switch: " + child.name)
                    goal = etree.SubElement(xig, "switch")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    gType = etree.SubElement(goal, "type")
                    gType.text = "PLAY"
                    group = etree.SubElement(goal, "animGroupId")
                    group.text = str(child["animId"])
                    continue

                elif "[SW_FF]" in child.name:
                    print("    switch: " + child.name)
                    goal = etree.SubElement(xig, "switch")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(loc.x), y = str(loc.z), z = str(-loc.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(rot.x)), y = str(math.degrees(rot.z)), z = str(math.degrees(-rot.y)))
                    gType = etree.SubElement(goal, "type")
                    gType.text = "FAST_FORWARD"
                    group = etree.SubElement(goal, "animGroupId")
                    group.text = str(child["animId"])
                    continue

                elif child.data != None:
                    print("    stageModel: " + child.name)
                    if child.name == child.data.name:
                        name = child.name.replace(" ", "_")
                    else:
                        name = (child.name + "_" + child.data.name).replace(" ", "_")

                    if "[NODISP]" in name:
                        dispName = "__" + name
                    else:
                        dispName = name

                    model = etree.SubElement(xig, "stageModel")
                    mn = etree.SubElement(model, "name")
                    mn.text = dispName

                    if not "[NOCOLI]" in child.name:
                        mc = etree.SubElement(model, "collision")
                        mm = etree.SubElement(mc, "meshCollision")
                        mmn = etree.SubElement(mm, "name")
                        mmn.text = name

            #Set this as the active (Required for the addPos/Rot anim, because I'm a lazy sod who can't be bothered to tweak it)
            bpy.context.scene.objects.active = ig

            animKeyframes = etree.Element("animKeyframes")
            hasInserted = False
            #Add animaton if requested
            if "posXAnim" in ig and ig["posXAnim"] != 0:
                posX = etree.SubElement(animKeyframes, "posX")
                addPosXAnim(posX)
                if not hasInserted:
                    xig.append(animKeyframes)
                    hasInserted = True
            if "posYAnim" in ig and ig["posYAnim"] != 0:
                posZ = etree.SubElement(animKeyframes, "posZ")
                addPosYAnim(posZ)
                if not hasInserted:
                    xig.append(animKeyframes)
                    hasInserted = True
            if "posZAnim" in ig and ig["posZAnim"] != 0:
                posY = etree.SubElement(animKeyframes, "posY")
                addPosZAnim(posY)
                if not hasInserted:
                    xig.append(animKeyframes)
                    hasInserted = True
            if "rotXAnim" in ig and ig["rotXAnim"] != 0:
                rotX = etree.SubElement(animKeyframes, "rotX")
                addRotXAnim(rotX)
                if not hasInserted:
                    xig.append(animKeyframes)
                    hasInserted = True
            if "rotYAnim" in ig and ig["rotYAnim"] != 0:
                rotZ = etree.SubElement(animKeyframes, "rotZ")
                addRotYAnim(rotZ)
                if not hasInserted:
                    xig.append(animKeyframes)
                    hasInserted = True
            if "rotZAnim" in ig and ig["rotZAnim"] != 0:
                rotY = etree.SubElement(animKeyframes, "rotY")
                addRotZAnim(rotY)
                if not hasInserted:
                    xig.append(animKeyframes)
                    hasInserted = True

        #Copy the XML to the clipboard
        # if platform == "linux" or platform == "linux2":
            # bpy.context.window_manager.clipboard = str(etree.tostring(root, pretty_print = True, encoding = "unicode"))
        # else:
            # bpy.context.window_manager.clipboard = str(etree.tostring(root, encoding = "unicode"))

        # self.report({"ERROR"}, "Config copied to clipboard - ready to export an OBJ\nYes animation was deleted, just press Ctrl-Z after exporting\n(No, this isn't an error, I just want it to show at the cursor)")

        config = ""
        if platform == "linux" or platform == "linux2":
            config = etree.tostring(root, pretty_print = True, encoding = "unicode")
        else:
            config = etree.tostring(root, encoding = "unicode")

        f = open(bpy.path.abspath(context.scene.targetConfigProp), "w")
        f.write(config)
        f.close()

        self.report({"ERROR"}, "Note that you WILL need a development version of ws2 for now - beta 1 won't work\n" +
                    "Download at https://bintray.com/craftedcart/the-workshop/smblevelworkshop2-develop/_latestVersion - under the \"Files\" tab\n" +
                    "(There's a button to go there under \"Export OBJ\")\n" +
                    "\n" +
                    "btw this isn't an error"
                    )

        return {'FINISHED'}

#Operation
class ExportOBJ(bpy.types.Operator):
    bl_idname = "object.export_obj"
    bl_label = "Export OBJ"
    bl_description = "Exports an OBJ to the path specified in modelImport"
    # bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        bpy.ops.export_scene.obj(
            filepath = bpy.path.abspath(context.scene.modelImportProp),
            use_triangles = True
        )

        return {'FINISHED'}

#Operation
class Ws2Link(bpy.types.Operator):
    bl_idname = "object.ws2_link"
    bl_label = "Download Workshop 2 dev builds"
    bl_description = "Beta builds won't work for now"
    # bl_options = {'REGISTER', 'UNDO'}

    #Execute function
    def execute(self, context):
        webbrowser.open("https://bintray.com/craftedcart/the-workshop/smblevelworkshop2-develop/_latestVersion", new=0, autoraise=True)

        return {'FINISHED'}

#Tool shelf panel
class SceneGraphPanel(bpy.types.Panel):
    bl_label = "Scene Graph"
    bl_idname = "blend_to_smb_stage_scene_graph_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS" #Put the menu on the left tool shelf
    bl_category = "BlendToSMBStage" #Tab name of the tool shelf
    bl_context = (("objectmode"))

    #Menu and input
    def draw(self, context):
        obj = context.object
        scene = context.scene

        layout = self.layout

        layout.label("Item groups are objects whose name has [IG]")
        layout.label("Do not change the [IG] name prefix!")
        layout.label("Parent objects to the item group to add them")
        layout.label("Existing animated objects can just have the [IG] prefix applied to their name")
        layout.operator(NewItemGroup.bl_idname)
        layout.operator(NewAnimatedItemGroup.bl_idname)

        layout.operator(ConvertToGroup.bl_idname)
        layout.operator(ConvertToAnimtedGroup.bl_idname)
        layout.operator(ConvertToBackground.bl_idname)

        layout.separator()

        layout.label("Placeables")
        layout.label("Don't forget to parent these to an item group (Excl. Start)")

        layout.operator(NewStart.bl_idname)

        row = layout.row()
        row.operator(NewGoalB.bl_idname)
        row.operator(NewGoalG.bl_idname)
        row.operator(NewGoalR.bl_idname)

        row = layout.row()
        row.operator(NewBananaS.bl_idname)
        row.operator(NewBananaB.bl_idname)

        layout.operator(NewBumper.bl_idname)
        layout.operator(NewWormhole.bl_idname)

        row = layout.row()
        row.operator(NewSwitchPlayRw.bl_idname, icon = "REW")
        row.operator(NewSwitchPlayBackwards.bl_idname, icon = "PLAY_REVERSE")
        row.operator(NewSwitchPause.bl_idname, icon = "PAUSE")
        row.operator(NewSwitchPlay.bl_idname, icon = "PLAY")
        row.operator(NewSwitchPlayFf.bl_idname, icon = "FF")

        layout.separator()

        layout.operator(MakeNocoli.bl_idname)
        layout.operator(MakeNodisp.bl_idname)

        layout.separator()

        layout.prop(scene, "falloutProp")
        layout.prop(scene, "drawFalloutProp")

#Tool shelf panel
class DetailsPanel(bpy.types.Panel):
    bl_label = "Details"
    bl_idname = "blend_to_smb_stage_details_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS" #Put the menu on the left tool shelf
    bl_category = "BlendToSMBStage" #Tab name of the tool shelf
    bl_context = (("objectmode"))
    bl_options = {'DEFAULT_CLOSED'}

    #Menu and input
    def draw(self, context):
        obj = context.object
        scene = context.scene

        layout = self.layout

        layout.label("Active object in SMB coordinate space")
        layout.label("Pos X: " + str(bpy.context.scene.objects.active.location.x))
        layout.label("Pos Y: " + str(bpy.context.scene.objects.active.location.z))
        layout.label("Pos Z: " + str(-bpy.context.scene.objects.active.location.y))
        layout.label("Rot X: " + str(math.degrees(bpy.context.scene.objects.active.rotation_euler.x)))
        layout.label("Rot Y: " + str(math.degrees(bpy.context.scene.objects.active.rotation_euler.z)))
        layout.label("Rot Z: " + str(math.degrees(-bpy.context.scene.objects.active.rotation_euler.y)))

        layout.prop(scene, "drawCollisionGridProp")

#Tool shelf panel
class ExportScenePanel(bpy.types.Panel):
    bl_label = "Export Scene"
    bl_idname = "blend_to_smb_stage_export_scene_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS" #Put the menu on the left tool shelf
    bl_category = "BlendToSMBStage" #Tab name of the tool shelf
    bl_context = (("objectmode"))

    #Menu and input
    def draw(self, context):
        obj = context.object
        scene = context.scene

        layout = self.layout

        layout.label("Lower timestep = more keyframes")
        layout.prop(scene, "timeStepProp")

        layout.prop(scene, "roundTimeProp")
        layout.prop(scene, "roundValueProp")

        layout.prop(scene, "autoPathsProp")
        col = layout.column()
        col.enabled = not context.scene.autoPathsProp
        col.prop(scene, "targetConfigProp")
        col.prop(scene, "modelImportProp")


        layout.operator(GenerateConfig.bl_idname)
        layout.operator(ExportOBJ.bl_idname)

        layout.separator()

        layout.operator(Ws2Link.bl_idname)

#Tool shelf panel
class ExportAnimPanel(bpy.types.Panel):
    bl_idname = "blend_to_smb_stage_export_anim_panel"
    bl_label = "Export Object Animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS" #Put the menu on the left tool shelf
    bl_category = "BlendToSMBStage" #Tab name of the tool shelf
    bl_context = (("objectmode"))
    bl_options = {'DEFAULT_CLOSED'}

    #Menu and input
    def draw(self, context):
        obj = context.object
        scene = context.scene

        layout = self.layout

        layout.label("Lower timestep = more keyframes")
        layout.prop(scene, "timeStepProp")

        layout.prop(scene, "roundTimeProp")
        layout.prop(scene, "roundValueProp")

        layout.label("Export single object animation")

        layout.prop(scene, "genPosXKeyframesProp")
        layout.prop(scene, "genPosYKeyframesProp")
        layout.prop(scene, "genPosZKeyframesProp")
        layout.prop(scene, "genRotXKeyframesProp")
        layout.prop(scene, "genRotYKeyframesProp")
        layout.prop(scene, "genRotZKeyframesProp")

        layout.operator(CopyAnimXML.bl_idname)

#Tool shelf panel
# class DebugPanel(bpy.types.Panel):
    # bl_idname = "blend_to_smb_debug_anim_panel"
    # bl_label = "Debug"
    # bl_space_type = "VIEW_3D"
    # bl_region_type = "TOOLS" #Put the menu on the left tool shelf
    # bl_category = "BlendToSMBStage" #Tab name of the tool shelf
    # bl_context = (("objectmode"))
    # bl_options = {'DEFAULT_CLOSED'}

    # #Menu and input
    # def draw(self, context):
        # obj = context.object
        # scene = context.scene

        # layout = self.layout

        # layout.prop(scene, "redrawCounterProp")
        # layout.prop(scene, "drawFalloutProp")

# def falloutUpdate(self, context):
    # context.scene.drawFalloutProp = True
    # context.scene.redrawCounterProp = 180

    # forceRedrawLoop(context, context.area, True);

#Drawing stuff below
def drawGrid(startX, startY, spaceX, spaceY, repeatX, repeatY, z):
    bgl.glBegin(bgl.GL_LINES)

    for i in range(0, repeatX + 1):
        bgl.glVertex3f(startX + spaceX * i, startY, z)
        bgl.glVertex3f(startX + spaceX * i, startY + spaceY * repeatY, z)

    for i in range(0, repeatY + 1):
        bgl.glVertex3f(startX, startY + spaceY * i, z)
        bgl.glVertex3f(startX + spaceX * repeatX, startY + spaceY * i, z)

    bgl.glEnd()

def drawSphere(posX, posY, posZ, radius):
    bgl.glBegin(bgl.GL_LINE_STRIP)
    for i in range(0, 17):
        normI = i / 16

        x = posX + radius * math.cos(normI * math.pi * 2)
        y = posY + radius * math.sin(normI * math.pi * 2)
        bgl.glVertex3f(x, y, posZ)
    bgl.glEnd()

    bgl.glBegin(bgl.GL_LINE_STRIP)
    for i in range(0, 17):
        normI = i / 16

        x = posX + radius * math.cos(normI * math.pi * 2)
        z = posZ + radius * math.sin(normI * math.pi * 2)
        bgl.glVertex3f(x, posY, z)
    bgl.glEnd()

    bgl.glBegin(bgl.GL_LINE_STRIP)
    for i in range(0, 17):
        normI = i / 16

        y = posY + radius * math.cos(normI * math.pi * 2)
        z = posZ + radius * math.sin(normI * math.pi * 2)
        bgl.glVertex3f(posX, y, z)
    bgl.glEnd()

def drawCallback3d():
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glLineWidth(4)

    #Fallout
    if bpy.context.scene.drawFalloutProp:
        # bgl.glColor4f(0.96, 0.26, 0.21, min(bpy.context.scene.redrawCounterProp / 60.0, 1) * 0.3)
        bgl.glColor4f(0.96, 0.26, 0.21, 0.3)
        drawGrid(-512, -512, 4, 4, 256, 256, bpy.context.scene.falloutProp)

    #Collision grids
    itemGroups = [obj for obj in bpy.context.scene.objects if obj.name.contains("[IG]")]

    if bpy.context.scene.drawCollisionGridProp:
        for ig in itemGroups:
            if ig in bpy.context.selected_objects:
                if ig != None and ig.name.contains("[IG]"):
                    bgl.glColor4f(0.30, 0.69, 0.31, 0.5)
                    collisionStartX = ig["collisionStartX"]
                    collisionStartY = ig["collisionStartY"]
                    collisionStepX = ig["collisionStepX"]
                    collisionStepY = ig["collisionStepY"]
                    collisionStepCountX = ig["collisionStepCountX"]
                    collisionStepCountY = ig["collisionStepCountY"]

                    animated = isItemGroupAnimated(ig)

                    #Only transform if animated
                    if animated:
                        origFrame = bpy.context.scene.frame_current
                        bpy.context.scene.frame_set(0)

                        origX = ig.location.x
                        origY = ig.location.y
                        origZ = ig.location.z
                        origRotX = ig.rotation_euler.x
                        origRotY = ig.rotation_euler.y
                        origRotZ = ig.rotation_euler.z

                        bpy.context.scene.frame_set(origFrame)

                        bgl.glPushMatrix()
                        bgl.glRotatef(math.degrees(ig.rotation_euler.x - origRotX), 1.0, 0.0, 0.0)
                        bgl.glRotatef(math.degrees(ig.rotation_euler.z - origRotZ), 0.0, 0.0, 1.0)
                        bgl.glRotatef(math.degrees(ig.rotation_euler.y - origRotY), 0.0, 1.0, 0.0)
                        bgl.glTranslatef(ig.location.x - origX, ig.location.y - origY, ig.location.z - origZ)

                    drawGrid(collisionStartX, -collisionStartY, collisionStepX, -collisionStepY, collisionStepCountX, collisionStepCountY, 0)

                    bgl.glDisable(bgl.GL_DEPTH_TEST)
                    bgl.glColor4f(0.30, 0.69, 0.31, 0.3)
                    drawGrid(collisionStartX, -collisionStartY, collisionStepX, -collisionStepY, collisionStepCountX, collisionStepCountY, 0)
                    bgl.glEnable(bgl.GL_DEPTH_TEST)

                    if animated:
                        bgl.glPopMatrix()

    #Draw start spheres
    posX = 0.0
    posY = 0.0
    posZ = 10.0

    bgl.glColor4f(0.13, 0.59, 0.95, 0.8)

    starts = [obj for obj in bpy.context.scene.objects if obj.name.startswith("[START]")]

    for start in starts:
        drawSphere(start.location.x, start.location.y, start.location.z, 0.5)

    #Restore OpenGL defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)

# def forceRedrawLoop(context, area, isInit):
    # if (context.scene.isInForceRenderLoop and isInit): return

    # context.scene.isInForceRenderLoop = True

    # area.tag_redraw()
    # context.scene.redrawCounterProp -= 1

    # if context.scene.redrawCounterProp > 0:
        # threading.Timer(0.016, forceRedrawLoop, [context, area, False]).start()
    # else:
        # bpy.context.scene.drawFalloutProp = False
        # context.scene.isInForceRenderLoop = False

def autoPathNames(self, context):
    if context.scene.autoPathsProp:
        context.scene.targetConfigProp = "//" + os.path.splitext(os.path.basename(bpy.context.blend_data.filepath))[0] + ".xml"
        context.scene.modelImportProp = "//" + os.path.splitext(os.path.basename(bpy.context.blend_data.filepath))[0] + ".obj"

def register():
    bpy.utils.register_module(__name__)

    bpy.types.Scene.roundTimeProp = bpy.props.IntProperty(name = "Time decimal places", default = 3)
    bpy.types.Scene.roundValueProp = bpy.props.IntProperty(name = "Pos/Rot decimal places", default = 3)
    bpy.types.Scene.timeStepProp = bpy.props.IntProperty(name = "Timestep", default = 1)

    # bpy.types.Scene.falloutProp = bpy.props.FloatProperty(name = "Fallout Y", default = -10.0, update = falloutUpdate)
    bpy.types.Scene.falloutProp = bpy.props.FloatProperty(name = "Fallout Y", default = -10.0)

    bpy.types.Scene.targetConfigProp = bpy.props.StringProperty(
        name = "Target Config File",
        description = "The XML file to write to",
        subtype = 'FILE_PATH',
        default = "//config.xml"
    )

    bpy.types.Scene.modelImportProp = bpy.props.StringProperty(
        name = "OBJ path",
        # description = "The OBJ file to reference in the config\n\n//filepath.obj for a relative filepath\nfile:///path/to/model.obj for an absolute filepath",
        description = "The path must be relative (Begins with //)",
        default = "//model.obj"
    )

    bpy.types.Scene.autoPathsProp = bpy.props.BoolProperty(name = "Automatic path names", default = True, update = autoPathNames)

    bpy.types.Scene.genPosXKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos X keyframes", default = True)
    bpy.types.Scene.genPosYKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos Y keyframes", default = True)
    bpy.types.Scene.genPosZKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos Z keyframes", default = True)
    bpy.types.Scene.genRotXKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot X keyframes", default = True)
    bpy.types.Scene.genRotYKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot Y keyframes", default = True)
    bpy.types.Scene.genRotZKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot Z keyframes", default = True)

    #Rendering
    # bpy.types.Scene.redrawCounterProp = bpy.props.IntProperty(name = "redrawCounterProp", default = 60)
    bpy.types.Scene.drawFalloutProp = bpy.props.BoolProperty(name = "Draw fallout plane", default = False)
    bpy.types.Scene.drawCollisionGridProp = bpy.props.BoolProperty(name = "Draw collision grid", default = True)

    bpy.types.Scene.isInForceRenderLoop = bpy.props.BoolProperty(name = "isInForceRenderLoop", default = False)

    #Idk the proper way of doing this
    try:
        bpy.types.SpaceView3D.draw_handler_remove(bpy.types.Scene.blendToSmbStageDrawCallback3d, 'WINDOW')
    except AttributeError:
        pass

    bpy.types.Scene.blendToSmbStageDrawCallback3d = bpy.types.SpaceView3D.draw_handler_add(drawCallback3d, (), 'WINDOW', 'POST_VIEW')

    if bpy.context.scene.autoPathsProp and bpy.path.basename(bpy.context.blend_data.filepath) != "":
        bpy.context.scene.targetConfigProp = "//" + os.path.splitext(os.path.basename(bpy.context.blend_data.filepath))[0] + ".xml"
        bpy.context.scene.modelImportProp = "//" + os.path.splitext(os.path.basename(bpy.context.blend_data.filepath))[0] + ".obj"

    print("BlendToSMBStage registered")

def unregister():
    bpy.utils.unregister_module(__name__)

    del bpy.types.Scene.roundTimeProp
    del bpy.types.Scene.roundValueProp
    del bpy.types.Scene.timeStepProp

    del bpy.types.Scene.falloutProp

    del bpy.types.Scene.targetConfigProp
    del bpy.types.Scene.modelImportProp
    del bpy.types.Scene.autoPathsProp

    del bpy.types.Scene.genPosXKeyframesProp
    del bpy.types.Scene.genPosYKeyframesProp
    del bpy.types.Scene.genPosZKeyframesProp
    del bpy.types.Scene.genRotXKeyframesProp
    del bpy.types.Scene.genRotYKeyframesProp
    del bpy.types.Scene.genRotZKeyframesProp

    # del bpy.types.Scene.redrawCounterProp
    del bpy.types.Scene.drawFalloutProp
    del bpy.types.Scene.drawCollisionGridProp

    bpy.types.SpaceView3D.draw_handler_remove(bpy.types.Scene.blendToSmbStageDrawCallback3d, 'WINDOW')
    del bpy.types.Scene.blendToSmbStageDrawCallback3d

    print("BlendToSMBStage unreigstered")

if __name__ == "__main__":
    register()

