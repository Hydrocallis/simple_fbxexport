import bpy

from bpy.types import (
        Menu,
        Operator,
        Panel,
        PropertyGroup,
        )

from .simplefbxexport_op_fbx_export import *


def get_filenameetc():
    context=bpy.context

    props = context.scene.simplefbxecport_propertygroup

    (
    blender_fbxfilename,
    obj_name,
    blend_fbx_save_dir,
        ) = bool_check(context)
    
    fbx_exportsavefile = filenameset(
                                    blender_fbxfilename,
                                    obj_name,
                                    blend_fbx_save_dir,
                                    )

    finalfbx_exportsavefile,mkdir = make_filename(context,fbx_exportsavefile)
            
    bool=checkpath()  

    return (finalfbx_exportsavefile,bool)


# fbx出力関連
class SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "pie setting panel fbxexport"
    bl_idname = "SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "simple fbx export"
    
    def draw(self, context):
        # print('###',get_filenameetc())
        layout = self.layout
        props = context.scene.simplefbxecport_propertygroup

        row = layout.row()
        # row.operator("object.getfbxinformation", text="ファイルの保存先を自動入力")
        box = layout.box()

        if get_filenameetc()[1] ==False:
            box.label(text = f" ファイルを保存してください")

        box.label(text = "File Path")
        box.prop(props,"use_otherfilepath_bool")
        if props.use_otherfilepath_bool== True:
            box.prop(props,"use_otherfilepath_path")
        box.label(text = f" {os.path.dirname(get_filenameetc()[0])}")

        box2 = layout.box()

        box2.label(text = "File Name")
        box2.label(text = f" {os.path.basename(get_filenameetc()[0])}")
        # row.label(text="※コレクショ名を優先")
        row = layout.row()
        
        row.prop(props, "fbx_blenderfilename__bool",)
        row = layout.row()

        row.label(text="オリジナルネーム")
        row = layout.row()
        row.prop(props, "fbx_filename",text="")

        row = layout.row()

        row.label(text="保存した名前リスト")
        row = layout.row(align=True)
        row.prop(context.scene, "filenameset", text="")
        row.operator("simplefbxexport.add", text="", icon="ADD")
        row.operator("simplefbxexport.remove", text="", icon="REMOVE")
        
        row = layout.row()
        row.prop(props, "fbx_selectfilename_bool")
        # row = layout.row()
        # row.prop(props, "fbx_get_col_name_bool")

        row = layout.row()
        row.prop(props, "fbx_selectbool")
        row = layout.row()
        
        row.prop(props, "fbx_name_replace_bool")
        row = layout.row()
        row.prop(props, "fbx_children_recursive")
        row = layout.row()
        row.prop(props, "clipstudio_body_modelset_bool")
        row = layout.row()
        row.prop(props, "workspace_fbxfolder_path")
        row = layout.row()
        row.prop(props, "fbx_act_collection_bool")
        row.prop(props, "fbx_get_col_name_bool")
        row = layout.row()
        row.label(text="出力の際にアクティブコレクションを指定する")
        row = layout.row()
        row.prop(props, "workspace_fbxfolder_path_Collection")
        # FBXを出力する
        row = layout.row()
        row.operator("object.fbxexortsupport", text = "FBXを出力する")

        