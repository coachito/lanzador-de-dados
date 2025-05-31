# Lanzador de Dados de Rol

**Autor:** Camilo Ortegon  
**Correo:** camilo.ortegonc@outlook.com

---

## Descripción

Este proyecto es un lanzador de dados para juegos de rol (RPG). Permite lanzar múltiples dados con diferentes números de caras, simulando tiradas de dados típicas en juegos de mesa. Además, añade comentarios temáticos según el resultado de cada dado y un efecto final que puede ser un buff o un curse para el personaje.

---

## Características

- Permite seleccionar el número de caras del dado (entre 4 y 20).
- Permite lanzar múltiples dados a la vez.
- Mensajes temáticos personalizados para cada dado lanzado.
- Clasificación del resultado (Fallo épico, Golpe normal, Golpe crítico).
- Efectos adicionales (buffs o curses) basados en el resultado total.
- Visualización de dados disponibles.
- Reintentos para relanzar los dados con las mismas características.

---

## Requisitos

- Python 3.6 o superior
- Módulos estándar (`random`, `time`)

---

## Cómo usarlo

1. Ejecuta el script `dados_rol.py` en tu intérprete de Python.
2. Selecciona la opción para lanzar dados.
3. Ingresa el número de caras (entre 4 y 20).
4. Ingresa la cantidad de dados que quieres lanzar.
5. Observa los resultados y decide si quieres relanzar los mismos dados.

---

## Ejemplo de uso
¿De cuántas caras será el dado? (entre 4 y 20): 6
¿Cuántos dados lanzarás?: 3

Lanzando el dado de la Valentía...
Dado número 1 tiene el resultado: 4
¡Fallo épico!

Lanzando el dado de la Muerte...
Dado número 2 tiene el resultado: 11
¡Golpe Crítico!

Lanzando el dado de la Leyenda...
Dado número 3 tiene el resultado: 7
Golpe normal

El resultado final es de 22

Tu personaje recibe un buff: Fuerza aumentada

---

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o realiza un pull request.

---

## Contacto

Camilo Ortegon - camilo.ortegonc@outlook.com  
[GitHub](https://github.com/coachito/lanzador-de-dados)

