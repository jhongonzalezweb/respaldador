
import os
import shutil
os.system("clear")
destination = "/home/marcos/Escritorio/respaldo_scripts"
lista_x = list()
with open("file_list") as fname:
	lineas = fname.readlines()
	for linea in lineas:
            sku = linea.strip('\n')
            if "packages" in sku or "networkx" in sku or "busqueda_lic" in sku or "PlayOnLinux" in sku:
                  pass
            else:
                lista_x.append(sku)
for source in lista_x:
    try:
        shutil.copy(source, destination)
        print("File copied successfully.")

    except:
         print(source)
