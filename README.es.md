# Most Wanted UFO Mini — Python para videojuegos con pygame

*[English version](README.md)*

Código y guías en PDF, paso a paso, de cada lección de **Python para videojuegos con pygame**, un curso
de Magic Lab Studio en el que construyes **Most Wanted UFO Mini**, un juego de naves completo, desde
una ventana vacía hasta el jefe final.

**El curso completo, con las videolecciones narradas, los quizzes y los ejercicios, está en Hotmart.**

## Qué hay aquí

| Lección | Carpeta | Qué aprendes |
|---|---|---|
| 1 | [`lecciones/01-ventana`](lecciones/01-ventana) | entorno virtual, `pip`, una ventana, el bucle de juego |
| 2 | [`lecciones/02-mover`](lecciones/02-mover) | `Rect`, orden de dibujo, teclado, no salirse de la pantalla |
| 3 | [`lecciones/03-disparar`](lecciones/03-disparar) | listas, cadencia de disparo (`cooldown`), listas por comprensión, sonido |
| 4 | [`lecciones/04-enemigos`](lecciones/04-enemigos) | clases, `self`, `Sprite`, `Group`, `random` |
| 5 | [`lecciones/05-choques`](lecciones/05-choques) | choques, puntos, texto en pantalla, vidas |
| 6 | [`lecciones/06-estados`](lecciones/06-estados) | estados del juego: menú, jugando, pausa, game over |
| 7 | [`lecciones/07-jefe`](lecciones/07-jefe) | seno y coseno, un jefe con vida, ganar, tu propio mod |

Cada carpeta de lección trae:

- **La guía en PDF** (`01-ventana.pdf`, …): las instrucciones en texto, paso a paso, con el código de cada paso y las líneas nuevas resaltadas, más un resumen, un ejercicio y su solución.
- **`paso-1.py`, `paso-2.py`, …**: el código tal como queda después de cada paso. Copia de estos archivos y no del PDF: los visores de PDF suelen perder los espacios del principio de cada línea, y en Python esos espacios importan.
- **`game.py`**: el código completo al final de la lección. Cada lección empieza desde el `game.py` de la anterior.

El código es el mismo en español y en inglés (los nombres van en inglés en los dos idiomas); la
versión en inglés está en [`lessons/`](lessons), con archivos `step-N.py`.

`assets/` tiene las imágenes y los sonidos del juego, y `original/main.py` es el archivo principal del
juego original, Most Wanted UFO Classic, que la lección 7 abre y lee.

## Correrlo

Necesitas Python 3.10 o más nuevo.

```bash
python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install pygame-ce==2.5.8
python lecciones/07-jefe/game.py
```

Corre los juegos desde esta carpeta (la raíz del repositorio): cargan sus imágenes y sonidos desde `assets/`.

## Créditos y licencias

- Arte y sonidos de `assets/`: **Most Wanted UFO Classic**, de Jose Daniel Soto, con licencia CC BY 4.0 (ver `assets/LICENSE`).
- `original/main.py`: de [Most Wanted UFO Classic](https://github.com/Magic-Lab-Studio/most-wanted-ufo-classic), de Jose Daniel Soto, licencia MIT (ver `original/LICENSE`). El juego original completo está en ese repositorio.

Un curso de Magic Lab Studio · https://magiclabstudio.com
