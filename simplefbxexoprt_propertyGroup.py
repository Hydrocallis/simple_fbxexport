
import bpy, sys, pathlib

from bpy.types import (
        Menu,
        Operator,
        Panel,
        PropertyGroup,
        )


from bpy.props import (
                        StringProperty, 
                        IntProperty, 
                        FloatProperty, 
                        EnumProperty, 
                        BoolProperty,
                        PointerProperty,
                        FloatVectorProperty,
                        StringProperty
                        )


class SIMPLEFBXECPORT_PropertyGroup(PropertyGroup):
 
    ######### fbx関係のプロパティ##########

    # クリップスタジオのボーン設定項目

    def clipstudio_body_modelset_bool(self, context):
        for i in bpy.context.scene.objects:
            if "clip_body_mesh" in i.name:
                if i.modifiers[0].object.name == "BODY":
                    i.select_set(True)
                    
                    try:
                        i.modifiers[0].object = bpy.data.objects["CLIP_BODY"]
                        a = 1
                        
                    except KeyError:
                        print("plese CLIP_BODY set!")
                else:
                    try:
                        i.modifiers[0].object = bpy.data.objects["BODY"]
                        a =0
                    except KeyError:
                        print("plese BODY set!")
            if "CLIP_BODY"==i.name:
                if a==1:
                
                    i.select_set(True)
                elif a==0:
                    i.select_set(False)
                    
            if "BODY"==i.name:
                if a==0:
                    i.select_set(True)
                elif a==1:
                    i.select_set(False)


    clipstudio_body_modelset_bool : BoolProperty(
                name = "クリップスタジオのボーン設定",
                default = False,
                update = clipstudio_body_modelset_bool,
                                )
#######　名前関係



    # コレクションのドロップリスト
    # https://blenderartists.org/t/blender-2-9-collectionproperty-howto/1312488/5 
    # https://docs.blender.org/api/current/bpy.types.ID.html#bpy.types.ID
    workspace_fbxfolder_path_Collection: PointerProperty(
        type=bpy.types.Collection,
        name="コレクションの指定",
        description="コレクションの名前が主力先のフォルダ名になる"
    )


    # コレクションの名前を使用する
    fbx_get_col_name_bool : BoolProperty(
                name = "指定したコレクションの名前を使用する",
                default = False,
                description="fbx_get_col_name_bool",

                                )



    # 選択したオブジェクトの名前を付ける
    fbx_selectfilename_bool : BoolProperty(
                name = "選択したオブジェクトの名前を付ける",
                default = False,
                description="fbx_selectfilename_bool",
                                )

    # 名前をリプレイスする
    fbx_name_replace_bool : BoolProperty(
                name = "名前をリプレイスする",
                default = True,
                description="fbx_name_replace_bool",

                                )


    # ブレンダーのファイル名をつける
    fbx_blenderfilename__bool : BoolProperty(
                name = "ブレンダーのファイル名をつける",
                default = False,
                description="fbx_blenderfilename__bool",

                                )

    # オリジナルの名前を付ける
    fbx_filename : StringProperty(
                name = "オリジナルの名前を付ける",
                # default = blender_fbxfilename,
                default = "",
                description="fbx_filename",

                                )


    # ブレンダーのファイル名をつける
    use_otherfilepath_bool : BoolProperty(
                name = "保存先を指定",
                default = False,
                description="use other filepath",

                                )

    use_otherfilepath_path : StringProperty(
                name="other filepath path",
                description="other filepath path",
                # default= blend_directory,
                subtype='DIR_PATH',
                    )


#######　パス関係

    # FBXファイルの出力先
    def get_filepath(self):
        p_sub = pathlib.Path(bpy.data.filepath)
        p_sub = p_sub.parent
        return str(p_sub)

    workspace_path : StringProperty(
                name="",
                description="Path to workspace folder",
                # default= blend_directory,
                subtype='DIR_PATH',
                get=get_filepath)

    # サブフォルダを使うかどうか
    # サブフォルダの名前
    workspace_fbxfolder_path : StringProperty(
                name="サブフォルダの名前",
                description="workspace_fbxfolder_path",
                default = "export_fbx",
                # default= blend_directory,
                subtype='FILE_NAME',)

####### ブレンダー出力関係

    # 選択したオブジェクトを主力する
    fbx_selectbool : BoolProperty(
                name = "選択したオブジェクトを出力",
                default = False,
                description="fbx_selectbool",

                                )

    # アクティブなコレクション内を出力
    fbx_act_collection_bool : BoolProperty(
                name = "アクティブなコレクション内を出力",
                default = False,
                description="fbx_act_collection_bool",

                                )
    copytexture_bool : BoolProperty(
                name = "copy texture",
                default = False,
                description="",

                                )
    embedtexture_bool : BoolProperty(
                name = "embed texture",
                default = False,
                description="",

                                )

    openfolder_bool : BoolProperty(
                name = "Open Folder ",
                default = False,
                description="",

                                )

#####その他のオプション
    # 下の階層のオブジェクトも選択して出力する
    fbx_children_recursive : BoolProperty(
                name = "下の階層のオブジェクトも選択して出力する",
                default = False,
                description="fbx_children_recursive",

                                )