def check_memory_alert(threshold):
    while True:
        # Obtiene el uso de memoria del proceso actual
        process = psutil.Process()
        memory_info = process.memory_info()
        memory_used = memory_info.rss / (1024 * 1024)  # Convertir a MB

        if memory_used > threshold:
            print(f"Alerta: Uso de memoria elevado: {memory_used:.2f} MB")

        time.sleep(5)  # Espera 5 segundos antes de volver a verificar

# Ejecutar el monitoreo en un hilo separado o en la función principal
check_memory_alert(100)  # Alerta si el uso de memoria excede 100 MB


def memory_monitor(func):
    def wrapper(*args, **kwargs):
        check_memory_alert(100)  # Límite de memoria en MB
        result = func(*args, **kwargs)
        return result
    return wrapper

