import matplotlib.pyplot as plt
import imageio
import random
from io import BytesIO


def bubble_sort_animation(arr):
    """Animacja sortowania bąbelkowego z wizualizacją za pomocą wykresu słupkowego"""
    frames = []
    n = len(arr)

    # Tworzymy mapę kolorów (colormap)
    colormap = plt.colormaps.get_cmap('viridis')
    norm = plt.Normalize(min(arr), max(arr))

    fig, ax = plt.subplots()

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Zamiana elementów, jeśli są w złej kolejności
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # Rysowanie wykresu słupkowego dla bieżącego stanu tablicy
            ax.clear()
            ax.bar(range(len(arr)), arr, color=colormap(norm(arr)))
            ax.set_title("Bubble Sort Animation")
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")

            # Zapisanie bieżącej klatki jako obraz w pamięci
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            frames.append(imageio.v2.imread(buf))
            buf.close()

    # Tworzenie pliku GIF z zapisanych klatek
    imageio.mimsave("bubble_sort_animation.gif", frames, fps=60)
    print("Animacja została zapisana jako 'bubble_sort_animation.gif'.")


l = list(range(1, 51))
random.shuffle(l)
bubble_sort_animation(l)