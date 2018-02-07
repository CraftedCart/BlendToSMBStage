import bpy
from sys import platform
import math

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

        itemGroups = [obj for obj in bpy.context.scene.objects if obj.name.startswith("[IG]")]

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
            animType = etree.SubElement(xig, "animSeesawType")
            animType.text = "LOOPING_ANIMATION"
            animLoopTime = etree.SubElement(xig, "animLoopTime") #TODO: Allow different loop times per item group
            animLoopTime.text = str(bpy.context.scene.frame_end / 60.0)

            #Collision grid #TODO: Adjustible collision grid
            grid = etree.SubElement(xig, "collisionGrid")
            etree.SubElement(grid, "start", x = "-256", z = "-256")
            etree.SubElement(grid, "step", x = "32", z = "32")
            etree.SubElement(grid, "count", x = "16", z = "16")

            #Find all level models who are children of this item group
            children = [ob_child for ob_child in bpy.context.scene.objects if ob_child.parent == ig]

            #The item group should be added as a level model if it's not an empty
            if ig.data != None:
                children.append(ig)

            for child in children:
                if "[GOAL_B]" in child.name:
                    print("    goal: " + child.name)
                    goal = etree.SubElement(xig, "goal")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(child.location.x), y = str(child.location.z), z = str(-child.location.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(child.rotation_euler.x)), y = str(math.degrees(child.rotation_euler.z)), z = str(math.degrees(-child.rotation_euler.y)))
                    type = etree.SubElement(goal, "type")
                    type.text = "BLUE"
                    continue

                elif "[GOAL_G]" in child.name:
                    print("    goal: " + child.name)
                    goal = etree.SubElement(xig, "goal")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(child.location.x), y = str(child.location.z), z = str(-child.location.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(child.rotation_euler.x)), y = str(math.degrees(child.rotation_euler.z)), z = str(math.degrees(-child.rotation_euler.y)))
                    type = etree.SubElement(goal, "type")
                    type.text = "GREEN"
                    continue

                elif "[GOAL_R]" in child.name:
                    print("    goal: " + child.name)
                    goal = etree.SubElement(xig, "goal")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(child.location.x), y = str(child.location.z), z = str(-child.location.y))
                    etree.SubElement(goal, "rotation", x = str(math.degrees(child.rotation_euler.x)), y = str(math.degrees(child.rotation_euler.z)), z = str(math.degrees(-child.rotation_euler.y)))
                    type = etree.SubElement(goal, "type")
                    type.text = "RED"
                    continue

                elif "[BANANA_S]" in child.name:
                    print("    banana: " + child.name)
                    goal = etree.SubElement(xig, "banana")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(child.location.x), y = str(child.location.z), z = str(-child.location.y))
                    type = etree.SubElement(goal, "type")
                    type.text = "SINGLE"
                    continue

                elif "[BANANA_B]" in child.name:
                    print("    banana: " + child.name)
                    goal = etree.SubElement(xig, "banana")
                    name = etree.SubElement(goal, "name")
                    name.text = child.name
                    etree.SubElement(goal, "position", x = str(child.location.x), y = str(child.location.z), z = str(-child.location.y))
                    type = etree.SubElement(goal, "type")
                    type.text = "BUNCH"
                    continue

                else:
                    print("    levelModel: " + child.name)
                    if child.data == None or  child.name == child.data.name:
                        model = etree.SubElement(xig, "levelModel")
                        model.text = child.name.replace(" ", "_")
                    else:
                        model = etree.SubElement(xig, "levelModel")
                        model.text = (child.name + "_" + child.data.name).replace(" ", "_")

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

        return {'FINISHED'}

#The tool shelf panel
class BlendToSMBStagePanel(bpy.types.Panel):
    bl_label = "BlendToSMBStage Tools"
    bl_idname = "blend_to_smb_stage_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS" #Put the menu on the left tool shelf
    bl_category = "BlendToSMBStage" #Tab name of the tool shelf
    bl_context = (("objectmode"))

    #Menu and input
    def draw(self, context):
        obj = context.object
        scene = context.scene

        layout = self.layout

        layout.label("Item groups are objects whose name begins with [IG]")
        layout.label("Do not change the [IG] name prefix!")
        layout.label("Parent objects to the item group to add them")
        layout.label("Existing animated objects can just have the [IG] prefix applied to their name")
        layout.operator(NewItemGroup.bl_idname)
        layout.operator(NewAnimatedItemGroup.bl_idname)

        layout.operator(ConvertToGroup.bl_idname)
        layout.operator(ConvertToAnimtedGroup.bl_idname)

        layout.separator()

        layout.label("Placeables")
        layout.label("Don't forget to parent these to an item group")

        layout.operator(NewStart.bl_idname)

        layout.operator(NewGoalB.bl_idname)
        layout.operator(NewGoalG.bl_idname)
        layout.operator(NewGoalR.bl_idname)

        layout.operator(NewBananaS.bl_idname)
        layout.operator(NewBananaB.bl_idname)

        layout.separator()

        layout.label("Active object in SMB coordinate space")
        layout.label("Pos X: " + str(bpy.context.scene.objects.active.location.x))
        layout.label("Pos Y: " + str(bpy.context.scene.objects.active.location.z))
        layout.label("Pos Z: " + str(-bpy.context.scene.objects.active.location.y))
        layout.label("Rot X: " + str(math.degrees(bpy.context.scene.objects.active.rotation_euler.x)))
        layout.label("Rot Y: " + str(math.degrees(bpy.context.scene.objects.active.rotation_euler.z)))
        layout.label("Rot Z: " + str(math.degrees(-bpy.context.scene.objects.active.rotation_euler.y)))

        layout.separator()

        layout.prop(scene, "genPosXKeyframesProp")
        layout.prop(scene, "genPosYKeyframesProp")
        layout.prop(scene, "genPosZKeyframesProp")
        layout.prop(scene, "genRotXKeyframesProp")
        layout.prop(scene, "genRotYKeyframesProp")
        layout.prop(scene, "genRotZKeyframesProp")

        layout.label("Lower timestep = more keyframes")
        layout.prop(scene, "timeStepProp")

        layout.prop(scene, "roundTimeProp")
        layout.prop(scene, "roundValueProp")
        # layout.label("Rotations are always rounded to the nearest int")

        layout.operator(CopyAnimXML.bl_idname)

        layout.separator()

        layout.prop(scene, "falloutProp")

        layout.prop(scene, "targetConfigProp")
        layout.prop(scene, "modelImportProp")
        layout.operator(GenerateConfig.bl_idname)

def register():
    bpy.utils.register_module(__name__)

    bpy.types.Scene.roundTimeProp = bpy.props.IntProperty(name = "Time decimal places", default = 3)
    bpy.types.Scene.roundValueProp = bpy.props.IntProperty(name = "Pos/Rot decimal places", default = 3)
    bpy.types.Scene.timeStepProp = bpy.props.IntProperty(name = "Timestep", default = 1)

    bpy.types.Scene.falloutProp = bpy.props.FloatProperty(name = "Fallout Y", default = -10.0)

    bpy.types.Scene.targetConfigProp = bpy.props.StringProperty(
        name = "Target Config File",
        description = "The XML file to write to",
        subtype = 'FILE_PATH'
    )

    bpy.types.Scene.modelImportProp = bpy.props.StringProperty(
        name = "Model import",
        description = "The OBJ file to reference in the config\n\n//filepath.obj for a relative filepath\nfile:///path/to/model.obj for an absolute filepath",
        default = "//model.obj"
    )

    bpy.types.Scene.genPosXKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos X keyframes", default = True)
    bpy.types.Scene.genPosYKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos Y keyframes", default = True)
    bpy.types.Scene.genPosZKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos Z keyframes", default = True)
    bpy.types.Scene.genRotXKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot X keyframes", default = True)
    bpy.types.Scene.genRotYKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot Y keyframes", default = True)
    bpy.types.Scene.genRotZKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot Z keyframes", default = True)

    print("BlendToSMBStage registered")

def unregister():
    bpy.utils.unregister_module(__name__)

    del bpy.types.Scene.roundTimeProp
    del bpy.types.Scene.roundValueProp
    del bpy.types.Scene.timeStepProp

    del bpy.types.Scene.falloutProp

    del bpy.types.Scene.targetConfigProp
    del bpy.types.Scene.modelImportProp

    del bpy.types.Scene.genPosXKeyframesProp
    del bpy.types.Scene.genPosYKeyframesProp
    del bpy.types.Scene.genPosZKeyframesProp
    del bpy.types.Scene.genRotXKeyframesProp
    del bpy.types.Scene.genRotYKeyframesProp
    del bpy.types.Scene.genRotZKeyframesProp

    print("BlendToSMBStage unreigstered")

if __name__ == "__main__":
    register()

