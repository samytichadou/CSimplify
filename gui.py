import bpy

from .simplify_functions import supported_object_types

def draw_csimplify_panel(container, props):
    row=container.row(align=True)
    if props.simplify_viewport:
        icon="RESTRICT_VIEW_OFF"
    else:
        icon="RESTRICT_VIEW_ON"
    row.prop(props, "simplify_viewport", text="", icon=icon)
    sub=row.row()
    sub.enabled=props.simplify_viewport
    sub.prop(props, "viewport_subdiv_simplify", text="Max Subdiv")

    row=container.row(align=True)
    if props.simplify_render:
        icon="RESTRICT_RENDER_OFF"
    else:
        icon="RESTRICT_RENDER_ON"
    row.prop(props, "simplify_render", text="", icon=icon)
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

class CSIMPLIFY_PT_general_popover(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    bl_label = "Playblasts"
    bl_ui_units_x = 8

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        scn = context.scene
        scn_props = scn.csimplify

        layout=self.layout
        col=layout.column(align=True)
        col.label(text="Scene")
        draw_csimplify_panel(col, scn_props)

        if context.active_object\
        and context.active_object.type in supported_object_types:
            col.separator()
            ob_props = context.active_object.csimplify
            col.label(text="Object Override")
            draw_csimplify_panel(col, ob_props)

def view_header_gui(self, context):
    props = context.scene.csimplify
    row=self.layout.row(align=True)
    if props.simplify_toggle:
        row.alert=True
    row.prop(props, 'simplify_toggle', text="", icon="MOD_SUBSURF")
    sub=row.row()
    if not props.simplify_toggle:
        sub.enabled=False
    sub.popover(panel="CSIMPLIFY_PT_general_popover", text="")

### REGISTER ---
def register():
    bpy.utils.register_class(CSIMPLIFY_PT_render_panel)
    bpy.utils.register_class(CSIMPLIFY_PT_object_panel)
    bpy.utils.register_class(CSIMPLIFY_PT_general_popover)
    bpy.types.VIEW3D_HT_header.append(view_header_gui)
def unregister():
    bpy.utils.unregister_class(CSIMPLIFY_PT_render_panel)
    bpy.utils.unregister_class(CSIMPLIFY_PT_object_panel)
    bpy.utils.unregister_class(CSIMPLIFY_PT_general_popover)
    bpy.types.VIEW3D_HT_header.remove(view_header_gui)
