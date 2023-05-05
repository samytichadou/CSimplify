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

@persistent
def load_post_handler(scene):
    scn=bpy.context.scene
    # Remove simplify state if needed
    if scn.csimplify.simplify_toggle:
        scn.csimplify.simplify_toggle=False
        print("CSIMPLIFY --- Removing simplify state")
