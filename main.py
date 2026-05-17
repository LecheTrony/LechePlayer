import customtkinter as ctk
import tkinter as tk
from pygame import mixer
from PIL import Image, ImageTk, ImageDraw
import os
import threading
import yt_dlp
import random
import time
import json
import subprocess
import platform
import shutil
import math
from tkinter import filedialog

# =========================================================
# PALETA DE COLORES GLOBAL - 60 TEMAS (ORIGINALES + NEKOPARA PASTEL)
# =========================================================
ctk.set_appearance_mode("dark")

CONFIG_FILE = "leche_config.json"

TEMAS_COLOR = {
    # --- Nekopara Ultra-Soft Pastel Series (Ajustados más claros y limpios) ---
    "Chocola Pastel": {"principal": "#ffe3ec", "hover": "#ffccd5", "paneles": "#2b2224", "borde": "#423236", "texto_osc": "#4a2831", "brillo": "#fff5f7", "lista_bg": "#211a1b"},
    "Vanilla Pastel": {"principal": "#e3faf5", "hover": "#cbf7ee", "paneles": "#1e2624", "borde": "#2d3b37", "texto_osc": "#1a3d35", "brillo": "#f4fdfb", "lista_bg": "#161c1b"},
    "Coconut Pastel": {"principal": "#f5efff", "hover": "#e8dcff", "paneles": "#24222b", "borde": "#363242", "texto_osc": "#2d1f47", "brillo": "#faf7ff", "lista_bg": "#1a1921"},
    "Azuki Pastel":   {"principal": "#ffebe6", "hover": "#ffd6cc", "paneles": "#2b211f", "borde": "#42322f", "texto_osc": "#47241c", "brillo": "#fff5f2", "lista_bg": "#211918"},
    "Cinnamon Pastel":{"principal": "#e3f2fd", "hover": "#bbdefb", "paneles": "#1e242b", "borde": "#2d3642", "texto_osc": "#152a47", "brillo": "#f1f8ff", "lista_bg": "#161a21"},
    "Maple Pastel":   {"principal": "#fff3e0", "hover": "#ffe0b2", "paneles": "#2b261f", "borde": "#423b2f", "texto_osc": "#47341c", "brillo": "#fffbf5", "lista_bg": "#211d18"},
    "Minaduki Family":{"principal": "#f3e5f5", "hover": "#e1bee7", "paneles": "#241f26", "borde": "#382f3d", "texto_osc": "#3c1a47", "brillo": "#faf5fa", "lista_bg": "#1b171c"},
    
    # --- Clásicos Retenidos (Bloque 1) ---
    "Verde Cyberpunk": {"principal": "#2ecc71", "hover": "#27ae60", "paneles": "#0b0c10", "borde": "#1f232b", "texto_osc": "#000000", "brillo": "#a3e4d7", "lista_bg": "#060709"},
    "Azul Neón":       {"principal": "#00d2ff", "hover": "#00a8cc", "paneles": "#09111e", "borde": "#162942", "texto_osc": "#000000", "brillo": "#e0f7fa", "lista_bg": "#040810"},
    "Rosa Sakura":     {"principal": "#ff7597", "hover": "#e05275", "paneles": "#1a0f13", "borde": "#3a1d27", "texto_osc": "#ffffff", "brillo": "#fce4ec", "lista_bg": "#0f080b"},
    "Naranja Fuego":   {"principal": "#ff6b4a", "hover": "#d94f30", "paneles": "#140e0c", "borde": "#361f19", "texto_osc": "#000000", "brillo": "#fff3e0", "lista_bg": "#0c0806"},
    "Vaporwave Retro": {"principal": "#9b5de5", "hover": "#f15bb5", "paneles": "#240046", "borde": "#5a189a", "texto_osc": "#ffffff", "brillo": "#00f5d4", "lista_bg": "#140029"},
    "Drácula Vampire": {"principal": "#50fa7b", "hover": "#ff79c6", "paneles": "#282a36", "borde": "#44475a", "texto_osc": "#282a36", "brillo": "#8be9fd", "lista_bg": "#1d1f27"},
    "Toxic Waste":     {"principal": "#aacc00", "hover": "#70e000", "paneles": "#0d1b2a", "borde": "#1b263b", "texto_osc": "#000000", "brillo": "#38b000", "lista_bg": "#09111b"},
    
    # --- Nuevos Pastel Cute ---
    "Algodón de Azúcar":{"principal": "#ffb7eb", "hover": "#f1a7e1", "paneles": "#261d2d", "borde": "#3d2e49", "texto_osc": "#1a131f", "brillo": "#f9fcfc", "lista_bg": "#1f1724"},
    "Menta Crema":     {"principal": "#a3ffeb", "hover": "#87f1da", "paneles": "#1d2d2a", "borde": "#2e4945", "texto_osc": "#131f1d", "brillo": "#fcf9fc", "lista_bg": "#172421"},
    "Boba Tea":        {"principal": "#d9bf9f", "hover": "#c8ac8a", "paneles": "#2d261d", "borde": "#493e2e", "texto_osc": "#1f1a13", "brillo": "#fdfaf7", "lista_bg": "#241f17"},
    "Kawaii Sky":      {"principal": "#d0f4ff", "hover": "#a2e9ff", "paneles": "#1a2226", "borde": "#2a373d", "texto_osc": "#11171a", "brillo": "#f5fcff", "lista_bg": "#151b1f"},
    "Melón Suave":     {"principal": "#ffefc1", "hover": "#ffe1a2", "paneles": "#26231a", "borde": "#3d392a", "texto_osc": "#1e1c14", "brillo": "#fffcfa", "lista_bg": "#1f1c15"},
    
    # --- Sintetizadores y Naturaleza (Bloque 2) ---
    "Synthwave 84":    {"principal": "#f15bb5", "hover": "#fee440", "paneles": "#180029", "borde": "#00f5d4", "texto_osc": "#000000", "brillo": "#00bbf9", "lista_bg": "#11001d"},
    "Deep Ocean":      {"principal": "#0077b6", "hover": "#0096c7", "paneles": "#03045e", "borde": "#023e8a", "texto_osc": "#ffffff", "brillo": "#90e0ef", "lista_bg": "#020336"},
    "Forest Moss":     {"principal": "#52b788", "hover": "#40916c", "paneles": "#1b4332", "borde": "#2d6a4f", "texto_osc": "#ffffff", "brillo": "#b7e4c7", "lista_bg": "#11291f"},
    "Monochrome Dark": {"principal": "#4a4a4a", "hover": "#333333", "paneles": "#121212", "borde": "#222222", "texto_osc": "#ffffff", "brillo": "#888888", "lista_bg": "#090909"},
    "Plum Velvet":     {"principal": "#c77dff", "hover": "#9d4edd", "paneles": "#240046", "borde": "#3c096c", "texto_osc": "#ffffff", "brillo": "#e0aaff", "lista_bg": "#140029"},
    "Electric Purple": {"principal": "#cc00ff", "hover": "#a300cc", "paneles": "#0a0014", "borde": "#1f003d", "texto_osc": "#ffffff", "brillo": "#f0b3ff", "lista_bg": "#06000d"},
    "Nordic Frost":    {"principal": "#88c0d0", "hover": "#81a1c1", "paneles": "#2e3440", "borde": "#4c566a", "texto_osc": "#2e3440", "brillo": "#eceff4", "lista_bg": "#21262f"},
    
    # --- Custom Extremos y Anime (Bloque 3) ---
    "Hatsune Miku":    {"principal": "#00c4b4", "hover": "#00a194", "paneles": "#191e24", "borde": "#2a323c", "texto_osc": "#000000", "brillo": "#7bf1a8", "lista_bg": "#12161b"},
    "Cyber Void":      {"principal": "#ff0055", "hover": "#d90429", "paneles": "#050505", "borde": "#1a1a1a", "texto_osc": "#ffffff", "brillo": "#ff758f", "lista_bg": "#000000"},
    "Electric Dream":  {"principal": "#a3ff00", "hover": "#7fb300", "paneles": "#0d1b11", "borde": "#1b3522", "texto_osc": "#0a130c", "brillo": "#ccff7a", "lista_bg": "#08110b"},
    "Pastel Nightmare":{"principal": "#d1c4e9", "hover": "#ef5350", "paneles": "#211a2d", "borde": "#3c096c", "texto_osc": "#ffffff", "brillo": "#ff9ebb", "lista_bg": "#1a1424"},
    "Goth Lolita":     {"principal": "#ff1744", "hover": "#b2102f", "paneles": "#000000", "borde": "#1a0004", "texto_osc": "#ffffff", "brillo": "#ff7597", "lista_bg": "#000000"},
    "Eva Unit 01":     {"principal": "#70e000", "hover": "#ccff00", "paneles": "#1a0033", "borde": "#00ccff", "texto_osc": "#240046", "brillo": "#ff9e00", "lista_bg": "#0e001c"},
    "Senpai Glow":     {"principal": "#ff9ebb", "hover": "#2ecc71", "paneles": "#1a0d14", "borde": "#3d1f2c", "texto_osc": "#000000", "brillo": "#fce4ec", "lista_bg": "#12090e"},

    # --- Relleno de temas Cute y Variaciones (Completando las 60 opciones exactas) ---
    "Melocotón Soft":   {"principal": "#ffcfb7", "hover": "#ffb08e", "paneles": "#2d2320", "borde": "#4a3a34", "texto_osc": "#211917", "brillo": "#fffcf5", "lista_bg": "#221a18"},
    "Lavanda Dreams":   {"principal": "#e1bee7", "hover": "#ce93d8", "paneles": "#231c26", "borde": "#392e3e", "texto_osc": "#1a151b", "brillo": "#f3e5f5", "lista_bg": "#1a151c"},
    "Limón Meringue":   {"principal": "#fff9c4", "hover": "#fff59d", "paneles": "#26251e", "borde": "#3e3d31", "texto_osc": "#1e1d18", "brillo": "#fffff5", "lista_bg": "#1c1c16"},
    "Fresa Batido":     {"principal": "#ffcdd2", "hover": "#ef9a9a", "paneles": "#261e1f", "borde": "#3e3132", "texto_osc": "#1e1818", "brillo": "#ffebee", "lista_bg": "#1c1617"},
    "Sky Pastel V2":    {"principal": "#b3e5fc", "hover": "#81d4fa", "paneles": "#151d26", "borde": "#22313e", "texto_osc": "#0e141a", "brillo": "#e1f5fe", "lista_bg": "#0e141a"},
    "Uva Soft":         {"principal": "#e1bee7", "hover": "#ba68c8", "paneles": "#231c26", "borde": "#3e096c", "texto_osc": "#ffffff", "brillo": "#f3e5f5", "lista_bg": "#1a151c"},
    "Kiwi Cream":       {"principal": "#dcedc8", "hover": "#c5e1a5", "paneles": "#21231d", "borde": "#36392f", "texto_osc": "#1a1c17", "brillo": "#f1f8e9", "lista_bg": "#181a15"},
    "Caramelo Latte":   {"principal": "#ffccbc", "hover": "#ffab91", "paneles": "#26211e", "borde": "#3e3631", "texto_osc": "#1e1a18", "brillo": "#fbe9e7", "lista_bg": "#1c1816"},
    "Cyan Cute":        {"principal": "#b2ebf2", "hover": "#80deea", "paneles": "#1b2526", "borde": "#2c3c3d", "texto_osc": "#131a1b", "brillo": "#e0f7fa", "lista_bg": "#141b1c"},
    "Orquídea Pastel":   {"principal": "#f8bbd0", "hover": "#f48fb1", "paneles": "#261c1e", "borde": "#3e2d31", "texto_osc": "#1e1618", "brillo": "#fce4ec", "lista_bg": "#1c1516"},
    "Lima Suave V2":     {"principal": "#f0f4c3", "hover": "#e6ee9c", "paneles": "#24241d", "borde": "#3b3b2f", "texto_osc": "#1c1c17", "brillo": "#f9fbe7", "lista_bg": "#1a1a15"},
    "Arándano Soft":    {"principal": "#c5cae9", "hover": "#9fa8da", "paneles": "#1f1f26", "borde": "#32323e", "texto_osc": "#ffffff", "brillo": "#e8eaf6", "lista_bg": "#16161c"},
    "Nube Rosa":        {"principal": "#fce4ec", "hover": "#f8bbd0", "paneles": "#262122", "borde": "#3d3637", "texto_osc": "#1e1a1a", "brillo": "#fff1f5", "lista_bg": "#1f1a1a"},
    "Sol Pastel":        {"principal": "#fffde7", "hover": "#fff9c4", "paneles": "#262622", "borde": "#3e3e37", "texto_osc": "#1e1e1b", "brillo": "#fffff9", "lista_bg": "#1f1f1b"},
    "Mar Pastel":        {"principal": "#e0f2f1", "hover": "#b2dfdb", "paneles": "#212423", "borde": "#363a39", "texto_osc": "#1a1c1c", "brillo": "#f0fdfc", "lista_bg": "#1b1d1d"},
    "Hada Mint":        {"principal": "#e0f2f1", "hover": "#a7ffeb", "paneles": "#212423", "borde": "#00f5d4", "texto_osc": "#1a1c1c", "brillo": "#f0fdfc", "lista_bg": "#1b1d1d"},
    "Unicornio Glow":   {"principal": "#ffccff", "hover": "#9b5de5", "paneles": "#241d2d", "borde": "#f15bb5", "texto_osc": "#ffffff", "brillo": "#f9fcfc", "lista_bg": "#1f1724"},
    "Magia Pastel":     {"principal": "#d1c4e9", "hover": "#f8bbd0", "paneles": "#211a2d", "borde": "#b3e5fc", "texto_osc": "#ffffff", "brillo": "#ede7f6", "lista_bg": "#1a1424"},
    "Kawaii Devil":     {"principal": "#ee5253", "hover": "#ffb7ce", "paneles": "#211a2d", "borde": "#3e096c", "texto_osc": "#ffffff", "brillo": "#ffccff", "lista_bg": "#1a1424"},
    "Brisa Cute":       {"principal": "#b3e5fc", "hover": "#a3f7bf", "paneles": "#151d26", "borde": "#52b788", "texto_osc": "#0e141a", "brillo": "#dad7cd", "lista_bg": "#0e141a"},
    "Dulce Mochi":      {"principal": "#d9bf9f", "hover": "#ffccd5", "paneles": "#2d261d", "borde": "#c77dff", "texto_osc": "#1f1a13", "brillo": "#ede0d4", "lista_bg": "#241f17"},
    "Rocío Pastel":      {"principal": "#b2ebf2", "hover": "#dcedc8", "paneles": "#1b2526", "borde": "#dad7cd", "texto_osc": "#131a1b", "brillo": "#dad7cd", "lista_bg": "#141b1c"},
    "Gomita Soft":      {"principal": "#b39ddb", "hover": "#f48fb1", "paneles": "#1f1929", "borde": "#c77dff", "texto_osc": "#ffffff", "brillo": "#ede7f6", "lista_bg": "#171221"},
    "Cute Alien":       {"principal": "#80deea", "hover": "#f0f4c3", "paneles": "#121d22", "borde": "#aacc00", "texto_osc": "#0e161a", "brillo": "#b3fff7", "lista_bg": "#0f161b"},
    "Arcoíris Soft":     {"principal": "#ffccd5", "hover": "#d0f4ff", "paneles": "#262021", "borde": "#dad7cd", "texto_osc": "#1e1a1a", "brillo": "#dad7cd", "lista_bg": "#1c1819"},
    "Estrella Cute":     {"principal": "#fff9c4", "hover": "#dcedc8", "paneles": "#26251e", "borde": "#ffb703", "texto_osc": "#1e1d18", "brillo": "#dad7cd", "lista_bg": "#1c1c16"},
    "Neon Cute V2":     {"principal": "#70e000", "hover": "#f15bb5", "paneles": "#0d1b2a", "borde": "#dad7cd", "texto_osc": "#000000", "brillo": "#dad7cd", "lista_bg": "#09111b"},
    "Sirena Pastel V2": {"principal": "#90e0ef", "hover": "#e1bee7", "paneles": "#122529", "borde": "#3c096c", "texto_osc": "#112226", "brillo": "#90e0ef", "lista_bg": "#0e1e21"}
}

class LechePlayer(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("LechePlayer")
        self.geometry("1200x850")
        self.minsize(1050, 750)

        mixer.init()

        # Configuración persistente
        self.config_data = self.cargar_configuracion()
        self.carpeta_musica = self.config_data.get("carpeta", "descargas")
        self.carpeta_fondos = "fondos_guardados"
        self.bg_ruta = self.config_data.get("bg_imagen", "")
        self.bg_oscuridad = self.config_data.get("bg_oscuridad", 0.5)
        self.modulo_actual = self.config_data.get("modulo_centro", "disco")
        self.nombre_tema_actual = self.config_data.get("tema_color", "Chocola Pastel")
        self.escala_widget = self.config_data.get("escala_widget", "mediano") 
        
        if self.nombre_tema_actual not in TEMAS_COLOR:
            self.nombre_tema_actual = "Chocola Pastel"
        self.tema = TEMAS_COLOR[self.nombre_tema_actual]

        self.menu_visible = True

        if not os.path.exists(self.carpeta_musica): os.makedirs(self.carpeta_musica)
        if not os.path.exists(self.carpeta_fondos): os.makedirs(self.carpeta_fondos)

        # Variables de control multimedia
        self.playlist = []
        self.indice_actual = 0
        self.modo_aleatorio = False
        self.reproduciendo = False
        self.pausado = False 
        self.cargando_pista = False 
        self.angulo_rotacion = 0
        self.bloquear_slider = False
        self._reproduccion_job = None
        self.tiempo_reproduccion = 0
        self.ultimo_tiempo_sistema = time.time()

        # Motor de GIFs
        self.gif_frames = []
        self.gif_delays = []       
        self.gif_indice = 0
        self.gif_ultimo_cambio = time.time()

        # Parámetros avanzados de física visual
        self.nodo_geometria = 4       
        self.fase_onda = 0.0 
        self.radio_radar = 10.0
        self.particulas_3d = [{"x": random.uniform(-1, 1), "y": random.uniform(-1, 1), "z": random.uniform(-1, 1)} for _ in range(50)]
        self.matriz_flujo = [random.uniform(0, math.pi*2) for _ in range(20)]
        self.historico_espectro = [[2]*32 for _ in range(10)]

        # Espectro de Audio
        self.barras_espectro = []
        self.alturas_actuales = [2] * 36
        self.alturas_objetivo = [2] * 36
        self.particulas_geom = [{"ang": random.uniform(0, 2*math.pi), "rad": random.randint(40, 110), "vel": random.uniform(0.01, 0.03)} for _ in range(25)]

        self.miniaturas_cache = {}
        self.img_fondo_procesada = None

        # UI de Ajustes Dinámicos
        self.dict_botones_opt = {}

        self.setup_ui()
        self.update_idletasks()
        self.aplicar_fondo()

        self.actualizar_lista_archivos()
        self.actualizar_estado_reproduccion()
        
        # Iniciar loops de pintado y espectro
        self.animar_espectro_fluido()
        self.bucle_renderizado_central()

        self.bind("<Configure>", self.on_resize)

    def cargar_configuracion(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f: return json.load(f)
            except: pass
        return {"carpeta": "descargas", "bg_imagen": "", "bg_oscuridad": 0.5, "modulo_centro": "disco", "tema_color": "Chocola Pastel", "escala_widget": "mediano"}

    def guardar_configuracion(self):
        self.config_data["carpeta"] = self.carpeta_musica
        self.config_data["bg_imagen"] = self.bg_ruta
        self.config_data["bg_oscuridad"] = self.bg_oscuridad
        self.config_data["modulo_centro"] = self.modulo_actual
        self.config_data["tema_color"] = self.nombre_tema_actual
        self.config_data["escala_widget"] = self.escala_widget
        try:
            with open(CONFIG_FILE, "w") as f: json.dump(self.config_data, f)
        except: pass

    def setup_ui(self):
        self.bg_canvas = tk.Canvas(self, highlightthickness=0, bd=0, bg="#0d0e12")
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # --- PANEL IZQUIERDO DE NAVEGACIÓN ---
        self.left_panel = ctk.CTkFrame(self.bg_canvas, fg_color=self.tema["paneles"], corner_radius=16, border_width=1, border_color=self.tema["borde"])
        
        self.lbl_titulo_marca = ctk.CTkLabel(self.left_panel, text="LECHE PLAYER", font=("Segoe UI", 18, "bold"), text_color=self.tema["principal"])
        self.lbl_titulo_marca.pack(pady=(60, 12)) 

        self.entry_url = ctk.CTkEntry(self.left_panel, placeholder_text="Enlace de YouTube...", width=220, fg_color="#13151a")
        self.entry_url.pack(pady=4)
        
        self.btn_download = ctk.CTkButton(self.left_panel, text="Descargar", fg_color=self.tema["principal"], text_color=self.tema["texto_osc"], hover_color=self.tema["hover"], font=("Segoe UI", 12, "bold"), command=self.start_download)
        self.btn_download.pack(pady=4)

        # Contenedor de la lista de canciones reactivo al color del tema
        self.scroll_playlist = ctk.CTkScrollableFrame(self.left_panel, fg_color=self.tema["lista_bg"], corner_radius=10)
        self.scroll_playlist.pack(pady=8, padx=10, fill="both", expand=True)

        self.frame_modos = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        self.frame_modos.pack(pady=4)

        self.btn_orden = ctk.CTkButton(self.frame_modos, text="En Orden", width=95, height=32, font=("Segoe UI", 11, "bold"), fg_color=self.tema["principal"], text_color=self.tema["texto_osc"], hover_color=self.tema["hover"], command=lambda: self.set_modo(False))
        self.btn_orden.pack(side="left", padx=4)

        self.btn_shuffle = ctk.CTkButton(self.frame_modos, text="Aleatorio", width=95, height=32, font=("Segoe UI", 11), fg_color="#1c2029", hover_color="#282e3d", text_color="white", command=lambda: self.set_modo(True))
        self.btn_shuffle.pack(side="left", padx=4)

        self.btn_config = ctk.CTkButton(self.left_panel, text="⚙️ Configuración", fg_color="#1c2029", height=38, hover_color="#252b38", command=self.abrir_configuracion)
        self.btn_config.pack(pady=12, padx=15, fill="x")

        self.win_left = self.bg_canvas.create_window(15, 15, anchor="nw", window=self.left_panel)

        # --- CANVAS VISUALIZADOR CENTRAL ---
        self.canvas_visual_centro = tk.Canvas(self.bg_canvas, width=450, height=450, highlightthickness=0, bd=0, bg="#111216")
        self.win_visual_centro = self.bg_canvas.create_window(0, 0, anchor="center", window=self.canvas_visual_centro)

        # --- DOCK DE CONTROL INFERIOR ---
        self.bottom_dock = ctk.CTkFrame(self.bg_canvas, fg_color=self.tema["paneles"], corner_radius=20, border_width=1, border_color=self.tema["borde"])
        
        self.frame_dock_izq = ctk.CTkFrame(self.bottom_dock, fg_color="transparent")
        self.frame_dock_izq.pack(side="left", fill="both", expand=True, padx=20, pady=10)
        
        self.lbl_info = ctk.CTkLabel(self.frame_dock_izq, text="Ninguna pista en reproducción", font=("Segoe UI", 15, "bold"), text_color="white", anchor="w")
        self.lbl_info.pack(fill="x", pady=(2, 2))
        
        self.canvas_espectro = tk.Canvas(self.frame_dock_izq, width=380, height=35, bg=self.tema["paneles"], highlightthickness=0)
        self.canvas_espectro.pack(anchor="w")
        self.crear_barras_iniciales()

        self.frame_dock_der = ctk.CTkFrame(self.bottom_dock, fg_color="transparent")
        self.frame_dock_der.pack(side="right", fill="both", expand=True, padx=20, pady=10)

        self.frame_linea_tiempo = ctk.CTkFrame(self.frame_dock_der, fg_color="transparent")
        self.frame_linea_tiempo.pack(fill="x", pady=2)

        self.lbl_tiempo_actual = ctk.CTkLabel(self.frame_linea_tiempo, text="00:00", font=("Consolas", 11), text_color="#a0a5b5")
        self.lbl_tiempo_actual.pack(side="left", padx=5)

        self.slider_musica = ctk.CTkSlider(self.frame_linea_tiempo, from_=0, to=100, command=self.mover_tiempo, progress_color=self.tema["principal"], button_color=self.tema["principal"])
        self.slider_musica.pack(side="left", fill="x", expand=True, padx=5)
        self.slider_musica.bind("<ButtonPress-1>", self.on_slider_press)
        self.slider_musica.bind("<ButtonRelease-1>", self.on_slider_release)

        self.lbl_tiempo_total = ctk.CTkLabel(self.frame_linea_tiempo, text="00:00", font=("Consolas", 11), text_color="#a0a5b5")
        self.lbl_tiempo_total.pack(side="right", padx=5)

        self.frame_controles_wrapper = ctk.CTkFrame(self.frame_dock_der, fg_color="transparent")
        self.frame_controles_wrapper.pack(pady=2)

        self.frame_controles = ctk.CTkFrame(self.frame_controles_wrapper, fg_color="transparent")
        self.frame_controles.pack()

        self.btn_prev = ctk.CTkButton(self.frame_controles, text="⏮", width=40, height=36, fg_color="#1c2029", text_color="white", command=self.anterior_cancion)
        self.btn_prev.pack(side="left", padx=8)

        self.btn_play = ctk.CTkButton(self.frame_controles, text="▶", width=50, height=40, corner_radius=10, font=("Arial", 16), fg_color=self.tema["principal"], hover_color=self.tema["hover"], text_color=self.tema["texto_osc"], command=self.toggle_reproduccion)
        self.btn_play.pack(side="left", padx=8)

        self.btn_next = ctk.CTkButton(self.frame_controles, text="⏭", width=40, height=36, fg_color="#1c2029", text_color="white", command=self.siguiente_cancion)
        self.btn_next.pack(side="left", padx=8)

        self.win_bottom_dock = self.bg_canvas.create_window(0, 0, anchor="s", window=self.bottom_dock)

        self.btn_hamburger = tk.Button(
            self.bg_canvas, text="☰", font=("Segoe UI", 12, "bold"),
            bg=self.tema["paneles"], fg=self.tema["principal"],
            activebackground=self.tema["hover"], activeforeground=self.tema["texto_osc"],
            bd=1, relief="solid", highlightthickness=0, width=4, height=1,
            command=self.toggle_menu_lateral
        )
        self.win_hamburger = self.bg_canvas.create_window(25, 25, anchor="nw", window=self.btn_hamburger)

    def toggle_menu_lateral(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.bg_canvas.itemconfig(self.win_left, state="normal")
            self.btn_hamburger.configure(text="☰")
        else:
            self.bg_canvas.itemconfig(self.win_left, state="hidden")
            self.btn_hamburger.configure(text="▶")
        
        self.mapear_posiciones_canvas()
        self.aplicar_fondo()
        self.bg_canvas.tag_raise(self.win_hamburger)

    def mapear_posiciones_canvas(self):
        ancho = self.winfo_width()
        alto = self.winfo_height()
        if ancho < 100 or alto < 100: return

        ancho_izq_ocupado = 260 if self.menu_visible else 0

        if self.menu_visible:
            alto_izq = alto - 30
            self.left_panel.configure(width=ancho_izq_ocupado, height=alto_izq)
            self.bg_canvas.itemconfig(self.win_left, width=ancho_izq_ocupado, height=alto_izq)
            self.bg_canvas.coords(self.win_left, 15, 15)

        espacio_libre_x = ancho - (ancho_izq_ocupado + 30 if self.menu_visible else 30)
        centro_x_dinamico = (ancho_izq_ocupado + 15 if self.menu_visible else 15) + (espacio_libre_x // 2)

        self.bottom_dock.configure(width=espacio_libre_x, height=115)
        self.bg_canvas.itemconfig(self.win_bottom_dock, width=espacio_libre_x, height=115)
        self.bg_canvas.coords(self.win_bottom_dock, centro_x_dinamico, alto - 15)

        centro_y_dinamico = 15 + ((alto - 130 - 30) // 2)
        self.bg_canvas.coords(self.win_visual_centro, centro_x_dinamico, centro_y_dinamico)
        self.bg_canvas.coords(self.win_hamburger, 25, 25)

    def cambiar_tema_sistema(self, nombre_nuevo):
        self.nombre_tema_actual = nombre_nuevo
        self.tema = TEMAS_COLOR[nombre_nuevo]
        
        self.left_panel.configure(fg_color=self.tema["paneles"], border_color=self.tema["borde"])
        self.bottom_dock.configure(fg_color=self.tema["paneles"], border_color=self.tema["borde"])
        self.scroll_playlist.configure(fg_color=self.tema["lista_bg"])
        self.canvas_espectro.configure(bg=self.tema["paneles"])
        self.btn_hamburger.configure(bg=self.tema["paneles"], fg=self.tema["principal"], activebackground=self.tema["hover"], activeforeground=self.tema["texto_osc"])
        self.lbl_titulo_marca.configure(text_color=self.tema["principal"])
        self.btn_download.configure(fg_color=self.tema["principal"], hover_color=self.tema["hover"], text_color=self.tema["texto_osc"])
        self.slider_musica.configure(progress_color=self.tema["principal"], button_color=self.tema["principal"])
        self.btn_play.configure(fg_color=self.tema["principal"], hover_color=self.tema["hover"], text_color=self.tema["texto_osc"])
        
        if not self.modo_aleatorio:
            self.btn_orden.configure(fg_color=self.tema["principal"], hover_color=self.tema["hover"], text_color=self.tema["texto_osc"])
        else:
            self.btn_shuffle.configure(fg_color=self.tema["principal"], hover_color=self.tema["hover"], text_color=self.tema["texto_osc"])
            
        self.actualizar_lista_archivos() # Forzar repintado de las canciones con su nuevo color reactivo
        self.guardar_configuracion()

    def abrir_configuracion(self):
        self.ventana_conf = ctk.CTkToplevel(self)
        self.ventana_conf.title("Ajustes Avanzados de Sistema")
        self.ventana_conf.geometry("980x680")
        self.ventana_conf.transient(self)

        contenedor = ctk.CTkFrame(self.ventana_conf)
        contenedor.pack(fill="both", expand=True, padx=15, pady=15)

        sidebar = ctk.CTkFrame(contenedor, width=210, fg_color=self.tema["paneles"])
        sidebar.pack(side="left", fill="y", padx=(0, 10))

        ctk.CTkLabel(sidebar, text="Menú", font=("Segoe UI", 18, "bold"), text_color=self.tema["principal"]).pack(pady=20)

        self.frame_config_dinamico = ctk.CTkFrame(contenedor, fg_color="transparent")
        self.frame_config_dinamico.pack(side="right", fill="both", expand=True)

        self.btn_tab_personalizar = ctk.CTkButton(sidebar, text="🎨 Personalización & Temas", height=40, fg_color="#1c2029", command=self.mostrar_tab_personalizacion)
        self.btn_tab_personalizar.pack(fill="x", padx=10, pady=5)

        self.btn_tab_widgets = ctk.CTkButton(sidebar, text="🔷 Galería de Widgets", height=40, fg_color="#1c2029", command=self.mostrar_tab_widgets)
        self.btn_tab_widgets.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(sidebar, text="Guardar Cambios", height=40, fg_color=self.tema["principal"], text_color=self.tema["texto_osc"], hover_color=self.tema["hover"], font=("Segoe UI", 12, "bold"), command=self.ventana_conf.destroy).pack(fill="x", padx=10, pady=20, side="bottom")
        
        self.mostrar_tab_personalizacion()

    def limpiar_tab(self):
        for widget in self.frame_config_dinamico.winfo_children(): 
            widget.destroy()
        self.dict_botones_opt.clear()

    def mostrar_tab_personalizacion(self):
        self.limpiar_tab()
        try: self.btn_tab_personalizar.configure(fg_color=self.tema["principal"], text_color=self.tema["texto_osc"])
        except: pass
        try: self.btn_tab_widgets.configure(fg_color="#1c2029", text_color="white")
        except: pass
        
        ctk.CTkLabel(self.frame_config_dinamico, text="Fondo de Pantalla Principal", font=("Segoe UI", 16, "bold")).pack(pady=(5, 5), anchor="w", padx=15)
        self.scroll_galeria = ctk.CTkScrollableFrame(self.frame_config_dinamico, orientation="horizontal", height=130)
        self.scroll_galeria.pack(fill="x", padx=15, pady=5)
        self.cargar_galeria_imagenes()
        
        ctk.CTkLabel(self.frame_config_dinamico, text="Filtro Opacidad del Wallpaper", font=("Segoe UI", 13, "bold")).pack(pady=(10, 2), anchor="w", padx=15)
        slider_osc = ctk.CTkSlider(self.frame_config_dinamico, from_=0, to=1, command=self.cambiar_oscuridad, progress_color=self.tema["principal"], button_color=self.tema["principal"])
        slider_osc.set(self.bg_oscuridad)
        slider_osc.pack(fill="x", padx=15, pady=5)
        
        # CAMBIO AQUÍ: Galería de 60 temas Cute / Pastel / Anime
        ctk.CTkLabel(self.frame_config_dinamico, text="Selección de Personaje / Estilo", font=("Segoe UI", 15, "bold")).pack(pady=(15, 5), anchor="w", padx=15)
        frame_grid_scroll = ctk.CTkScrollableFrame(self.frame_config_dinamico, height=230, fg_color="#13151a")
        frame_grid_scroll.pack(fill="both", expand=True, padx=15, pady=5)

        fila_frame = None
        for idx, (nombre_color, paleta) in enumerate(TEMAS_COLOR.items()):
            if idx % 3 == 0:
                fila_frame = ctk.CTkFrame(frame_grid_scroll, fg_color="transparent")
                fila_frame.pack(fill="x", pady=4)
            
            btn_color_item = ctk.CTkButton(
                fila_frame, 
                text=nombre_color, 
                fg_color=paleta["principal"], 
                text_color=paleta["texto_osc"], 
                hover_color=paleta["hover"],
                width=190,
                height=40,
                font=("Segoe UI", 11, "bold" if nombre_color == self.nombre_tema_actual else "normal"),
                border_width=2 if nombre_color == self.nombre_tema_actual else 1,
                border_color="white" if nombre_color == self.nombre_tema_actual else paleta["borde"],
                command=lambda n=nombre_color: [self.cambiar_tema_sistema(n), self.mostrar_tab_personalizacion()]
            )
            btn_color_item.pack(side="left", padx=6, expand=True, fill="x")

    def cargar_galeria_imagenes(self):
        for w in self.scroll_galeria.winfo_children(): w.destroy()
        self.miniaturas_cache.clear()

        btn_agregar = ctk.CTkButton(self.scroll_galeria, text="Agregar imagen\n+", width=120, height=85, fg_color="#13151a", border_width=1, border_color=self.tema["principal"], command=self.agregar_nueva_imagen)
        btn_agregar.pack(side="left", padx=8, pady=5)

        if os.path.exists(self.carpeta_fondos):
            for archivo in os.listdir(self.carpeta_fondos):
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    ruta_completa = os.path.join(self.carpeta_fondos, archivo)
                    try:
                        img_raw = Image.open(ruta_completa)
                        img_raw.thumbnail((120, 80), Image.Resampling.LANCZOS)
                        img_tk = ImageTk.PhotoImage(img_raw)
                        self.miniaturas_cache[archivo] = img_tk
                        frame_item = ctk.CTkFrame(self.scroll_galeria, fg_color="transparent")
                        frame_item.pack(side="left", padx=8)
                        tk.Button(frame_item, image=img_tk, bd=0, bg="#0d0e12", activebackground=self.tema["principal"], cursor="hand2", command=lambda r=ruta_completa: self.aplicar_fondo_desde_galeria(r)).pack()
                    except: pass

    def agregar_nueva_imagen(self):
        ruta = self.selector_nativo("Seleccionar Imagen", es_carpeta=False)
        if ruta:
            nueva_ruta = os.path.join(self.carpeta_fondos, os.path.basename(ruta))
            shutil.copy(ruta, nueva_ruta)
            self.aplicar_fondo_desde_galeria(nueva_ruta)

    def aplicar_fondo_desde_galeria(self, ruta):
        self.bg_ruta = ruta
        self.aplicar_fondo()
        self.guardar_configuracion()
        self.cargar_galeria_imagenes()

    def mostrar_tab_widgets(self):
        self.limpiar_tab()
        try: self.btn_tab_widgets.configure(fg_color=self.tema["principal"], text_color=self.tema["texto_osc"])
        except: pass
        try: self.btn_tab_personalizar.configure(fg_color="#1c2029", text_color="white")
        except: pass

        ctk.CTkLabel(self.frame_config_dinamico, text="Escala de Tamaño del Widget Central", font=("Segoe UI", 15, "bold")).pack(pady=(5, 4))
        frame_tamanos = ctk.CTkFrame(self.frame_config_dinamico, fg_color="#13151a", height=50)
        frame_tamanos.pack(fill="x", padx=20, pady=(0, 10))

        for sz in ["pequeño", "mediano", "grande"]:
            btn_sz = ctk.CTkButton(
                frame_tamanos, 
                text=sz.upper(), 
                width=140,
                height=34,
                fg_color=self.tema["principal"] if self.escala_widget == sz else "#1c2029",
                text_color=self.tema["texto_osc"] if self.escala_widget == sz else "white",
                font=("Segoe UI", 11, "bold" if self.escala_widget == sz else "normal"),
                command=lambda s=sz: self.cambiar_escala_widget(s)
            )
            btn_sz.pack(side="left", padx=15, expand=True, pady=6)

        ctk.CTkLabel(self.frame_config_dinamico, text="Estilo Visual del Elemento Central", font=("Segoe UI", 15, "bold")).pack(pady=4)
        frame_opciones = ctk.CTkScrollableFrame(self.frame_config_dinamico, fg_color="transparent", height=340)
        frame_opciones.pack(fill="both", expand=True, padx=20)

        lista_widgets = [
            ("disco", "DJ 💿 Vinilo Clásico + Espectro Radial"),
            ("geometria", "CYBER 🔷 Constelación de Nodos Cuántica"),
            ("ondas", "WAVE 🌊 Ondas Fluidas Sinusoidales Inteligentes"),
            ("matriz", "CUBOS 📊 Espectro Isométrico 3D (Matriz)"),
            ("radar", "SONAR 📡 Radar de Pulsos de Frecuencia"),
            ("tunel", "RETRO 🌀 Túnel de Perspectiva Espacial"),
            ("dna", "BIO 🧬 Hélice de Partículas de ADN Reactiva"),
            ("tesseract", "CORE 🕋 Cubo Hyper-Espacial 4D Proyectado"),
            ("particulas", "STARS ✨ Campo de Estrellas Estereoscópico 3D"),
            ("osciloscopio", "BEAT ⚡ Osciloscopio Vectorial de Alta Frecuencia"),
            ("anillos", "ORBIT ⭕ Anillos Orbitales Concéntricos"),
            ("flujo", "FLOW 🌪️ Campo de Vector de Flujo Líquido"),
            ("liquido", "BLOB 🧪 Gota Líquida de Plasma Orgánica"),
            ("caleidoscopio", "KALEIDO 💮 Espejo Caleidoscópico de Frecuencias"),
            ("particulas_vortex", "VORTEX 🌀 Remolino de Polvo Estelar Cuántico"),
            ("gif", "ANIME 🎞️ Loop GIF Animado Reactivo (Sincronizado)"),
            ("ninguno", "❌ Ocultar Elementos Centrales")
        ]

        for clave, texto in lista_widgets:
            btn = ctk.CTkButton(
                frame_opciones, 
                text=texto, 
                height=38,
                anchor="w",
                font=("Segoe UI", 12),
                command=lambda k=clave: self.seleccionar_widget_modulo(k)
            )
            btn.pack(fill="x", pady=2)
            self.dict_botones_opt[clave] = btn

        self.refrescar_estilo_opciones_widgets()

    def cambiar_escala_widget(self, nuevo_tamano):
        self.escala_widget = nuevo_tamano
        self.guardar_configuracion()
        self.mostrar_tab_widgets()

    def seleccionar_widget_modulo(self, modo):
        self.modulo_actual = modo
        if modo == "geometria":
            self.nodo_geometria = 4 if self.nodo_geometria == 3 else 6 if self.nodo_geometria == 4 else 3
        elif modo == "gif":
            self.importar_gif_central()
        
        self.guardar_configuracion()
        self.refrescar_estilo_opciones_widgets()

    def refrescar_estilo_opciones_widgets(self):
        for clave, btn in self.dict_botones_opt.items():
            try:
                if btn.winfo_exists():
                    if clave == self.modulo_actual:
                        if clave == "ninguno":
                            btn.configure(fg_color="#e74c3c", text_color="white", font=("Segoe UI", 12, "bold"))
                        else:
                            btn.configure(fg_color=self.tema["principal"], text_color=self.tema["texto_osc"], font=("Segoe UI", 12, "bold"))
                    else:
                        btn.configure(fg_color="#1c2029", text_color="white", font=("Segoe UI", 12, "normal"))
            except: pass

    # =========================================================
    # CORE DE RENDERIZADO CENTRAL DE ALTA PRECISIÓN
    # =========================================================
    def bucle_renderizado_central(self):
        try:
            amplitud_promedio = sum(self.alturas_actuales) / len(self.alturas_actuales) if self.alturas_actuales else 2
            
            if self.reproduciendo and not self.pausado:
                self.angulo_rotacion += 2.0
                self.fase_onda += 0.18
                self.radio_radar += 3.0 + (amplitud_promedio * 0.3)
                if self.radio_radar > 160: self.radio_radar = 10.0
                
                self.historico_espectro.pop(0)
                self.historico_espectro.append(list(self.alturas_actuales))
            else:
                self.angulo_rotacion += 0.2

            tamano_canvas = 450
            cx, cy = tamano_canvas // 2, tamano_canvas // 2

            mult_escala = 1.0 if self.escala_widget == "pequeño" else 1.35 if self.escala_widget == "mediano" else 1.85

            if self.img_fondo_procesada is not None:
                try:
                    coords = self.bg_canvas.coords(self.win_visual_centro)
                    if coords:
                        bx, by = int(coords[0] - cx), int(coords[1] - cy)
                        img_canvas = self.img_fondo_procesada.crop((bx, by, bx + tamano_canvas, by + tamano_canvas)).convert("RGBA")
                    else: img_canvas = Image.new("RGBA", (tamano_canvas, tamano_canvas), (15, 16, 22, 255))
                except: img_canvas = Image.new("RGBA", (tamano_canvas, tamano_canvas), (15, 16, 22, 255))
            else:
                img_canvas = Image.new("RGBA", (tamano_canvas, tamano_canvas), (15, 16, 22, 255))

            draw = ImageDraw.Draw(img_canvas)

            rgb_color = tuple(int(self.tema["principal"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (255,)
            rgb_brillo = tuple(int(self.tema["brillo"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (255,)

            # --- WIDGET 1: DISCO DE VINILO ---
            if self.modulo_actual == "disco":
                num_barras_circ = 36
                radio_espectro_base = 105 * mult_escala
                
                for i in range(num_barras_circ):
                    angulo_rad = math.radians((i * (360 / num_barras_circ)) + self.angulo_rotacion)
                    h_barra = (self.alturas_actuales[i % len(self.alturas_actuales)] * 1.8) * mult_escala
                    
                    x_ini = cx + radio_espectro_base * math.cos(angulo_rad)
                    y_ini = cy + radio_espectro_base * math.sin(angulo_rad)
                    x_fin = cx + (radio_espectro_base + h_barra) * math.cos(angulo_rad)
                    y_fin = cy + (radio_espectro_base + h_barra) * math.sin(angulo_rad)
                    draw.line((x_ini, y_ini, x_fin, y_fin), fill=rgb_color if h_barra < (20 * mult_escala) else rgb_brillo, width=3)

                vinilo_capa = Image.new("RGBA", (tamano_canvas, tamano_canvas), (0, 0, 0, 0))
                v_draw = ImageDraw.Draw(vinilo_capa)
                rad_v = 90 * mult_escala
                v_draw.ellipse((cx-rad_v, cy-rad_v, cx+rad_v, cy+rad_v), fill=(12, 13, 17, 250), outline=(50, 55, 70, 255), width=2)
                
                for r in range(int(20*mult_escala), int(85*mult_escala), max(1, int(8*mult_escala))): 
                    v_draw.ellipse((cx-r, cy-r, cx+r, cy+r), outline=(32, 35, 45, 150), width=1)
                
                radio_centro = int((28 + (amplitud_promedio * 0.6)) * mult_escala)
                v_draw.ellipse((cx-radio_centro, cy-radio_centro, cx+radio_centro, cy+radio_centro), fill=rgb_color)
                v_draw.ellipse((cx-4, cy-4, cx+4, cy+4), fill=(5, 6, 8, 255))
                
                vinilo_rotado = vinilo_capa.rotate(self.angulo_rotacion, resample=Image.BICUBIC, center=(cx, cy))
                img_canvas = Image.alpha_composite(img_canvas, vinilo_rotado)

            # --- WIDGET 2: CONSTELACIÓN DE NODOS ---
            elif self.modulo_actual == "geometria":
                radio_dinamico = (65 + (amplitud_promedio * 1.8)) * mult_escala
                puntos_core = []
                rad_rot = math.radians(self.angulo_rotacion)
                for i in range(self.nodo_geometria):
                    angulo = rad_rot + (2 * math.pi * i / self.nodo_geometria)
                    puntos_core.append((cx + radio_dinamico * math.cos(angulo), cy + radio_dinamico * math.sin(angulo)))
                draw.polygon(puntos_core, outline=rgb_color, width=3)
                for p in self.particulas_geom:
                    if self.reproduciendo and not self.pausado: p["ang"] += p["vel"]
                    dist = (p["rad"] + (amplitud_promedio * 0.8)) * mult_escala
                    x_part, y_part = cx + dist * math.cos(p["ang"]), cy + dist * math.sin(p["ang"])
                    for pt in puntos_core:
                        if math.hypot(x_part - pt[0], y_part - pt[1]) < (95 * mult_escala):
                            draw.line((x_part, y_part, pt[0], pt[1]), fill=rgb_color[:3]+(70,), width=1)
                    draw.ellipse((x_part-3, y_part-3, x_part+3, y_part+3), fill=rgb_brillo)

            # --- WIDGET 3: ONDAS SINUSOIDALES ---
            elif self.modulo_actual == "ondas":
                num_puntos = 60
                paso_x = tamano_canvas / num_puntos
                for capa, opacidad, desfase, mult_amp in [(1, 240, 0.0, 1.8), (2, 140, 2.1, 1.2), (3, 80, 4.2, 0.6)]:
                    puntos_onda = []
                    for i in range(num_puntos + 1):
                        x = i * paso_x
                        atenuacion = math.sin(math.pi * (x / tamano_canvas))
                        amp = ((amplitud_promedio * mult_amp + 4) * atenuacion) * mult_escala
                        y = cy + math.sin(self.fase_onda + (i * 0.2) + desfase) * amp
                        puntos_onda.append((x, y))
                    for i in range(len(puntos_onda) - 1):
                        draw.line((puntos_onda[i], puntos_onda[i+1]), fill=rgb_color[:3]+(opacidad,), width=3 if capa==1 else 2)

            # --- WIDGET 4: ESPECTRO ISOMÉTRICO ---
            elif self.modulo_actual == "matriz":
                num_bloques = 12
                ancho_barra = int(16 * mult_escala)
                salto_barra = int(24 * mult_escala)
                offset_inicial_x = cx - ((num_bloques * salto_barra) // 2)
                for i in range(num_bloques):
                    h_cruda = self.alturas_actuales[(i * 2) % len(self.alturas_actuales)]
                    columnas_activas = int((h_cruda / 32) * 8) + 1
                    x_pos = offset_inicial_x + i * salto_barra
                    for j in range(columnas_activas):
                        y_pos = cy + int(80*mult_escala) - (j * int(18*mult_escala))
                        draw.rectangle((x_pos, y_pos, x_pos + ancho_barra, y_pos + int(12*mult_escala)), fill=rgb_color[:3]+(190,), outline=(10,11,15,255))

            # --- WIDGET 5: RADAR DE FRECUENCIA ---
            elif self.modulo_actual == "radar":
                limite_r = 160 * mult_escala
                opac_radar = max(0, min(255, int(255 * (1.0 - (self.radio_radar / limite_r)))))
                r_radar_actual = self.radio_radar if self.radio_radar < limite_r else 10.0
                draw.ellipse((cx - r_radar_actual, cy - r_radar_actual, cx + r_radar_actual, cy + r_radar_actual), outline=rgb_color[:3]+(opac_radar,), width=2)
                for r_fijo, mult in [(40, 0.4), (80, 0.8), (120, 1.2)]:
                    r_din = (r_fijo + (amplitud_promedio * mult)) * mult_escala
                    draw.ellipse((cx - r_din, cy - r_din, cx + r_din, cy + r_din), outline=rgb_brillo[:3]+(90,), width=1)
                rad_radar = math.radians(self.angulo_rotacion * 2)
                draw.line((cx, cy, cx + (140 * mult_escala) * math.cos(rad_radar), cy + (140 * mult_escala) * math.sin(rad_radar)), fill=rgb_color[:3]+(160,), width=2)

            # --- WIDGET 6: TÚNEL DE PERSPECTIVA ---
            elif self.modulo_actual == "tunel":
                for c in range(6):
                    factor_persp = (c + 1) / 6
                    radio_anillo = (140 * factor_persp + (amplitud_promedio * 0.5 * factor_persp)) * mult_escala
                    draw.ellipse((cx - radio_anillo, cy - radio_anillo, cx + radio_anillo, cy + radio_anillo), outline=rgb_color[:3]+(40 + c*30,), width=1)
                    for i, ang_fijo in enumerate([0, 45, 90, 135, 180, 225, 270, 315]):
                        rad = math.radians(ang_fijo + (self.angulo_rotacion * 0.1))
                        h_barra = (self.alturas_actuales[i % len(self.alturas_actuales)] * 0.9 * factor_persp) * mult_escala
                        draw.line((cx + radio_anillo * math.cos(rad), cy + radio_anillo * math.sin(rad), cx + (radio_anillo + h_barra) * math.cos(rad), cy + (radio_anillo + h_barra) * math.sin(rad)), fill=rgb_brillo if c % 2 == 0 else rgb_color, width=2)

            # --- WIDGET 7: HÉLICE BIO-REACTIVA ADN ---
            elif self.modulo_actual == "dna":
                num_nodos_dna = 16
                ancho_hube = 260 * mult_escala
                for i in range(num_nodos_dna):
                    fase_nodo = (i * (math.pi * 2 / num_nodos_dna)) + (self.angulo_rotacion * 0.04)
                    x_offset = (i * (ancho_hube / num_nodos_dna)) - (ancho_hube / 2)
                    amp_dinamica = (40 + (self.alturas_actuales[i % len(self.alturas_actuales)] * 1.2)) * mult_escala
                    y1 = math.sin(fase_nodo) * amp_dinamica
                    y2 = math.sin(fase_nodo + math.pi) * amp_dinamica
                    draw.line((cx + x_offset, cy + y1, cx + x_offset, cy + y2), fill=rgb_color[:3]+(90,), width=2)
                    draw.ellipse((cx + x_offset - 4, cy + y1 - 4, cx + x_offset + 4, cy + y1 + 4), fill=rgb_brillo)
                    draw.ellipse((cx + x_offset - 4, cy + y2 - 4, cx + x_offset + 4, cy + y2 + 4), fill=rgb_color)

            # --- WIDGET 8: CORE TESSERACT 4D ---
            elif self.modulo_actual == "tesseract":
                rad_rot1 = math.radians(self.angulo_rotacion)
                rad_rot2 = math.radians(self.angulo_rotacion * 0.6)
                for escala, es_reactivo in [(85*mult_escala, False), ((35 + amplitud_promedio * 1.5)*mult_escala, True)]:
                    puntos_cubo = []
                    for sx in [-1, 1]:
                        for sy in [-1, 1]:
                            for sz in [-1, 1]:
                                x_rot = sx * math.cos(rad_rot1) - sz * math.sin(rad_rot1)
                                y_rot = sy * math.cos(rad_rot2) - (sz * math.cos(rad_rot1)) * math.sin(rad_rot2)
                                puntos_cubo.append((cx + x_rot * escala, cy + y_rot * escala))
                    conexiones = [(0,1), (1,3), (3,2), (2,0), (4,5), (5,7), (7,6), (6,4), (0,4), (1,5), (2,6), (3,7)]
                    for c1, c2 in conexiones:
                        draw.line((puntos_cubo[c1], puntos_cubo[c2]), fill=rgb_brillo if es_reactivo else rgb_color, width=2 if es_reactivo else 1)

            # --- WIDGET 9: ESTRELLAS ESTEREOSCÓPICAS 3D ---
            elif self.modulo_actual == "particulas":
                vel_estrellas = 0.02 + (amplitud_promedio * 0.003)
                for p in self.particulas_3d:
                    if self.reproduciendo and not self.pausado:
                        p["z"] -= vel_estrellas
                        if p["z"] <= 0.1:
                            p["z"] = 1.0
                            p["x"] = random.uniform(-1, 1)
                            p["y"] = random.uniform(-1, 1)
                    px = cx + (p["x"] / p["z"]) * (140 * mult_escala)
                    py = cy + (p["y"] / p["z"]) * (140 * mult_escala)
                    r_part = int((1.0 - p["z"]) * 5) + 1
                    if 0 < px < tamano_canvas and 0 < py < tamano_canvas:
                        draw.ellipse((px - r_part, py - r_part, px + r_part, py + r_part), fill=rgb_brillo if r_part > 3 else rgb_color)

            # --- WIDGET 10: OSCILOSCOPIO VECTORIAL ---
            elif self.modulo_actual == "osciloscopio":
                num_muestSamples = 40
                paso_ang = (2 * math.pi) / num_muestSamples
                puntos_osc = []
                for i in range(num_muestSamples):
                    h_cruda = self.alturas_actuales[i % len(self.alturas_actuales)]
                    modulador = (90 + math.sin(self.fase_onda * 2 + i) * (h_cruda * 1.5)) * mult_escala
                    ang = i * paso_ang + (self.angulo_rotacion * 0.02)
                    puntos_osc.append((cx + modulador * math.cos(ang), cy + modulador * math.sin(ang)))
                if puntos_osc:
                    puntos_osc.append(puntos_osc[0])
                    for i in range(len(puntos_osc) - 1):
                        draw.line((puntos_osc[i], puntos_osc[i+1]), fill=rgb_brillo, width=2)

            # --- WIDGET 11: ANILLOS ORBITALES ---
            elif self.modulo_actual == "anillos":
                for index, r_base in enumerate([45, 80, 115]):
                    din_r = (r_base + (self.alturas_actuales[index * 4 % 32] * 0.9)) * mult_escala
                    draw.ellipse((cx - din_r, cy - din_r, cx + din_r, cy + din_r), outline=rgb_color[:3] + (120,), width=2)
                    ang_orb = math.radians(self.angulo_rotacion * (1.5 / (index + 1)))
                    ox, oy = cx + din_r * math.cos(ang_orb), cy + din_r * math.sin(ang_orb)
                    draw.ellipse((ox - 6, oy - 6, ox + 6, oy + 6), fill=rgb_brillo)

            # --- WIDGET 12: VÓRTICE DE VECTOR DE FLUJO ---
            elif self.modulo_actual == "flujo":
                num_lineas_flow = len(self.matriz_flujo)
                for idx in range(num_lineas_flow):
                    if self.reproduciendo and not self.pausado:
                        self.matriz_flujo[idx] += 0.02 + (amplitud_promedio * 0.001)
                    r_din = (30 + idx * 9 + (amplitud_promedio * 0.5)) * mult_escala
                    ang = self.matriz_flujo[idx]
                    x_start = cx + (r_din - int(12*mult_escala)) * math.cos(ang)
                    y_start = cy + (r_din - int(12*mult_escala)) * math.sin(ang)
                    x_end = cx + (r_din + int(12*mult_escala)) * math.cos(ang + 0.4)
                    y_end = cy + (r_din + int(12*mult_escala)) * math.sin(ang + 0.4)
                    draw.line((x_start, y_start, x_end, y_end), fill=rgb_brillo if idx % 2 == 0 else rgb_color, width=2)

            # --- WIDGET 13: GOTA LÍQUIDA DE PLASMA (BLOB) ---
            elif self.modulo_actual == "liquido":
                num_puntos_blob = 40
                puntos_blob = []
                for i in range(num_puntos_blob):
                    ang = i * (2 * math.pi / num_puntos_blob)
                    h_cruda = self.alturas_actuales[i % len(self.alturas_actuales)]
                    mod_organico = math.sin(self.fase_onda + i * 0.5) * (h_cruda * 1.4)
                    radio_b = (80 + mod_organico) * mult_escala
                    puntos_blob.append((cx + radio_b * math.cos(ang), cy + radio_b * math.sin(ang)))
                if len(puntos_blob) > 2:
                    draw.polygon(puntos_blob, fill=rgb_color[:3]+(60,), outline=rgb_brillo, width=3)

            # --- WIDGET 14: CALEIDOSCOPIO GEOMÉTRICO ---
            elif self.modulo_actual == "caleidoscopio":
                espejos = 8
                radio_k = (95 + amplitud_promedio * 1.2) * mult_escala
                for i in range(espejos):
                    ang_v = i * (2 * math.pi / Mirrors if 'Mirrors' in locals() else 2 * math.pi / espejos) + (self.fase_onda * 0.2)
                    h_val = self.alturas_actuales[i % len(self.alturas_actuales)] * 2.0 * mult_escala
                    px = cx + radio_k * math.cos(ang_v)
                    py = cy + radio_k * math.sin(ang_v)
                    draw.regular_polygon((int(px), int(py), int(15 + h_val)), n_sides=4, rotation=int(self.angulo_rotacion), fill=rgb_color[:3]+(140,), outline=rgb_brillo)

            # --- WIDGET 15: REMOLINO DE POLVO ESTELAR (VORTEX) ---
            elif self.modulo_actual == "particulas_vortex":
                for i, p in enumerate(self.particulas_geom):
                    if self.reproduciendo and not self.pausado:
                        p["ang"] += 0.04  
                    dist_v = ((p["rad"] % 130) + math.sin(self.fase_onda + i) * (amplitud_promedio * 0.7)) * mult_escala
                    vx = cx + dist_v * math.cos(p["ang"] + dist_v*0.01)
                    vy = cy + dist_v * math.sin(p["ang"] + dist_v*0.01)
                    draw.ellipse((vx-2, vy-2, vx+2, vy+2), fill=rgb_brillo if i % 2 == 0 else rgb_color)

            # --- WIDGET 16: LOOP GIF SINCRONIZADO ---
            elif self.modulo_actual == "gif":
                if self.gif_frames:
                    ahora_gif = time.time()
                    retraso_cuadro_seg = self.gif_delays[self.gif_indice] / 1000.0
                    
                    if self.reproduciendo and not self.pausado:
                        if (ahora_gif - self.gif_ultimo_cambio) >= retraso_cuadro_seg:
                            self.gif_indice = (self.gif_indice + 1) % len(self.gif_frames)
                            self.gif_ultimo_cambio = ahora_gif

                    gif_actual = self.gif_frames[self.gif_indice].copy()
                    nuevo_tam = int((260 * (1.0 + (amplitud_promedio * 0.004))) * mult_escala)
                    if nuevo_tam > 10:
                        gif_resiz = gif_actual.resize((nuevo_tam, nuevo_tam), Image.Resampling.LANCZOS)
                        offset = (tamano_canvas - nuevo_tam) // 2
                        img_canvas.paste(gif_resiz, (offset, offset), gif_resiz)
                else:
                    draw.text((cx - 85, cy - 10), "[ Selecciona un GIF en Ajustes ]", fill=rgb_color)

            self.tk_visual_centro = ImageTk.PhotoImage(img_canvas)
            self.canvas_visual_centro.delete("all")
            self.canvas_visual_centro.create_image(0, 0, anchor="nw", image=self.tk_visual_centro)
            
        except Exception as e:
            print(f"Error evitado en motor visual: {e}")
        
        self.bg_canvas.tag_raise(self.win_hamburger)
        self.after(35, self.bucle_renderizado_central)

    # =========================================================
    # EXTRACCIÓN AVANZADA DE FOTOGRAMAS Y CRONOMETRAJE REAL
    # =========================================================
    def importar_gif_central(self):
        ruta = self.selector_nativo("Seleccionar animación GIF", es_carpeta=False)
        if ruta and ruta.lower().endswith('.gif'):
            try:
                self.gif_frames = []
                self.gif_delays = []
                gif = Image.open(ruta)
                
                for frame in range(0, gif.n_frames):
                    gif.seek(frame)
                    info_delay = gif.info.get('duration', 100)
                    if info_delay == 0: info_delay = 100
                    
                    self.gif_delays.append(info_delay)
                    self.gif_frames.append(gif.convert("RGBA").resize((280, 280), Image.Resampling.LANCZOS))
                
                self.gif_indice = 0
                self.gif_ultimo_cambio = time.time()
            except: pass

    def crear_barras_iniciales(self):
        ancho, espacio = 8, 3
        for i in range(32):
            x0 = i * (ancho + espacio)
            barra = self.canvas_espectro.create_rectangle(x0, 35, x0 + ancho, 35, fill="#2ecc71", outline="")
            self.barras_espectro.append(barra)

    def animar_espectro_fluido(self):
        if self.reproduciendo and not self.pausado:
            for i in range(36):
                if random.random() < 0.45: 
                    self.alturas_objetivo[i] = random.randint(5, 32)
        else:
            for i in range(36): 
                self.alturas_objetivo[i] = 2

        for i in range(min(32, len(self.barras_espectro))):
            self.alturas_actuales[i] += (self.alturas_objetivo[i] - self.alturas_actuales[i]) * 0.3
            try:
                barra = self.barras_espectro[i]
                x0, _, x1, _ = self.canvas_espectro.coords(barra)
                h = max(2, self.alturas_actuales[i])
                self.canvas_espectro.coords(barra, x0, 35 - h, x1, 35)
                self.canvas_espectro.itemconfig(barra, fill=self.tema["principal"] if h < 18 else self.tema["brillo"])
            except: pass
            
        for i in range(32, 36):
            self.alturas_actuales[i] += (self.alturas_objetivo[i] - self.alturas_actuales[i]) * 0.3

        self.after(25, self.animar_espectro_fluido)

    def aplicar_fondo(self):
        if not self.bg_ruta or not os.path.exists(self.bg_ruta): return
        try:
            ancho, alto = self.winfo_width(), self.winfo_height()
            if ancho < 100 or alto < 100: ancho, alto = 1200, 850
            self.img_fondo_procesada = Image.open(self.bg_ruta).convert("RGBA").resize((ancho, alto), Image.Resampling.LANCZOS)
            overlay = Image.new("RGBA", self.img_fondo_procesada.size, (10, 11, 14, int(255 * self.bg_oscuridad)))
            self.img_fondo_procesada = Image.alpha_composite(self.img_fondo_procesada, overlay)
            self.fondo_tk = ImageTk.PhotoImage(self.img_fondo_procesada)
            self.bg_canvas.delete("bg_tag")
            self.bg_canvas.create_image(ancho // 2, alto // 2, image=self.fondo_tk, tags="bg_tag")
            self.bg_canvas.tag_lower("bg_tag")
            self.mapear_posiciones_canvas()
        except: pass

    def on_resize(self, event):
        if event.widget == self:
            if hasattr(self, "_resize_after"): self.after_cancel(self._resize_after)
            self._resize_after = self.after(80, self._ejecutar_redimension)

    def _ejecutar_redimension(self):
        self.mapear_posiciones_canvas()
        self.aplicar_fondo()

    # CAMBIO AQUÍ: La lista ahora pinta los botones usando los subcolores del tema activo
    def actualizar_lista_archivos(self):
        for widget in self.scroll_playlist.winfo_children(): widget.destroy()
        try:
            self.playlist = [f for f in os.listdir(self.carpeta_musica) if f.endswith(('.mp3', '.wav'))]
            self.playlist.sort()
            for i, cancion in enumerate(self.playlist):
                es_actual = (i == self.indice_actual and self.reproduciendo)
                
                # Los botones de la lista adaptan sus colores según el tema seleccionado
                btn_cancion = ctk.CTkButton(
                    self.scroll_playlist, 
                    text=f" 🎵 {cancion[:22]}", 
                    anchor="w", 
                    fg_color=self.tema["borde"] if es_actual else "transparent", 
                    text_color=self.tema["principal"] if es_actual else "white",
                    hover_color=self.tema["paneles"],
                    font=("Segoe UI", 12, "bold" if es_actual else "normal"),
                    command=lambda idx=i: self.seleccionar_cancion(idx)
                )
                btn_cancion.pack(fill="x", pady=2, padx=4)
        except: pass

    def seleccionar_cancion(self, indice):
        self.indice_actual = indice
        self.reproducir_actual()

    def reproducir_actual(self):
        if not self.playlist: return
        self.cargando_pista = True 
        if self._reproduccion_job is not None: self.after_cancel(self._reproduccion_job)
        mixer.music.stop()
        self.reproduciendo = False
        self.lbl_info.configure(text=f"Cargando pista...")
        self.slider_musica.set(0)
        self._reproduccion_job = self.after(200, self._cargar_audio_pesado)

    def _cargar_audio_pesado(self):
        ruta = os.path.join(self.carpeta_musica, self.playlist[self.indice_actual])
        try:
            mixer.music.load(ruta)
            duracion = mixer.Sound(ruta).get_length() 
            self.slider_musica.configure(to=duracion)
            self.lbl_tiempo_total.configure(text=time.strftime('%M:%S', time.gmtime(duracion)))
            mixer.music.play()
            self.reproduciendo = True
            self.pausado = False  
            self.tiempo_reproduccion = 0
            self.ultimo_tiempo_sistema = time.time()
            self.lbl_info.configure(text=os.path.splitext(self.playlist[self.indice_actual])[0][:35])
            self.btn_play.configure(text="Ⅱ")
            self.actualizar_lista_archivos() # Refrescar para marcar el tema activo en la lista
            self.after(100, self._liberar_carga)
        except:
            self.lbl_info.configure(text="Error de códec de audio")
            self.cargando_pista = False

    def _liberar_carga(self): self.cargando_pista = False

    def toggle_reproduccion(self):
        if not self.playlist: return
        if not self.reproduciendo: self.reproducir_actual()
        else:
            if self.pausado:
                mixer.music.unpause()
                self.pausado = False
                self.ultimo_tiempo_sistema = time.time() 
                self.btn_play.configure(text="Ⅱ")
            else:
                mixer.music.pause()
                self.pausado = True
                self.btn_play.configure(text="▶")

    def siguiente_cancion(self):
        if not self.playlist or self.cargando_pista: return
        self.indice_actual = random.randint(0, len(self.playlist) - 1) if self.modo_aleatorio else (self.indice_actual + 1) % len(self.playlist)
        self.reproducir_actual()

    def anterior_cancion(self):
        if not self.playlist or self.cargando_pista: return
        self.indice_actual = (self.indice_actual - 1) % len(self.playlist)
        self.reproducir_actual()

    def set_modo(self, shuffle):
        self.modo_aleatorio = shuffle
        self.btn_shuffle.configure(fg_color=self.tema["principal"] if shuffle else "#1c2029", text_color=self.tema["texto_osc"] if shuffle else "white", font=("Segoe UI", 12, "bold" if shuffle else "normal"))
        self.btn_orden.configure(fg_color=self.tema["principal"] if not shuffle else "#1c2029", text_color=self.tema["texto_osc"] if not shuffle else "white", font=("Segoe UI", 12, "bold" if not shuffle else "normal"))

    def actualizar_estado_reproduccion(self):
        ahora = time.time()
        delta = ahora - self.ultimo_tiempo_sistema
        self.ultimo_tiempo_sistema = ahora
        if self.reproduciendo and not self.pausado and not self.bloquear_slider and not self.cargando_pista:
            try:
                self.tiempo_reproduccion += delta
                if self.tiempo_reproduccion >= 0:
                    self.slider_musica.set(self.tiempo_reproduccion)
                    self.lbl_tiempo_actual.configure(text=time.strftime('%M:%S', time.gmtime(self.tiempo_reproduccion)))
                if self.tiempo_reproduccion >= self.slider_musica.cget("to"): self.siguiente_cancion()
            except: pass
        self.after(100, self.actualizar_estado_reproduccion)

    def mover_tiempo(self, valor):
        if self.reproduciendo and not self.cargando_pista:
            try: mixer.music.set_pos(valor)
            except: 
                mixer.music.play(start=valor)
                if self.pausado: mixer.music.pause()
            self.tiempo_reproduccion = valor

    def on_slider_press(self, event): self.bloquear_slider = True
    def on_slider_release(self, event):
        self.bloquear_slider = False
        self.mover_tiempo(self.slider_musica.get())

    def start_download(self):
        url = self.entry_url.get()
        if url:
            self.btn_download.configure(state="disabled", text="...")
            threading.Thread(target=self.proceso_descarga, args=(url,), daemon=True).start()

    def proceso_descarga(self, url):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{self.carpeta_musica}/%(title)s.%(ext)s',
                'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])
            self.after(0, self.actualizar_lista_archivos)
        except: pass
        finally: self.btn_download.configure(state="normal", text="Descargar")

    def cambiar_oscuridad(self, valor):
        self.bg_oscuridad = float(valor)
        self.aplicar_fondo()
        self.guardar_configuracion()

    def selector_nativo(self, titulo, es_carpeta=False):
        if platform.system() == "Linux":
            try:
                comando = ["zenity", "--file-selection", f"--title={titulo}"]
                if es_carpeta: comando.append("--directory")
                res = subprocess.run(comando, capture_output=True, text=True)
                if res.returncode == 0: return res.stdout.strip()
            except: pass
        return filedialog.askdirectory() if es_carpeta else filedialog.askopenfilename()

if __name__ == "__main__":
    app = LechePlayer()
    app.mainloop()