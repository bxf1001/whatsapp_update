import subprocess
from pywinauto import Desktop, Application

app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
app = Application(backend='uia').connect(title_re=".*WhatsApp.*")