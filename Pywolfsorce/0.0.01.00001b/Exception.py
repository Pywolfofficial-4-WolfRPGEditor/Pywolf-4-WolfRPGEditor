import funcs
class PywolfException(Exception):
    def __init__(self, arg=""):
        self.arg = arg
    class FileException(Exception):
        def __init__(self,filename,func=""):
            self.func = func
            self.filename = filename
        def __str__(self):
            return (
                f"{self.filename}は{self.func}に渡すことができる有効なファイルではありません。"
            )
        class EmptyArchiveFileException(Exception):
            def __init__(self,filename,func=""):
                self.func = func
                self.filename = filename
            def __str__(self):
                return (
                    f"{self.filename}は{self.func}に渡すことができる有効なアーカイブファイルではありません。{self.func}に渡すアーカイブは空ではあってはいけません。"
                )
    class InternalException(Exception):
        def __init__ (self):
            pass
        class FileException(Exception):
            def __init__ (self):
                pass
            class WinaudioNotFoundException(Exception):
                def __init__ (self,name):
                    self.name=name
                def __str__(self):
                    return f"{self.name}のウィンドウズオーディオはPywolfに登録されていません。別の名前を使用してください。ウィンドウズオーディオとしてPywolfに認識されている有効な名前の一覧はfuncs.winaudiolibs()で確認できます。"
    class SecurityException(Exception):
        def __init__ (self):
            pass
        class PolicyException(Exception):
            def __init__ (self):
                pass
            class FilePolicyException(Exception):
                def __init__ (self,path):
                    self.path=path
                class FileAccessModeException(Exception):
                    def __init__ (self,path,mode):
                        self.path=path
                        self.mode=mode
                    def __str__(self):
                        return f"{self.path}は読み取り専用ではない{self.mode}のモードで開くことはPywolfのセキュリティポリシーで認可されていないため、{self.path}への{self.mode}アクセスはPywolfにより拒否されました。読み取り専用モードを使用するか、アクセスするパスを変更してください。"