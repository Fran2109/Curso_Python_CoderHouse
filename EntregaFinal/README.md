# Coderhouse, curso de python #34670
## Entrega final

### Revisiones:
* [x] Herencia en los templates.
* [x] Clases basadas en vistas y mixins.
* [x] Busqueda de Posts.
* [x] Advertencias si no hay posts o si no se encuentra nada en la busqueda.

### Consignas:
* [x] Se deberá de manera individual. Crearás una aplicación web estilo blog programada en Python en Django. Esta web tendrá admin, perfiles, registró, páginas y formularios.
* [x] La entrega se realizará enviando el link a GitHub.
* [x] En el github debe haber un video o link a vídeo donde nos muestran su web funcionando en no más de diez minutos. 
* [x] Dentro del Github deberá existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados.
* [x] Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca de los dueños de la página manejado en el route about/. (En castellano un “acerca de mí” que hable un poco de los creadores de la web y del proyecto).
* [x] Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Es decir un html que permite listar todos los blogs de la BD, con una información mínima de dicho blog).
* [x] Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>. (O sea al hacer click se ve más detalle de lo que se veía en el apartado anterior).
* [x] Si no existe ninguna página mostrar un "No hay páginas aún". (Aclarando, si en la página hacemos clic en algún lugar que no existe que diga eso, o que lleve a un html con esos mensaje, no dejar botones que no responden).
* [x] Para crear, editar o borrar los posts debes estar registrado como Administrador.
* [x] Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).
* [x] Piezas sugeridas, no hace falta que estén todas, pero tiene que haber por lo menos un CRUD completo y el módulo de Login debe ser sólido:
    * [x] NavBar
    * [x] Home
    * [x] About
    * [x] Pages
    * [x] Login
    * [x] Signup
    * [x] Messages
    * [x] Profile
    * [x] Logout
    * [x] Get pages
    * [x] Get page
    * [x] Create page
    * [x] Update Page
    * [x] Delete page
    * [x] Get profile
    * [x] Update profile
* [x] Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.
* [x] Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.
* [x] Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción - un link a una página web - email y contraseña.
* [x] Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.
* [x] Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar entre sí.

# Cómo testear el proyecto:
* Clonar el repositorio
* Iniciar el servidor con 'python manage.py runserver'
* La base de datos creada cuenta con informacion cargada.
* Hay tres cuentas registradas para probar.
    * Usuario 1:
        * username: Fran2109
        * password: Nico2709
    * Usuario 2:
        * username: Nico2709
        * password: Fran2709
    * Admin:
        * username: franciscofilosi
        * password: Fran2109
* Con estas cuentas podemos probar las acciones de lectura, eliminar, editar y crear un post.
* Podremos comunicar los usuarios entre si con mensajes en el area de mensajes.
* Podremos editar el perfil de cada usuario.
* Podremos crear un nuevo usuario.
* Podremos loguearnos con un usuario ya creado.
* Podremos ver la informacion de los usuarios en el area de perfiles.


Para mas informacion ver el video explicativo.