# ¿Para qué usamos Clases en Python?

La programación orientada a objetos (POO) es una técnica muy útil para estructurar y organizar el código de manera lógica y coherente, lo que hace que el código sea más fácil de entender, mantener y mejorar. 

                            Creación de objetos a partir de una clase
![](https://aprendepython.es/_images/mold.png)

Una clase define una plantilla o molde para crear objetos, los cuales son instancias de esa clase. Los objetos creados a partir de una clase tienen las mismas propiedades y comportamientos definidos por la clase, pero pueden tener valores diferentes para los atributos que se definen en la clase.


                            Atributos y métodos en un objeto «bicicleta»
![](https://aprendepython.es/_images/bike-object.jpg)

##### Sintaxis

Una clase se define mediante la palabra clave «class», seguida del nombre de la clase y dos puntos (:) y luego el cuerpo de la clase.
```
class Saludar:
    def saludo(self):
        return 'Buenos días'
saludo_mañanas = Saludar()                /*Creamos una instancia de clase*/
print (saludo_mañanas.saludo())           /*Llamamos a la función de la clase*/
```
**Ejemplo:** en este ejemplo creamos la clase Saludar y dentro esta el método saludo(self), siempre hay que pasar el argumento self que hace referencia a la propia instancia, atributo de objeto.

### Ventajas del uso de las clases en Python

- **Reutilización de código:** las clases pueden reutilizarse en diferentes partes del programa o en distintos programas, lo que ahorra tiempo y reduce la duplicación de código.
- **Encapsulación:** Las clases permiten encapsular datos y comportamientos relacionados en un solo objeto. Esto ayuda a organizar y estructurar el código de manera más clara y comprensible.
- **Modularidad:** pueden descomponer un programa en componentes más pequeños y manejables, lo que facilita el mantenimiento y la solución de problemas.
- **Polimorfismo:** ayudan a implementar el mismo conjunto de métodos con diferentes comportamientos para distintos tipos de objetos, lo que permite una mayor flexibilidad y extensibilidad en el diseño de programas.

##### Para ampliar conocimientos
Para ampliar conocimientos sobre las clases, os animo a leer los siguientes enlaces:
<https://docs.python.org/es/3/tutorial/classes.html#class-definition-syntax>
<https://aprendepython.es/core/modularity/oop/>

# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

Existe un método especial que se ejecuta cuando creamos una instancia de clase. Este método es **\__init__** y nos permite asignar atributos y realizar operaciones con el objeto en el momento de su creación. Este método se conoce como el "constructor" de la clase y se utiliza para inicializar los atributos de la instancia.

```
class Coche:
    def __init__(self, name:str):
        self.name = name
        
coche = Coche('Volvo')
print(coche.name)
```
**Ejemplo:** en este ejemplo definimos el constructor, pasamos argumentos self, name (es importante tener en cuenta que si no usamos self estaremos creando una variable local en vez de un atributo del objeto).
Creamos una instancia a un objeto.
Tenemos acceso al atributo name creado previamente en el constructor.

# ¿Cuáles son los tres verbos de API?

Las API (Interfaz de Programación de Aplicaciones) son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos.Hay diferentes tipos de API, uno de ellos son las API REST, siguen los principios de la arquitectura REST y utiliza el protocolo HTTP para interactuar con recursos a través de la web.

![](https://images.ctfassets.net/vwq10xzbe6iz/5sBH4Agl614xM7exeLsTo7/9e84dce01735f155911e611c42c9793f/rest-api.png)

### Como funciona REST
##### Llamadas al API

Las llamadas al API se implementan como peticiones HTTP, en las que:

La URL representa el recurso
```
http://www.formandome.es/api/cursos/1
```
El método (HTTP Verbs) representa la operación:
```
GET http://www.formandome.es/api/cursos/1
```
El código de estado HTTP representa el resultado:
```
200 OK HTTP/1.1
404 NOT FOUND HTTP/1.1
```
Las API REST utilizan los siguientes verbos principales para realizar operaciones en recursos:
- **GET:** es el que usamos para consultar un recurso o una colección de recursos. Una de las principales características de una petición GET es que no causan efectos secundarios en el servidor, no producen nuevos registros, ni modifican los ya existentes. Cuando se realiza una solicitud GET a una URL determinada, el servidor responde proporcionando los datos solicitados, generalmente en formato JSON, XML o algún otro formato de intercambio de datos.
- **POST:** las peticiones con POST son sólo para crear recursos nuevos. Cada llamada con POST debería producir un nuevo recurso. Por lo general, se utiliza cuando se quiere enviar datos de un formulario o de algún otro origen al servidor para que los procese y cree un nuevo recurso en la base de datos.
- **DELETE:** DELETE es el verbo que usamos para eliminar registros, bien pudiera ser para eliminar un recurso individual o una colección completa. Cuando se realiza una solicitud DELETE a una URL determinada, el servidor elimina el recurso correspondiente y devuelve una respuesta indicando si la eliminación fue exitosa.
- **PUT:** se usa para modificar/ actualizar un recurso existente. Cuando se realiza una solicitud PUT a una URL específica, el servidor actualiza el recurso correspondiente con los datos proporcionados en el cuerpo de la solicitud. Si el recurso no existe, PUT puede crear uno nuevo con el identificador proporcionado en la URL.

##### Para ampliar conocimientos
Para ampliar conocimientos sobre las API os dejo unos enlaces que pueden ser de vuestro interés:
<https://juanda.gitbooks.io/webapps/content/api/arquitectura-api-rest.html>

# ¿Es MongoDB una base de datos SQL o NoSQL?
MongoDB es un sistema de gestión de bases de datos no relacionales y de código abierto, que utiliza elementos flexibles en lugar de tablas y filas para procesar y almacenar varias formas de datos.
MongoDB es una base de datos NoSQL orientada a documentos, los documentos o colecciones de documentos de MongoDB son las unidades básicas de datos y se almacenan en formato JSON binario con esquemas dinámicos que ke dan mucha flexibilidad para crear registros de datos, consultar colecciones de documentos a través de la agregación de MongoDB y analizar grandes cantidades de información.

![](https://lh6.googleusercontent.com/rX3g_L15dQ-PVdl6ETTjG4eph7BwypDw8qFSlJHahe9Hc0xUT0hEcKkssoeFRn6cIUPdKNVdgPt3Ci462DAzSbqG4eFHC87nx9Zh6L09ScN09o2_QOjFiTlHacXYoKcq9RG6d6kB)

Algunas de sus características:
- **Documentos BSON:** son documentos JSON pero binarios codificados. Cada documento es una entidad independiente que puede contener diferentes campos y estructuras de datos.
- **Escalabilidad horizontal:** MongoDB está diseñado para ser escalable horizontalmente, lo que significa que puedes distribuir tu base de datos en varios servidores para manejar grandes volúmenes de datos y de cargas de trabajo.
- **Alto rendimiento:** MongoDB ofrece un alto rendimiento mediante el uso de índices, consultas optimizadas y otras técnicas de optimización interna.
-  **Flexibilidad:** Debido a su esquema dinámico, MongoDB es muy flexible y puede adaptarse fácilmente a cambios en los requisitos de tu aplicación.
-  MongoDB tiene una gran comunidad de desarrolladores y una amplia gama de herramientas y recursos disponibles.
-  **Soporte a múltiples lenguajes:** Uno de los mejores aspectos de MongoDB es su soporte a múltiples lenguajes. Se han publicado varias versiones de MongoDB y están en continuo desarrollo con soporte de controlador para los lenguajes de programación más populares, incluidos Python, PHP, Ruby, Node.js, C++, Scala, JavaScript y muchos más.

##### Para ampliar conocimientos
Para ampliar conocimientos sobre la bases de datos MongoDB, os animo a leer el siguiente enlace y realizar los ejercicios prácticos que puedes encontrar:
<https://www.w3schools.com/mongodb/index.php>
<https://sitiobigdata.com/2017/12/27/mongodb-arquitectura-y-modelo-de-datos/>
<https://datademia.es/blog/que-es-mongodb>

# ¿Qué es una API?
Las API (Interfaz de Programación de Aplicaciones) son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Una API especifica cómo los componentes de software deben interactuar entre sí.
### Para qué sirve una API
Una de las principales funciones de las API es poder facilitarle el trabajo a los desarrolladores y ahorrarles tiempo y dinero. Por ejemplo, si estás creando una aplicación que es una tienda online, no necesitarás crear desde cero un sistema de pagos u otro para verificar si hay stock disponible de un producto. Podrás utilizar la API de un servicio de pago ya existente, por ejemplo PayPal, y pedirle a tu distribuidor una API que te permita saber el stock que ellos tienen.
No será necesario tener que reinventar con cada servicio que se crea, ya que podrás utilizar piezas o funciones que otros ya han creado. 
También son útiles para cuando lo único que se quiere es utilizar deliberadamente las funciones de un determinado servicio para ofrecer ventajas a sus usuarios o atraer a los usuarios de ese servicio a que utilicen tu aplicación.

### ¿Qué tipos de API hay?
Hay básicamente cuatro tipos de API en lo que se refiere a sus políticas de uso compartido, como veremos a continuación.
##### APIs según sus políticas de uso
1. **APIs públicas o abiertas**
Las APIs públicas también son conocidas como API abiertas y están disponibles para que otros usuarios o desarrolladores las empleen con mínimas restricciones o, en algunos casos incluso, están totalmente accesibles.
2. **APIs privadas o internas**
Las APIs privadas o internas están ocultas de los usuarios externos y se exponen únicamente para los sistemas internos de una organización. Se emplean para el desarrollo interno de la empresa, optimizando la productividad y la reutilización de servicios.
3. **APIs de aliados comerciales**
Las APIs de aliados comerciales son aquellas que se exponen entre los miembros de una alianza comercial. Como no están disponibles para todos, se necesita una autorización especial para usarlas.
4. **APIs compuestas**
Las APIs compuestas utilizan distintos datos o diversas APIs de servicio y permiten que los desarrolladores puedan acceder a varios terminales.
Asimismo, podemos también dividir las APIs en cuatro según lo que ofrecen o casos de uso, como verás ahora.

##### APIs según sus casos de uso

![](https://assets-global.website-files.com/62e153e41d6ee298cc9a98f7/63becf42923e2bf220790838_APIS.png)
1. **API de datos**
Las APIs de datos proporcionan a varios bancos de datos o proveedores SaaS (Software as a Service o Software como Servicio) acceso CRUD (Create, Read, Update, Delete) a conjuntos de datos subyacentes, permitiendo la comunicación entre una aplicación y un sistema de gestión de bases de datos.
2. **API de sistemas operativos**
Este grupo de APIs definen cómo las aplicaciones usan los recursos disponibles y servicios del sistema operativo. Por lo que cada OS (Operative System) posee un conjunto de APIs, por ejemplo, Windows API o Linux API tienen el kernel-user space API y kernel internal API.
3. **APIs remotas**
Este grupo define los estándares de interacción que las aplicaciones tienen en diferentes dispositivos, es decir, un software accede a ciertos recursos ubicados fuera del dispositivo que los solicita, como dice su nombre. Como dos aplicaciones se conectan de forma remota a través de una red, las APIs remotas usan protocolos para lograr la conexión.
4. **APIs web**
Esta clase de API es la más común, dado que las APIs web proporcionan datos que los dispositivos pueden leer y transferirlos entre sistemas basados en la web o arquitectura cliente-servidor.

##### Para ampliar conocimientos
Os dejo unos enlaces que os vendrá bien para entender mejor el concepto de API:
<https://www.deltaprotect.com/blog/que-es-una-api>
<https://www.sydle.com/es/blog/api-6214f68876950e47761c40e7>

# ¿Qué es Postman?

Postman es una herramienta utilizada para probar API's. Con la ayuda de esta herramienta, los desarrolladores pueden crear, probar, compartir y documentar API fácilmente.
Es una interfaz gráfica de usuario sencilla para enviar y ver solicitudes y respuestas HTTP.
Al utilizar Postman, para fines de prueba, no es necesario escribir ningún código de red de cliente HTTP. En su lugar, creamos conjuntos de pruebas llamados colecciones y dejamos que Postman interactúe con la API.
En esta herramienta, está integrada casi cualquier funcionalidad que cualquier desarrollador pueda necesitar. Esta herramienta tiene la capacidad de realizar varios tipos de solicitudes HTTP como GET, POST, PUT, PATCH y convertir la API a código para lenguajes como JavaScript y Python.

Postman nos ofrece la posibilidad de guardar y agrupar conjuntos de solicitudes en lo que ellos denominan “Collections”, es decir simples carpetas en distintos niveles que organizarán nuestras peticiones HTTP.

### ¿Por qué utilizar cartero?
Postman se ha convertido en una herramienta cómoda. Algunas razones son:
- **Creación de entornos:** el diseño de múltiples entornos da como resultado una menor replicación de pruebas, ya que se puede usar la misma colección pero para una configuración diferente.
- **Desarrollo de pruebas:** para probar los puntos de control, se agregará la verificación del estado de respuesta HTTP exitosa a cada llamada API.
- **Documentación de APIs:** Una parte fundamental de la creación y uso de una API es disponer de una documentación completa y bien estructurada. Postman genera esta documentación de forma automática, utilizando la información de las peticiones y las descripciones que hayas introducido al crearlas.
- **Pruebas de automatización:** las pruebas se pueden realizar en varias repeticiones o iteraciones utilizando Collection Runner o Newman, lo que ahorra tiempo para pruebas repetidas. La opción más sencilla es utilizar el Collection Runner, que a partir de una colección que definas, ejecuta ese conjunto de peticiones el número de veces que establezcas. 
- **Depuración:** para depurar eficazmente las pruebas, la consola de cartero ayuda a realizar un seguimiento de los datos que se recuperan.

Os dejo el enlace a su web <https://www.postman.com> donde podeis trabajar con su versión gratuita o versiones diferentes de pago.

##### Para ampliar conocimientos
Si quereis ampliar conocimientos os dejo el enlace de un tutorial que puede ser de gran ayuda.
<https://www.javatpoint.com/postman>
<https://lamadriguerabit.com/articulos/que-es-postman/>

# ¿Qué es el polimorfismo?
Es una técnica de la programación orientada a objetos que nos ayuda a implementar el mismo conjunto de métodos con diferentes comportamientos para distintos tipos de objetos, lo que permite una mayor flexibilidad.
El polimorfismo en Python está relacionado con la herencia, que es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. 

```
class Vehiculo:
  def __init__(self, marca, modelo):
      self.marca = marca
      self.modelo = modelo
  def descripcion(self):
      return f"Vehículo: {self.marca} {self.modelo}"

class Coche(Vehiculo):
  def sonido(self):
      return "Ruuuummmm"

class Moto(Vehiculo):
  def sonido(self):
      return "Vroom vroom"

coche = Coche("Seat", "Leon")
moto = Moto( "Honda", "CBR")

print(coche.descripcion())  /* Vehículo: Seat Leon
print(moto.descripcion())   /* Vehículo: Honda CBR
print(coche.sonido())       /* Ruuuummmm
print(moto.sonido())        /* Vroom vroom
```
**Ejemplo:** este código crea dos tipos de vehículos (Coche y Moto) que heredan de la clase  Vehiculo. Cada tipo de vehículo tiene su propio método para describirse y para hacer sonidos característicos (polimorfismo). Al crear instancias de estos vehículos y llamar a sus métodos, obtenemos la descripción y el sonido de cada uno de ellos.

# ¿Qué es un método dunder?
Son métodos que se proporcionan directamente desde el lenguaje Python, se pueden usar pero no se deben anular ni cambiar.Estos métodos comienzan y finalizan con doble guión bajo (\__init__ ).
En otros lenguajes de programación no se utiliza esta sintaxis de los guiones porque tienen lo que se llaman métodos privados.

### También llamados métodos mágicos:
##### \__str__: Devuelve una cadena de carácteres. Representación legible para usuarios.
```
class Persona:
  def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

  def __str__(self):
      return f"Persona: {self.nombre}, Edad: {self.edad}"

persona1 = Persona("Juan", 30)

print(persona1)   /*Persona: Juan, Edad: 30
```
**Ejemplo:** definimos el método __str__, que devuelve una cadena que describe el objeto de la clase Persona.

##### \__repr__:Devuelve una cadena de carácteres.Similar al __str__ con la diferencia que lo representa sin formato.

##### \__len__:Devuelve la cantidad de elementos que tiene una lista.
```
class MiLista:
  def __init__(self, elementos=[]):
      self.elementos = elementos

  def __len__(self):
      return len(self.elementos)

# Crear una instancia de la clase MiLista
mi_lista = MiLista([1, 2, 3, 4, 5])

# Obtener la longitud de la lista usando el método __len__()
longitud = len(mi_lista)

print("Longitud de la lista:", longitud)   /*Longitud de la lista: 5
```
##### Para ampliar conocimientos
Si quieres conocer más métodos especiales te animo a leer la siguiente información:
<https://geekflare.com/es/magic-methods-in-python/>
<https://jolthgs.wordpress.com/2013/04/20/metodos-especiales-de-las-clases-en-python/>
<https://aprendepython.es/core/modularity/oop/#metodos-magicos>

# ¿Qué es un decorador de python?
Un decorador es una función que recibe otra función como parámetro, le añade cosas y retorna una función diferente. Son herramientas muy útiles. Nos permiten envolver una función dentro de otra y modificar el comportamiento de esta última sin modificarla permanentemente.

```
def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

print(suma(5,8))    /* Se va a llamar
                    /* Entra en la función
                    /* Se ha llamado
                    /* 13
```
**Ejemplo:** el decorador **@mi_decorado**r imprime mensajes antes y después de llamar a la función original **suma**, lo que permite realizar acciones adicionales alrededor de la ejecución de la función original.

##### Para ampliar conocimientos
Si quieres ampliar conocimientos te dejo aquí unos enlaces que te animo a revisar.
<https://ellibrodepython.com/decoradores-python#decoradores>
<https://python-intermedio.readthedocs.io/es/latest/decorators.html#>
<https://platzi.com/blog/decoradores-en-python-que-son-y-como-funcionan/#:~:text=Un%20decorador%20en%20Python%20es,esta%20%C3%BAltima%20sin%20modificarla%20permanentemente.>




