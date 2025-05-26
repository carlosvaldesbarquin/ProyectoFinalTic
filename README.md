# Proyecto Final TIC: Comparativa de Rendimiento entre Máquinas Virtuales y Contenedores Docker

## Introducción
El proyecto compara el rendimiento de **máquinas virtuales (VM)** y **contenedores Docker**, analizando su eficiencia en términos de CPU, memoria y disco. Las VM virtualizan hardware completo, mientras que Docker comparte el kernel del host, lo que lo hace más ligero.

## Configuración del Entorno
- **Máquina host**:  
  - Procesador: AMD Ryzen 3 3250U.  
  - RAM: 8 GB.  
  - Almacenamiento: SSD 238 GB.  
  - SO: Ubuntu (64-bit).  

- **Máquina Virtual**:  
  - Hipervisor: VirtualBox 6.1.  
  - SO invitado: Ubuntu.  
  - Recursos: 2.5 GB RAM, 2 CPUs.  

- **Contenedor Docker**:  
  - Imagen base: Ubuntu oficial.  

## Métricas y Herramientas
- **Métricas**: Eventos por segundo, latencia, uso de CPU, RAM y disco.  
- **Herramientas**: Sysbench, Python 3.13, Matplotlib, Psutil.  

## Resultados

### CPU
- **VM**: 372.11 eventos/segundo, latencia promedio 2.68 ms.  
- **Docker**: 374.62 eventos/segundo, latencia promedio 2.66 ms.  
- **Conclusión**: Rendimiento similar, Docker con ligeramente mejor latencia máxima.  

### Disco
- **VM**: 89.77 MiB/s (lectura secuencial).  
- **Docker**: 2931.18 MiB/s (lectura secuencial).  
- **Conclusión**: Docker es **30 veces más rápido** en operaciones de disco.  

### Memoria
- **VM**: 3461.79 MiB/s.  
- **Docker**: 3457.93 MiB/s.  
- **Conclusión**: Rendimiento prácticamente idéntico.  

## Consumo de Recursos
- **Docker**:  
  - CPU post-prueba: 6.3%.  
  - RAM: incremento mínimo (+5.8 MB).  
- **VM**:  
  - CPU post-prueba: 9.4%.  
  - RAM: ligera reducción en uso.  

## Análisis Comparativo

### Docker
**Fortalezas**:  
- Alto rendimiento en disco.  
- Baja sobrecarga del sistema.  
- Consumo de recursos optimizado.  

**Debilidades**:  
- Aislamiento menos robusto que una VM.  

### Máquina Virtual
**Fortalezas**:  
- Aislamiento completo.  
- Compatibilidad con cualquier SO.  

**Debilidades**:  
- Rendimiento de disco inferior.  
- Mayor consumo de recursos.  

## Conclusión
- **Usar Docker** para:  
  - Alto rendimiento (especialmente en disco).  
  - Despliegues rápidos y escalables.  
- **Usar VM** para:  
  - Aislamiento completo o ejecución de SO distintos.  
  - Entornos críticos o pruebas de seguridad.  

**Repositorio del proyecto**: [GitHub](https://github.com/carlosvaldesbarquin/ProyectoFinalTic)  
**Autor**: Carlos Valdés Barquín.  
**Profesor**: Lázaro Hernández.  
**Fecha**: 26/05/2025.  