import matplotlib.pyplot as plt
import numpy as np


def make_pieplot() -> tuple[plt.Figure, plt.Axes]:
    # Zufällige Daten generieren
    data = np.random.randint(20, 100, 5)
    
    # Plot erstellen
    fig, ax = plt.subplots(1, 1)
    ax.pie(data)
    
    # Plot formatieren
    ax.set_title("Zufallskuchen")
    
    return fig, ax


if __name__ == "__main__":
    fig, ax = make_pieplot()
    plt.show()