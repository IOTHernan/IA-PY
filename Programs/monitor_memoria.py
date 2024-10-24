# pip install memory-profiler

def memory_monitor(func):
    def wrapper(*args, **kwargs):
        # Aquí podrías verificar la memoria antes de ejecutar la función
        result = func(*args, **kwargs)
        # Aquí podrías verificar la memoria después de ejecutar la función
        return result
    return wrapper

@memory_monitor
def my_function():
    # Tu código aquí
    pass
