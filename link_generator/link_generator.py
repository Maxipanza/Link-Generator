import os
import pathlib
from pathlib import Path

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_final=dir_actual.replace('\\','/')
archivos_list = [ archivo.as_posix() for archivo in Path(dir_actual).glob('**/*')]

link = "https://www.landinginteligente.com/fotos"

archivos_final = [s.replace(dir_final, link) for s in archivos_list if s.endswith((".txt", ".pdf", ".jpg", ".jpeg", ".png", ".gif"))]
with open(os.path.join(os.path.join(os.environ['USERPROFILE']),'Links generados.txt'), "w") as outfile:
    outfile.writelines("\n".join(str(item) for item in archivos_final) + '\n')
