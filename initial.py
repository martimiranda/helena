import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QWidget,QVBoxLayout, QGridLayout, QSizePolicy, QCheckBox)
from PyQt6.QtGui import QPixmap, QFont, QIcon, QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtSvg import QSvgRenderer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100, 100, 1400, 800)
        self.setWindowTitle("Helena Peluqueria")
        self.generar_contenido()
        
    
    def generar_contenido(self):
        # Configuramos la ventana principal
        self.setWindowTitle("Ventana con Imagen de Fondo")
        self.setGeometry(100, 100, 1400, 800)  # Posición y tamaño de la ventana
        
        # Establecer el color de fondo de la ventana a blanco
        self.setStyleSheet("background-color: white;")

        # Cargar la imagen de fondo
        self.background_label = QLabel(self)
        pixmap = QPixmap("icono.png")  # Reemplaza con la ruta de tu imagen de fondo
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)  # Escala la imagen al tamaño del label
        self.background_label.setGeometry(300, 40, 800, 400)  # Ajusta el tamaño del label para que cubra la ventana

        # Crear un QLineEdit para la entrada de texto
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Cercar clients")  # Texto de marcador de posición
        self.text_input.setGeometry(300, 50, 800, 40)  # Ajustar la posición y el tamaño del QLineEdit

        # Aplicar estilo al QLineEdit para hacerlo redondeado y con borde naranja
        self.text_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid orange;
                border-radius: 15px;  /* Cambia este valor para ajustar el redondeado */
                padding: 5px;  /* Añade un poco de espacio interior */
                font-size: 16px;  /* Tamaño de fuente */
            }
        """)

        # Crear una tabla debajo del QLineEdit
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(100, 100, 1200, 300)  # Aumentar el tamaño de la tabla
        self.table_widget.setColumnCount(4)  # Número de columnas
        self.table_widget.setHorizontalHeaderLabels(["Nom", "Cognoms", "Telèfon", "Color"])  # Nombres de las columnas
        self.table_widget.setRowCount(10)  # Establecer el número de filas iniciales a 10

        # Añadir algunos datos de ejemplo a la tabla
        sample_data = [
            ["Joan", "Martínez Lorca", "123456789", "55/00 1/2 7/66"],
            ["Maria", "López Gutiérrez", "987654321", "55/00 1/2 7/66"],
            ["Pere", "García Sánchez", "456789123", "55/00 1/2 7/66"],
            ["Anna", "Sánchez Ruiz", "789123456", "55/00 1/2 7/66"],
            ["Marc", "Fernández Luque", "321654987", "55/00 1/2 7/66"],
            ["Laura", "Cruz Martínez", "159753486", "55/00 1/2 7/66"],
            ["Jordi", "Vidal González", "753951456", "55/00 1/2 7/66"],
            ["Sofia", "Torres Pérez", "852147963", "55/00 1/2 7/66"],
            ["Alejandro", "Romero López", "963258741", "55/00 1/2 7/66"],
            ["Cristina", "Mendoza Salas", "654987321", "55/00 1/2 7/66"]
        ]
        
        # Rellenar la tabla con los datos de ejemplo
        for row, data in enumerate(sample_data):
            for column, value in enumerate(data):
                item = QTableWidgetItem(value)
                item.setFont(QFont("Arial", 16))  # Establecer tamaño de fuente para las celdas
                self.table_widget.setItem(row, column, item)

        # Establecer el ancho de las columnas
        self.table_widget.setColumnWidth(0, 200)  # Ancho de la primera columna
        self.table_widget.setColumnWidth(1, 400)  # Ancho de la segunda columna
        self.table_widget.setColumnWidth(2, 300)  # Ancho de la tercera columna
        self.table_widget.setColumnWidth(3, 240)  # Ancho de la cuarta columna

        # Ocultar el encabezado vertical para eliminar los números de fila
        self.table_widget.verticalHeader().setVisible(False)

        # Estilo para hacer la tabla transparente y sin bordes
        self.table_widget.setStyleSheet("""
            QTableWidget {
                background: transparent;  /* Fondo transparente */
                border: 1px solid #d3d3d3;  /* Sin borde para la tabla */
                border-radius: 10px;  /* Bordes redondeados para la tabla (sin efecto visible ahora) */
            }
            QHeaderView::section {
                background-color: rgba(255, 165, 0, 100);
                border: none;  /* Sin borde en los encabezados */
                font-weight: bold;  /* Encabezados en negrita */
                font-size: 18px;  /* Tamaño de fuente para encabezados */
                border-radius: 10px;  /* Bordes redondeados para encabezados */
            }
            QTableWidget::item {
                background-color: rgba(255, 255, 255, 150);  /* Fondo semi-transparente para las celdas */
                border: 1px solid #d3d3d3;  /* Sin borde para las celdas */
            }
        """)

        create_button = QPushButton(self)
        create_button.setText('Afegir nou client')
        create_button.resize(320 , 120)
        create_button.move(100,400)
        create_button.setStyleSheet(""" QPushButton{
            
            font-size: 16px;
            border: 1px solid black;
            border-radius: 10px;


        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        create_button.clicked.connect(self.crear_usuario)


        svg_renderer = QSvgRenderer('crear-svg.svg')
        svg_pixmap = QPixmap(64, 64)  # Elige el tamaño que quieras para tu ícono
        svg_pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(svg_pixmap)
        svg_renderer.render(painter)
        painter.end()
        icon = QIcon(svg_pixmap)

        create_button.setIcon(icon)
        create_button.setIconSize(svg_pixmap.size())
        create_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        
        
        calculs_button = QPushButton(self)
        calculs_button.setText('Càlculs')
        calculs_button.resize(320 , 200)
        calculs_button.move(100,550)
        calculs_button.setStyleSheet(""" QPushButton{
            
            font-size: 16px;
            border: 1px solid black;
            border-radius: 10px;


        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        calculs_button.clicked.connect(self.calculs)


        svg_renderer_calculs = QSvgRenderer('calculator-svg.svg')
        svg_pixmap_calculs = QPixmap(64, 64)  # Elige el tamaño que quieras para tu ícono
        svg_pixmap_calculs.fill(Qt.GlobalColor.transparent)
        painter_calculs = QPainter(svg_pixmap_calculs)
        svg_renderer_calculs.render(painter_calculs)
        painter_calculs.end()
        icon_calculs = QIcon(svg_pixmap_calculs)

        calculs_button.setIcon(icon_calculs)
        calculs_button.setIconSize(svg_pixmap_calculs.size())
        calculs_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        botones_izquierda = QWidget(self)  # El QWidget dentro de la ventana principal
        botones_izquierda.move(90, 400)
        botones_izquierda.setMinimumSize(320, 400)
        botones_izquierda.setStyleSheet("""
            background-color: transparent;
            border: none;
        """)

        # Crear un layout dentro del contenedor (como si fuera un div)
        layout_botones = QGridLayout(botones_izquierda)
        layout_botones.addWidget(create_button,0,0)
        layout_botones.addWidget(calculs_button,1,0)
        layout_botones.setRowStretch(0,5)
        layout_botones.setRowStretch(1,5)



        

        

       

        ficha_usuario = QWidget(self)  # El QWidget dentro de la ventana principal
        ficha_usuario.move(420, 400)
        ficha_usuario.setMinimumSize(880, 400)

        # Añadir estilo para que se vea como un "div"
        ficha_usuario.setStyleSheet("""
            background-color: transparent;
            border: 1px solid #d3d3d3;
        """)

        # Crear un layout dentro del contenedor (como si fuera un div)
        layout = QGridLayout(ficha_usuario)

        # Añadir widgets dentro del contenedor (QWidget)
        label = QLabel("Fitxa de client")
        label.setStyleSheet("""
            font-weight: 100; /* Peso de la fuente (más fino) */
            background-color: rgba(255, 165, 0, 100);
            border: 1px solid #d3d3d3;
            border-radius: 10px;
            font-weight: bold;  /* Encabezados en negrita */
            font-size: 18px;
            text-align: center;

        """)
        
        #label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding) 
        
        svg_renderer_edit = QSvgRenderer('edit-svg.svg')
        svg_pixmap_edit = QPixmap(24, 24)  # Elige el tamaño que quieras para tu ícono
        svg_pixmap_edit.fill(Qt.GlobalColor.transparent)
        painter_edit = QPainter(svg_pixmap_edit)
        svg_renderer_edit.render(painter_edit)
        painter_edit.end()

        icon_edit = QIcon(svg_pixmap_edit)

        edit_name_button = QPushButton(self)
        edit_name_button.setText('Editar')
        edit_name_button.setStyleSheet(""" QPushButton{
            
            font-size: 14px;
            border: 1px solid black;
            border-radius: 10px;

        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        edit_name_button.setIcon(icon_edit)
        edit_name_button.setIconSize(svg_pixmap_edit.size())
        edit_name_button.clicked.connect(self.editar_nombre)
        edit_name_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        edit_surname_button = QPushButton(self)
        edit_surname_button.setText('Editar')
        edit_surname_button.setStyleSheet(""" QPushButton{
            
            font-size: 14px;
            border: 1px solid black;
            border-radius: 10px;

        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        edit_surname_button.setIcon(icon_edit)
        edit_surname_button.setIconSize(svg_pixmap_edit.size())
        edit_surname_button.clicked.connect(self.editar_apellido)
        edit_surname_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        edit_color_button = QPushButton(self)
        edit_color_button.setText('Editar')
        edit_color_button.setStyleSheet(""" QPushButton{
            
            font-size: 14px;
            border: 1px solid black;
            border-radius: 10px;

        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        edit_color_button.setIcon(icon_edit)
        edit_color_button.setIconSize(svg_pixmap_edit.size())
        edit_color_button.clicked.connect(self.editar_color)
        edit_color_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        edit_telefon_button = QPushButton(self)
        edit_telefon_button.setText('Editar')
        edit_telefon_button.setStyleSheet(""" QPushButton{
            
            font-size: 14px;
            border: 1px solid black;
            border-radius: 10px;

        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        edit_telefon_button.setIcon(icon_edit)
        edit_telefon_button.setIconSize(svg_pixmap_edit.size())
        edit_telefon_button.clicked.connect(self.editar_telefono)
        edit_telefon_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)



        informacio_usuari = QGridLayout()

        # Estilo común para los QLabel
        label_style = """
            font-size: 16px;
            font-weight: bold;
            border: none;
        """

        # Añadir los QLabel con el estilo
        nom_label = QLabel("Nom:")
        nom_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(nom_label, 0, 0)

        nom_value_label = QLabel("Joan")
        nom_value_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(nom_value_label, 0, 1)
        informacio_usuari.addWidget(edit_name_button, 0, 2)

        cognoms_label = QLabel("Cognoms:")
        cognoms_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(cognoms_label, 1, 0)

        cognoms_value_label = QLabel("Martínez Lorca")
        cognoms_value_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(cognoms_value_label, 1, 1)
        informacio_usuari.addWidget(edit_surname_button, 1, 2)

        color_label = QLabel("Color:")
        color_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(color_label, 2, 0)

        color_value_label = QLabel("55/00 1/2 7/66")
        color_value_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(color_value_label, 2, 1)
        informacio_usuari.addWidget(edit_color_button, 2, 2)

        telefon_label = QLabel("Telèfon:")
        telefon_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(telefon_label, 3, 0)

        telefon_value_label = QLabel("123456789")
        telefon_value_label.setStyleSheet(label_style)
        informacio_usuari.addWidget(telefon_value_label, 3, 1)
        informacio_usuari.addWidget(edit_telefon_button, 3, 2)


        



        informacio_usuari.setColumnStretch(0, 4)  # Columna 0 ocupa el 40%
        informacio_usuari.setColumnStretch(1, 4)  # Columna 1 ocupa el 40%
        informacio_usuari.setColumnStretch(2, 2)

        layout_eleccion = QGridLayout()
        checkbox_nou = QCheckBox("Client nou")
        checkbox_antic = QCheckBox("Client antic")

        checkbox_nou.setStyleSheet("""
        QCheckBox {
            font-size: 16px;
            padding: 5px;
            border-radius: 10px;
            
        }
        QCheckBox:checked {
            font-weight:bold;
            border: 1px solid orange;


        }
        """)

        checkbox_antic.setStyleSheet("""
        QCheckBox {
            font-size: 16px;
            padding: 5px;
            border-radius: 10px;


        }
        QCheckBox:checked {
            font-weight:bold;
            border: 1px solid orange;

        }
        """)

        checkbox_antic.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        checkbox_nou.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        layout_eleccion.addWidget(checkbox_antic,0,0)
        layout_eleccion.addWidget(checkbox_nou,0,1)

        layout_tipus_client = QGridLayout()
        label_tipus = QLabel("Tipus de client:")
        label_tipus.setStyleSheet(label_style)
        layout_tipus_client.addWidget(label_tipus, 0, 0)

        layout_tipus_client.addLayout(layout_eleccion, 1, 0)
        layout_tipus_client.setRowStretch(0, 5)  # Primera fila 20%
        layout_tipus_client.setRowStretch(1, 5)
        
        pack_informacio_usuari = QGridLayout()
        pack_informacio_usuari.addLayout(informacio_usuari,0,0)
        pack_informacio_usuari.addLayout(layout_tipus_client,1,0)
        pack_informacio_usuari.setRowStretch(0,7)
        pack_informacio_usuari.setRowStretch(1,3)



        

        svg_renderer_drop = QSvgRenderer('trash-svg.svg')
        svg_pixmap_drop = QPixmap(64, 64)  # Elige el tamaño que quieras para tu ícono
        svg_pixmap_drop.fill(Qt.GlobalColor.transparent)
        painter_drop = QPainter(svg_pixmap_drop)
        svg_renderer_drop.render(painter_drop)
        painter_drop.end()

        icon_drop = QIcon(svg_pixmap_drop)

        svg_renderer_services = QSvgRenderer('services-svg.svg')
        svg_pixmap_services = QPixmap(64, 64)  # Elige el tamaño que quieras para tu ícono
        svg_pixmap_services.fill(Qt.GlobalColor.transparent)
        painter_services = QPainter(svg_pixmap_services)
        svg_renderer_services.render(painter_services)
        painter_services.end()

        icon_services = QIcon(svg_pixmap_services)

        serveis_button = QPushButton(self)
        serveis_button.setText('Serveis del client')
        serveis_button.clicked.connect(self.servicios_usuario)
        serveis_button.setIcon(icon_services)
        serveis_button.setIconSize(svg_pixmap_services.size())
        serveis_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding) 
        serveis_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;  /* Tamaño de letra de 16px */
                border: 1px solid black;
                border-radius: 10px;
            }
            QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        """) 



        

        

        grid_layout = QGridLayout()
        grid_layout.addLayout(pack_informacio_usuari, 0, 0)
        grid_layout.addWidget(serveis_button, 0, 1)

        grid_layout.setColumnStretch(0,6)
        grid_layout.setColumnStretch(1,4)
        


        drop_button = QPushButton(self)
        drop_button.setText('Eliminar client')
        drop_button.clicked.connect(self.eliminar_usuario)
        drop_button.setIcon(icon_drop)
        drop_button.setIconSize(svg_pixmap_drop.size())
        drop_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;  /* Tamaño de letra de 16px */
                border: 1px solid black;
                border-radius: 10px;
            }

            QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        """) 
        drop_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        

        layout.addWidget(label,0,0)
        layout.addLayout(grid_layout,1,0)
        layout.addWidget(drop_button,2,0)

        
        

        layout.setRowStretch(0, 1)  # Primera fila 20%
        layout.setRowStretch(1, 7)
        layout.setRowStretch(2, 2)

        # Asignar el layout al contenedor
        #ficha_usuario.setLayout(layout)

        # Mostrar la ventana
        self.show()
    
    def crear_usuario(self):
        pass

    def editar_nombre(self):
        pass

    def editar_apellido(self):
        pass

    def editar_color(self):
        pass

    def editar_telefono(self):
        pass

    def eliminar_usuario(self):
        pass

    def servicios_usuario(self):
        pass

    def calculs(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
