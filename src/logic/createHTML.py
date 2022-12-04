import os



# Función que crea archivos en un directorio seleccioado según el parametro "directory"


def createHTML(filename, content, directory, path):

    if os.path.isdir(directory) == True: #consulta si el directorio solicitado existe en el sistema 

        with open(path, "w+") as htmlFile:
            htmlFile.write(content)
            status = filename + " has been created in " + directory
            print(status)
        return status

    else:
        print("Directory doesn't exist")
        
