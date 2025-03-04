# **LaPyX**

Este proyecto permite convertir expresiones matemáticas escritas en LaTeX a expresiones equivalentes en Python. Utiliza **PLY (Python Lex-Yacc)** para analizar y transformar las ecuaciones.

## Características
- Soporta operadores matemáticos básicos (`+`, `-`, `*`, `/`, `^`).
- Convierte funciones trigonométricas (`\sin`, `\cos`, `\tan`).
- Soporta fracciones (`\frac{a}{b}`).
- Soporta raíces cuadradas (`\sqrt{x}`).
- Soporta logaritmos y exponenciales (`\log{x}`, `\exp{x}`).
- Maneja `\left` y `\right` correctamente.
- Soporta expresiones anidadas.

## Instalación
### Requisitos
- **Python 3.8 o superior**
- **PLY (Python Lex-Yacc)**

Instalar PLY si no lo tienes:
```sh
pip install ply
```

## Estructura del Proyecto
```
.
├── lex.py      # Analizador léxico
├── parse.py    # Analizador sintáctico
├── main.py     # Script principal
├── test_cases.py # Pruebas automáticas
└── README.md   # Documentación
```

## Uso
Ejecuta el archivo `main.py` para convertir ecuaciones de LaTeX a Python:
```sh
python main.py
```
Luego, ingresa una ecuación en formato LaTeX, por ejemplo:
```
\frac{3}{4} + \sin{(x^3)} - \tan{\left(\sqrt{x}\right)}
```
Salida esperada:
```python
(3 / 4) + math.sin((x ** 3)) - math.tan((x ** 0.5))
```

## Pruebas
Ejecuta el archivo `test.py` para probar múltiples ecuaciones:
```sh
python test.py
```

## Notas
- El analizador ignora `\left` y `\right`, ya que no afectan la semántica.
- Se asume que todas las variables (`x`, `y`, `a`, `b`, etc.) son nombres válidos en Python.
- La función `math.log(x)` usa el logaritmo natural (`ln` en matemáticas). Para `log10`, usa `math.log10(x)`.

