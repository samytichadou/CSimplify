import bpy

from .simplify_functions import supported_object_types

def draw_csimplify_panel(container, props):
    row=container.row()
    if props.simplify_viewport:
        icon="RESTRICT_VIEW_OFF"
    else:
        icon="RESTRICT_VIEW_ON"
    row.prop(props, "simplify_viewport", text="Viewport", icon=icon)
    sub=row.row()
    sub.enabled=props.simplify_viewport
    sub.prop(props, "viewport_subdiv_simplify", text="Max Subdiv")

    row=container.row()
    if props.simplify_render:
        icon="RESTRICT_RENDER_OFF"
    else:
        icon="RESTRICT_RENDER_ON"
    row.prop(props, "simplify_render", text="Render", icon=icon)
    sub=row.row()
    sub.enabled=props.simplify_render
    sub.prop(props, "render_subdiv_simplify", text="Max Subdiv")

class CSIMPLIFY_PT_render_panel(bpy.types.Panel):
    bl_label = "CSimplify"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        scn = context.scene
        props = scn.csimplify
        self.layout.prop(props, "simplify_toggle", text="")

    def draw(self, context):
        scn = context.scene
        props = scn.csimplify
        layout=self.layout
        layout.enabled=props.simplify_toggle

        draw_csimplify_panel(layout, props)

class CSIMPLIFY_PT_object_panel(bpy.types.Panel):
    bl_label = "CSimplify Override"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        return context.active_object.type in supported_object_types

    def draw_header(self, context):
        props = context.active_object.csimplify
        self.layout.prop(props, "simplify_object_override", text="")

    def draw(self, context):
        props = context.active_object.csimplify
        layout=self.layout
        layout.enabled=props.simplify_object_override

        draw_csimplify_panel(layout, props)

### REGISTER ---
def register():
    bpy.utils.register_class(CSIMPLIFY_PT_render_panel)
    bpy.utils.register_class(CSIMPLIFY_PT_object_panel)
def unregister():
    bpy.utils.unregister_class(CSIMPLIFY_PT_render_panel)
    bpy.utils.unregister_class(CSIMPLIFY_PT_object_panel)
