'''
Executando programas e comandos externos com
o módulo Subprocess
'''
import subprocess

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

output = proc.stdout
print(output)