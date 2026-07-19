import funcs
import imports
# This file is the main entry point for the PyWolf Launcher application. It initializes the application and displays the main window.
systempath = funcs.initsystempath()
title = f"PyWolf Launcher v{funcs.pywolfversion()} on {systempath['Pywolfroot']}"
if __name__ == "__main__":
    pywolf = imports.PySide6.QtWidgets.QApplication(imports.sys.argv)
    logtime=imports.datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    imports.logging.basicConfig(level=imports.logging.INFO,format='%(asctime)s - %(levelname)s %(message)s From %(filename)s ',filename=funcs.joinpath(systempath["systemassetroot"],"log",f"Pywolf_Lancher{logtime}.log"),filemode='w')
    imports.logging.info(f"PywolfLancherを{title}のタイトルで起動")
    # Initialize the PySide6 application
    main_window = funcs.create_main_window(title)
    main_window.setWindowTitle(title)
    imports.logging.info("PywolfLancherのメインウィンドウを作成")
    funcs.creatwinaudiolib(systempath)
    funcs.playSE(funcs.winauduolib(systempath,"Windows Logon"),loop=False,window=main_window)
    main_window.show()
    imports.logging.info("PywolfLancherのメインウィンドウを表示")
    funcs.winaudiolibs(systempath)
    userlist = funcs.createuserlist(guest=True)
    imports.logging.info(f"ユーザーリストを作成完了。")
    if len(userlist) == 0 or (len(userlist) == 1 and userlist[0].lower() == "guest"):
        result = funcs.accountselect()
        if result == 0:
            imports.logging.info("ユーザーはゲストアクセスを選択しました。")
            imports.PySide6.QtWidgets.QMessageBox.information(main_window, "ゲストアクセス", "ゲストアクセスが選択されました。ユーザーデータは保存されません。")
            imports.os.makedirs(exist_ok=True, name=funcs.getguestpath())
            imports.os.makedirs(funcs.joinpath(funcs.getguestpath(),"games"),exist_ok=True)
            imports.os.makedirs(funcs.joinpath(funcs.getguestpath(),"saves"),exist_ok=True)
            imports.os.makedirs(funcs.joinpath(funcs.getguestpath(),"screenshots"),exist_ok=True)
            imports.os.makedirs(funcs.joinpath(funcs.getguestpath(),"settings"),exist_ok=True)
            imports.logging.info("ゲストユーザーのディレクトリを作成しました。")
        elif result == 1:
            imports.logging.info("ユーザーはアカウント作成を選択しました。")
            main_window.hide()
            funcs.createlocaluser(systempath)
            main_window.show()
    else:
        imports.logging.info(f"ユーザーリストに{len(userlist)}人のユーザーが存在します。")
        selecteduser=funcs.userselect(userlist)
        if selecteduser is not None:
            userlist=userlist
            if userlist[selecteduser].lower() == "guest":
                imports.PySide6.QtWidgets.QMessageBox.information(main_window, "ゲストアクセス", "このユーザーのログインにはパスワードは必要ありません。ユーザーデータは保存されません。")
            else:
                # ユーザーが選択され、ゲストでない場合の処理をここに追加できます。
                #パスワードが空ではなく、かつユーザーの正当なパスワードが入力された場合にログインを許可するためにループ
                varidate,username=funcs.logon(main_window,systempath,userlist[selecteduser])
                if varidate:
                    imports.logging.info(f"ユーザー{username}としてログインしています。")
                    # ログイン成功後の処理をここに追加できます。
                    my_button = main_window.findChild(imports.PySide6.QtWidgets.QPushButton, "LogonButton")
                    my_button.setText(f"{username}")
                    userpath=funcs.inituserpath(systempath,username)
                    funcs.connect(main_window,systempath,userpath,username,pywolf)
                    my_button.clicked.connect(lambda: funcs.Logoutfunc(main_window))
        else:
            imports.logging.info("ユーザーリストからユーザーが選択されませんでした。")
    pywolf.exec()
    imports.logging.info("PywolfLancherを終了")
    imports.sys.exit()
