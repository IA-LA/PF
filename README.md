# Extracción de contenidos de los Foros aLF

_Herramienta de obtención y generación de contenidos estructurados de los Foros académicos de las asignaturas del 
entorno de aprendizaje aLF de la Universidad Nacional de Educación a Distancia (UNED) de España._

## Instrucciones ⚙

_Utilizar un entorno de desarrollo que admita el control de versiones (VCS) compatible Git, o que permita clonar, 
importar o compartir un proyecto GitHub nativo._

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Despliegue** para conocer cómo desplegar el proyecto.


### Pre-requisitos 📋

* _Python 3_

```
    > python --version
    > Python 3.x.x
```

* [_requirements.txt_](https://github.com/IA-LA/PF/blob/master/v1.0/requirements.txt) - Listado de dependencias

```
    > pip list
```

### Instalación 🔧

_Una serie de ejemplos paso a paso explica lo que debe ejecutarse para tener un entorno de desarrollo de la herramienta_

_Primer paso: instalación de dependencias_

```
    > pip install -r requirements.txt
```

_Y comprobación de las dependencias_

```
    > pip freeze
    > pip list
    anytree==2.6.0
    beautifulsoup4==4.6.0
    bs4==0.0.1
    colorama==0.3.9
    decorator==4.2.1
    et-xmlfile==1.0.1
    graphviz==0.11.1
    html5lib==1.0.1
    ipython==6.2.1
    ipython-genutils==0.2.0
    jdcal==1.4
    jedi==0.11.1
    nltk==3.4.5
    numpy==1.16.2
    openpyxl==2.6.2
    pandas==0.24.2
    parso==0.1.1
    pickleshare==0.7.4
    prompt-toolkit==1.0.15
    Pygments==2.2.0
    python-dateutil==2.8.0
    pytz==2018.9
    simplegeneric==0.8.1
    singledispatch==3.4.0.3
    six==1.12.0
    stats==0.1.2a0
    traitlets==4.3.2
    wcwidth==0.1.7
    webencodings==0.5.1
```

_Ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_
* **Aitor Díaz** - [*Versión 1.0*](https://github.com/IA-LA/PF/tree/master/v1.0):
```
    > python nombre.archivo ID_ASIGNATURA_UNED
    > python Foros.txt 0123456
```

* **Francisco Sánchez** - [*Versión 1.1*](https://github.com/IA-LA/foros)
* **Francisco Sánchez** - [*Versión 1.2*](https://github.com/IA-LA/foros)
```
    > python nombre.archivo ID (python Foros.txt 0123456)
    > python archivo____XXX____ID____AÑO (python ForosR____ABC____0123456____2019.txt)
    > python directorio (python C:\carpetas\)
```


## Despliegue ⌨

_Agrega notas adicionales sobre cómo hacer el despliegue_

```
    > pip install -r requirements.txt
```

## Construido con 🛠️

_Menciona las herramientas que utilizadas para crear el proyecto_

* [Python](https://www.python.org/) - El lenguaje usado
* [Pip](https://pypi.org/project/pip/) - Manejador de dependencias
* [Pycharm](https://www.jetbrains.com/pycharm/) - El framework web utilizado

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://github.com/IA-LA/PF/CONTRIBUTING.md) para detalles de nuestro código de conducta, y el proceso para el envío de solicitudes de pull.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/IA-LA/PF/wiki)

## Versionado 📌

Se utilizará [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/IA-LA/PF/tags).

## Autores ✒

_A todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Aitor Díaz** - [*Versión 1.0*](https://github.com/IA-LA/PF/tree/master/v1.0) - [aitordiaz](https://github.com/Aitower) - [aitordiaz](mailto:aitordiaz@pas.uned.es)
* **Álvaro Rodrigo** - [alvarory](mailto:alvarory@lsi.uned.es)
* **Francisco Sánchez** - [*Versión 1.1*](https://github.com/IA-LA/foros) - [fsanchez](https://github.com/IA-LA)
* **Francisco Sánchez** - [*Versión 1.2*](https://github.com/IA-LA/foros) - [fsanchez](https://github.com/IA-LA)
* **José Luis F. Vindel** - [jlvindel](mailto:jlvindel@dia.uned.es)

También puede consultarse la lista de todos los [contribuyentes](https://github.com/IA-LA/PF/contributors) que han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (GNU 3) - mira el archivo [LICENCIA](LICENSE) para más detalles




---
⌨ con ❤ por [fsanchez](https://github.com/IA-LA) 😊
