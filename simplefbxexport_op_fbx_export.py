import sys

from bpy.types import (
        Menu,
        Operator,
        Panel,
        PropertyGroup,
        )


from .simplefbxexport_def import *


class SIMPLEFBXECPORT_OT_FbxExort(Operator):
    bl_idname = 'object.fbxexortsupport'
    bl_label = 'fbxexortsupport'
    bl_description = f" CLASS_NAME_IS={sys._getframe().f_code.co_name}\n ID_NAME_IS={bl_idname}\n FILENAME_IS={__file__}\n "

    # 実際の実行文
    def execute(self, context):

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

        finalfbx_exportsavefile,mkdirefilepath = make_filename(context,fbx_exportsavefile)
             
        bool=checkpath()  

        if bool == False:
            self.report({'INFO'}, 'ファイルを保存して下さい。')

            return {'FINISHED'}

        else:

            save_active_col=actcol(
                    props.fbx_act_collection_bool, 
                            )
            select_childob()

            makdier(mkdirefilepath)
                            
            fbx_export_oprator(
                finalfbx_exportsavefile, 
                props.fbx_selectbool,
                props.fbx_act_collection_bool,
                finalfbx_exportsavefile,
                save_active_col,
                props.copytexture_bool,
                props.embedtexture_bool,
                props.openfolder_bool
                            )

            self.report({'INFO'}, str(finalfbx_exportsavefile))
    
            return {'FINISHED'}