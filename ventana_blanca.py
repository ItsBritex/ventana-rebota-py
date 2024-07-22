import sys
import random
import pygame
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana como un cuadro sin bordes
        self.setWindowTitle("Ventana Rebotando")
        self.setGeometry(100, 100, 300, 200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Sin bordes y siempre encima
        self.setStyleSheet("background-color: white;")  # Color de fondo de la ventana

        # Variables de posición y velocidad
        self.x_velocity = 5
        self.y_velocity = 5
        self.window_width = 300
        self.window_height = 200

        # Inicializar pygame para reproducir sonidos
        pygame.init()
        pygame.mixer.init()  # Inicializar el mezclador de pygame
        self.sound = pygame.mixer.Sound('steve-old.mp3')  # Asegúrate de tener un archivo de sonido 'steve-old.mp3' en el mismo directorio

        # Crear un temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(30)  # Actualizar cada 30 ms

    def update_position(self):
        # Obtener la posición actual
        x = self.x()
        y = self.y()
        
        # Obtener el tamaño de la pantalla
        screen_width = QApplication.desktop().screenGeometry().width()
        screen_height = QApplication.desktop().screenGeometry().height()

        # Actualizar la posición
        x += self.x_velocity
        y += self.y_velocity

        # Rebotar en los bordes y cambiar de color
        rebote = False
        if x <= 0 or x + self.window_width >= screen_width:
            self.x_velocity = -self.x_velocity
            rebote = True
        if y <= 0 or y + self.window_height >= screen_height:
            self.y_velocity = -self.y_velocity
            rebote = True

        if rebote:
            self.change_color()
            self.play_sound()

        # Mover la ventana a la nueva posición
        self.move(x, y)

    def change_color(self):
        # Cambiar el color de fondo de la ventana
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.setStyleSheet(f"background-color: {color.name()};")

    def play_sound(self):
        # Reproducir el sonido de rebote
        self.sound.play()

    def paintEvent(self, event):
        # Dibujar el fondo de la ventana con el color establecido
        painter = QPainter(self)
        painter.setBrush(self.palette().window())
        painter.drawRect(self.rect())

# Crear una instancia de QApplication
app = QApplication(sys.argv)

# Crear una instancia de la ventana principal
window = MainWindow()

# Mostrar la ventana
window.show()

# Ejecutar el bucle principal de la aplicación
sys.exit(app.exec_())
