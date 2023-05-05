import bpy
import os

from . import handlers as hdl

addon_name = os.path.basename(os.path.dirname(__file__))

def save_handler_callback(self, context):
    if self.save_handler:
        bpy.app.handlers.save_pre.append(hdl.save_pre_handler)
        bpy.app.handlers.save_post.append(hdl.save_post_handler)
        print("CSIMPLIFY --- Save handlers registered")
    else:
        bpy.app.handlers.save_pre.remove(hdl.save_pre_handler)
        bpy.app.handlers.save_post.remove(hdl.save_post_handler)
        print("CSIMPLIFY --- Save handlers unregistered")

def startup_handler_callback(self, context):
    if self.startup_handler:
        bpy.app.handlers.load_post.append(hdl.load_post_handler)
        print("CSIMPLIFY --- Startup handler registered")
    else:
        bpy.app.handlers.load_post.remove(hdl.load_post_handler)
        print("CSIMPLIFY --- Startup handler unregistered")

class CSIMPLIFY_PF_preferences(bpy.types.AddonPreferences) :
    bl_idname = addon_name

    save_handler: bpy.props.BoolProperty(
        name="Remove Simplify on Save",
        update=save_handler_callback,
        default=True,
        )
    startup_handler: bpy.props.BoolProperty(
        name="Remove Simplify on Startup",
        update=startup_handler_callback,
        default=True,
        )

    def draw(self, context) :
        wm = context.window_manager
        layout = self.layout
        layout.prop(self, "save_handler")
        layout.prop(self, "startup_handler")

# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(addon_name)
    return getattr(addon, "preferences", None)


### REGISTER ---
def register():
    bpy.utils.register_class(CSIMPLIFY_PF_preferences)
    if get_addon_preferences().save_handler:
        bpy.app.handlers.save_pre.append(hdl.save_pre_handler)
        bpy.app.handlers.save_post.append(hdl.save_post_handler)
        print("CSIMPLIFY --- Save handlers registered")
    if get_addon_preferences().startup_handler:
        print("CSIMPLIFY --- Startup handler registered")
        bpy.app.handlers.load_post.append(hdl.load_post_handler)
def unregister():
    bpy.utils.unregister_class(CSIMPLIFY_PF_preferences)
    if get_addon_preferences().save_handler:
        bpy.app.handlers.save_pre.remove(hdl.save_pre_handler)
        bpy.app.handlers.save_post.remove(hdl.save_post_handler)
    if get_addon_preferences().startup_handler:
        bpy.app.handlers.load_post.remove(hdl.load_post_handler)
