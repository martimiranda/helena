import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QCheckBox)
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

        label_style = """
            font-size: 16px;
            font-weight: bold;
        """

        label_serveis = QLabel("Serveis fets per el client:")
        label_serveis.setStyleSheet(label_style)

        svg_renderer_edit = QSvgRenderer('edit-svg.svg')
        svg_pixmap_edit = QPixmap(34, 34)  # Elige el tamaño que quieras para tu ícono
        svg_pixmap_edit.fill(Qt.GlobalColor.transparent)
        painter_edit = QPainter(svg_pixmap_edit)
        svg_renderer_edit.render(painter_edit)
        painter_edit.end()

        icon_edit = QIcon(svg_pixmap_edit)

        editar_servei_button = QPushButton(self)
        editar_servei_button.setStyleSheet(""" QPushButton{
            
            font-size: 14px;

        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        editar_servei_button.setIcon(icon_edit)
        editar_servei_button.setIconSize(svg_pixmap_edit.size())
        #editar_servei_button.clicked.connect(self.editar_nombre)

        svg_renderer_drop = QSvgRenderer('trash-svg.svg')
        svg_pixmap_drop = QPixmap(34, 34)  # Elige el tamaño que quieras para tu ícono
        svg_pixmap_drop.fill(Qt.GlobalColor.transparent)
        painter_edit = QPainter(svg_pixmap_edit)
        svg_renderer_edit.render(painter_edit)
        painter_edit.end()

        icon_drop = QIcon(svg_pixmap_drop)

        eliminar_servei_button = QPushButton(self)
        eliminar_servei_button.setStyleSheet(""" QPushButton{
            
            font-size: 14px;

        } 
        
        QPushButton:hover {
        background-color: rgba(255, 165, 0, 100);  /* Fondo naranja semi-transparente */
        border: 2px solid #FFA500;  /* Borde naranja */
        color: white;  /* Cambiar el color del texto a blanco */
          /* Cambiar el cursor a una mano */
    }
        
        """)
        eliminar_servei_button.setIcon(icon_drop)
        eliminar_servei_button.setIconSize(svg_pixmap_drop.size())
        #eliminar_servei_button.clicked.connect(self.editar_nombre)

        # Cambiar table_widget a table_serveis
        self.table_serveis = QTableWidget(self)
        self.table_serveis.setColumnCount(3)  # Número de columnas
        self.table_serveis.setHorizontalHeaderLabels(["Servei","Borrar","Editar"])  # Nombres de las columnas
        self.table_serveis.setRowCount(5)  # Establecer el número de filas iniciales a 10

        # Añadir algunos datos de ejemplo a la tabla
        sample_data = [
            ["2024-10-04 Tall 25€", eliminar_servei_button, editar_servei_button],
            ["2024-09-15 Pentinat 15€", eliminar_servei_button, editar_servei_button],
            ["2024-07-12 Color Llarg 65€", eliminar_servei_button, editar_servei_button],
            ["2024-05-09 Tall 25€", eliminar_servei_button, editar_servei_button],
            ["2024-04-11 Color Llarg 65€", eliminar_servei_button, editar_servei_button],
        ]
        
        # Rellenar la tabla con los datos de ejemplo
        for row, data in enumerate(sample_data):
            for column, value in enumerate(data):
                item = QTableWidgetItem(value)
                item.setFont(QFont("Arial", 16))  # Establecer tamaño de fuente para las celdas
                self.table_serveis.setItem(row, column, item)

        # Establecer el ancho de las columnas
        self.table_serveis.setColumnWidth(0, 300)  # Ancho de la primera columna
        self.table_serveis.setColumnWidth(1, 100)  # Ancho de la segunda columna
        self.table_serveis.setColumnWidth(2, 100)  # Ancho de la tercera columna

        # Ocultar el encabezado vertical para eliminar los números de fila
        self.table_serveis.verticalHeader().setVisible(False)

        # Estilo para hacer la tabla transparente y sin bordes
        self.table_serveis.setStyleSheet("""
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
                border: none;  /* Sin borde para las celdas */
            }
        """)

        layout_serveis = QGridLayout()
        layout_serveis.addWidget(label_serveis, 0, 0)
        layout_serveis.addWidget(self.table_serveis, 1, 0)  # Cambiar aquí también
        layout_serveis.addWidget(afegir_servei_button, 2, 0)

        widget_contenido = QWidget()
        widget_contenido.setLayout(layout_serveis)

        # Establecer el widget como el widget central de la ventana
        self.setCentralWidget(widget_contenido)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
