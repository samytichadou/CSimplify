import bpy

from .simplify_functions import reset_modifier_simplify

class CSIMPLIFY_OT_fix_simplify(bpy.types.Operator):
    bl_idname = "csimplify.fix_simplify"
    bl_label = "Fix CSimplify"
    bl_description = "Fix old CSimplify value for active object"
    bl_options = {"INTERNAL","REGISTER","UNDO"}

    @classmethod
    def poll(cls, context):
        if not context.scene.csimplify.simplify_toggle:
            if context.active_object:
                return not context.active_object.library\
                and not context.active_object.override_library

    def execute(self, context):
        ob=context.active_object
        ob_props=ob.csimplify

        if not ob_props.subdiv_modifiers:
            self.report({'INFO'}, f"{ob.name} : nothing to correct")
            return {'FINISHED'}

        reset_modifier_simplify(ob, ob_props.subdiv_modifiers)

        ob_props.subdiv_modifiers.clear()
        self.report({'INFO'}, f"{ob.name} corrected")

        return {'FINISHED'}

### REGISTER ---
def register():
    bpy.utils.register_class(CSIMPLIFY_OT_fix_simplify)
def unregister():
    bpy.utils.unregister_class(CSIMPLIFY_OT_fix_simplify)
