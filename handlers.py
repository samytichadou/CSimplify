import bpy
import atexit
from bpy.app.handlers import persistent

@persistent
def save_pre_handler(scene):
    context=bpy.context
    scn=context.scene
    if scn.csimplify.simplify_toggle:
        scn.csimplify.simplify_toggle=False
        context.window_manager.csimplify_to_enable=True
        print("CSIMPLIFY --- Simplify state removed to prevent save")

@persistent
def save_post_handler(scene):
    context=bpy.context
    scn=context.scene
    if context.window_manager.csimplify_to_enable:
        scn.csimplify.simplify_toggle=True
        context.window_manager.csimplify_to_enable=False
        print("CSIMPLIFY --- Simplify state enabled back")

def remove_simplify_atexit(scn):
    # Remove simplify state if needed
    if scn.csimplify.simplify_toggle:
        scn.csimplify.simplify_toggle=False
        print("CSIMPLIFY --- Removing simplify state")

@persistent
def load_post_handler(scene):
    scn=bpy.context.scene

    # Register atext function for quit
    #atexit.register(remove_simplify_atexit, scn)
    # print("CSIMPLIFY --- Registering atexit function")

    # Remove simplify state if needed
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
