# プロパティをシーンに登録する場合は、
# クラスをレジスターの項目も登録してあげる。	bpy.types.Scene.####使用したシーンの名前 = bpy.props.PointerProperty(type=クラス名)
# 削除も忘れずに	del bpy.types.Scene.####使用したシーンの名前

bl_info = {
    "name": "simple fbx export",
    "description": " ",
    "author": "hydro",
    "version": (0, 0, 1),
    "blender": (3, 2, 1),
    "location": "",
    "warning": "",
    "doc_url": "",
    "category": "3d"
    }



import bpy

if "bpy" in locals():
	import importlib
	reloadable_modules = [

    "simplefbxexport_op_fbx_export",
    "simplefbxexport_def",
    "simplefbxexport_panel",
    "simplefbxexoprt_propertyGroup",
    "simplefbxexoprt_filelist",

	]
	for module in reloadable_modules:
		if module in locals():
			importlib.reload(locals()[module])



from .simplefbxexport_op_fbx_export import *
from .simplefbxexport_panel import *
from .simplefbxexoprt_propertyGroup import *
from .simplefbxexoprt_filelist import *


classes = (

SIMPLEFBXECPORT_PropertyGroup,

SIMPLEFBXECPORT_OT_FbxExort,

SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2,
SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2_previw,
SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2_nameset,
SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT2_1,
SIMPLEFBXECPORT_PT_SETTINGFBXEXPORT3,

#filelist----
SIMPLEFBXECPORT_OT_Add_Operator,
SIMPLEFBXECPORT_OT_Remove_Operator,
# SIMPLEFBXECPORT_PT_Panel,
SIMPLEFBXECPORT_PG_filenameset,
#filelist----
)


#filelist----
def fbxfilenameset_items(self, context):

	Enum_items = []
	if len(bpy.context.scene.fbxfilenameset_collection) != 0:
		for filenameset in context.scene.fbxfilenameset_collection:
			
			data = str(filenameset.fbxfilenameset_text)
			item = (data, data, data)
			
			Enum_items.append(item)
	else:
		# コレクションになにもないとエミューがバグるのでダミー
		Enum_items.append(("None","None","None"))
	return Enum_items
#filelist----




def register():
	for cls in classes:
		bpy.utils.register_class(cls)
	
	bpy.types.Scene.simplefbxecport_propertygroup = bpy.props.PointerProperty(type=SIMPLEFBXECPORT_PropertyGroup)
    
	#filelist----
	bpy.types.Scene.filenameset = bpy.props.EnumProperty(items=fbxfilenameset_items,
														)
	bpy.types.Scene.fbxfilenameset_collection = bpy.props.CollectionProperty(type=SIMPLEFBXECPORT_PG_filenameset)
 	#filelist----
   

def unregister():
	for cls in reversed(classes):
		bpy.utils.unregister_class(cls)

	del bpy.types.Scene.simplefbxecport_propertygroup


	#filelist----
	del bpy.types.Scene.filenameset
	del bpy.types.Scene.fbxfilenameset_collection
	#filelist----

if __name__ == "__main__":
	register()
