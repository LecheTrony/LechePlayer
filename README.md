<div align="center">
  <h1>LechePlayer v1.0</h1>
  <p><strong>Un reproductor de música avanzado, ligero y de interfaz moderna inspirado en paletas de colores pastel.</strong></p>

  <p>
    <a href="https://github.com/LecheTrony/LechePlayer/stargazers"><img src="https://img.shields.io/github/stars/LecheTrony/LechePlayer?style=for-the-badge&color=ffe3ec" alt="Stars"></a>
    <a href="https://github.com/LecheTrony/LechePlayer/network/members"><img src="https://img.shields.io/github/forks/LecheTrony/LechePlayer?style=for-the-badge&color=ffe3ec" alt="Forks"></a>
    <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-blue?style=for-the-badge&color=6fa8dc" alt="Platform">
  </p>
</div>

<hr>

<h2>🇲🇽 Versión en Español</h2>

<h3>✨ Descripción del Proyecto</h3>
<p>
  <strong>LechePlayer</strong> es un reproductor multimedia autónomo optimizado para entornos Linux y Windows. Construido sobre la potencia gráfica de <code>CustomTkinter</code> y el motor de sonido de <code>Pygame</code>, ofrece una navegación de audio limpia, fluida y con un alto nivel de personalización visual.
</p>

<h3>🎨 Características Principales</h3>
<ul>
  <li><strong>60 Temas Estilizados:</strong> Modifica por completo el look & feel del reproductor con paletas de color cuidadosamente seleccionadas (incluyendo variaciones <em>Chocola Pastel</em>, modos oscuros profundos y contrastes neón).</li>
  <li><strong>Descargador integrado (yt-dlp):</strong> Descarga tus canciones, álbumes o listas de reproducción de forma directa pegando el enlace en la barra correspondiente.</li>
  <li><strong>Controles Responsivos:</strong> Barra de progreso interactiva, visualizador de portadas y gestión dinámica de listas de reproducción con refresco automático.</li>
</ul>

<h3>🚀 Guía de Instalación y Uso</h3>

<h4>🪟 Para usuarios de Windows (Ejecutable Directo)</h4>
<p>Si estás en Windows y no quieres lidiar con la terminal, ve a la sección de <strong>Releases</strong> en el lateral derecho de este repositorio, descarga el archivo <code>LechePlayer_v1.0_Windows.zip</code>, descomprímelo y ejecuta directamente el archivo <code>main.exe</code>.</p>

<h4>🐧 Ejecución desde Código Fuente (Linux / Fedora)</h4>
<p>Sigue estos pasos en tu terminal para clonar el repositorio y ejecutar el reproductor directamente:</p>

<h5>1. Clonar el repositorio</h5>
<pre><code>git clone https://github.com/LecheTrony/LechePlayer.git
cd LechePlayer</code></pre>

<h5>2. Instalar Dependencias Nativas del Sistema</h5>
<p>El reproductor interactúa con herramientas del sistema operativo para abrir el selector de archivos nativo y procesar los formatos de audio:</p>
<ul>
  <li><strong>Fedora:</strong>
    <pre><code>sudo dnf install zenity ffmpeg</code></pre>
  </li>
  <li><strong>Ubuntu / Debian / Mint / Pop!_OS:</strong>
    <pre><code>sudo apt update && sudo apt install zenity ffmpeg</code></pre>
  </li>
</ul>

<h5>3. Instalar Librerías de Python</h5>
<pre><code>pip install customtkinter pygame pillow yt-dlp</code></pre>

<h5>4. Lanzar la Aplicación</h5>
<pre><code>python3 main.py</code></pre>

<hr>

<h2>🇺🇸 English Version</h2>

<h3>✨ Project Description</h3>
<p>
  <strong>LechePlayer</strong> is a standalone multimedia player optimized for Linux and Windows environments. Built on the graphical power of <code>CustomTkinter</code> and the <code>Pygame</code> audio engine, it offers a clean, fluid audio navigation experience with a high level of visual personalization.
</p>

<h3>🎨 Key Features</h3>
<ul>
  <li><strong>60 Stylized Themes:</strong> Completely modify the look & feel of the player with carefully selected color palettes (including <em>Chocola Pastel</em> variations, deep dark modes, and neon contrasts).</li>
  <li><strong>Built-in Downloader (yt-dlp):</strong> Download your favorite tracks, albums, or playlists directly through the app by pasting the link into the designated bar.</li>
  <li><strong>Responsive Controls:</strong> Interactive progress bar, cover art display, and dynamic playlist management with automatic list refreshing.</li>
</ul>

<h3>🚀 Installation and Usage Guide</h3>

<h4>🪟 For Windows Users (Direct Executable)</h4>
<p>If you are on Windows and prefer not to use the terminal, go to the <strong>Releases</strong> section on the right side of this repository, download <code>LechePlayer_v1.0_Windows.zip</code>, extract it, and launch the <code>main.exe</code> file directly.</p>

<h4>🐧 Running from Source Code (Linux / Fedora)</h4>
<p>Follow these steps in your terminal to clone the repository and run the player from its original source code:</p>

<h5>1. Clone the repository</h5>
<pre><code>git clone https://github.com/LecheTrony/LechePlayer.git
cd LechePlayer</code></pre>

<h5>2. Install Native System Dependencies</h5>
<p>The player interacts with operating system tools to open the native file picker and process audio formats:</p>
<ul>
  <li><strong>Fedora:</strong>
    <pre><code>sudo dnf install zenity ffmpeg</code></pre>
  </li>
  <li><strong>Ubuntu / Debian / Mint / Pop!_OS:</strong>
    <pre><code>sudo apt update && sudo apt install zenity ffmpeg</code></pre>
  </li>
</ul>

<h5>3. Install Python Libraries</h5>
<pre><code>pip install customtkinter pygame pillow yt-dlp</code></pre>

<h5>4. Launch the Application</h5>
<pre><code>python3 main.py</code></pre>

<hr>

<h2>📂 Structure / Archivos</h2>
<ul>
  <li><code>main.py</code>: Archivo maestro con la interfaz de usuario y lógica de audio / Main master script containing the UI and core audio/download logic.</li>
  <li><code>.gitignore</code>: Filtro de archivos basura temporales / Configuration to keep the repository clean from build and cache folders.</li>
</ul>

<hr>

<div align="center">
  <p>Desarrollado con 💖 por <a href="https://github.com/LecheTrony">LecheTrony</a></p>
</div>
