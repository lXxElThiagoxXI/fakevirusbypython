import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class InterfazMultiplataforma(GridLayout):
    def __init__(self, **kwargs):
        super(InterfazMultiplataforma, self).__init__(**kwargs)
        self.rows = 3  # Organización limpia en filas
        self.spacing = 25
        self.padding = 40

        # 1. TÍTULO EN NEÓN (Se adapta a TV o Celular automáticamente)
        self.lbl_titulo = Label(
            text="⚡ SILVER MULTI-OS V1.0 ⚡", 
            font_size='32sp', 
            size_hint_y=0.2,
            bold=True,
            color=get_color_from_hex('#00ffcc')
        )
        self.add_widget(self.lbl_titulo)

        # 2. CONTENEDOR DE BOTONES (Formato Rejilla Horizontal)
        self.grid_botones = GridLayout(cols=3, spacing=20, size_hint_y=0.6)
        
        self.btn_juego = Button(text="🎮\n\nAVENTURA\nMÁGICA", font_size='18sp', halign='center')
        self.btn_media = Button(text="📺\n\nANDROID TV\nMODES", font_size='18sp', halign='center')
        self.btn_salir = Button(text="🛑\n\nCERRAR\nAPP", font_size='18sp', halign='center')

        self.grid_botones.add_widget(self.btn_juego)
        self.grid_botones.add_widget(self.btn_media)
        self.grid_botones.add_widget(self.btn_salir)
        self.add_widget(self.grid_botones)

        # 3. BARRA DE ESTADO INFERIOR
        self.lbl_status = Label(
            text="CONTROL: USA LAS FLECHAS O TOCA LA PANTALLA", 
            font_size='14sp', 
            size_hint_y=0.2,
            color=get_color_from_hex('#555555')
        )
        self.add_widget(self.lbl_status)

        # --- SISTEMA DE CONTROL REMOTO / JOYSTICK / TECLADO ---
        Window.bind(on_key_down=self.capturar_control)
        self.lista_botones = [self.btn_juego, self.btn_media, self.btn_salir]
        self.indice = 0
        self.actualizar_foco_tv()

    def actualizar_foco_tv(self):
        # Limpia los colores de todos los botones
        for btn in self.lista_botones:
            btn.background_normal = ''
            btn.background_color = get_color_from_hex('#16161a') # Fondo oscuro gamer
            btn.color = get_color_from_hex('#ffffff')
        
        # Le mete brillo neón al botón que tiene el control remoto encima
        boton_activo = self.lista_botones[self.indice]
        boton_activo.background_color = get_color_from_hex('#ff0055') # Fucsia potente
        self.lbl_status.text = f"SELECCIONADO: {boton_activo.text.split()[1]}"

    def capturar_control(self, window, key, scancode, codepoint, modifiers):
        # Flecha Derecha (Moverse en Android TV o PC)
        if key == 275:
            self.indice = (self.indice + 1) % len(self.lista_botones)
            self.actualizar_foco_tv()
        # Flecha Izquierda
        elif key == 276:
            self.indice = (self.indice - 1) % len(self.lista_botones)
            self.actualizar_foco_tv()
        # Botón Central del Control Remoto o ENTER en PC (Keycode 13 o 271)
        elif key in [13, 271]:
            self.lista_botones[self.indice].trigger_action()

class SilverMultiPlatformApp(App):
    def build(self):
        # Configuración automática para arrancar en pantalla completa si se desea
        Window.clearcolor = get_color_from_hex('#0a0a0c')
        return InterfazMultiplataforma()

if __name__ == '__main__':
    SilverMultiPlatformApp().run()
