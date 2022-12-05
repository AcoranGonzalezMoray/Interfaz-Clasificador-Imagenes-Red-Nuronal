from keras.models import model_from_json
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
import shutil
import pathlib
import sys
from datetime import datetime

CURR_DIR = os.getcwd()
sys.stdout = open(CURR_DIR+'/log.txt', 'w')
def  clean():
  path = CURR_DIR+"/Test/Vegetales/"
  shutil.rmtree(path+"Carrot/", ignore_errors=False, onerror=None)
  shutil.rmtree(path+"Papaya/", ignore_errors=False, onerror=None)
  shutil.rmtree(path+"Tomato/", ignore_errors=False, onerror=None)
  shutil.rmtree(path+"Potato/", ignore_errors=False, onerror=None)
  shutil.rmtree(path+"Capsicum/", ignore_errors=False, onerror=None)
  shutil.rmtree(path+"Broccoli/", ignore_errors=False, onerror=None)
  shutil.rmtree(path+"Pummking/", ignore_errors=False, onerror=None)

def Clasificar_Vegetales(ruta):
 
  # cargar json y crear el modelo
  json_file = open(CURR_DIR+ "/Network/model.json", 'r')
  loaded_model_json = json_file.read()
  json_file.close()
  loaded_model =  model_from_json(loaded_model_json)
  # cargar pesos al nuevo modelo
  loaded_model.load_weights(CURR_DIR +"/Network/model.h5")
  print("Cargado modelo desde disco.", datetime.now())
  
  # Compilar modelo cargado y listo para usar.
  #loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
  loaded_model.compile(loss=tf.keras.losses.categorical_crossentropy, # se cambio de categorical_crossentropy a sparse_categorical_crossentropy si int
                optimizer=tf.keras.optimizers.Adam(1e-3),
                metrics=['accuracy'])

  def  classification_report(nombre_archivo, numero):


    if numero == 0:
      pathlib.Path(CURR_DIR+"/Test/Vegetales/Carrot/").mkdir(exist_ok=True)
      shutil.copy(ruta+nombre_archivo, CURR_DIR+"/Test/Vegetales/Carrot/"+nombre_archivo)
      return(nombre_archivo+": Carrot")
    if numero == 1:
      pathlib.Path(CURR_DIR+"/Test/Vegetales/Papaya/").mkdir(exist_ok=True)
      shutil.copy(ruta+nombre_archivo, CURR_DIR+"/Test/Vegetales/Papaya/"+nombre_archivo)
      return(nombre_archivo+": Papaya")
    if numero == 2:
      pathlib.Path(CURR_DIR+"/Test/Vegetales/Tomato/").mkdir(exist_ok=True)
      shutil.copy(ruta+nombre_archivo, CURR_DIR+"/Test/Vegetales/Tomato/"+nombre_archivo)
      return(nombre_archivo+": Tomato")
    if numero == 3:
      pathlib.Path(CURR_DIR+"/Test/Vegetales/Potato/").mkdir(exist_ok=True)
      shutil.copy(ruta+nombre_archivo, CURR_DIR+"/Test/Vegetales/Potato/"+nombre_archivo)
      return(nombre_archivo+": Potato")
    if numero == 4:
      pathlib.Path(CURR_DIR+"/Test/Vegetales/Capsicum/").mkdir(exist_ok=True)
      shutil.copy(ruta+nombre_archivo, CURR_DIR+"/Test/Vegetales/Capsicum/"+nombre_archivo)
      return(nombre_archivo+": Capsicum")
    if numero == 5:
      pathlib.Path(CURR_DIR+"/Test/Vegetales/Broccoli/").mkdir(exist_ok=True)
      shutil.copy(ruta+nombre_archivo, CURR_DIR+"/Test/Vegetales/Broccoli/"+nombre_archivo)
      return(nombre_archivo+": Broccoli")
    if numero == 6:
      pathlib.Path(CURR_DIR+"/Test/Vegetales/Pummking/").mkdir(exist_ok=True)
      shutil.copy(ruta+nombre_archivo, CURR_DIR+"/Test/Vegetales/Pummking/"+nombre_archivo)
      return(nombre_archivo+": Pummking")

    return 0



  image_size = (150, 150) #En realidad 224x224 pixeles lo que mide la imagen
  contenido = os.listdir(ruta)
 
  for i in contenido:
    img = keras.preprocessing.image.load_img(
        ruta+i, target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = loaded_model.predict(img_array)
    print(classification_report(i, np.argmax(predictions[0])), datetime.now())