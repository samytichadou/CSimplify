import bpy

from .import simplify_functions as spf

def toggle_simplify_callback(self, context):
    scn=context.scene
    if self.simplify_toggle:
        spf.simplify_on(scn)
    else:
        spf.simplify_off(scn)

def update_simplify_callback(self, context):
    scn=context.scene
    if not scn.csimplify.simplify_toggle:
        return
    spf.simplify_off(scn)
    spf.simplify_on(scn)



class CSIMPLIFY_PR_subdivision_modifier_list(bpy.types.PropertyGroup):
    viewport_subdiv: bpy.props.IntProperty(
        name="Viewport Subdivision Levels",
        default=1,
        min=0,
        max=10,
        )
    render_subdiv: bpy.props.IntProperty(
        name="Render Subdivision Levels",
        default=2,
        min=0,
        max=10,
        )
    modifier_index: bpy.props.IntProperty(
        name="Modifier Stack Index",
        )

class CSIMPLIFY_PR_object_list(bpy.types.PropertyGroup):
    object: bpy.props.PointerProperty(
        name="Object",
        type = bpy.types.Object,
        )
    subdiv_modifiers: bpy.props.CollectionProperty(
        name="Subdivision Modifiers",
        type = CSIMPLIFY_PR_subdivision_modifier_list,
        )

class CSIMPLIFY_PR_object(bpy.types.PropertyGroup):
    simplify_object_override: bpy.props.BoolProperty(
        name="Simplify Object Override",
        update=update_simplify_callback,
        override = {"LIBRARY_OVERRIDABLE"},
        )

    simplify_viewport: bpy.props.BoolProperty(
        name="Simplify Viewport On",
        default=True,
        update=update_simplify_callback,
        override = {"LIBRARY_OVERRIDABLE"},
        )
    simplify_render: bpy.props.BoolProperty(
        name="Simplify Render On",
        default=False,
        update=update_simplify_callback,
        override = {"LIBRARY_OVERRIDABLE"},
        )
    viewport_subdiv_simplify: bpy.props.IntProperty(
        name="Viewport Subdivision Max Levels",
        default=0,
        min=0,
        max=10,
        update=update_simplify_callback,
        override = {"LIBRARY_OVERRIDABLE"},
        )
    render_subdiv_simplify: bpy.props.IntProperty(
        name="Render Subdivision Max Levels",
        default=1,
        min=0,
        max=10,
        update=update_simplify_callback,
        override = {"LIBRARY_OVERRIDABLE"},
        )

class CSIMPLIFY_PR_scene(bpy.types.PropertyGroup):
    simplify_toggle: bpy.props.BoolProperty(
        name="Simplify",
        update=toggle_simplify_callback,
        )
    simplify_viewport: bpy.props.BoolProperty(
        name="Simplify Viewport On",
        default=True,
        update=update_simplify_callback,
        )
    simplify_render: bpy.props.BoolProperty(
        name="Simplify Render On",
        default=False,
        update=update_simplify_callback,
        )
    viewport_subdiv_simplify: bpy.props.IntProperty(
        name="Viewport Subdivision Max Levels",
        default=0,
        min=0,
        max=10,
        update=update_simplify_callback,
        )
    render_subdiv_simplify: bpy.props.IntProperty(
        name="Render Subdivision Max Levels",
        default=1,
        min=0,
        max=10,
        update=update_simplify_callback,
        )
    object_list: bpy.props.CollectionProperty(
        name="Objects",
        type = CSIMPLIFY_PR_object_list,
        )
    to_enable: bpy.props.BoolProperty()

### REGISTER ---
def register():
    bpy.utils.register_class(CSIMPLIFY_PR_subdivision_modifier_list)
    bpy.utils.register_class(CSIMPLIFY_PR_object_list)
    bpy.utils.register_class(CSIMPLIFY_PR_object)
    bpy.utils.register_class(CSIMPLIFY_PR_scene)
    bpy.types.Object.csimplify= \
        bpy.props.PointerProperty(
            type = CSIMPLIFY_PR_object,
            name="CSimplify",
            override = {"LIBRARY_OVERRIDABLE"},
            )
    bpy.types.Scene.csimplify= \
        bpy.props.PointerProperty(type = CSIMPLIFY_PR_scene, name="CSimplify")
def unregister():
    bpy.utils.unregister_class(CSIMPLIFY_PR_subdivision_modifier_list)
    bpy.utils.unregister_class(CSIMPLIFY_PR_object_list)
    bpy.utils.unregister_class(CSIMPLIFY_PR_object)
    bpy.utils.unregister_class(CSIMPLIFY_PR_scene)
    del bpy.types.Object.csimplify
    del bpy.types.Scene.csimplify
