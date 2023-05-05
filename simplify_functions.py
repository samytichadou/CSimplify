import bpy

supported_object_types={
    "MESH",
    "CURVE",
    "FONT",
    "SURFACE",
    }

def remove_collection_entry(entry_name, collection):
    index=collection.find(entry_name)
    collection.remove(index)
    return index

def simplify_on(scene):
    obj_list=scene.csimplify.object_list
    # Clear old objects
    obj_list.clear()

    for ob in scene.objects:
        if ob.type in supported_object_types:
            chk_subsurf=False

            # Create entry
            ob_entry=obj_list.add()
            ob_entry.name=ob.name
            ob_entry.object=ob

            # Get object override value if needed
            if ob.csimplify.simplify_object_override:
                props=ob.csimplify
            else:
                props=scene.csimplify

            if props.simplify_viewport or props.simplify_render:

                # Find, store, change subdiv mods
                idx=0
                for m in ob.modifiers:
                    if m.type=="SUBSURF":
                        if (props.simplify_viewport\
                        and props.viewport_subdiv_simplify<m.levels)\
                        or (props.simplify_render\
                        and props.render_subdiv_simplify<m.render_levels):
                            chk_subsurf=True
                            # Store
                            new=ob_entry.subdiv_modifiers.add()
                            new.name=m.name
                            new.modifier_index=idx
                            new.viewport_subdiv=m.levels
                            new.render_subdiv=m.render_levels
                            # Store Fallback
                            try:
                                new_fallback=ob.csimplify.subdiv_modifiers.add()
                                new_fallback.name=m.name
                                new_fallback.modifier_index=idx
                                new_fallback.viewport_subdiv=m.levels
                                new_fallback.render_subdiv=m.render_levels
                            except TypeError:
                                pass
                            # Change
                            if props.simplify_viewport:
                                m.levels=props.viewport_subdiv_simplify
                            if props.simplify_render:
                                m.render_levels=props.render_subdiv_simplify
                    idx+=1
            # Remove entry if empty
            if not chk_subsurf:
                remove_collection_entry(ob.name, obj_list)

def simplify_off(scene):
    obj_list=scene.csimplify.object_list
    for ob_entry in obj_list:
        ob=ob_entry.object
        ob_props=ob.csimplify

        # Find, store, change subdiv mods
        idx=0
        for m in ob.modifiers:
            old_mod=None
            if m.type=="SUBSURF":
                for s in ob_entry.subdiv_modifiers:
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
                remove_collection_entry(old_mod.name, ob_entry.subdiv_modifiers)
            idx+=1
        # Clear Fallback Mod List
        try:
            ob_props.subdiv_modifiers.clear()
        except TypeError:
            pass
    obj_list.clear()
