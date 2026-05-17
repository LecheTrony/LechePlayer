<div align="center">
  <h1>LechePlayer v1.0</h1>
  <p><strong>Un reproductor de música avanzado, ligero y de interfaz moderna inspirado en paletas de colores pastel.</strong></p>

  <p>
    <a href="https://github.com/LecheTrony/LechePlayer/stargazers"><img src="https://img.shields.io/github/stars/LecheTrony/LechePlayer?style=for-the-badge&color=ffe3ec" alt="Stars"></a>
    <a href="https://github.com/LecheTrony/LechePlayer/network/members"><img src="https://img.shields.io/github/forks/LecheTrony/LechePlayer?style=for-the-badge&color=ffe3ec" alt="Forks"></a>
    <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Fedora-blue?style=for-the-badge&color=6fa8dc" alt="Platform">
  </p>
</div>

<hr>

<h2>✨ Descripción del Proyecto</h2>
<p>
  <strong>LechePlayer</strong> es un reproductor multimedia autónomo optimizado para entornos Linux. Construido sobre la potencia gráfica de <code>CustomTkinter</code> y el motor de sonido de <code>Pygame</code>, ofrece una navegación de audio limpia, fluida y con un alto nivel de personalización visual.
</p>

<h3>🎨 Características Principales</h3>
<ul>
  <li><strong>60 Temas Estilizados:</strong> Modifica por completo el look & feel del reproductor con paletas de color cuidadosamente seleccionadas (incluyendo variaciones <em>Chocola Pastel</em>, modos oscuros profundos y contrastes neón).</li>
  <li><strong>Descargador integrado (yt-dlp):</strong> Descarga tus canciones, álbumes o listas de reproducción de forma directa pegando el enlace en la barra correspondiente.</li>
  <li><strong>Fondo Personalizable:</strong> Utiliza el archivo <code>imagen.png</code> para renderizar un fondo difuminado u opaco detrás de los widgets del reproductor.</li>
  <li><strong>Controles Responsivos:</strong> Barra de progreso interactiva, visualizador de portadas y gestión dinámica de listas de reproducción.</li>
</ul>

<hr>

<h2>🚀 Guía de Instalación y Uso</h2>
<p>Sigue estos pasos en tu terminal para clonar el repositorio y ejecutar el reproductor desde el código fuente original:</p>

<h3>1. Clonar el repositorio</h3>
<pre><code>git clone https://github.com/LecheTrony/LechePlayer.git
cd LechePlayer</code></pre>

<h3>2. Instalar Dependencias Nativas del Sistema</h3>
<p>El reproductor interactúa con herramientas del sistema operativo para abrir el selector de archivos nativo y procesar los formatos de audio:</p>
<ul>
  <li><strong>Fedora:</strong>
    <pre><code>sudo dnf install zenity ffmpeg</code></pre>
  </li>
  <li><strong>Ubuntu / Debian / Mint / Pop!_OS:</strong>
    <pre><code>sudo apt update && sudo apt install zenity ffmpeg</code></pre>
  </li>
</ul>

<h3>3. Instalar Librerías de Python</h3>
<p>Se recomienda activar tu entorno virtual (<code>venv</code>) y ejecutar la instalación de los módulos necesarios a través de <code>pip</code>:</p>
<pre><code>pip install customtkinter pygame pillow yt-dlp</code></pre>

<h3>4. Lanzar la Aplicación</h3>
<pre><code>python3 main.py</code></pre>

<hr>

<h2>📂 Archivos Estructura</h2>
<ul>
  <li><code>main.py</code>: Archivo maestro con la interfaz de usuario, gestión de hilos de audio y algoritmos de descarga.</li>
  <li><code>imagen.png</code>: Recurso gráfico utilizado como fondo de pantalla de la interfaz multimedia.</li>
  <li><code>.gitignore</code>: Configuración para mantener el repositorio limpio de carpetas temporales de compilación (<code>__pycache__</code>, <code>build</code>, <code>dist</code>).</li>
</ul>

<hr>

<div align="center">
  <p>Desarrollado con 💖 por <a href="https://github.com/LecheTrony">LecheTrony</a></p>
</div>
