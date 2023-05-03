import bpy

class CSIMPLIFY_PR_main(bpy.types.PropertyGroup):
    viewport_subdiv: bpy.props.IntProperty(
        name="Viewport Subdivision Levels",
        default=1,
        )
    render_subdiv: bpy.props.IntProperty(
        name="Render Subdivision Levels",
        default=2,
        )
    viewport_simplify: bpy.props.IntProperty(
        name="Viewport Subdivision Levels",
        default=0,
        )
    render_simplify: bpy.props.IntProperty(
        name="Render Subdivision Levels",
        default=1,
        )
    simplify: bpy.props.BoolProperty(
        name="Simplify On",
        default=True,
        )

### REGISTER ---
def register():
    bpy.utils.register_class(CSIMPLIFY_PR_main)
    bpy.types.Modifier.csimplify= \
        bpy.props.PointerProperty(type = CSIMPLIFY_PR_main, name="CSimplify")
    bpy.types.Modifier.csimplifytest= \
        bpy.props.BoolProperty(name="Test", default=True)
def unregister():
    bpy.utils.unregister_class(CSIMPLIFY_PR_main)
    del bpy.types.Modifier.csimplify
    del bpy.types.Modifier.csimplifytest
