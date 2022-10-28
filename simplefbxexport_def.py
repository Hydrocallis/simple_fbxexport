import bpy,os,subprocess


# パネルの出力設定項目のチェック
# ファイルネームの生成

def bool_check(context):
    props = context.scene.simplefbxecport_propertygroup
    blend_fbx_save_dir=props.workspace_path

    # ブレンダーファイルの拡張子なしの名前
    blender_fbxfilename = bpy.path.basename(bpy.context.blend_data.filepath).replace(".blend","")
 
    # アクティブ中のコレクションの名前
    get_collection_name=bpy.context.view_layer.active_layer_collection.name
    obj = bpy.context.object

    # チェック箇所によってのファイルネームの変更イフ文

    # オブジェクト選択系のいふ分
    if obj != None:
        obj_name = obj.name

    else:

        obj_name = None


    return (
            blender_fbxfilename,
            obj_name,
            blend_fbx_save_dir,
            )


def filenameset(
    blender_fbxfilename,
    obj_name,
    blend_fbx_save_dir,
        ):

    props = bpy.context.scene.simplefbxecport_propertygroup
    filenameset=bpy.context.scene.filenameset
    if filenameset=="None":
        filenameset = ""
    # ここからファイル名をデコレーションしていく

    # 選択したオブジェクトの名前と入力したファイル名と選択したファイル名を入れる
    if props.fbx_filename =="":
        filename2=""
    else:
        if blender_fbxfilename!="":
            filename2 ="_"+props.fbx_filename
        else:
            filename2 =props.fbx_filename

    if props.fbx_blenderfilename__bool == True:
        fbx_exportsavefile = blender_fbxfilename  + filename2 
   
    elif props.fbx_blenderfilename__bool == False:
        fbx_exportsavefile = props.fbx_filename

    # セットネームを入れる
    if filenameset != "":
        if fbx_exportsavefile!="":
            fbx_exportsavefile = fbx_exportsavefile +"_" + filenameset
        else:
            fbx_exportsavefile = fbx_exportsavefile + filenameset


    # 選択したオブジェクトの名前を仕様
    if props.fbx_selectfilename_bool == True:
        if fbx_exportsavefile!="":

            fbx_exportsavefile = fbx_exportsavefile + "_" + obj_name
        else:
            fbx_exportsavefile = obj_name



    # 指定したコレクション名を使用
    try:
        if fbx_exportsavefile !="":
            colname = "_"+props.workspace_fbxfolder_path_Collection.name
        else:
            colname = props.workspace_fbxfolder_path_Collection.name

    except AttributeError:
        colname =""

    if props.fbx_get_col_name_bool == True:
        fbx_exportsavefile = fbx_exportsavefile + colname

    # デコレーションの終わり。下記に拡張子とディレクトリをジョインする
    fbx_exportsavefile = os.path.join(blend_fbx_save_dir,fbx_exportsavefile+".fbx")
 
    return fbx_exportsavefile


# パスの成形と名前のジョイン
def make_filename(context,fbx_exportsavefile):
    props = context.scene.simplefbxecport_propertygroup
    
    filepath = os.path.dirname(bpy.data.filepath)


     # サブフォルダを追加する
    if props.use_otherfilepath_bool !=True:

        mkdirefilepath = os.path.join(filepath, props.workspace_fbxfolder_path, "")
    else:

        mkdirefilepath = os.path.join(props.use_otherfilepath_path, props.workspace_fbxfolder_path, "")
    
    # サブフォルダをファイルパスに組み込む
    direpath = os.path.dirname(fbx_exportsavefile)
    direfilename = os.path.basename(fbx_exportsavefile)


    # コレクションを選択してない場合
    # if props.workspace_fbxfolder_path_Collection != None:
    #     finalfbx_exportsavefile = os.path.join(direpath,props.workspace_fbxfolder_path, props.workspace_fbxfolder_path_Collection.name, direfilename)
    # else:
    if props.use_otherfilepath_bool == False:
        finalfbx_exportsavefile = os.path.join(
            direpath,props.workspace_fbxfolder_path, 
            "", 
            direfilename)

    elif props.use_otherfilepath_bool ==True:
        finalfbx_exportsavefile = os.path.join(
            props.use_otherfilepath_path, 
            props.workspace_fbxfolder_path, 
            "", 
            direfilename)


    # fbxの名前が.fbxの場合は自動連番機能がバグるため、リネームする。
    if os.path.basename(fbx_exportsavefile) == ".fbx":
        fbx_exportsavefilename = "export_fbx.fbx"
        finalfbx_exportsavefile = os.path.join(mkdirefilepath, fbx_exportsavefilename)
    # print('###final file name is ',finalfbx_exportsavefile)

    # 重複してるかどうかチェックする関数を実行
    if props.fbx_name_replace_bool == False:
        finalfbx_exportsavefile = filename_check(finalfbx_exportsavefile)

    return finalfbx_exportsavefile,mkdirefilepath


# フォルダ名のリプレイス回避
# フォルダを参照して重複してるファイルネームをチェックする
def filename_check(fbx_exportsavefile):
    if os.path.exists(fbx_exportsavefile) == True:

        # print('###found same file name. ',fbx_exportsavefile)

        (filepath, fileex) = os.path.splitext(fbx_exportsavefile) 
        # 該当なしないファイルネームが見つかるまでフォアを回す
        for i in range(100):
            newname = '{}_{}{}'.format(filepath, i, fileex)
            newpath = os.path.join(filepath, newname)
            if not os.path.exists(newpath):
                fbx_exportsavefile = newpath
                break  # 名前が空いている場合
    else:
        # print('###not same file name',)
        pass
    return fbx_exportsavefile


# コレクションの検索関数
def recurLayerCollection(layerColl, collName):
    found = None
    if (layerColl.name == collName):
        return layerColl
    for layer in layerColl.children:
        found = recurLayerCollection(layer, collName)
        if found:
            return found


# メインの出力関係
def checkpath():

    props = bpy.context.scene.simplefbxecport_propertygroup
    # ここにブレンダーファイルのファイルパスが入る
    blend_fbx_save_dir=props.workspace_path

    # ブレンダーファイルを保存していなかったりする場合は
    if os.path.dirname(bpy.data.filepath)=="":
        if props.use_otherfilepath_path =="" and props.use_otherfilepath_bool ==False:
            return False
        elif props.use_otherfilepath_path =="" and props.use_otherfilepath_bool ==True:
            return False
        elif props.use_otherfilepath_path !="" and props.use_otherfilepath_bool ==False:
            return False
        elif props.use_otherfilepath_path !="" and props.use_otherfilepath_bool ==True:
            return True
    else:
        return True



def actcol(
    fbx_act_collection_bool, 
    ):
    props = bpy.context.scene.simplefbxecport_propertygroup
    #　保存している場合

        # コレクション指定ににチェックが入っていたら
    if fbx_act_collection_bool == True:
        # 現在のアクティブコレクションを定義
        save_active_col = bpy.context.view_layer.active_layer_collection
        # コレクションを指定していたら
        if props.workspace_fbxfolder_path_Collection !=None:
            # アクティブコレクションを一時的に変える
            layer_collection = bpy.context.view_layer.layer_collection
            layerColl = recurLayerCollection(layer_collection, props.workspace_fbxfolder_path_Collection.name)
            bpy.context.view_layer.active_layer_collection = layerColl

    else:
        save_active_col = None

    return save_active_col



def select_childob():
    props = bpy.context.scene.simplefbxecport_propertygroup

    if props.fbx_children_recursive == True:
        bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')
        bpy.context.object.select_set(True)
    else:
        pass



def makdier(mkdirefilepath):

        

    # コレクションを選択してない場合
    if not os.path.exists(mkdirefilepath):
        os.makedirs(mkdirefilepath)
        # print("make dirfile")
    else:
        pass
        # print("already file")

# 出力する本体
def fbx_export_oprator(
    fbx_exportsavefile, 
    fbx_selectbool, 
    fbx_act_collection_bool, 
    fbxexportpath,
    save_active_col,
    copytexture_bool,
    embedtexture_bool,
    openfolder_bool,
    ):

    texturepath_mode = "AUTO"
    if copytexture_bool == True:
        texturepath_mode = "COPY"






    bpy.ops.export_scene.fbx(
    # FBXの設定項目
    filepath=fbx_exportsavefile,
    #選択状態
    use_selection=fbx_selectbool,
    #アクティブなコレクション
    use_active_collection=fbx_act_collection_bool,
    #reference paths (enum in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP'(KANZENNI WAKARERU), 'COPY'], 
    
    path_mode=texturepath_mode,
    # テクスチャをFBXにはめ込むか
    embed_textures=embedtexture_bool,
    )        

    # ファイルパス先を変える
    if openfolder_bool == True:
        subprocess.run('explorer /select,{}'.format(fbxexportpath))

    # アクティブコレクションを元に戻す
    if fbx_act_collection_bool == True:
        bpy.context.view_layer.active_layer_collection=save_active_col
    


# パネルの表示で使用
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
