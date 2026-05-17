<div align="center">
  <h1>🍼 LechePlayer v7.8</h1>
  <p><strong>Un reproductor de música avanzado, ligero y de interfaz moderna inspirado en paletas de colores pastel.</strong></p>

  <p>
    <a href="https://github.com/LecheTrony/LechePlayer/stargazers"><img src="https://img.shields.io/github/stars/LecheTrony/LechePlayer?style=for-the-badge&color=ffe3ec" alt="Stars"></a>
    <a href="https://github.com/LecheTrony/LechePlayer/network/members"><img src="https://img.shields.io/github/forks/LecheTrony/LechePlayer?style=for-the-badge&color=ffe3ec" alt="Forks"></a>
    <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Fedora-blue?style=for-the-badge&color=6fa8dc" alt="Platform">
  </p>
</div>

<hr>

<h2>🇲🇽 Versión en Español</h2>

<h3>✨ Descripción del Proyecto</h3>
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

<h3>🚀 Guía de Instalación y Uso</h3>
<p>Sigue estos pasos en tu terminal para clonar el repositorio y ejecutar el reproductor desde el código fuente original:</p>

<h4>1. Clonar el repositorio</h4>
<pre><code>git clone https://github.com/LecheTrony/LechePlayer.git
cd LechePlayer</code></pre>

<h4>2. Instalar Dependencias Nativas del Sistema</h4>
<p>El reproductor interactúa con herramientas del sistema operativo para abrir el selector de archivos nativo y procesar los formatos de audio:</p>
<ul>
  <li><strong>Fedora:</strong>
    <pre><code>sudo dnf install zenity ffmpeg</code></pre>
  </li>
  <li><strong>Ubuntu / Debian / Mint / Pop!_OS:</strong>
    <pre><code>sudo apt update && sudo apt install zenity ffmpeg</code></pre>
  </li>
</ul>

<h4>3. Instalar Librerías de Python</h4>
<pre><code>pip install customtkinter pygame pillow yt-dlp</code></pre>

<h4>4. Lanzar la Aplicación</h4>
<pre><code>python3 main.py</code></pre>

<hr>

<h2>🇺🇸 English Version</h2>

<h3>✨ Project Description</h3>
<p>
  <strong>LechePlayer</strong> is a standalone multimedia player optimized for Linux environments. Built on the graphical power of <code>CustomTkinter</code> and the <code>Pygame</code> audio engine, it offers a clean, fluid audio navigation experience with a high level of visual personalization.
</p>

<h3>🎨 Key Features</h3>
<ul>
  <li><strong>60 Stylized Themes:</strong> Completely modify the look & feel of the player with carefully selected color palettes (including <em>Chocola Pastel</em> variations, deep dark modes, and neon contrasts).</li>
  <li><strong>Built-in Downloader (yt-dlp):</strong> Download your favorite tracks, albums, or playlists directly through the app by pasting the link into the designated bar.</li>
  <li><strong>Custom Background:</strong> Uses the <code>imagen.png</code> file to render a blurred or opaque background behind the player's widgets.</li>
  <li><strong>Responsive Controls:</strong> Interactive progress bar, cover art display, and dynamic playlist management.</li>
</ul>

<h3>🚀 Installation and Usage Guide</h3>
<p>Follow these steps in your terminal to clone the repository and run the player from its original source code:</p>

<h4>1. Clone the repository</h4>
<pre><code>git clone https://github.com/LecheTrony/LechePlayer.git
cd LechePlayer</code></pre>

<h4>2. Install Native System Dependencies</h4>
<p>The player interacts with operating system tools to open the native file picker and process audio formats:</p>
<ul>
  <li><strong>Fedora:</strong>
    <pre><code>sudo dnf install zenity ffmpeg</code></pre>
  </li>
  <li><strong>Ubuntu / Debian / Mint / Pop!_OS:</strong>
    <pre><code>sudo apt update && sudo apt install zenity ffmpeg</code></pre>
  </li>
</ul>

<h4>3. Install Python Libraries</h4>
<pre><code>pip install customtkinter pygame pillow yt-dlp</code></pre>

<h4>4. Launch the Application</h4>
<pre><code>python3 main.py</code></pre>

<hr>

<h2>📂 Structure / Archivos</h2>
<ul>
  <li><code>main.py</code>: Archivo maestro con la interfaz de usuario y lógica de audio / Main master script containing the UI and core audio/download logic.</li>
  <li><code>imagen.png</code>: Recurso gráfico para el fondo / Graphic asset used for the interface background.</li>
  <li><code>.gitignore</code>: Filtro de archivos basura temporales / Configuration to keep the repository clean from build and cache folders.</li>
</ul>

<hr>

<div align="center">
  <p>Desarrollado con 💖 por <a href="https://github.com/LecheTrony">LecheTrony</a></p>
</div>
