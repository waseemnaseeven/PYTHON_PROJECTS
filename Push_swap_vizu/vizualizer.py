import matplotlib.pyplot as plt

def visualize_push_swap(pile):
    # Créer une liste d'indices pour les éléments de la pile
    indices = list(range(len(pile)))

    # Initialiser la figure
    fig, ax = plt.subplots()
    ax.set_title("Push_swap Visualizer")
    ax.set_xlabel("Indices")
    ax.set_ylabel("Valeurs")

    # Dessiner la pile initiale
    ax.bar(indices, pile)

    # Afficher la figure
    plt.show()

# Exemple d'utilisation
pile_initiale = [4, 2, 7, 1, 3]
visualize_push_swap(pile_initiale)
