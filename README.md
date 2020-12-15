# GCP Bookshelf

Una web app que usa múltiples servicios de Google Cloud Platform: 
* App Engine (versión standard con runtime python 2.7)
* Datastore
* Cloud Storage
* Cloud Functions
* Vision API

# Despliega tu aplicación en GCP

##### 1.

[Crea](https://console.cloud.google.com/projectcreate) un proyecto en Google Cloud Platform

##### 2. 

Asegura tener instalado el [Google Cloud SDK](https://cloud.google.com/sdk/downloads?hl=es)

##### 3. 

Una vez clonado este repositorio, en tu archivo ```config.py``` asigna tu valor a:

```
CLOUD_STORAGE_BUCKET
```

Nota:
Puedes crear tu bucket usando el Google Cloud SDK ejecutando

```
gsutil mb gs://<el-nombre-que-quieras>
```

Y asignarle permisos públicos de lectura

```
gsutil defacl set public-read gs://<el-nombre-que-quieras>
```

##### 4. 

Confirma, nuevamente en tu archivo ```config.py```, que tu base de datos es Datastore 

```
DATA_BACKEND = 'datastore'
```

##### 5.

Crea un ambiente virtual de Python y actívalo para luego resolver las dependencias del proyecto ejecutando:

```
virtualenv -p python mivenv
source mivenv/bin/activate
pip install -r requirements.txt -t lib
```

##### 6. 

Despliega tu aplicación usando el Google Cloud SDK ejecutando:

```
gcloud app deploy --version='elnombrequequieras'
```

Si todo salió bien podrás acceder a tu aplicación a través de https:project_id.appspot.com donde project_id es el 
identificador único que se asignó a tu proyecto de Google Cloud Platform 

##### 7.

Una vez que tienes tu web app puedes desplegar una Google Cloud Function que analice, mediante Google Vision API, 
si las portadas contienen contenido violento o adulto.

Descarga [```index.js```](https://gitlab.com/tonioguzmanf/gcp-bookshelf/snippets/1716444) y 
[```package.json```](https://gitlab.com/tonioguzmanf/gcp-bookshelf/snippets/1716445) y ejecuta los siguientes comandos 
mediante el Google Cloud SDK

```
gcloud beta functions deploy imageDetection --trigger-resource [el_nombre_que_hayas_dado_a_tu_bucket] --trigger-event google.storage.object.finalize
```

Dado que Cloud Functions todavía está en Beta debemos usar ```gcloud beta functions deploy``` y luego dar el nombre de 
nuestra función que para este caso es ```imageDetection``` 

También debemos identificar cuál recurso (cloud storage) y cuál evento asociado al (la finalización/confirmación de una 
operación de escritura) recurso desencadenará la ejecución por lo tanto completamos nuestro comando con información de 
los triggers 

```--trigger-resource [el_nombre_que_hayas_dado_a_tu_bucket] --trigger-event google.storage.object.finalize```

Nota: Para que puedas completar correctamente esta parte del ejercicio no olvides asegurar que está habilitada 
[Vision API](https://console.cloud.google.com/apis/api/vision.googleapis.com/overview)
en tu proyecto de GCP. 

#### Si encuentras mejoras para el código o errores por ayúdanos reportándolos (y si tienes una solución propuesta por favor compártela) 

###### Este ejemplo es una modificación del publicado originalmente por Google en 
https://github.com/GoogleCloudPlatformTraining/cp100-bookshelf/tree/master/cloud-storage