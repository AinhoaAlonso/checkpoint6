# ¿Para qué usamos Clases en Python?

La programación orientada a objetos (POO) es una técnica muy útil para estructurar y organizar el código de manera lógica y coherente, lo que hace que el código sea más fácil de entender, mantener y mejorar. 

Una clase define una plantilla o molde para crear objetos, los cuales son instancias de esa clase. Los objetos creados a partir de una clase tienen las mismas propiedades y comportamientos definidos por la clase, pero pueden tener valores diferentes para los atributos que se definen en la clase.

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

Las API REST utilizan los siguientes verbos principales para realizar operaciones en recursos:
- **GET:** es el que usamos para consultar un recurso o una colección de recursos. Una de las principales características de una petición GET es que no causan efectos secundarios en el servidor, no producen nuevos registros, ni modifican los ya existentes. Cuando se realiza una solicitud GET a una URL determinada, el servidor responde proporcionando los datos solicitados, generalmente en formato JSON, XML o algún otro formato de intercambio de datos.
- **POST:** las peticiones con POST son sólo para crear recursos nuevos. Cada llamada con POST debería producir un nuevo recurso. Por lo general, se utiliza cuando se quiere enviar datos de un formulario o de algún otro origen al servidor para que los procese y cree un nuevo recurso en la base de datos.
- **DELETE:** DELETE es el verbo que usamos para eliminar registros, bien pudiera ser para eliminar un recurso individual o una colección completa. Cuando se realiza una solicitud DELETE a una URL determinada, el servidor elimina el recurso correspondiente y devuelve una respuesta indicando si la eliminación fue exitosa.
- **PUT:** se usa para modificar/ actualizar un recurso existente. Cuando se realiza una solicitud PUT a una URL específica, el servidor actualiza el recurso correspondiente con los datos proporcionados en el cuerpo de la solicitud. Si el recurso no existe, PUT puede crear uno nuevo con el identificador proporcionado en la URL.

# ¿Es MongoDB una base de datos SQL o NoSQL?
MongoDB es una base de datos NoSQL potente y versátil (no relacional) que se utilizar en una gran variedad de aplicaciones.
MongoDB no utiliza tablas con filas y columnas como las bases de datos tradicionales, MongoDB es una base de datos NoSQL orientada a documentos, almacena datos en documentos BJSON  flexibles y esquemas dinámicos.
Algunas características:
- **Documentos BSON:** son documentos JSON pero binarios codificados. Cada documento es una entidad independiente que puede contener diferentes campos y estructuras de datos.
- **Escalabilidad horizontal:** MongoDB está diseñado para ser escalable horizontalmente, lo que significa que puedes distribuir tu base de datos en varios servidores para manejar grandes volúmenes de datos y de cargas de trabajo.
- **Alto rendimiento:** MongoDB ofrece un alto rendimiento mediante el uso de índices, consultas optimizadas y otras técnicas de optimización interna.
-  **Flexibilidad:** Debido a su esquema dinámico, MongoDB es muy flexible y puede adaptarse fácilmente a cambios en los requisitos de tu aplicación.
-  MongoDB tiene una gran comunidad de desarrolladores y una amplia gama de herramientas y recursos disponibles.

##### Para ampliar conocimientos
Para ampliar conocimientos sobre la bases de datos MongoDB, os animo a leer el siguiente enlace y realizar los ejercicios prácticos que puedes encontrar:
<https://www.w3schools.com/mongodb/index.php>

# ¿Qué es una API?
Las API (Interfaz de Programación de Aplicaciones) son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Una API especifica cómo los componentes de software deben interactuar entre sí.
### Para qué sirve una API
Una de las principales funciones de las API es poder facilitarle el trabajo a los desarrolladores y ahorrarles tiempo y dinero. Por ejemplo, si estás creando una aplicación que es una tienda online, no necesitarás crear desde cero un sistema de pagos u otro para verificar si hay stock disponible de un producto. Podrás utilizar la API de un servicio de pago ya existente, por ejemplo PayPal, y pedirle a tu distribuidor una API que te permita saber el stock que ellos tienen.
No será necesario tener que reinventar con cada servicio que se crea, ya que podrás utilizar piezas o funciones que otros ya han creado. 
También son útiles para cuando lo único que se quiere es utilizar deliberadamente las funciones de determinado servicio para ofrecer ventajas a sus usuarios o atraer a los usuarios de ese servicio a que utilicen tu aplicación.

# ¿Qué es Postman?

Postman es una herramienta utilizada para probar API's. Con la ayuda de esta herramienta, los desarrolladores pueden crear, probar, compartir y documentar API fácilmente. Os dejo el enlace a su web <https://www.postman.com> donde podeis trabajar con su versión gratuita o versiones diferentes de pago.

##### Para ampliar conocimientos
Si quereis ampliar conocimientos os dejo el enlace de un tutorial que puede ser de gran ayuda.
<https://www.javatpoint.com/postman>

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




