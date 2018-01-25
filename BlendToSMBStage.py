import bpy
from lxml import etree
import math

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

def addPosXAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)
    initVal = bpy.context.scene.objects.active.location.x

    for i in range(startFrame, endFrame):
        bpy.context.scene.frame_set(i)
        seconds = i / bpy.context.scene.render.fps

        val = bpy.context.scene.objects.active.location.x - initVal

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addPosYAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)
    initVal = bpy.context.scene.objects.active.location.y

    for i in range(startFrame, endFrame):
        bpy.context.scene.frame_set(i)
        seconds = i / bpy.context.scene.render.fps

        val = bpy.context.scene.objects.active.location.y - initVal

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addPosZAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)
    initVal = bpy.context.scene.objects.active.location.z

    for i in range(startFrame, endFrame):
        bpy.context.scene.frame_set(i)
        seconds = i / bpy.context.scene.render.fps

        val = bpy.context.scene.objects.active.location.z - initVal

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addRotXAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)
    initVal = bpy.context.scene.objects.active.rotation_euler.x

    for i in range(startFrame, endFrame):
        bpy.context.scene.frame_set(i)
        seconds = i / bpy.context.scene.render.fps

        val = (bpy.context.scene.objects.active.rotation_euler.x - initVal) / (2 * math.pi) * 0xFFFF;

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addRotYAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)
    initVal = bpy.context.scene.objects.active.rotation_euler.y

    for i in range(startFrame, endFrame):
        bpy.context.scene.frame_set(i)
        seconds = i / bpy.context.scene.render.fps

        val = (bpy.context.scene.objects.active.rotation_euler.y - initVal) / (2 * math.pi) * 0xFFFF;

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

        parent.append(keyframe);

def addRotZAnim(parent):
    startFrame = bpy.context.scene.frame_start
    endFrame = bpy.context.scene.frame_end

    bpy.context.scene.frame_set(0)
    initVal = bpy.context.scene.objects.active.rotation_euler.z

    for i in range(startFrame, endFrame):
        bpy.context.scene.frame_set(i)
        seconds = i / bpy.context.scene.render.fps

        val = (bpy.context.scene.objects.active.rotation_euler.z - initVal) / (2 * math.pi) * 0xFFFF;

        keyframe = etree.Element("keyframe")
        keyframe.set("time", str(seconds))
        keyframe.set("value", str(val))
        keyframe.set("easing", "LINEAR")

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
        ig["collisionStartX"] = -256
        ig["collisionStartY"] = -256
        ig["collisionStepX"] = 32
        ig["collisionStepY"] = 32
        ig["collisionStepCountX"] = 16
        ig["collisionStepCountY"] = 16

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
            addPosXAnim(posY)
            kf.append(posY)
        if context.scene.genPosZKeyframesProp:
            posZ = etree.Element("posZ")
            addPosXAnim(posZ)
            kf.append(posZ)
        if context.scene.genRotXKeyframesProp:
            rotX = etree.Element("rotX")
            addRotXAnim(rotX)
            kf.append(rotX)
        if context.scene.genRotYKeyframesProp:
            rotY = etree.Element("rotY")
            addRotXAnim(rotY)
            kf.append(rotY)
        if context.scene.genRotZKeyframesProp:
            rotZ = etree.Element("rotZ")
            addRotXAnim(rotZ)
            kf.append(rotZ)

        #Copy the XML to the clipboard
        bpy.context.window_manager.clipboard = str(etree.tostring(kf, pretty_print = True, encoding = "unicode"))

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

        layout.prop(scene, "genPosXKeyframesProp")
        layout.prop(scene, "genPosYKeyframesProp")
        layout.prop(scene, "genPosZKeyframesProp")
        layout.prop(scene, "genRotXKeyframesProp")
        layout.prop(scene, "genRotYKeyframesProp")
        layout.prop(scene, "genRotZKeyframesProp")

        layout.operator(CopyAnimXML.bl_idname)

def register():
    bpy.utils.register_module(__name__)

    bpy.types.Scene.genPosXKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos X keyframes", default = True)
    bpy.types.Scene.genPosYKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos Y keyframes", default = True)
    bpy.types.Scene.genPosZKeyframesProp = bpy.props.BoolProperty(name = "Generate Pos Z keyframes", default = True)
    bpy.types.Scene.genRotXKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot X keyframes", default = True)
    bpy.types.Scene.genRotYKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot Y keyframes", default = True)
    bpy.types.Scene.genRotZKeyframesProp = bpy.props.BoolProperty(name = "Generate Rot Z keyframes", default = True)

    print("BlendToSMBStage registered")

def unregister():
    bpy.utils.unregister_module(__name__)

    del bpy.types.Scene.genPosXKeyframesProp
    del bpy.types.Scene.genPosYKeyframesProp
    del bpy.types.Scene.genPosZKeyframesProp
    del bpy.types.Scene.genRotXKeyframesProp
    del bpy.types.Scene.genRotYKeyframesProp
    del bpy.types.Scene.genRotZKeyframesProp

    print("BlendToSMBStage unreigstered")

if __name__ == "__main__":
    register()

