# Scripts para generar capas geográficas

Algunas capas geográficas de interés para México.

## Instrucciones para crear capa de ejemplo
1. Clonar este repositorio
2. Instalar las dependencias con `pip install -r requirements.txt`
2. Crear dos subdirectorios `raw_data` y `results`
3. Bajar [Marco Geoestádistico del INEGI en CSV](https://www.inegi.org.mx/app/ageeml/) y guardarlos como `raw_data/marco.csv`
4. Bajar [Catálogo de centros de trabajo SEP](https://datos.gob.mx/busca/dataset/catalogo-de-centros-de-trabajo-2017) y ponerlo en 
   `raw_data/CATALOGO_CT.csv`
5. Ejecutar `scripts/1_createLayer.py` 