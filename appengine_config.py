"""
`appengine_config.py` es cargado automáticamente cuando Google App Engine
inicia una nueva instancia de tu aplicación. Esto se ejecuta antes que cualquier
otro elemento WSGI, especificado en el app.yaml, sea cargado.
"""

from google.appengine.ext import vendor
import tempfile
import tempfile2
tempfile.SpooledTemporaryFile = tempfile2.SpooledTemporaryFile

# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
vendor.add('lib')
