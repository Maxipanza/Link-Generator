import os
import pathlib
from pathlib import Path


dir_actual = os.path.dirname(os.path.abspath(__file__))

dir_final=dir_actual.replace('\\','/')

gif_list = [ archivo.with_suffix(".gif").as_posix() for archivo in Path(dir_actual).glob('**/*')]
jpg_list = [ archivo.with_suffix(".jpg").as_posix() for archivo in Path(dir_actual).glob('**/*')]
png_list = [ archivo.with_suffix(".png").as_posix() for archivo in Path(dir_actual).glob('**/*')]
jpeg_list = [ archivo.with_suffix(".jpeg").as_posix() for archivo in Path(dir_actual).glob('**/*')]
pdf_list = [ archivo.with_suffix(".pdf").as_posix() for archivo in Path(dir_actual).glob('**/*')]

link = "https://www.landinginteligente.com/fotos"

gif_final = [s.replace(dir_final, link) for s in gif_list]
jpg_final = [s.replace(dir_final, link) for s in jpg_list]
png_final = [s.replace(dir_final, link) for s in png_list]
jpeg_final = [s.replace(dir_final, link) for s in jpeg_list]
pdf_final = [s.replace(dir_final, link) for s in pdf_list]


with open(os.path.join(os.path.expanduser('~'),'Desktop','Links generados.txt'), "w") as outfile:
    outfile.writelines("\n".join(str(item) for item in gif_final) + '\n')
    outfile.writelines("\n")
    outfile.writelines("\n".join(str(item) for item in jpg_final) + '\n')
    outfile.writelines("\n")
    outfile.writelines("\n".join(str(item) for item in png_final) + '\n')
    outfile.writelines("\n")
    outfile.writelines("\n".join(str(item) for item in jpeg_final) + '\n')
    outfile.writelines("\n")
    outfile.writelines("\n".join(str(item) for item in pdf_final) + '\n')

