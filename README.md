# TextKit

TextKit es una herramienta de línea de comandos diseñada para el análisis de texto y la extracción de información estructurada.



## Tabla de contenidos
- [TextKit](#textkit)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Características principales:](#características-principales)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Instalación](#instalación)
  - [Uso de la CLI](#uso-de-la-cli)
    - [Analyze](#analyze)
    - [Extract](#extract)
    - [Transform](#transform)
  - [Licencia](#licencia)

---

## Características principales:
- **Transformación (transformers)**: Funciones para la limpieza de caracteres, normalización de texto, eliminación de stopwords (ES, EN, FR) y tokenización a nivel de palabra y sentencia.

- **Extracción (extractors)**: Detección de entidades mediante expresiones regulares para capturar correos electrónicos, direcciones URL, formatos de fecha y números de teléfono.

- **Análisis (analyzers)**: Componentes que mantienen el estado para calcular métricas globales como densidad léxica, detección de idioma basada en sufijos y conteo de n-gramas.

---

## Estructura del proyecto

```text
src/
└── textkit/
    ├── analyzers/
    │   ├── __init__.py
    │   ├── base_analyzer.py
    │   ├── extract_analyzer.py
    │   ├── language_detector.py
    │   ├── sequence_analyzer.py
    │   └── statistics_analyzer.py
    │
    ├── extractors/
    │   ├── __init__.py
    │   ├── date.py
    │   ├── email.py
    │   ├── patterns.py
    │   ├── phone.py
    │   └── url.py
    │
    ├── pipelines/
    │   ├── __init__.py
    │   ├── analyze.py
    │   ├── extract.py
    │   └── transform.py
    │
    ├── transformers/
    │   ├── __init__.py
    │   ├── cleaning.py
    │   ├── normalization.py
    │   ├── stopwords.py
    │   ├── tokenization.py
    │   └── resources/
    │
    └── __init__.py
```

---

## Instalación

Using uv:

```bash
uv sync
```
Or with pip:
```bash
pip install -e .
```

---

## Uso de la CLI
Sintaxis general:
```bash
textkit [analyze | extract | transform] [options]
```
### Analyze
Analiza un archivo de texto y genera un informe.
```bash
textkit analyze --input FILE --output FILE --ngram_size N
```
Donde `N` puede ser 1, 2, 3, 4 o 5 para unigramas, bigramas, trigramas, cuatro-gramas o cinco-gramas.

### Extract
```bash
textkit extract --input FILE --type TYPE
```
Where `TYPE` can be:

- email
- url
- date
- phone

Ejemplo:
```bash
textkit extract --input document.txt --type email
```
### Transform
```bash
textkit transform --input FILE --operation OPERATION
```
Donde `OPERATION` puede ser:
- normalize
- clean
- tokenize_words
- tokenize_sentenes

Ejemplo:
```bash
textkit extract --input document.txt --opeartion normalize
```

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [LICENSE](LICENSE) para más detalles