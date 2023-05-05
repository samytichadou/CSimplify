import bpy

from .simplify_functions import remove_collection_entry

class CSIMPLIFY_OT_fix_simplify(bpy.types.Operator):
    bl_idname = "csimplify.fix_simplify"
    bl_label = "Fix CSimplify"
    bl_description = "Fix old CSimplify value for active object"
    bl_options = {"INTERNAL","REGISTER","UNDO"}

    @classmethod
    def poll(cls, context):
        if not context.scene.csimplify.simplify_toggle:
            if context.active_object:
                return not context.active_object.library

    def execute(self, context):
        ob=context.active_object
        ob_props=ob.csimplify

        if not ob_props.subdiv_modifiers:
            self.report({'INFO'}, f"{ob.name} : nothing to correct")
            return {'FINISHED'}

        for m in ob.modifiers:
            old_mod=None
            if m.type=="SUBSURF":
                for s in ob_props.subdiv_modifiers:
                    if s.name==m.name:
                        old_mod=s
                        break
                    if s.modifier_index==idx:
                        old_mod=s
                        break
                if old_mod is None:
                    print(f"CSIMPLIFY --- Error with {ob.name} - {m.name}")
                    break
                # Change
                m.levels=old_mod.viewport_subdiv
                m.render_levels=old_mod.render_subdiv
                # Remove old entry
                remove_collection_entry(old_mod.name, ob_props.subdiv_modifiers)
        ob_props.subdiv_modifiers.clear()
        self.report({'INFO'}, f"{ob.name} corrected")

        return {'FINISHED'}

### REGISTER ---
def register():
    bpy.utils.register_class(CSIMPLIFY_OT_fix_simplify)
def unregister():
    bpy.utils.unregister_class(CSIMPLIFY_OT_fix_simplify)
