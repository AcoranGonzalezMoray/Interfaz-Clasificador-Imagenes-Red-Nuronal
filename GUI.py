import PySimpleGUI as sg
import os.path
from PySimpleGUI.PySimpleGUI import FolderBrowse, Listbox
from Network import RN
from PIL import Image
import io

class GUI:
    layout = []
    dir = ""
    def __init__(self):
        self.setComponent()
        self.init()

    def setComponent(self):
        sg.theme('DarkBlack') 
        file_list_column = [
            [
                sg.Text("Directorio de Imágenes Dataset"),
                sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse()
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20),
                    key="-FILE LIST-"
                )
            ]
        ]
        image_viewer_column = [
            [sg.Text("Elija la imagen que quiere visualizar:")],
            [sg.Text(size=(100,1), key="-TOUT-")],
            [sg.Image(key="-IMAGE-")]
        ]
        clasificator_column = [
            [sg.Text("Elija el tipo de clasificación:")],
            [sg.OptionMenu(values=('Vegetales'),  k='-OPTION MENU-', default_value="Vegetables")],
            [sg.Text("La Red Neuronal esta entrenada para detectar las siguientes clases:")],
            [sg.Text(" - Broccoli")],
            [sg.Text(" - Capsicum")],
            [sg.Text(" - Carrot")],
            [sg.Text(" - Papaya")],
            [sg.Text(" - Potato")],
            [sg.Text(" - Pumking")],
            [sg.Text(" - Tomato")],
            [sg.Button('Clasificar'),sg.Button("Vaciar")]
        ]
        self.layout = [
            [
                sg.Column(file_list_column),
                sg.VSeparator(),
                sg.Column(image_viewer_column),
                sg.VSeparator(),
                sg.Column(clasificator_column)
            ]
        ]

    def init(self):
        window = sg.Window("Visualizador", self.layout)
        
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "-FOLDER-":
                folder = values["-FOLDER-"]
                self.dir = folder
                try:
                    file_list = os.listdir(folder)
                except:
                    file_list =[]
                
                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                    and f.lower().endswith((".png",".gif", ".jpg", ".JPG", ".PNG", ".jfif"))
                    
                ]
                window["-FILE LIST-"].update(fnames)
            elif event == "-FILE LIST-":
                try:
                    filename = os.path.join(
                        values["-FOLDER-"], values["-FILE LIST-"][0]
                    )
                    image = Image.open(filename)
                    image.thumbnail((2000, 2000))
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    filename=filename
                    window["-TOUT-"].update(bio.getvalue())
                    window["-IMAGE-"].update(bio.getvalue())
                except:
                    pass
            elif event == "Clasificar":
                RN.Clasificar_Vegetales(self.dir+'/')
            elif event == "Vaciar":
                RN.clean()
        window.close()