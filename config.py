# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Este archivo contiene los valores de configuración para la aplicación.
Actualiza este archivo con los respectivos valores de tu proyecto de GCP.
Crea y administra tus proyectos en https://console.developers.google.com
"""

# Puedes almacenar datos de diferentes formas en tu aplicación.
# Eliges entre 'datastore' y 'cloudsql'.
# 'datastore' es la opción predefinida porque, entre otras cosas, nos ofrece un nivel de servicio gratuito.
DATA_BACKEND = 'datastore'

# SQLAlchemy configuration
# Cambia el valor de user, pass, host y database con los de tu instancia de Cloud SQL
# Recuerda que una instancia de Cloud SQL incurre en gastos (que pueden cargarse a los 300.00 USD de crédito que te da
# GCP si activaste la facturación en tu proyecto).
SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://user:password@host/database'

# Configuraciones de Google Cloud Storage y de subida de archivos.
# Puedes nombrar tu bucket como tu proyecto o darle el nombre que desees (siempre que esté disponible).
# El bucket se puede crear desde la consola web o con el cloud sdk ejecutando:
#
#   $ gsutil mb gs://<your-bucket-name>
#
# Ajusta la ACL (lista de control de accesos) para que se pueda hacer lectura pública de las imágenes,
# para que cualquier usuario pueda ver las imágenes que se han subido. Eso lo consigues ejecutando:
#
#   $ gsutil defacl set public-read gs://<your-bucket-name>
#
# Puedes ajustar el tamaño máximo del archivo y las extensiones válidas.
CLOUD_STORAGE_BUCKET = 'myxerticalabsproject'
MAX_CONTENT_LENGTH = 8 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
