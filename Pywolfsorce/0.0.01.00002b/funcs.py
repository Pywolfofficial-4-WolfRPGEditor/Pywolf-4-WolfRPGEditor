import imports
import Exception
def connectcheckaddr()-> str: 
    return "https://example.com:443/index.html"
def _normalize_entries(entries: list[str]) -> list[str]:
    ignored = {".DS_Store", "desktop.ini", "Thumbs.db", "thumbs.db", "users.txt"}
    return [entry for entry in entries if entry not in ignored]
def _ensure_dir(path: str) -> None:
    imports.os.makedirs(path, exist_ok=True)
def initsystempath() -> dict[str, str]:
    path=dict()
    path["Pywolfroot"]=imports.os.getcwd()
    path["assetroot"]=normpath(joinpath(path["Pywolfroot"],"asset"))
    path["tmproot"]=normpath(joinpath(path["Pywolfroot"],"tmp"))
    path["logroot"]=normpath(joinpath(path["Pywolfroot"],"log"))
    path["userdirroot"]=normpath(joinpath(path["assetroot"],"users"))
    path["systemassetroot"]=normpath(joinpath(path["assetroot"],"system"))
    path["autodownload"]=normpath(joinpath(path["systemassetroot"],"autodownload"))
    path["shereassetroot"]=normpath(joinpath(path["assetroot"],"shere"))
    path["configroot"]=normpath(joinpath(path["systemassetroot"],"config"))
    path["userappsroot"]=normpath(joinpath(path["systemassetroot"],"apps"))
    path["iconroot"]=normpath(joinpath(path["systemassetroot"],"icon"))
    path["internalapproot"]=normpath(joinpath(path["systemassetroot"],"programs"))
    path["winaudioroot"]=normpath(joinpath(path["systemassetroot"],"audio","windows","media"))
    return path
def inituserpath(systempath,username,guest=False):
    path=dict()
    path["username"]=username
    path["userroot"]=normpath(joinpath(systempath["userdirroot"],username))
    path["userassetroot"]=normpath(joinpath(path["userroot"],"asset"))
    path["userconfigroot"]=normpath(joinpath(path["userroot"],"config"))
    path["usersaveroot"]=normpath(joinpath(path["userroot"],"saves"))
    path["userscreenshotroot"]=normpath(joinpath(path["userroot"],"screenshots"))
    path["usergameroot"]=normpath(joinpath(path["userroot"],"games"))
    return path
def normpath(path):
    return imports.os.path.normpath(path)
def joinpath(*args):
    return imports.os.path.join(*args)   
def create_main_window(title):
    loader=imports.PySide6.QtUiTools.QUiLoader()
    file=imports.PySide6.QtCore.QFile(joinpath(imports.os.getcwd(),"asset","system","config","PywolfLanchermainui.ui"))
    file.setParent(loader)
    loader.registerCustomWidget(imports.PySide6.QtWidgets.QMainWindow)
    file.open(imports.PySide6.QtCore.QFile.ReadOnly)
    main_window=loader.load(file)
    return main_window
def pywolfversion():
    version = "0.0.01.00002b"
    return version
def getappicon():
    iconpath=joinpath(initsystempath()["iconroot"],"PywolfLanchericon.png")
    icon=imports.PySide6.QtGui.QIcon(iconpath)
    return icon
def getapplogo():
    logopath=joinpath(initsystempath()["iconroot"],"PywolfLancherlogo.png")
    logo=imports.PySide6.QtGui.QPixmap(logopath)
    return logo
def getapplogoicon():
    logopath=joinpath(initsystempath()["iconroot"],"PywolfLancherlogo.png")
    logoicon=imports.PySide6.QtGui.QIcon(logopath)
    return logoicon
def getapplogopixmap():
    logopath=joinpath(initsystempath()["iconroot"],"PywolfLancherlogo.png")
    logopixmap=imports.PySide6.QtGui.QPixmap(logopath)
    return logopixmap
def createuserlist(guest=False) -> list[str]:
    imports.logging.info("ユーザーリストを作成")
    users = _normalize_entries(imports.os.listdir(initsystempath()["userdirroot"]))
    if not guest:
        users = [user for user in users if user.lower() != "guest"]
    imports.logging.info("ユーザーリストを作成完了。認識されたユーザー数：" + str(len(users)))
    return users
def createapplist() -> list[str]:
    imports.logging.info("アプリケーションリストを作成")
    return _normalize_entries(imports.os.listdir(initsystempath()["userappsroot"]))
def createapplistwithicon():
    apps=createapplist()
    appiconlist=[]
    for app in apps:
        appiconpath=joinpath(initsystempath()["userappsroot"],app,"icon.png")
        if imports.os.path.exists(appiconpath):
            appicon=imports.PySide6.QtGui.QIcon(appiconpath)
        else:
            appicon=getappicon()
        appiconlist.append((app,appicon))
    return appiconlist
def createapplistwithlogopic():
    apps=createapplist()
    applogopiclist=[]
    for app in apps:
        applogopicpath=joinpath(initsystempath()["userappsroot"],app,"logo.png")
        if imports.os.path.exists(applogopicpath):
            applogopic=imports.PySide6.QtGui.QPixmap(applogopicpath)
        else:
            applogopic=getapplogopixmap()
        applogopiclist.append((app,applogopic))
    return applogopiclist
def createapplistwithlogoicon():
    apps=createapplist()
    applogoiconlist=[]
    for app in apps:
        applogoiconpath=joinpath(initsystempath()["userappsroot"],app,"logo.png")
        if imports.os.path.exists(applogoiconpath):
            applogoicon=imports.PySide6.QtGui.QIcon(applogoiconpath)
        else:
            applogoicon=getapplogoicon()
        applogoiconlist.append((app,applogoicon))
    return applogoiconlist
def createapplistwithlogopicandicon():
    apps=createapplist()
    applogopiciconlist=[]
    for app in apps:
        applogopicpath=joinpath(initsystempath()["userappsroot"],app,"logo.png")
        if imports.os.path.exists(applogopicpath):
            applogopic=imports.PySide6.QtGui.QPixmap(applogopicpath)
            applogoicon=imports.PySide6.QtGui.QIcon(applogopicpath)
        else:
            applogopic=getapplogopixmap()
            applogoicon=getapplogoicon()
        applogopiciconlist.append((app,applogopic,applogoicon))
    return applogopiciconlist
def getguestpath():
    guestpath=joinpath(initsystempath()["userdirroot"],"guest")
    return guestpath
def accountselect():
    class LoginSelectionDialog(imports.PySide6.QtWidgets.QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("開始方法の選択")
            self.resize(400, 150)
            # レイアウトの作成
            layout = imports.PySide6.QtWidgets.QVBoxLayout(self)
            # メッセージラベル
            label = imports.PySide6.QtWidgets.QLabel("続行するには、以下のいずれかを選択してください：")
            layout.addWidget(label)
            # 1. ゲストアクセスのボタン
            self.guest_btn = imports.PySide6.QtWidgets.QCommandLinkButton("ゲストとして続行")
            self.guest_btn.setDescription("アカウントを作成せずに、すぐに利用を開始します。")
            self.guest_btn.clicked.connect(self.on_guest_selected)
            layout.addWidget(self.guest_btn)
            # 2. アカウント作成のボタン
            self.signup_btn = imports.PySide6.QtWidgets.QCommandLinkButton("新しくアカウントを作成")
            self.signup_btn.setDescription("設定を保存し、すべての機能を利用できるようにします。")
            self.signup_btn.clicked.connect(self.on_signup_selected)
            layout.addWidget(self.signup_btn)
        def on_guest_selected(self):
            self.done(0)  # ダイアログを閉じる（戻り値：Accepted）
        def on_signup_selected(self):
            self.done(1)  # 独自のカスタム値を返して閉じることも可能
    dialog = LoginSelectionDialog()
    result = dialog.exec()
    return result  # 0: ゲスト, 1: アカウント作成
def createlocaluser(systempath):
    imports.logging.info("ローカルユーザーを作成開始")
    class UserCreationWindow(imports.PySide6.QtWidgets.QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Pywolfローカルユーザー作成")
            self.setMinimumWidth(400)
            self.setup_ui(systempath=systempath)
        def setup_ui(self,systempath):
            self.resize(690,350)
            layout = imports.PySide6.QtWidgets.QVBoxLayout(self)
            self.form = imports.PySide6.QtWidgets.QFormLayout()
            # 入力フィールドの定義
            self.username = imports.PySide6.QtWidgets.QLineEdit()
            self.username.setPlaceholderText("ユーザー名はフォルダに使用できない文字を含んでいてはならず、このPC内でユニークである必要があります。")
            self.username_kana = imports.PySide6.QtWidgets.QLineEdit()
            self.username_kana.setPlaceholderText("ふりがなはひらがなのみで、225文字以内で入力してください。")
            self.alias = imports.PySide6.QtWidgets.QLineEdit()
            self.alias.setPlaceholderText("別名は半角英数字のみで、225文字以内で入力してください。")
            self.alias_kana = imports.PySide6.QtWidgets.QLineEdit()
            self.alias_kana.setPlaceholderText("別名ふりがなはひらがなのみで、225文字以内で入力してください。")
            self.password = imports.PySide6.QtWidgets.QLineEdit()
            self.password.setPlaceholderText("パスワードは英大文字、小文字、数字、記号を全て含み、強固である必要があります。")
            self.password.setEchoMode(imports.PySide6.QtWidgets.QLineEdit.EchoMode.Password)
            self.password_confirm = imports.PySide6.QtWidgets.QLineEdit()
            self.password_confirm.setPlaceholderText("パスワードを再入力してください。")
            self.password_confirm.setEchoMode(imports.PySide6.QtWidgets.QLineEdit.EchoMode.Password)
            # 実績通知（ドロップダウン）
            self.notif_range = imports.PySide6.QtWidgets.QComboBox()
            self.notif_range.addItems(notfrange())
            self.notif_content = imports.PySide6.QtWidgets.QComboBox()
            self.notif_content.addItems(notfcontent())
            # フォームへの追加
            self.form.addRow("ユーザー名:", self.username)
            self.form.addRow("ふりがな:", self.username_kana)
            self.form.addRow("別名 (半角英数):", self.alias)
            self.form.addRow("別名ふりがな:", self.alias_kana)
            self.form.addRow("パスワード:", self.password)
            self.form.addRow("パスワード確認:", self.password_confirm)
            self.form.addRow("実績通知範囲:", self.notif_range)
            self.form.addRow("実績通知内容:", self.notif_content)
            layout.addLayout(self.form)
            # ボタン
            self.btn_create = imports.PySide6.QtWidgets.QPushButton("ユーザー作成")
            self.btn_server = imports.PySide6.QtWidgets.QPushButton("サーバー起動")
            self.btn_cancel = imports.PySide6.QtWidgets.QPushButton("キャンセル")
            self.btn_create.clicked.connect(lambda:self.validate_and_save(systempath=systempath))
            self.btn_cancel.clicked.connect(self.close)
            layout.addWidget(self.btn_create)
            layout.addWidget(self.btn_server)
            layout.addWidget(self.btn_cancel)
        def validate_and_save(self,systempath):
            # 1. ユーザー名 (フォルダ名使用不可文字: \ / : * ? " < > |)
            invalid_chars = r'[\\/:*?"<>|]'
            if imports.re.search(invalid_chars, self.username.text()) or not self.username.text():
                return self.error("ユーザー名にフォルダ名に使用できない文字が含まれているか、空です。")

            # 2. ふりがな (ひらがなのみ、225文字以内)
            kana_pattern = r'^[ぁ-んー]+$'
            if not imports.re.match(kana_pattern, self.username_kana.text()) or len(self.username_kana.text()) > 225:
                return self.error("ユーザー名ふりがなは、ひらがなのみ225文字以内で入力してください。")

            # 3. 別名 (半角英数のみ)
            if not self.alias.text().isalnum() or not self.alias.text().isascii():
                return self.error("別名は半角英数字のみで入力してください。")

            # 4. 別名ふりがな
            if not imports.re.match(kana_pattern, self.alias_kana.text()) or len(self.alias_kana.text()) > 225:
                return self.error("別名ふりがなは、ひらがなのみ225文字以内で入力してください。")
            # 5. パスワード強度
            # 大文字、小文字、記号、数字、8文字以上を想定
            pw = self.password.text()
            strong_pw = (imports.re.search(r'[A-Z]', pw) and imports.re.search(r'[a-z]', pw) and 
                        imports.re.search(r'[0-9]', pw) and imports.re.search(r'[!@#$%^&*(),.?":{}|<>]', pw) and len(pw) >= 8)
            
            if not strong_pw:
                return self.error("パスワードは英大文字、小文字、数字、記号を全て含み、強固である必要があります。")

            # 6. パスワード一致確認とハッシュ化
            if pw != self.password_confirm.text():
                return self.error("パスワード確認が一致しません。")

            # ハッシュ化処理 (PBKDF2-SHA256)
            salt = imports.os.urandom(16)
            hashed_password = imports.hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, 100000)           
            userdate={"username":self.username.text(),"username_kana":self.username_kana.text(),"alias":self.alias.text(),"alias_kana":self.alias_kana.text(),"password_hash":hashed_password.hex().upper(),"salt":salt.hex().upper(),"notif_range":notfrangebool()[self.notif_range.currentIndex()],"notif_content":notfcontentbool()[self.notif_content.currentIndex()]}
            user_data_json = imports.json.dumps(userdate,ensure_ascii=True,indent=4)
            user_dir = joinpath(initsystempath()["userdirroot"], self.username.text())
            if imports.os.path.exists(user_dir):
                return self.error("ユーザー名はこのPC内でユニークである必要があります。")
            imports.os.makedirs(user_dir)
            userfilecontent=dict({"version": "1.0","content":{"userdate":1},"publisher":"System","description":"ユーザーデータを保存するファイル。ユーザー名、パスワードハッシュ、ソルト、実績通知設定などが含まれます。","guarded":True,"verified":True})
            base64_user_data = imports.base64.b64encode(user_data_json.encode()).decode()
            imports.os.makedirs(systempath["tmproot"], exist_ok=True)
            imports.os.makedirs(normpath(joinpath(systempath["tmproot"],"userdate")),exist_ok=True)
            imports.os.makedirs(systempath["userdirroot"], exist_ok=True)
            manifest_file = normpath(joinpath(systempath["tmproot"],"userdate", f"manifest.json"))
            with open(manifest_file, "w", encoding="utf-8") as f:
                imports.json.dump(userfilecontent, f, ensure_ascii=True, indent=4)
            with open(joinpath(normpath(joinpath(systempath["tmproot"],"userdate", f"userdata.b64"))), "w", encoding="utf-8") as f:
                f.write(base64_user_data)
            imports.os.makedirs(joinpath(user_dir, "games"), exist_ok=True)
            imports.os.makedirs(joinpath(user_dir, "saves"), exist_ok=True)
            imports.os.makedirs(joinpath(user_dir, "screenshots"), exist_ok=True)
            imports.os.makedirs(joinpath(user_dir, "settings"), exist_ok=True)
            temp_archive_base = normpath(joinpath(systempath["tmproot"], "userdate_archive"))
            archive_path = imports.shutil.make_archive(root_dir=normpath(joinpath(systempath["tmproot"], "userdate")), format="zip", base_name=temp_archive_base)
            if not archive_path or not imports.os.path.exists(archive_path):
                return self.error("ユーザーデータの圧縮に失敗しました。")
            with open(archive_path, "rb") as a:
                zip_bytes = a.read()
            encoded_data = imports.base64.b64encode(zip_bytes).decode()
            with open(normpath(joinpath(systempath["userdirroot"], self.username.text(), "userdata.pwpack")), "wt+", encoding="utf-8") as d:
                d.write(encoded_data)
            imports.shutil.rmtree(normpath(joinpath(systempath["tmproot"], "userdate")), ignore_errors=True)
            imports.os.remove(archive_path)
            imports.PySide6.QtWidgets.QMessageBox.information(self, "成功", "ユーザーが正常に作成され、パスワードはハッシュ化されて保存されました。")
            imports.logging.info(f"ユーザー{self.username.text()}を作成しました。ユーザーデータはハッシュ化されて保存されました。")
            imports.logging.info(f"ユーザーデータの保存場所: {normpath(joinpath(user_dir, 'userdata.pwpack'))}")
            imports.PySide6.QtWidgets.QMessageBox.warning(self, "Pywolfの再起動が必要", "変更を適用するにはPywolfの再起動が必要です。再起動後、ユーザーリストに新しいユーザーが表示されるようになります。")
            self.close()
            imports.os.execl(imports.sys.executable, imports.sys.executable, *imports.sys.argv)
        def error(self, message):
            imports.PySide6.QtWidgets.QMessageBox.warning(self, "エラー", message)
    window = UserCreationWindow()
    window.exec()
def notfrange():
    return ["どこにも通知を送信しない", "このPCにのみ通知を送信する", "このPC以外のローカルネットワークに通知を送信する", "ローカルネットワーク上の全てのPCに通知を送信する"]
def notfrangebool():
    return [(False,False),(True,False),(False,True),(True,True)]
def notfcontent():
    return ["実績の達成のみ", "ゲームの起動と終了のみ", "発展的なウェイポイントのみ","実績の達成以外","ゲームの起動と終了以外","発展的ウェイポイント以外", "すべての通知を表示する"]
def notfcontentbool():
    return [(True,False,False),(False,True,False),(False,False,True),(False,True,True),(True,False,True),(True,True,False),(True,True,True)]
def userselect(userlist):
    class UserSelectorApp(imports.PySide6.QtWidgets.QDialog):
        def __init__(self, userlist):
            super().__init__()
            self.returnvalue=None
            self.setWindowTitle("Pywolfログインユーザーの選択")
            self.resize(300, 400)
            # --- UIレイアウトの設定 ---
            layout = imports.PySide6.QtWidgets.QVBoxLayout()
            # ラベル
            self.label = imports.PySide6.QtWidgets.QLabel("ログインするユーザーを選択してください。")
            layout.addWidget(self.label)
            # リストウィジェット
            self.list_widget = imports.PySide6.QtWidgets.QListWidget()
            users = userlist
            self.list_widget.addItems(users) # 一括追加
            layout.addWidget(self.list_widget)
            # 選択ボタン
            self.btn_select = imports.PySide6.QtWidgets.QPushButton("選択")
            self.btn_select.clicked.connect(lambda: self.on_select_clicked())
            layout.addWidget(self.btn_select)
            self.setLayout(layout)
        def on_select_clicked(self):
            """選択ボタンが押された時の処理"""
            # 現在選択されているアイテムを取得
            current_item = self.list_widget.currentItem()
            if current_item:
                selected_user=self.list_widget.currentRow()
                imports.logging.info(f"ユーザーリストから{current_item.text()}が選択されました。")
                self.done(selected_user)  # ダイアログを閉じる（戻り値：選択されたユーザーのインデックス）
                self.returnvalue=selected_user
            else:
                imports.PySide6.QtWidgets.QMessageBox.warning(self, "未選択", "ユーザーを選択してください。")
    window = UserSelectorApp(userlist)
    window.exec()
    return window.returnvalue
def startserver():
    pass
def logondialog(username):
    class LoginDialog(imports.PySide6.QtWidgets.QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ログイン")
            self.setFixedSize(500, 200)
            # メインレイアウト
            layout = imports.PySide6.QtWidgets.QVBoxLayout(self)
            layout.addWidget(imports.PySide6.QtWidgets.QLabel(f"{username}のPywolfユーザーとして続行するには"))
            layout.addWidget(imports.PySide6.QtWidgets.QLabel("パスワードの入力が必要です。"))
            # ユーザー名入力
            layout.addWidget(imports.PySide6.QtWidgets.QLabel("ユーザー名:"))
            self.username_input = imports.PySide6.QtWidgets.QLineEdit()
            self.username_input.setText(username)
            self.username_input.setReadOnly(True)  # ユーザー名は変更不可
            self.username_input.setEnabled(False)  # ユーザー名入力を無効化
            layout.addWidget(self.username_input)
            # パスワード入力
            layout.addWidget(imports.PySide6.QtWidgets.QLabel("パスワード:"))
            self.password_input = imports.PySide6.QtWidgets.QLineEdit()
            self.password_input.setPlaceholderText("Password")
            self.password_input.setEchoMode(imports.PySide6.QtWidgets.QLineEdit.EchoMode.Password) # 初期状態は非表示
            # --- パスワード表示/非表示の切り替え機能 ---
            # 標準のスタイルから「表示」アイコンを取得
            self.toggle_action = self.password_input.addAction(
                self.style().standardIcon(imports.PySide6.QtWidgets.QStyle.StandardPixmap.SP_FileDialogContentsView),
                imports.PySide6.QtWidgets.QLineEdit.ActionPosition.TrailingPosition
            )
            self.toggle_action.setToolTip("パスワードの表示/非表示を切り替える")
            self.toggle_action.triggered.connect(self.toggle_password_visibility)
            # ------------------------------------------        
            layout.addWidget(self.password_input)
            # ボタン
            self.login_button = imports.PySide6.QtWidgets.QPushButton("ログイン")
            self.login_button.clicked.connect(self.handle_login)
            layout.addWidget(self.login_button)

        def toggle_password_visibility(self):
            """パスワードの表示状態を反転させる"""
            if self.password_input.echoMode() == imports.PySide6.QtWidgets.QLineEdit.EchoMode.Password:
                self.password_input.setEchoMode(imports.PySide6.QtWidgets.QLineEdit.EchoMode.Normal)
            else:
                self.password_input.setEchoMode(imports.PySide6.QtWidgets.QLineEdit.EchoMode.Password)
        def handle_login(self):
            user = self.username_input.text()
            pw = self.password_input.text()
            imports.logging.info(f"ログインの試行: {user} / {imports.hashlib.sha256(pw.encode()).hexdigest().upper()}")
            self.accept()
    dialog = LoginDialog()
    if dialog.exec() == imports.PySide6.QtWidgets.QDialog.DialogCode.Accepted and dialog.username_input.text() and dialog.password_input.text():
        return dialog.username_input.text(), dialog.password_input.text()
    return None, None
def varidatepassword(username, systempath) -> tuple[imports.typing.Optional[str], imports.typing.Optional[bytes]]:
    _ensure_dir(initsystempath()["tmproot"])
    user_dir = joinpath(initsystempath()["userdirroot"], username)
    user_data_file = joinpath(user_dir, "userdata.pwpack")
    if not imports.os.path.exists(user_data_file):
        imports.logging.error(f"ユーザーデータファイルが見つかりません: {user_data_file}")
        return None, None

    try:
        with open(user_data_file, "rb") as f:
            user_data_bytes = imports.base64.b64decode(f.read())
    except Exception as e:
        imports.logging.error(f"ユーザーデータのデコードに失敗: {e}")
        return None, None

    temp_zip_path = joinpath(initsystempath()["tmproot"], f"{username}_userdata.zip")
    with open(temp_zip_path, "wb") as f:
        f.write(user_data_bytes)

    temp_extract_path = joinpath(systempath["tmproot"], f"{username}_userdata")
    imports.shutil.unpack_archive(temp_zip_path, temp_extract_path)

    user_data_base_path = joinpath(temp_extract_path, "userdata.b64")
    if not imports.os.path.exists(user_data_base_path):
        imports.logging.error(f"解凍されたユーザーデータが見つかりません: {user_data_base_path}")
        imports.shutil.rmtree(temp_extract_path, ignore_errors=True)
        imports.os.remove(temp_zip_path)
        return None, None

    try:
        with open(user_data_base_path, "r", encoding="utf-8") as f:
            userdate = imports.base64.b64decode(f.read()).decode()
    except Exception as e:
        imports.logging.error(f"ユーザーデータの読み込みに失敗: {e}")
        imports.shutil.rmtree(temp_extract_path, ignore_errors=True)
        imports.os.remove(temp_zip_path)
        return None, None

    imports.os.remove(temp_zip_path)
    imports.os.remove(user_data_base_path)

    try:
        userdate_json = imports.json.loads(userdate)
        stored_password_hash = userdate_json["password_hash"]
        stored_salt = bytes.fromhex(userdate_json["salt"])
    except Exception as e:
        imports.logging.error(f"ユーザーデータの解析に失敗: {e}")
        stored_password_hash = None
        stored_salt = None

    imports.shutil.rmtree(temp_extract_path, ignore_errors=True)
    return stored_password_hash, stored_salt
def not_implemented(mainwindow):
    imports.PySide6.QtWidgets.QMessageBox.information(mainwindow,"未実装","この機能は未実装です。\n今後のアップデートに乞う(こう)ご期待!!!")
def gameselect(username,systempath,mainwindow,gamelist):
    class GameSelectorApp(imports.PySide6.QtWidgets.QDialog):
        def __init__(self):
            super().__init__()
        def setup_ui(self):
            self.returnvalue=None
            self.setWindowTitle("ゲームの選択")
            self.resize(400, 300)
            layout = imports.PySide6.QtWidgets.QVBoxLayout(self)
            self.label = imports.PySide6.QtWidgets.QLabel("起動するゲームを選択してください。")
            layout.addWidget(self.label)
            self.list_widget = imports.PySide6.QtWidgets.QListWidget()
            games=scanusergames(username,systempath)
            self.list_widget.addItems(games) # 一括追加
            layout.addWidget(self.list_widget)
            self.btn_select = imports.PySide6.QtWidgets.QPushButton("選択")
            self.btn_select.clicked.connect(lambda: self.on_select_clicked(window=mainwindow,systempath=systempath))
            layout.addWidget(self.btn_select)
        def on_select_clicked(self,systempath,window=mainwindow):
            """選択ボタンが押された時の処理"""
            # 現在選択されているアイテムを取得
            current_item = self.list_widget.currentItem()
            if current_item:
                selected_game = self.list_widget.currentRow()
                imports.logging.info(f"ゲームリストから{current_item.text()}が選択されました。")
                self.done(selected_game + 1)  # 0 はキャンセル扱いにするため、1基準で返す
            else:
                imports.PySide6.QtWidgets.QMessageBox.warning(self, "未選択", "ゲームを選択してください。")
    window = GameSelectorApp()
    window.setup_ui()
    games = scanusergames(username, systempath)
    result = window.exec()
    if result <= 0 or result > len(games):
        imports.logging.warning("ゲーム選択がキャンセルされました。")
        return
    game = games[result - 1]
    bootgame(joinpath(systempath["Pywolfroot"], "asset", "users", username, "games", game))
def scanusergames(username, systempath) -> list[str]:
    path = inituserpath(systempath, username)
    raw_games = _normalize_entries(imports.os.listdir(path["usergameroot"]))
    valid_games: list[str] = []
    for game in raw_games:
        game_dir = joinpath(path["usergameroot"], game)
        if not imports.os.path.isdir(game_dir):
            continue
        if imports.os.path.exists(joinpath(game_dir, "Game.exe")) or imports.os.path.exists(joinpath(game_dir, "GamePro.exe")):
            if game.lower() != "game":
                valid_games.append(game)
    return valid_games
def is_wolf_Rpg_Editor(gamepath):
    if imports.os.path.exists(joinpath(gamepath,"game.exe"))or imports.os.path.exists(joinpath(gamepath,"Game.exe")):
        try:
            TARGET_STRINGS = [b"WOLF RPG Editor",b"WolfRPG",b"CommonEvent.dat",b"Game.dat"]
            pe = imports.pefile.PE(joinpath(gamepath,"Game.exe"))
            a=imports.pprint.pformat(pe.dump_info())
            with open("pe_dump.txt", "w", encoding="utf-8") as f:
                f.write(a)
            # .rdata や .data セクションを見る
            info=pe.dump_info()
            for target in TARGET_STRINGS:
                if target in info.encode():
                    return True
        except Exception as e:
            imports.logging.error(f"PEファイルの解析に失敗: {e}")
    return False
def install_game(mainwindow, systempath, userpath, username, importfrom="archive", net=False, **kwargs):
    imports.logging.info(f"ゲームのインストールオペレーションを開始します。インストール元: {importfrom}")
    match importfrom:
        case "archive":
            archive_path = ""
            if not net:
                selected = imports.PySide6.QtWidgets.QFileDialog.getOpenFileName(
                    mainwindow,
                    "インストールするゲームのアーカイブファイルを選択してください",
                    filter="対応しているアーカイブファイル (*.zip *.tar *.gz *.tar.gz *.tgz *.bz2 *.tar.bz2 *.xz *.tar.xz)"
                )
                archive_path = selected[0]
            else:
                archive_path = normpath(joinpath(systempath["autodownload"], "autodownload.zip"))

            if not archive_path:
                imports.logging.warning("アーカイブのパスが指定されませんでした。インストールを中止します。")
                return

            _ensure_dir(systempath["tmproot"])
            try:
                imports.shutil.unpack_archive(archive_path, systempath["tmproot"])
            except RuntimeError:
                imports.shutil.rmtree(systempath["tmproot"], ignore_errors=True)
                _ensure_dir(systempath["tmproot"])
                imports.logging.info("このゲームのインストールにはパスワードが必要")
                password_text, ok = imports.PySide6.QtWidgets.QInputDialog.getText(
                    mainwindow,
                    "認証が必須",
                    "このゲームの制作者はゲームのインストールに認証を要求しています。\nゲームの制作者から提供されたパスワードを入力してください。",
                    imports.PySide6.QtWidgets.QLineEdit.EchoMode.Password
                )
                if not ok or not password_text:
                    imports.logging.warning("パスワード入力がキャンセルされました。インストールを中断します。")
                    return
                unpack_archive(zip_path=archive_path, extract_dir=systempath["tmproot"], pwd_str=password_text)
            extracted_items = _normalize_entries(imports.os.listdir(normpath(systempath["tmproot"])))
            if not extracted_items:
                raise imports.Exception.PywolfException.FileException.EmptyArchiveFileException(
                    archive_path,
                    imports.inspect.currentframe().f_code.co_name + "()"
                )
            top_has_files, top_has_dirs = check_zip_top_directory(archive_path)
            temp_root = normpath(systempath["tmproot"])
            if top_has_files and not top_has_dirs and len(extracted_items) == 1:
                temp_root = normpath(joinpath(systempath["tmproot"], extracted_items[0]))
            source_dirs: list[str] = []
            archive_name = imports.os.path.splitext(imports.os.path.basename(archive_path))[0]
            if imports.os.path.exists(joinpath(temp_root, "Game.exe")) or imports.os.path.exists(joinpath(temp_root, "game.exe")):
                source_dirs.append(temp_root)
            for item in _normalize_entries(imports.os.listdir(temp_root)):
                item_path = joinpath(temp_root, item)
                if imports.os.path.isdir(item_path) and (imports.os.path.exists(joinpath(item_path, "Game.exe")) or imports.os.path.exists(joinpath(item_path, "game.exe"))):
                    source_dirs.append(item_path)

            if not source_dirs:
                imports.logging.warning("有効なゲームディレクトリが見つかりませんでした。")
                imports.shutil.rmtree(systempath["tmproot"], ignore_errors=True)
                return

            for src_dir in source_dirs:
                canonical_name = imports.os.path.basename(src_dir) if src_dir != temp_root else archive_name
                if canonical_name.lower() == "":
                    canonical_name = archive_name
                dst_dir = normpath(joinpath(userpath["usergameroot"], canonical_name))
                _ensure_dir(dst_dir)
                copy_folder_with_progress(src_dir=src_dir, dst_dir=dst_dir)
                imports.logging.info(f"ゲーム{canonical_name}をユーザーフォルダに移動しました。")
                imports.logging.info("ゲームのインストールオペレーションが完了しました。")
            imports.shutil.rmtree(systempath["tmproot"], ignore_errors=True)
        case "pwpack":
            pass
        case "folder":
            #ディレクトリからWOLFRPGエディターのゲームをインストールする
            src=imports.PySide6.QtWidgets.QFileDialog.getExistingDirectory(mainwindow,"インストールを行うWolfRPGエディター製のゲームを選択してください。",systempath["Pywolfroot"])
            dsttemp=userpath["usergameroot"]
            gamename=normpath(src).split(imports.os.path.sep)[-1]
            imports.os.makedirs(normpath(joinpath(dsttemp,gamename)),exist_ok=True)
            dst=normpath(joinpath(dsttemp,gamename))
            copy_folder_with_progress(src_dir=src,dst_dir=dst)
            imports.logging.info("ゲームのインストールオペレーションが完了しました。")
        case "wolfstore":
            pass
        case "indevrepo":
            pass
        case "globalnetwork":
            sorce=None
            while sorce is None:
                sorcetemp=imports.PySide6.QtWidgets.QInputDialog().getText(mainwindow,"URLの入力","インストールしたいゲームのURLを入力してください。\nなお、URLはファイルを直接ダウンロードできるものである必要があります。")
                if sorcetemp[0]=="" or sorcetemp[1]==False:
                    sorce=None
                else:
                    sorce=sorcetemp[0]
            downresult=autodownloadfromglobalnet(sorce,systempath["autodownload"],binary=True,ensure_globalnet_connected=True)
            if downresult:
                imports.logging.info(f"{sorce}からゲームファイルのダウンロードが完了しました。")
            else:
                imports.logging.error(f"{sorce}からゲームファイルのダウンロードに失敗しました。")
                imports.shutil.rmtree(systempath["autodownload"], ignore_errors=True)
                return
            imports.os.makedirs(normpath(joinpath(systempath["autodownload"])),exist_ok=True)
            install_game(mainwindow, systempath=systempath, userpath=userpath, username=username, importfrom="archive", net=True)
            imports.os.remove(normpath(joinpath(systempath["autodownload"], "autodownload.zip")))
        case _:
            imports.logging.error(f"不明なインストールソース: {importfrom}")
def bootgame(gamepath):
    imports.logging.info(f"ゲームを起動します: {gamepath}")
    if imports.os.path.exists(joinpath(gamepath,"Game.exe")):
        imports.subprocess.Popen(joinpath(gamepath,"Game.exe"))
    elif imports.os.path.exists(joinpath(gamepath,"game.exe")):
        imports.subprocess.Popen(joinpath(gamepath,"game.exe"))
    else:
        imports.logging.error(f"ゲームの実行ファイルが見つかりません: {gamepath}")
def gamemanage(systempath,username,mainwindow,userpath):
    #ゲームの管理を行うためのウィンドウを表示する処理
    class GameManagementDialog(imports.PySide6.QtWidgets.QDialog):
        def __init__(self, target_folder, parent=None,userpath=None):
            super().__init__(parent)
            self.target_folder = target_folder
            self.init_ui()
            self.load_folders()
        def init_ui(self):
            self.setWindowTitle("ゲーム管理")
            self.resize(500, 600)
            # メインレイアウト
            main_layout = imports.PySide6.QtWidgets.QVBoxLayout(self)
            # 1. フォルダ一覧リスト
            self.folder_list = imports.PySide6.QtWidgets.QListWidget()
            self.folder_list.itemSelectionChanged.connect(self.update_button_states)
            main_layout.addWidget(self.folder_list)
            # 2. アクションボタン群の配置用レイアウト
            self.btn_layout = imports.PySide6.QtWidgets.QVBoxLayout()
            main_layout.addLayout(self.btn_layout)
            # 各種ボタンの生成
            self.btn_imp_all = imports.PySide6.QtWidgets.QPushButton("全セーブデータの .pwpack ファイルからのインポート")
            self.btn_imp_single = imports.PySide6.QtWidgets.QPushButton("単一セーブデータの .sav からのインポート")
            self.btn_exp_all = imports.PySide6.QtWidgets.QPushButton("全セーブデータの .pwpack ファイルへのエクスポート")
            self.btn_exp_single = imports.PySide6.QtWidgets.QPushButton("単一セーブデータの .sav へのエクスポート")
            self.btn_archive = imports.PySide6.QtWidgets.QPushButton("ゲームをアーカイブする")
            self.btn_option = imports.PySide6.QtWidgets.QPushButton("このゲームの起動オプションを設定する")
            # 赤文字ボタン（スタイルシートで色を変更）
            self.btn_delete_saves = imports.PySide6.QtWidgets.QPushButton("このゲームのセーブデータを全消去")
            self.btn_delete_saves.setStyleSheet("color: red; font-weight: bold;")
            self.btn_delete_game = imports.PySide6.QtWidgets.QPushButton("このゲームをアカウントから削除")
            self.btn_delete_game.setStyleSheet("color: red; font-weight: bold;")

            # ボタンをリストにまとめて一括管理
            self.action_buttons = [
                self.btn_imp_all, 
                self.btn_imp_single, 
                self.btn_exp_all, 
                self.btn_exp_single, 
                self.btn_archive, 
                self.btn_option, 
                self.btn_delete_saves, 
                self.btn_delete_game
            ]
            #リストにまとめたボタンにスロットをまとめて割り当て
            self.connect_slots=[
                lambda:not_implemented(self),
                lambda:saveactionexec(self.window(),systempath,userpath,self.folder_list.selectedItems()[0].text(),"import",False),
                lambda:not_implemented(self),
                lambda:saveactionexec(self,systempath,userpath,self.folder_list.selectedItems()[0].text(),"export",False),
                lambda:saveactionexec(self,systempath,userpath,self.folder_list.selectedItems()[0].text(),"archive",False),
                lambda:not_implemented(self),
                lambda:saveactionexec(self,systempath=systempath,userpath=userpath,game=self.folder_list.selectedItems()[0].text(),managed=False,action="delete_all"),
                lambda:gamedelete(self,self.folder_list.selectedItems()[0].text(),systempath,userpath,imports.PySide6.QtWidgets.QProgressDialog("ファイルを削除中...", "キャンセル", 0, 100, dialog))]
            #対応するシグナルとスロットを合体。
            con=0
            for bt in self.action_buttons:
                bt.clicked.connect(self.connect_slots[con])
                con+=1
            # レイアウトへ追加し、初期状態を「無効（選択中のみ有効）」にする
            for btn in self.action_buttons:
                self.btn_layout.addWidget(btn)
                btn.setEnabled(False)  # 初期状態は無効
            # 3. 確定 / キャンセルボタン
            self.button_box = imports.PySide6.QtWidgets.QDialogButtonBox(imports.PySide6.QtWidgets.QDialogButtonBox.Ok | imports.PySide6.QtWidgets.QDialogButtonBox.Cancel)
            # 日本語表記に変更
            self.button_box.button(imports.PySide6.QtWidgets.QDialogButtonBox.Ok).setText("確定")
            self.button_box.button(imports.PySide6.QtWidgets.QDialogButtonBox.Cancel).setText("キャンセル")
            self.button_box.accepted.connect(self.accept)
            self.button_box.rejected.connect(self.reject)
            main_layout.addWidget(self.button_box)
        def load_folders(self):
            """指定されたフォルダ内のディレクトリを一覧表示する"""
            if not imports.os.path.exists(self.target_folder):
                return
            for name in imports.os.listdir(self.target_folder):
                if name=="game":
                    continue
                full_path = imports.os.path.join(self.target_folder, name)
                if imports.os.path.isdir(full_path):
                    self.folder_list.addItem(name)
        def update_button_states(self):
            """項目が選択されている時だけボタンを有効化する"""
            has_selection = len(self.folder_list.selectedItems()) > 0
            for btn in self.action_buttons:
                btn.setEnabled(has_selection)
    dialog = GameManagementDialog(userpath["usergameroot"],mainwindow,userpath)
    dialog.exec()
def gamedelete(window, game, systempath, userpath, dialog):
    if FunnyFunction.youwontregretthis(
        window,
        (f"{game}のゲームを消去しますか？", "はい。このゲームを消します。", "いいえ、このゲームを残しておいてください。"),
        ("この操作は既存のゲームを全て完全消去します。それでも続行しますか?", "はい。それでも続行します。(次の画面では警告音注意です。)", "いいえ。ここで中止してください。"),
        (f"この操作は取り消しできません!<br>このまま続行すると{game}のゲームが全て消えてしまいになりますよ?<br>私は言いましたからね?<br>3回言いましたからね?<br>それでもあなたは本当に、、、<br><span style='color: red;'>こうかいしませんね?</span>", "はい、ぜったいにこうかいしません!!!", "いいえ、やっぱりけしたくないです、、、"),
        systempath,
    ):
        deletegame(game, userpath, systempath, dialog)
def deletegame(game : str, userpath: dict[str, str], systempath: dict[str, str], dialog: imports.PySide6.QtWidgets.QDialog):
    worker = DeleteWorker(joinpath(userpath["usergameroot"], game), dialog, systempath)
    def on_progress(value: int, path: str, dialog: imports.PySide6.QtWidgets.QProgressDialog) -> None:
        dialog.setValue(value)
        dialog.setLabelText(f"{normpath(path)} を削除中…")
    worker.progress_changed.connect(on_progress)
    progress_dialog = dialog
    progress_dialog.setWindowTitle("削除中")
    progress_dialog.setMinimumDuration(0)
    progress_dialog.setValue(0)
    progress_dialog.setWindowModality(imports.PySide6.QtCore.Qt.WindowModality.ApplicationModal)
    progress_dialog.setCancelButtonText("キャンセル")
    worker.cancelled.connect(progress_dialog.close)
    def on_worker_finished() -> None:
        progress_dialog.close()
        worker.deleteLater()
        worker.finished.disconnect(on_worker_finished)
        imports.logging.info(f"{game}の削除オペレーションが完了しました。")
        imports.PySide6.QtWidgets.QMessageBox.information(None, "オペレーションの完了", f"{game}の削除が終わりました。")
    worker.finished.connect(on_worker_finished)
    progress_dialog.canceled.connect(worker.cancelled.emit)
    worker.start()
    progress_dialog.exec()
class DeleteWorker(imports.PySide6.QtCore.QThread):
    progress_changed = imports.PySide6.QtCore.Signal(int, str,imports.PySide6.QtWidgets.QProgressBar)
    finished = imports.PySide6.QtCore.Signal()
    cancelled = imports.PySide6.QtCore.Signal()
    error_occurred = imports.PySide6.QtCore.Signal(str)
    def __init__(self, file_path: str, dialog: imports.PySide6.QtWidgets.QDialog,systempath: dict[str, str]):
        super().__init__()
        self.file_path = file_path
        self._is_cancelled = False
        self.dialog = dialog
        self.systempath = systempath
    def run(self) -> None:
        def canceled(self) -> None:
            imports.logging.info("ファイルの削除オペレーションが中止されました。")
        self._is_cancelled = False
        imports.logging.info(f"{self.file_path}のフォルダの削除オペレーションを開始")
        if not imports.os.path.exists(self.file_path):
            self.finished.emit()
            return
        all_paths: list[str] = []
        for root, dirs, files in imports.os.walk(self.file_path):
            for file_name in files:
                all_paths.append(joinpath(root, file_name))
            for dir_name in dirs:
                all_paths.append(joinpath(root, dir_name))
        all_paths = sorted(all_paths, key=lambda p: imports.os.path.isdir(p))
        all_paths.append(self.file_path)
        total_files = len(all_paths)
        if total_files == 0:
            self.finished.emit()
            imports.logging.info(f"{self.file_path}のフォルダの削除オペレーションはフォルダが空だったことにより強制終了しました。")
            return
        with imports.tqdm.tqdm(total=len(self.file_path), desc="消去中", unit="ファイル",leave=True) as pbar:
            for index, file_path in enumerate(all_paths):
                if self._is_cancelled:
                    self.cancelled.emit()
                    return
                try:
                    if fileaccessaudit("d", file_path,systempath=self.systempath):
                        if imports.os.path.isfile(file_path) or imports.os.path.islink(file_path):
                            imports.os.remove(file_path)
                        elif imports.os.path.isdir(file_path):
                            imports.shutil.rmtree(file_path)
                except Exception as e:
                    self.error_occurred.emit(f"削除失敗: {file_path}\nエラー: {str(e)}")
                    return
                progress_percentage = int((index + 1) / total_files * 100)
                self.progress_changed.emit(progress_percentage, file_path,self.dialog)
                pbar.update(1)
def copy_folder_with_progress(src_dir, dst_dir, system=False):
    files = []
    for root, dirs, filenames in imports.os.walk(src_dir):
        for filename in filenames:
            files.append(imports.os.path.join(root, filename))
    a = imports.PySide6.QtWidgets.QProgressDialog(parent=None, minimum=0, maximum=len(files))
    a.setWindowModality(imports.PySide6.QtCore.Qt.WindowModality.ApplicationModal)
    b = copythread(src_dir=src_dir, dst_dir=dst_dir, files=files)
    a.setMinimumDuration(0)
    a.setWindowTitle("データのコピー中…")

    def progressconnect(progress_dialog: imports.PySide6.QtWidgets.QProgressDialog, count: int, file_path: str) -> None:
        progress_dialog.setValue(count)
        progress_dialog.setLabelText(f"{normpath(file_path)} を\n{normpath(joinpath(dst_dir, imports.os.path.relpath(file_path, src_dir)))} にコピー中…")

    b.progress_signal.connect(lambda count: progressconnect(a, count, files[count - 1] if count > 0 and count <= len(files) else ""))

    def copyfinish(progress_dialog: imports.PySide6.QtWidgets.QProgressDialog, thread: copythread, src_dir: str, dst_dir: str, system=False) -> None:
        progress_dialog.close()
        thread.deleteLater()
        if not system:
            imports.logging.info(f"{src_dir}から{dst_dir}へのデータコピーは正常に完了しました。")

    b.finished.connect(lambda: copyfinish(a, b, src_dir, dst_dir, system))
    b.start()
    a.exec()
class UnpackThread(imports.PySide6.QtCore.QThread):
    # メインスレッドに通知するためのシグナル定義
    progress_max = imports.PySide6.QtCore.Signal(int)   # 全ファイル数
    progress_changed = imports.PySide6.QtCore.Signal(int, str)  # 現在のカウント, 処理中のファイル名
    finished_status = imports.PySide6.QtCore.Signal(bool, str)  # 成功成否, メッセージ

    def __init__(self, zip_path, extract_dir, password=None):
        super().__init__()
        self.zip_path = zip_path
        self.extract_dir = extract_dir
        self.password = password
        self._is_cancelled = False
    def cancel(self):
        self._is_cancelled = True
    def run(self):
        imports.logging.info("アーカイブ解凍処理開始")
        try:
            # cp932でメタデータを読み込み
            with imports.zipfile.ZipFile(self.zip_path, "r", allowZip64=True, metadata_encoding="cp932") as zf:
                ziplist = zf.namelist()
                self.progress_max.emit(len(ziplist))
                pwd_bytes = self.password.encode() if self.password else None
                for i, file in enumerate(ziplist):
                    if self._is_cancelled:
                        self.finished_status.emit(False, "キャンセルされました。")
                        return
                    # 進捗とファイル名をメインスレッドへ通知
                    self.progress_changed.emit(i, file)
                    # 解凍実行
                    zf.extract(file, self.extract_dir, pwd=pwd_bytes)
                self.progress_changed.emit(len(ziplist), "完了")
                self.finished_status.emit(True, "解凍が完了しました。")
                imports.logging.info("アーカイブ解凍処理完了")
        except Exception as e:
            imports.logging.error(f"解凍エラー: {str(e)}")
            self.finished_status.emit(False, f"エラーが発生しました: {str(e)}")
def compress_zip_with_progress(window,sorce_dir,target_zip,password,compression=imports.zipfile.ZIP_LZMA,compression_level=9,userpath=dict()):
    a=imports.glob.glob(sorce_dir+imports.os.sep+"**",recursive=True)
    b=imports.PySide6.QtWidgets.QProgressDialog(labelText="zip圧縮開始中,,,",minimum=0,maximum=len(a),minimumDuration=0.01)
    b.setWindowModality(imports.PySide6.QtCore.Qt.WindowModality.ApplicationModal)
    b.setWindowTitle("アーカイブ中です。")
    c = compressthread(window, list(a), target_zip, password, compression=compression, compression_level=compression_level, userpath=userpath)
    def progressconnect(progress_dialog: imports.PySide6.QtWidgets.QProgressDialog, index: int, file: str) -> None:
        progress_dialog.setValue(index)
        progress_dialog.setLabelText(f"{file}をアーカイブしています。")
    c.progress_changed.connect(lambda index, file: progressconnect(b, index, file))
    def compressfinish(a,b,compress_dir,compression,compression_level):
        compression_dict={0:"無",8:"標準",12:"Bzip2",14:"LZMA"}
        a.close()
        b.deleteLater()
        try:
            imports.logging.info(f"{compress_dir}のアーカイブは{compression_dict[compression]}のレベル{str(compression_level)}圧縮を使用して正常に完了しました。")
        except Exception:
                    imports.logging.info(f"{compress_dir}のアーカイブは{compression}のレベル{str(compression_level)}圧縮を使用して正常に完了しました。")
    c.finished_status.connect(lambda success, message: compressfinish(b, c, sorce_dir, compression, compression_level))
    c.start()
class compressthread(imports.PySide6.QtCore.QThread):
    # メインスレッドに通知するためのシグナル定義
    progress_max = imports.PySide6.QtCore.Signal(int)   # 全ファイル数
    progress_changed = imports.PySide6.QtCore.Signal(int, str)  # 現在のカウント, 処理中のファイル名
    finished_status = imports.PySide6.QtCore.Signal(bool, str)  # 成功成否, メッセージ
    def __init__(self,window,sorce_list,target_zip,password,compression,compression_level,userpath):
        super().__init__()
        self.window=window
        self.sorce_list=sorce_list
        self.target_zip=target_zip
        self.userpath=userpath
        if password is not None:
            self.password=password.encode()
        self.compression=compression
        self.compression_level=compression_level
    def run(self):
        self.progress_max.emit(len(self.sorce_list))
        with imports.tqdm.tqdm(total=len(self.sorce_list), desc="ファイルのアーカイブ中", unit="ファイル",leave=True) as pbar:
            with imports.zipfile.ZipFile(self.target_zip,"w",compression=self.compression,compresslevel=self.compression_level,allowZip64=True)as file:
                try:
                    file.setpassword(self.password)
                except AttributeError:
                    pass
                for index, files in enumerate(self.sorce_list, start=1):
                    file_path = imports.os.path.abspath(files)
                    self.progress_changed.emit(index, file_path)
                    arcname = imports.os.path.relpath(file_path, self.userpath.get("usergameroot", imports.os.path.dirname(file_path)))
                    file.write(filename=file_path, arcname=arcname)
                    pbar.update()
def unpack_archive(zip_path,extract_dir,pwd_str):
    # 1. 進捗ダイアログをメインスレッドで生成
    imports.logging.info("解凍処理突入"+imports.hashlib.sha256(open(zip_path, 'rb').read()).hexdigest().upper())
    prog = imports.PySide6.QtWidgets.QProgressDialog("解凍処理中…", "キャンセル", 0, 100,None)
    prog.setWindowTitle("進捗状況")
    prog.setWindowModality(imports.PySide6.QtCore.Qt.WindowModal)
    prog.setMinimumDuration(0)
    prog.setValue(0)
    # 2. スレッドのインスタンス化
    unpack_worker = UnpackThread(zip_path, extract_dir, pwd_str)
    # 3. シグナルとスロットの接続
    unpack_worker.progress_max.connect(prog.setMaximum)
    unpack_worker.progress_changed.connect(
        lambda count, filename: (prog.setValue(count), prog.setLabelText(f"解凍中: {filename}"))
    )
    # キャンセルボタンが押されたらスレッドに停止を要求
    prog.canceled.connect(unpack_worker.cancel)
    # 終了時のクリーンアップ処理
    unpack_worker.finished.connect(prog.close)
    # 4. スレッド開始
    unpack_worker.finished.connect(lambda:unpackfinish(unpack_worker))
    unpack_worker.start()
    prog.exec()
def unpackfinish(worker):
    worker.deleteLater()
    a=FunnyFunction.selfdestractdiag()
    a.exec()
def check_zip_top_directory(zip_path) -> tuple[bool, bool]:
    with imports.zipfile.ZipFile(zip_path, 'r') as z:
        top_entries = {}
        for name in z.namelist():
            if name.startswith('__MACOSX/') or name.endswith('/') and name.count('/') == 1:
                continue
            entry = name.split('/')[0]
            if not entry:
                continue
            is_dir = any(member.startswith(entry + '/') for member in z.namelist())
            top_entries[entry] = top_entries.get(entry, False) or is_dir

        if not top_entries:
            return False, False

        has_top_dirs = any(is_dir for is_dir in top_entries.values())
        has_top_files = any(not is_dir for is_dir in top_entries.values())
        return has_top_files, has_top_dirs
class copythread(imports.PySide6.QtCore.QThread):
    def __init__(self,src_dir,dst_dir,files):
        super().__init__()
        self.src_dir=src_dir
        self.dst_dir=dst_dir
        self.files=files
    progress_signal = imports.PySide6.QtCore.Signal(int)
    def run(self):
        with imports.tqdm.tqdm(total=len(self.files), desc="コピー中", unit="ファイル") as pbar:
            for index, file_path in enumerate(self.files, start=1):
                rel_path = imports.os.path.relpath(file_path, self.src_dir)
                target_path = imports.os.path.join(self.dst_dir, rel_path)
                imports.os.makedirs(imports.os.path.dirname(target_path), exist_ok=True)
                imports.shutil.copy2(file_path, target_path)
                pbar.update(1)
                self.progress_signal.emit(index)
def fileaccessaudit(mode, path, systempath) -> bool:
    readonlypathlist = [r"C:\Windows", r"C:\Program Files", r"C:\Program Files (x86)", r"C:\ProgramData", r"C:\Microsoft"]
    try:
        other_users = [joinpath(r"C:\Users", name) for name in imports.os.listdir(r"C:\Users") if name not in {"desktop.ini", "Thumbs.db", "thumbs.db"}]
    except Exception:
        other_users = []

    current_user = imports.os.path.expanduser('~')
    other_users = [user for user in other_users if user != current_user]
    readonlypathlist.extend(other_users)
    for accesspath in readonlypathlist:
        if path.startswith(accesspath):
            return not (mode in {"d", "m"})
    return True
def saveactionexec(window,systempath,userpath,game,action="import",managed=False):
    upd=updatemanifest(window,systempath,imports.os.listdir(userpath["usergameroot"]))
    if not upd:
        return
    if managed:
        gamepath=joinpath(userpath["usersaveroot"],game)
    else:
        gamepath=joinpath(userpath["usergameroot"],game,"Save")
    #次にアクションで分岐
    match action:
        case "import":
            importpath=imports.PySide6.QtWidgets.QFileDialog.getOpenFileName(window,caption="セーブデータを開く",filter="ゲームのセーブデータ(*.sav)")[0]
            sel=FunnyFunction.youwontregretthis(window,("このセーブデータをインポートしますか？", "はい、インポートを続行します。", "いいえ、ここでインポートを終了してください。"),("この操作は既存のセーブデータを上書きする可能性があります。それでも続行しますか?", "はい。それでも続行します。", "いいえ。ここで中止してください。"),("この操作は取り消しできません!<br>既存のセーブデータを上書きすることは、<br>それが何を意図する物であっても、<br>取り返しのつかない結果をもたらす可能性がありますよ?<br>それでもあなたは本当に、、、<br><span style='color: red;'>こうかいしませんね?</span>", "はい、ぜったいにこうかいしません!!!", "いいえ、やっぱりうわがきしたくないです、、、"),systempath)
            saveselectdialog = imports.PySide6.QtWidgets.QDialog(parent=window, modal=True)
            saveselectdialog.setWindowTitle("どのセーブスロットにインポートしますか?")
            #userpath["usergameroot"]
            layout = imports.PySide6.QtWidgets.QVBoxLayout()
            savelist = imports.PySide6.QtWidgets.QListWidget()
            with open(joinpath(systempath["systemassetroot"], "manifest", game + ".json"), encoding="utf-8") as manifest_file:
                manifest = imports.json.load(manifest_file)
            max_slot = int(manifest.get("savemaxslot", 0))
            for c in range(1, max_slot + 1):
                slot_path = joinpath(gamepath, "SaveData" + str(c).zfill(2) + ".sav")
                imports.logging.info(f"{slot_path}のセーブデータの存在を確認")
                if imports.os.path.isfile(slot_path):
                    savelist.addItem(f"セーブデータ{str(c).zfill(2)}:セーブデータが存在します")
                else:
                    savelist.addItem(f"セーブデータ{str(c).zfill(2)}:空スロット")
            layout.addWidget(savelist)
            saveselectdialog.setLayout(layout)

            def on_item_clicked(item, window):
                match = imports.re.search(r"^\D*(\d+):", item.text())
                if not match:
                    imports.PySide6.QtWidgets.QMessageBox.warning(window, "無効な選択", "有効なセーブスロットを選択してください。")
                    return
                index = match.group(1)
                imports.shutil.copy2(importpath, joinpath(userpath["usergameroot"], game, "Save", "SaveData" + index + ".sav"))
                imports.PySide6.QtWidgets.QMessageBox.information(window, "作業完了", "データのインポートが終わりました。")
                window.close()
            savelist.itemClicked.connect(lambda:on_item_clicked(savelist.selectedItems()[0],saveselectdialog))
            saveselectdialog.exec()
        case "export":
            saveselectdialog = imports.PySide6.QtWidgets.QDialog(parent=window, modal=True)
            saveselectdialog.setWindowTitle("どのセーブデータをエクスポートしますか?")
            #userpath["usergameroot"]
            layout = imports.PySide6.QtWidgets.QVBoxLayout()
            savelist = imports.PySide6.QtWidgets.QListWidget()
            with open(joinpath(systempath["systemassetroot"], "manifest", game + ".json"), encoding="utf-8") as manifest_file:
                manifest = imports.json.load(manifest_file)
            max_slot = int(manifest.get("savemaxslot", 0))
            for c in range(1, max_slot + 1):
                slot_path = joinpath(gamepath, "SaveData" + str(c).zfill(2) + ".sav")
                imports.logging.info(f"{slot_path}のセーブデータの存在を確認")
                if imports.os.path.isfile(slot_path):
                    savelist.addItem(f"セーブデータ{str(c).zfill(2)}:セーブデータが存在します")
                else:
                    savelist.addItem(f"セーブデータ{str(c).zfill(2)}:空スロット")
            layout.addWidget(savelist)
            saveselectdialog.setLayout(layout)
            def on_item_clicked(item, window):
                match = imports.re.search(r"^\D*(\d+):(.*)$", item.text())
                if not match:
                    imports.PySide6.QtWidgets.QMessageBox.warning(window, "無効な選択", "有効なセーブスロットを選択してください。")
                    return
                index = match.group(1)
                description = match.group(2).strip()
                if description == "空スロット":
                    imports.PySide6.QtWidgets.QMessageBox.critical(
                        window,
                        "重大なオペレーションエラー",
                        "空のセーブスロットをエクスポート対象にすることはできません!!!\n別のスロットを指定してください!!!",
                    )
                    return
                exppath = imports.PySide6.QtWidgets.QFileDialog.getSaveFileName(
                    window,
                    "セーブデータに名前を付けて保存",
                    filter="ゲームのセーブデータ(*.sav)",
                )[0]
                if not exppath:
                    return
                imports.shutil.copy2(joinpath(userpath["usergameroot"], game, "Save", "SaveData" + index + ".sav"), exppath)
                imports.PySide6.QtWidgets.QMessageBox.information(window, "作業完了", "データのエクスポートが終わりました。")
                window.close()
            savelist.itemClicked.connect(lambda:on_item_clicked(savelist.selectedItems()[0],saveselectdialog))
            saveselectdialog.exec()
        case "archive":
            class Ui_Dialog(imports.PySide6.QtWidgets.QDialog):
                def setupUi(self, Dialog):
                    if not Dialog.objectName():
                        Dialog.setObjectName(u"Dialog")
                    Dialog.setWindowModality(imports.PySide6.QtCore.Qt.WindowModality.ApplicationModal)
                    Dialog.resize(506, 199)
                    self.layoutWidget = imports.PySide6.QtWidgets.QWidget(Dialog)
                    self.layoutWidget.setObjectName(u"layoutWidget")
                    self.layoutWidget.setGeometry(imports.PySide6.QtCore.QRect(20, 10, 481, 181))
                    self.gridLayout = imports.PySide6.QtWidgets.QGridLayout(self.layoutWidget)
                    self.gridLayout.setObjectName(u"gridLayout")
                    self.gridLayout.setContentsMargins(0, 0, 0, 0)
                    self.label = imports.PySide6.QtWidgets.QLabel(self.layoutWidget)
                    self.label.setObjectName(u"label")

                    self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

                    self.comboBox = imports.PySide6.QtWidgets.QComboBox(self.layoutWidget)
                    self.comboBox.addItem("")
                    self.comboBox.setObjectName(u"comboBox")

                    self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 2)

                    self.label_2 = imports.PySide6.QtWidgets.QLabel(self.layoutWidget)
                    self.label_2.setObjectName(u"label_2")

                    self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

                    self.comboBox_2 = imports.PySide6.QtWidgets.QComboBox(self.layoutWidget)
                    self.comboBox_2.addItem("")
                    self.comboBox_2.addItem("")
                    self.comboBox_2.addItem("")
                    self.comboBox_2.addItem("")
                    self.comboBox_2.setObjectName(u"comboBox_2")

                    self.gridLayout.addWidget(self.comboBox_2, 1, 3, 1, 1)

                    self.label_3 = imports.PySide6.QtWidgets.QLabel(self.layoutWidget)
                    self.label_3.setObjectName(u"label_3")

                    self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

                    self.comboBox_3 = imports.PySide6.QtWidgets.QComboBox(self.layoutWidget)
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.addItem("")
                    self.comboBox_3.setObjectName(u"comboBox_3")

                    self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 3)

                    self.checkBox = imports.PySide6.QtWidgets.QCheckBox(self.layoutWidget)
                    self.checkBox.setObjectName(u"checkBox")

                    self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 4)

                    self.buttonBox = imports.PySide6.QtWidgets.QDialogButtonBox(self.layoutWidget)
                    self.buttonBox.setObjectName(u"buttonBox")
                    self.buttonBox.setOrientation(imports.PySide6.QtCore.Qt.Orientation.Horizontal)
                    self.buttonBox.setStandardButtons(imports.PySide6.QtWidgets.QDialogButtonBox.StandardButton.Cancel|imports.PySide6.QtWidgets.QDialogButtonBox.StandardButton.Ok)
                    self.buttonBox.setCenterButtons(True)
                    ok_button = self.buttonBox.button(imports.PySide6.QtWidgets.QDialogButtonBox.StandardButton.Ok)
                    if ok_button:
                        ok_button.setText("次へ")
                    cancel_button = self.buttonBox.button(imports.PySide6.QtWidgets.QDialogButtonBox.StandardButton.Cancel)
                    if cancel_button:
                        cancel_button.setText("キャンセル")
                    self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 4)
                    self.retranslateUi(Dialog)
                    self.buttonBox.accepted.connect(Dialog.accept)
                    self.buttonBox.rejected.connect(Dialog.reject)
                    imports.PySide6.QtCore.QMetaObject.connectSlotsByName(Dialog)
                def retranslateUi(self, Dialog):
                    Dialog.setWindowTitle(imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"\u30b2\u30fc\u30e0\u306e\u30a2\u30fc\u30ab\u30a4\u30d6\u30aa\u30d7\u30b7\u30e7\u30f3", None))
                    self.label.setText(imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"\u30a2\u30fc\u30ab\u30a4\u30d6\u306e\u5f62\u5f0f\uff1a", None))
                    self.comboBox.setItemText(0, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"zip\u30a2\u30fc\u30ab\u30a4\u30d6(*.zip)", None))

                    self.label_2.setText(imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"\u30a2\u30fc\u30ab\u30a4\u30d6\u306e\u5727\u7e2e\u65b9\u5f0f\uff1a", None))
                    self.comboBox_2.setItemText(0, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"ZIP_STORED(\u5727\u7e2e\u3057\u306a\u3044)", None))
                    self.comboBox_2.setItemText(1, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"ZIP_DEFLATED(\u6a19\u6e96\u306e\u5727\u7e2e)", None))
                    self.comboBox_2.setItemText(2, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"ZIP_LZMA(LZMA\u5727\u7e2e)", None))
                    self.comboBox_2.setItemText(3, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"ZIP_BZIP2(Bzip2\u5727\u7e2e)", None))

                    self.label_3.setText(imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"\u5727\u7e2e\u30ec\u30d9\u30eb\uff1a", None))
                    self.comboBox_3.setItemText(0, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"-1(\u30b7\u30b9\u30c6\u30e0\u306e\u30c7\u30d5\u30a9\u30eb\u30c8)", None))
                    self.comboBox_3.setItemText(1, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"0(\u5727\u7e2e\u3057\u306a\u3044)", None))
                    self.comboBox_3.setItemText(2, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"1(\u30ec\u30d9\u30eb1\u5727\u7e2e\u3002\u5727\u7e2e\u3059\u308b\u4e2d\u30671\u756a\u9ad8\u901f\u3060\u304c\u4e00\u756a\u5bb9\u91cf\u304c\u5927\u304d\u3044\u3002)", None))
                    self.comboBox_3.setItemText(3, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"2(\u30ec\u30d9\u30eb2\u5727\u7e2e)", None))
                    self.comboBox_3.setItemText(4, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"3(\u30ec\u30d9\u30eb3\u5727\u7e2e)", None))
                    self.comboBox_3.setItemText(5, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"4(\u30ec\u30d9\u30eb4\u5727\u7e2e)", None))
                    self.comboBox_3.setItemText(6, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"5(\u30ec\u30d9\u30eb5\u5727\u7e2e)", None))
                    self.comboBox_3.setItemText(7, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"6(\u30ec\u30d9\u30eb6\u5727\u7e2e)", None))
                    self.comboBox_3.setItemText(8, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"7(\u30ec\u30d9\u30eb7\u5727\u7e2e)", None))
                    self.comboBox_3.setItemText(9, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"8(\u30ec\u30d9\u30eb8\u5727\u7e2e)", None))
                    self.comboBox_3.setItemText(10, imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"9(\u30ec\u30d9\u30eb9\u5727\u7e2e\u3002\u5727\u7e2e\u3059\u308b\u4e2d\u3067\u4e00\u756a\u4f4e\u901f\u3060\u304c\u4e00\u756a\u5bb9\u91cf\u304c\u5c0f\u3055\u3044\u3002)", None))
                    self.checkBox.setText(imports.PySide6.QtCore.QCoreApplication.translate("Dialog", u"\u30a2\u30fc\u30ab\u30a4\u30d6\u3092\u30d1\u30b9\u30ef\u30fc\u30c9\u3067\u4fdd\u8b77\u3059\u308b", None))
            dialog=Ui_Dialog()
            dialog.setupUi(dialog)
            if dialog.exec()==0:
                dialog.close()
            else:
                if dialog.checkBox.isChecked():
                    pass1temp=imports.PySide6.QtWidgets.QInputDialog.getText(dialog,"パスワードの登録","アーカイブの保護に使うパスワードを入力してください。",echo=imports.PySide6.QtWidgets.QLineEdit.PasswordEchoOnEdit)
                    if not pass1temp[1]:
                        imports.PySide6.QtWidgets.QMessageBox.warning(dialog,"オペレーションのキャンセル","オペレーションはキャンセルされました。")
                    else:
                        pass1=pass1temp[0]
                        pass2temp=imports.PySide6.QtWidgets.QInputDialog.getText(dialog,"パスワードの再入力","アーカイブの保護に使うパスワードをもう一度入力してください。",echo=imports.PySide6.QtWidgets.QLineEdit.PasswordEchoOnEdit)
                    if not pass2temp[1]:
                        imports.PySide6.QtWidgets.QMessageBox.warning(dialog,"オペレーションのキャンセル","オペレーションはキャンセルされました。")
                    else:
                        pass2=pass2temp[0]
                        if not imports.hashlib.sha256(pass1.encode()).hexdigest()==imports.hashlib.sha256(pass2.encode()).hexdigest():
                            imports.PySide6.QtWidgets.QMessageBox.critical(dialog,"重大なオペレーションエラー","パスワードが違います。操作をやり直してください。")
                            dialog.close()
                        else:
                            pass
                else:
                    #ゲームのアーカイブ最終準備
                    compresslist=[imports.zipfile.ZIP_STORED,imports.zipfile.ZIP_DEFLATED,imports.zipfile.ZIP_LZMA,imports.zipfile.ZIP_BZIP2]
                    pathtemp=imports.PySide6.QtWidgets.QFileDialog.getSaveFileName(parent=dialog,dir=joinpath(imports.pathlib.Path.home(),"Documents",game+"_archive.zip"),caption="ゲームのアーカイブファイルに名前を付けて保存",filter="zipアーカイブ(*.zip)")
                    if not pathtemp[0]or pathtemp[0]=="":
                        imports.PySide6.QtWidgets.QMessageBox.warning(dialog,"オペレーションのキャンセル","オペレーションはキャンセルされました。")
                    else:
                        #オペレーションを実行
                        try:
                            compress_zip_with_progress(dialog,joinpath(userpath["usergameroot"],game),pathtemp[0],pass2,userpath=userpath,compression=compresslist[dialog.comboBox_2.currentIndex()],compression_level=dialog.comboBox_2.currentIndex()-1)
                        except UnboundLocalError:
                            compress_zip_with_progress(dialog,joinpath(userpath["usergameroot"],game),pathtemp[0],None,userpath=userpath,compression=compresslist[dialog.comboBox_2.currentIndex()],compression_level=dialog.comboBox_3.currentIndex()-1)
        case "import_all":
            not_implemented(window)
        case "export_all":
            not_implemented(window)
        case "delete_all":
            res=FunnyFunction.youwontregretthis(window,(f"{game}のゲームのセーブデータを全部消去しますか？", "はい。このゲームのセーブデータを全部消します。", "いいえ、このゲームのセーブデータを残しておいてください。"),("この操作は既存のセーブデータを全て完全消去します。それでも続行しますか?", "はい。それでも続行します。(次の画面では警告音注意です。)", "いいえ。ここで中止してください。"),(f"この操作は取り消しできません!<br>このまま続行すると{game}のゲームの進捗が全て消えて最初からになりますよ?<br>私は言いましたからね?<br>3回言いましたからね?<br>それでもあなたは本当に、、、<br><span style='color: red;'>こうかいしませんね?</span>", "はい、ぜったいにこうかいしません!!!", "いいえ、やっぱりけしたくないです、、、"),systempath)
            if res:
                imports.shutil.rmtree(gamepath, ignore_errors=True)
                imports.PySide6.QtWidgets.QMessageBox.information(window,"けしました。",f"{game}のゲームのセーブデータをぜんぶけしました。")
def creatwinaudiolib(systempath):
    imports.logging.info("オーディオライブラリ作成開始")
    if not imports.os.path.isdir(systempath["winaudioroot"]):
        copy_folder_with_progress("C:\\Windows\\Media",systempath["winaudioroot"])
        #もし.wav以外があったら爆破。
        imports.shutil.rmtree(joinpath(systempath["winaudioroot"],"dm"))
        imports.os.remove(joinpath(systempath["winaudioroot"],"ding.wav"))
        imports.os.remove(joinpath(systempath["winaudioroot"],"notify.wav"))
        imports.os.remove(joinpath(systempath["winaudioroot"],"recycle.wav"))
        imports.os.remove(joinpath(systempath["winaudioroot"],"ringout.wav"))
        filelist=imports.glob.glob(systempath["winaudioroot"]+"\\*",recursive=True)
        for file in filelist:
            if not str(file).endswith(".wav") or str(file).endswith("Windows User Account Control.wav") or str(file).endswith("Windows Hardware Insert.wav") or str(file).endswith("Windows Hardware Remove.wav"):
                imports.os.remove(file)
                continue
            if not str(file).split("\\")[-1].startswith("Windows"):
                filetemp=str(file).split("\\")
                filetemp.pop()
                filetemp.append("Windows "+str(file).split("\\")[-1])
                try:
                    imports.os.rename(file,"\\".join(filetemp))
                except FileExistsError:
                    continue
        imports.shutil.copy2(joinpath(systempath["systemassetroot"],"Windows Hardware Insert.wav"),joinpath(systempath["winaudioroot"],"Windows Hardware Insert.wav"))
        imports.shutil.copy2(joinpath(systempath["systemassetroot"],"Windows Hardware Remove.wav"),joinpath(systempath["winaudioroot"],"Windows Hardware Remove.wav"))
        imports.shutil.copy2(joinpath(systempath["systemassetroot"],"Windows Logon.wav"),joinpath(systempath["winaudioroot"],"Windows Logon.wav"))
        imports.shutil.copy2(joinpath(systempath["systemassetroot"],"Windows User Account Control.wav"),joinpath(systempath["winaudioroot"],"Windows User Account Control.wav"))
    else:
        return
def winauduolib(systempath=initsystempath(),name=None):
    if name is None:
        pass
    else:
        sefile=joinpath(systempath["winaudioroot"],name+".wav")
        if imports.os.path.isfile(sefile):
            return sefile
        else:
            raise imports.Exception.PywolfException.InternalException.FileException.WinaudioNotFoundException(name)
def winaudiolibs(systempath=initsystempath()):
    libs=imports.os.listdir(systempath["winaudioroot"])
    result=list()
    for lib in libs:
        result.append(imports.os.path.splitext(lib)[0])
    return result
def playSE(file,loop=True,window=None):
    effect=imports.PySide6.QtMultimedia.QSoundEffect(window)
    effect.setSource(imports.PySide6.QtCore.QUrl().fromLocalFile(file))
    if loop:
        effect.setLoopCount(0)
    effect.play()
def updatemanifest(window,systempath,gamelist) -> bool:
    suc=True
    base="https://raw.githubusercontent.com/Pywolfofficial-4-WolfRPGEditor/Pywolf-4-WolfRPGEditor/refs/heads/main/Pywolfmanifest/game/"
    manifestpath=joinpath(systempath["systemassetroot"],"manifest","game")
    manifestlist=imports.os.listdir(manifestpath)
    if len(gamelist)!=len(manifestlist):
        #マニフェストファイルのアップデートが必要
        imports.PySide6.QtWidgets.QMessageBox.warning(window,"更新が必要","この操作を続行するには後方互換を確保するためのマニフェストファイルが必要です。")
        progressdiag=imports.PySide6.QtWidgets.QProgressDialog(window)
        progressdiag.setWindowTitle("マニフェストファイルの更新")
        for game in gamelist:
            path=base+game+".json"
            imports.logging.info(f"{path}にGETリクエストを送信")
            try:
                result=autodownloadfromglobalnet(path,joinpath(manifestpath,game+".json"),params={},headers={},window=progressdiag,binary=False,ensure_globalnet_connected=True)
                if result:
                    imports.logging.info(f"{game}のマニフェストファイルの更新が完了しました。")
                else:
                    imports.logging.warning(f"{game}のマニフェストファイルの更新に失敗しました。")
                    suc=False
                    break
            except BaseException as e:
                imports.logging.error(f"マニフェストファイルの更新に失敗: {e}")
                imports.PySide6.QtWidgets.QMessageBox.critical(window,"更新エラー",f"マニフェストファイルの更新に失敗しました:\n{e}")
                suc=False
                break
        if suc:
            imports.PySide6.QtWidgets.QMessageBox.information(window,"更新が完了","マニフェストファイルの更新が完了しました。")
            return True
        else:
            imports.PySide6.QtWidgets.QMessageBox.critical(window,"更新失敗","マニフェストのダウンロードに失敗しました。")
            imports.logging.error("マニフェストのダウンロードに失敗しました。")
            imports.shutil.rmtree(manifestpath)
            progressdiag.close()
            window.close()
            return False
def Logoutfunc(window):
    if imports.PySide6.QtWidgets.QMessageBox.question(window, "オペレーションの確認", "ログアウトしますか？") == imports.PySide6.QtWidgets.QMessageBox.StandardButton.Yes:
        my_button = window.findChild(imports.PySide6.QtWidgets.QPushButton, "LogonButton")
        if my_button is None:
            imports.logging.warning("LogonButton が見つかりませんでした。ログアウト処理を中止します。")
            return
        my_button.setText("ログイン")
        imports.PySide6.QtWidgets.QMessageBox.information(window, "オペレーションの完了", "ログアウトしました。")
        try:
            my_button.clicked.disconnect()
        except Exception:
            pass
        my_button.clicked.connect(lambda: logon(window))
def logon(window,systempath,user):
    while True:
        username=None
        password=None
        varidate=None
        while password is None and varidate is None:
            username, password = logondialog(user)
            if password is None:
                imports.logging.warning("パスワード入力がキャンセルされました。再度入力を促します。")
                imports.PySide6.QtWidgets.QMessageBox.warning(window, "入力エラー", "パスワードの入力がキャンセルされました。パスワードは空ではならないため、再度入力してください。")
            else:
                #パスワードが入力されている場合、ユーザーの正当なパスワードと比較して検証する
                password_hash, salt = varidatepassword(username, systempath)
                if not password_hash or not salt:
                    imports.logging.warning("ユーザーデータの読み取りに失敗しました。ログインを再試行します。")
                    imports.PySide6.QtWidgets.QMessageBox.warning(window, "認証エラー", "ユーザーデータの読み取りに失敗しました。再度お試しください。")
                    continue
                try:
                    input_password_hash = imports.hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex().upper()
                except Exception as e:
                    imports.logging.error(f"パスワードハッシュの作成に失敗: {e}")
                    continue
                if input_password_hash == password_hash:
                    varidate = True
                    break
        if varidate:
            break
    return True,username
def userdelete(window,systempath,userpath,username):
    if FunnyFunction.youwontregretthis(window,(f"{username}のアカウントを削除しますか？", "はい。このアカウントを削除します。", "いいえ、このアカウントは残しておいてください。"),("この操作は既存のアカウントを完全に削除します。それでも続行しますか?", "はい。それでも続行します。(次の画面では警告音注意です。)", "いいえ。ここで中止してください。"),(f"この操作は取り消しできません!<br>このまま続行すると{username}のアカウントが完全に削除されますよ?<br>私は言いましたからね?<br>3回言いましたからね?<br>それでもあなたは本当に、、、<br><span style='color: red;'>こうかいしませんね?</span>", "はい、ぜったいにこうかいしません!!!", "いいえ、やっぱりけしたくないです、、、"),systempath):
        progress_dialog=imports.PySide6.QtWidgets.QProgressDialog(window)
        worker=DeleteWorker(userpath["userroot"],progress_dialog,systempath)
        def on_progress(value: int, path: str, dialog: imports.PySide6.QtWidgets.QProgressDialog) -> None:
            dialog.setValue(value)
            dialog.setLabelText(f"{normpath(path)} を削除中…")
        worker.progress_changed.connect(on_progress)
    progress_dialog.setWindowTitle("削除中")
    progress_dialog.setMinimumDuration(0)
    progress_dialog.setValue(0)
    progress_dialog.setWindowModality(imports.PySide6.QtCore.Qt.WindowModality.ApplicationModal)
    progress_dialog.setCancelButtonText("キャンセル")
    worker.cancelled.connect(progress_dialog.close)
    worker.error_occurred.connect(lambda error_message: imports.PySide6.QtWidgets.QMessageBox.critical(window, "削除エラー", f"削除中にエラーが発生しました:\n{error_message}"))
    def on_worker_finished() -> None:
        progress_dialog.close()
        worker.deleteLater()
        worker.finished.disconnect(on_worker_finished)
        imports.logging.info(f"{username}の削除オペレーションが完了しました。")
        imports.PySide6.QtWidgets.QMessageBox.information(window,"けしました。",f"{username}のアカウントをぜんぶけしました。")
    worker.error_occurred.connect(progress_dialog.close)
    worker.progress_changed.connect(on_progress)
    worker.finished.connect(on_worker_finished)
    worker.start()
def autodownloadfromglobalnet(url: str, download_to: str, params: dict, headers: dict, window: imports.PySide6.QtWidgets.QProgressDialog,binary:bool =True,ensure_globalnet_connected:bool=True) -> bool:
    if ensure_globalnet_connected:
        # ここにグローバルネットワーク接続の確認ロジックを追加
        try:
            resp=imports.requests.get(connectcheckaddr())
            resp.raise_for_status()

        except imports.requests.exceptions.ConnectionError:
            imports.PySide6.QtWidgets.QMessageBox.critical(window,"ネットワークに接続されていません","ネットワークに接続されていないか、ネットワークから切断されました。\n有線接続の場合はパソコンのLAN端子やモデム、ルーターのLAN端子およびイーサネット端子からLANケーブルが抜けていないか、\n無線接続の場合はパソコン本体のWi-Fiが有効になっており、機内モードになっていないかと接続するSSIDを間違えていないか、\n光回線からネットワークに接続している場合は終端装置からケーブルが抜けていないかをそれぞれ確認してください。")
            return False
    response = imports.requests.get(url, params=params, headers=headers, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    fileformat = imports.mimetypes.guess_extension(response.headers.get('content-type', '').split(';')[0])
    # ユーザーがキャンセル（一時停止）したか追跡するフラグ
    is_paused_or_cancelled = False
    mode=""
    if binary:
        mode="wb"
    else:
        mode="wt"
    with open(download_to+fileformat,mode) as f:
        downloaded_size = 0
        for chunk in response.iter_content(chunk_size=8192):
            # PySide6のキャンセルボタンが押されたか確認
            if window.wasCanceled():
                is_paused_or_cancelled = True
                break
            if chunk:
                f.write(chunk)
                downloaded_size += len(chunk)
                # ゼロ除算を防ぎつつ進捗を計算
                if total_size > 0:
                    progress = int((downloaded_size / total_size) * 100)
                    window.setWindowTitle(f"ダウンロード中... {progress}%")
                    window.setValue(progress)
                else:
                    window.setWindowTitle(f"ダウンロード中... ({downloaded_size} bytes)")
def connect(mainwindow,systempath,userpath,
            username,app):
    mainwindow.actionQt.triggered.connect(lambda: imports.PySide6.QtWidgets.QMessageBox.aboutQt(mainwindow))
    mainwindow.actionUser_Manual.triggered.connect(lambda: not_implemented(mainwindow))
    mainwindow.actionabout.triggered.connect(lambda: not_implemented(mainwindow))
    mainwindow.actionbootgame.triggered.connect(lambda: gameselect(username=username,systempath=systempath,mainwindow=mainwindow,gamelist=scanusergames(username,systempath)))
    mainwindow.actioninstallfromarchive.triggered.connect(lambda: install_game(mainwindow, systempath,userpath,username,importfrom="archive",net=False))
    mainwindow.actioninstallfromdir.triggered.connect(lambda: install_game(mainwindow, systempath,userpath,username,importfrom="folder",net=False))
    mainwindow.actioninstallfromglobalnet.triggered.connect(lambda: install_game(mainwindow, systempath,userpath,username,importfrom="globalnetwork",net=False))
    mainwindow.actionmanagegame.triggered.connect(lambda: gamemanage(systempath, username,mainwindow,userpath))
    mainwindow.actionaddaccount.triggered.connect(lambda: createlocaluser(systempath))
    mainwindow.actionexit.triggered.connect(app.quit)
    mainwindow.actiondeleteuser.triggered.connect(lambda: userdelete(mainwindow,systempath,userpath,username))
class FunnyFunction(imports.PySide6.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
    def selfdestractdiag():
        a=imports.PySide6.QtWidgets.QDialog()
        a.setWindowTitle("読めたらすごい。")
        layout = imports.PySide6.QtWidgets.QVBoxLayout()
        label = imports.PySide6.QtWidgets.QLabel("くぁｗせｄｒｆｔｇｙふじこｌｐ")
        layout.addWidget(label)
        a.setLayout(layout)
        imports.PySide6.QtCore.QTimer.singleShot(16.66666666666667,  a.close)
        return a
    def youwontregretthis(parent,q1,q2,q3,systempath):
    # 3回分の質問設定 (質問文, はいボタンのテキスト, いいえボタンのテキスト)
        steps = [q1,q2,q3
        ]
        i=0
        for i, (text, yes_text, no_text) in enumerate(steps):
            # 1. ダイアログの作成と設定
            dialog = imports.PySide6.QtWidgets.QDialog(parent)
            dialog.setWindowTitle(f"確認 ({i+1}/3)")
            layout = imports.PySide6.QtWidgets.QVBoxLayout(dialog)

        # 2. QLabelの作成 (3回目はHTML形式で一部を赤文字にする)
            label = imports.PySide6.QtWidgets.QLabel(dialog)
            if i == 2:
                label.setText(text)  # リッチテキスト(HTML)として認識される
            else:
                label.setText(text)
            layout.addWidget(label)

            # 3. QCommandLinkButtonの作成
            btn_yes = imports.PySide6.QtWidgets.QCommandLinkButton(yes_text, dialog)
            btn_no = imports.PySide6.QtWidgets.QCommandLinkButton(no_text, dialog)
            btn_no.setFocus()
            # 4. ボタンの配置 (2回目のみ逆にする)
            if i == 1:
                layout.addWidget(btn_no)
                layout.addWidget(btn_yes)
            else:
                layout.addWidget(btn_yes)
                layout.addWidget(btn_no)

            # 5. シグナルとスロットの設定 (QDialogの組み込み結果を利用)
            btn_yes.clicked.connect(dialog.accept) # accept()は結果1(True)を返す
            btn_no.clicked.connect(dialog.reject)   # reject()は結果0(False)を返す
            # 6. ダイアログを表示して結果を待つ (execでブロッキング)
            if i==2:
                playSE(file=joinpath(systempath["systemassetroot"],"3E96BC53EA50C3C504420FEE8315480A116B078EC19C52771128D254F575FA9A.wav"),window=dialog)
            result = dialog.exec()

            # 「選択肢を選んだらダイアログが一瞬消える」挙動のための処理
            # dialog.exec() が終わった時点で画面からダイアログは消えます。
            # 次のダイアログが表示される前に一瞬だけウェイトを入れます。
            if i < 2:  # 最後の質問以外で一瞬（0.15秒）待つ
                imports.time.sleep(0.15)
                imports.PySide6.QtWidgets.QApplication.processEvents() # 画面描画を強制更新して確実に消す
            # 7. 「いいえ」が選ばれた、または閉じられた場合は即終了 (Falseを返す)
            if not result:
                return False

    # 3回とも「はい」をクリアした場合のみTrue
        return True
if __name__=="__main__":
    raise imports.Exception.PywolfException.InternalException.EntrypointException(imports.os.path.basename(__file__),__name__)