from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialisation de l'application Ursina
app = Ursina()

# Modèles et Textures
grass_texture = load_texture('assets/grass_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
sky_texture   = load_texture('assets/skybox.png')

# Type de bloc actuellement sélectionné
block_pick = 1

def update():
    global block_pick

    # Sélection de type de bloc
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

# Définition de la classe Voxel (Bloc)
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            # Clic Gauche : Détruire le bloc
            if key == 'left mouse down':
                destroy(self)

            # Clic Droit : Poser un bloc selon la face ciblée
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)

# Classe du Ciel
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )

# Génération d'une carte 3D de base (16x16 blocs)
for z in range(16):
    for x in range(16):
        voxel = Voxel(position=(x, 0, z), texture=grass_texture)

# Instanciation du Joueur et du Ciel
player = FirstPersonController()
sky = Sky()

# Lancement du moteur
if __name__ == '__main__':
    app.run()
