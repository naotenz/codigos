""" Liberia time forma de importar una liberia """
import time


class Timer:
    def __enter__(self):
        """
        Enter the context and record the start time.
        """
        self.start_time = time.time()  # Tiempo de inicio
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context and print the elapsed time.
        """
        end_time = time.time()  # Tiempo de fin
        print(f"Time taken: {end_time - self.start_time} seconds")


if __name__ == "__main__":
    with Timer():
        total = sum(range(1000000))  # Bloque de código a medir