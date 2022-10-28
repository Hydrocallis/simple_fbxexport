import bpy

from bpy.types import (
        Menu,
        Operator,
        Panel,
        PropertyGroup,
        )

from .simplefbxexport_def import *



# fbx出力関連
class SIMPLEFBXECPORT_PT_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "simple fbx export"




        

class SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2(SIMPLEFBXECPORT_PT_panel,Panel):
    bl_label = "Simple Fbx Export"
    bl_idname = "SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT1"

    def draw_header(self, context):
        layout = self.layout
       
        layout.operator("object.fbxexortsupport", text="",icon="EXPORT")
    def draw(self, context):
        pass

class SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2_previw(SIMPLEFBXECPORT_PT_panel,Panel):
    bl_label = "previw"
    bl_parent_id = "SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT1"


    def draw(self, context):
        ########　出力結果のプレビュー
        # print('###',get_filenameetc())
        layout = self.layout
        props = context.scene.simplefbxecport_propertygroup

        row = layout.row()
        # row.operator("object.getfbxinformation", text="ファイルの保存先を自動入力")
        box = layout.box()

        if get_filenameetc()[1] ==False:
            box.label(text = f"Please save the file")

        box.label(text = "File Path")
        box.prop(props,"use_otherfilepath_bool",text="Specify destination")
        if props.use_otherfilepath_bool== True:
            box.prop(props,"use_otherfilepath_path")
        box.label(text = f" {os.path.dirname(get_filenameetc()[0])}")
        box.prop(props, "workspace_fbxfolder_path",text="Sub Folder")
        
        box2 = layout.box()

        box2.label(text = "File Name")
        box2.label(text = f" {os.path.basename(get_filenameetc()[0])}")
        box2.prop(props, "fbx_filename",text="")

        # row.label(text="※コレクショ名を優先")
class SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2_nameset(SIMPLEFBXECPORT_PT_panel,Panel):
    bl_label = "Name Setting"
    bl_parent_id = "SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT1"


    def draw(self, context):

        layout = self.layout
        props = context.scene.simplefbxecport_propertygroup
        ########　名前の設定
        row = layout.row()
        
        row.prop(props, "fbx_blenderfilename__bool",text="Use blender file name")
        row = layout.row()
        row.label(text="Name List")
        row = layout.row(align=True)
        row.prop(context.scene, "filenameset", text="")
        row.operator("simplefbxexport.add", text="", icon="ADD")
        row.operator("simplefbxexport.remove", text="", icon="REMOVE")
        
        row = layout.row()
        row.prop(props, "fbx_selectfilename_bool",text="Name the selected object")
        row = layout.row()
        row.prop(props, "fbx_name_replace_bool",text="Overwrite file name")
        # row = layout.row()
        # row.prop(props, "clipstudio_body_modelset_bool")
        row = layout.row()
        row.prop(props, "fbx_get_col_name_bool",text="Use the name of the given collection")


class SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2_1(SIMPLEFBXECPORT_PT_panel,Panel):
    bl_label = "Export Setting"
    bl_parent_id = "SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT1"



    def draw(self, context):
        ########　出力結果のプレビュー
        # print('###',get_filenameetc())
        layout = self.layout
        props = context.scene.simplefbxecport_propertygroup



        row = layout.row()

        ########　出力関係
        row = layout.row()
        row.prop(props, "copytexture_bool",text="Copy Texture")
        row = layout.row()
        row.prop(props, "embedtexture_bool",text="Embed textures")
        row = layout.row()
        row.prop(props, "fbx_selectbool",text="Output selected objects")
        row = layout.row()
        row.prop(props, "fbx_act_collection_bool",text="Output in active collection")
        # row.label(text="Specify active collection for output")
        row = layout.row()
        row.prop(props, "workspace_fbxfolder_path_Collection")

        row = layout.row()
        row.prop(props, "openfolder_bool",text="Open output folder")
        ######## FBXを出力する
        row = layout.row()
        row.operator("object.fbxexortsupport", text = "Output FBX")


class SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT3(SIMPLEFBXECPORT_PT_panel,Panel):
    bl_label = "Other Setting"
    bl_parent_id = "SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT1"
    bl_options = {"DEFAULT_CLOSED"}




    def draw(self, context):
        # print('###',get_filenameetc())
        layout = self.layout
        props = context.scene.simplefbxecport_propertygroup

        row = layout.row()
        row.prop(props, "fbx_children_recursive",text="Select and output objects in the lower level as well")



# class EXAMPLE_panel:
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "Example Tab"
#     bl_options = {"DEFAULT_CLOSED"}


# class EXAMPLE_PT_panel_1(EXAMPLE_panel, bpy.types.Panel):
#     bl_idname = "EXAMPLE_PT_panel_1"
#     bl_label = "Panel 1"

#     def draw(self, context):
#         layout = self.layout
#         layout.label(text="This is the main panel.")

# class EXAMPLE_PT_panel_2(EXAMPLE_panel, bpy.types.Panel):
#     bl_parent_id = "EXAMPLE_PT_panel_1"
#     bl_label = "Panel 2"

#     def draw(self, context):
#         layout = self.layout
#         layout.label(text="First Sub Panel of Panel 1.")

# class EXAMPLE_PT_panel_3(EXAMPLE_panel, bpy.types.Panel):
#     bl_parent_id = "EXAMPLE_PT_panel_1"
#     bl_label = "Panel 3"

#     def draw(self, context):
#         layout = self.layout
#         layout.label(text="Second Sub Panel of Panel 1.")