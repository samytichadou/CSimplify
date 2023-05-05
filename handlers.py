import bpy
from bpy.app.handlers import persistent

@persistent
def save_pre_handler(scene):
    scn=bpy.context.scene
    if scn.csimplify.simplify_toggle:
        scn.csimplify.simplify_toggle=False
        scn.csimplify.to_enable=True
        print("CSIMPLIFY --- Preventing save of simplify state")

@persistent
def save_post_handler(scene):
    scn=bpy.context.scene
    if scn.csimplify.to_enable:
        scn.csimplify.simplify_toggle=True
        scn.csimplify._to_enable=False
        print("CSIMPLIFY --- Save of simplify state avoided")

@persistent
def load_post_handler(scene):
    scn=bpy.context.scene
    if scn.csimplify.simplify_toggle:
        scn.csimplify.simplify_toggle=False
        print("CSIMPLIFY --- Removing simplify state")

### REGISTER ---
def register():
    bpy.app.handlers.save_pre.append(save_pre_handler)
    bpy.app.handlers.save_post.append(save_post_handler)
    bpy.app.handlers.load_post.append(load_post_handler)
def unregister():
    bpy.app.handlers.save_pre.remove(save_pre_handler)
    bpy.app.handlers.save_post.remove(save_post_handler)
    bpy.app.handlers.load_post.remove(load_post_handler)
