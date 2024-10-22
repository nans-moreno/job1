def draw_triangle(height):
    # Pour chaque ligne, du sommet à la base
    for i in range(height - 1):
        # Ajouter des espaces pour aligner le triangle
        print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')
    
    # Dessiner la base du triangle avec des "_"
    print('/' + '_' * (2 * (height - 1)) + '\\')

# Exemple d'utilisation     
draw_triangle(5)
