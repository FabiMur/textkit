# TextKit

TextKit is a lightweight command-line toolkit for text analysis and structured information extraction.

It is designed to process text efficiently using streaming techniques and a modular architecture.

# Table of contents
- [TextKit](#textkit)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
  - [CLI Usage](#cli-usage)
    - [Analyze](#analyze)
    - [Extract](#extract)
    - [Transform](#transform)
  - [Project Structure](#project-structure)
    - [analyzers/](#analyzers)
    - [extractors/](#extractors)
    - [readers](#readers)
    - [transformers](#transformers)
  - [License](#license)

---

# Installation

Using uv:

```bash
uv sync
```
Or with pip:
```bash
pip install -e .
```

---

## CLI Usage
General syntax:
```bash
textkit [analyze | extract | transform] [options]
```
### Analyze
Analyze a text file and generate.
```bash
textkit analyze --input FILE --output FILE
```
### Extract
```bash
textkit extract --input FILE --type TYPE
```
Where `TYPE` can be:

- email
- url
- date
- phone

Example:
```bash
textkit extract --input document.txt --type email
```
### Transform
```bash
textkit trasnform --input FILE -opeartion OPERATION
```
Where `OPERATION` can be:
- normalize
- clean
- tokenize_words
- tokenize_sentenes

Example:
```bash
textkit extract --input document.txt --opeartion Operation
```
---
## Project Structure
### analyzers/
### extractors/
### readers
### transformers

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details