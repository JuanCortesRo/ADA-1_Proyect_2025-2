# Proyecto Final - Asociación de Deportes

**Estudiante:** Juan José Cortés Rodríguez  
**Código:** 2325109  
**Materia:** Análisis y Diseño de Algoritmos I   
**Fecha:** Diciembre 2025

**Universidad del Valle**

---

## Descripción de Archivos

### **Archivos Principales**

- **`main.py`**: Archivo principal que ejecuta ambas soluciones del proyecto secuencialmente.
- **`loader.py`**: Carga los datos de jugadores, equipos y sedes desde los archivos de entrada.
- **`classes.py`**: Define las clases base Jugador, Equipo y Sede para interpretar los archivos de entrada.

### **Carpeta: `inputs/`**
Contiene los archivos de entrada con datos de prueba:
- **`input0.py`**: Caso de prueba 0
- **`input1.py`**: Caso de prueba 1
- **`input2.py`**: Caso de prueba 2
- **`input3.py`**: Caso de prueba 3

### **Carpeta: `First Solution/`**
Primera solución utilizando **Árboles Rojinegros**:
- **`first_solution.py`**: Implementación de árboles rojinegros para ordenar jugadores, equipos y sedes.
- **`processor_first.py`**: Procesador que ejecuta la primera solución y genera los archivos de salida.
- **`outputs/`**: Carpeta donde se generan los archivos de salida (output0.txt, output1.txt, etc.)

### **Carpeta: `Second Solution/`**
Segunda solución utilizando **Merge Sort + Insertion Sort**:
- **`second_solution.py`**: Implementación de Merge Sort para jugadores e Insertion Sort para equipos y sedes.
- **`processor_second.py`**: Procesador que ejecuta la segunda solución y genera los archivos de salida.
- **`outputs/`**: Carpeta donde se generan los archivos de salida (output0.txt, output1.txt, etc.)


### **Carpeta: `output-comparison-tools/`**
Esta carpeta se añadió para cumplir con los requisitos del informe. Contiene herramientas para analizar y comparar el rendimiento de ambas soluciones:
- **`benchmark.py`**: Mide los tiempos de ejecución de ambas soluciones con diferentes tamaños de entrada.
- **`generate_graphs.py`**: Genera visualizaciones basadas en los resultados de las pruebas comparativas.
- **`benchmark_results.csv`**: Contiene los resultados de las pruebas comparativas pregenerados que se utilizan en el informe.
- **`README.md`**: Instrucciones para usar las herramientas. **(IMPORTANTE)**
---

## Instrucciones de Ejecución

### **Requisitos**
- Python 3.8 o superior
- No requiere instalación de librerías externas

### **Ejecutar el Proyecto Completo**

Para ejecutar ambas soluciones y generar todos los archivos de salida:

```bash
python main.py
```

Esto ejecutará:
1. Primera solución (Árboles Rojinegros) → Genera archivos en `First Solution/outputs/`
2. Segunda solución (Merge Sort + Insertion Sort) → Genera archivos en `Second Solution/outputs/`

## Archivos de Salida

Después de la ejecución, se generarán los siguientes archivos:

- `First Solution/outputs/output0.txt`
- `First Solution/outputs/output1.txt`
- `First Solution/outputs/output2.txt`
- `First Solution/outputs/output3.txt`
- `Second Solution/outputs/output0.txt`
- `Second Solution/outputs/output1.txt`
- `Second Solution/outputs/output2.txt`
- `Second Solution/outputs/output3.txt`

Cada archivo contiene:
- Sedes ordenadas con sus equipos y jugadores
- Ranking global de jugadores
- Estadísticas completas (equipo/jugador mayor/menor rendimiento, promedios, etc.)

---

## Notas

- Ambas soluciones generan outputs idénticos (mismos resultados, diferentes algoritmos).
- Los archivos de salida se sobrescriben en cada ejecución.
- Si no existen las carpetas `outputs/`, se crearán automáticamente, por lo que se puede probar borrando estas.

---

## Contacto

**Juan José Cortés Rodríguez**  
- Email: [juan.jose.cortes@correounivalle.edu.co]
- GitHub: [JuanCortesRo](https://github.com/JuanCortesRo)

---

*Diciembre 2025*