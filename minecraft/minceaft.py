 m
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()
window.title = 'Minecraft Clone'

# Textures
grass_top = load_texture('white_cube')
stone = load_texture('stone')
dirt = load_texture('dirt')
wood = load_texture('wood')
skin = load_texture('brick')

# Player
player = FirstPersonController(speed=10, height=2)

# Create visible player model
player_body = Entity(
    model='cube',
    scale=(0.6, 1.8, 0.6),
    texture=skin
)

player_head = Entity(
    model='cube',
    scale=(0.6, 0.6, 0.6),
    texture=skin,
    parent=player_body
)
player_head.position = (0, 0.9, 0)

# Update player body position
def update():
    player_body.position = player.position
    player_body.y -= 0.9

# Block dictionary
block_textures = {
    'grass': grass_top,
    'stone': stone,
    'dirt': dirt,
    'wood': wood
}

blocks = []

# Generate terrain
def generate_terrain():
    for x in range(-20, 21):
        for z in range(-20, 21):
            height = random.randint(0, 3)
            
            for y in range(-5, height):
                if y < -2:
                    block_type = 'stone'
                elif y < height - 1:
                    block_type = 'dirt'
                else:
                    block_type = 'grass'
                
                block = Block(
                    position=(x, y, z),
                    texture=block_textures[block_type],
                    scale=1
                )
                blocks.append(block)

generate_terrain()

# Plant trees
def plant_trees():
    for _ in range(15):
        x = random.randint(-15, 15)
        z = random.randint(-15, 15)
        
        for y in range(5):
            Block(position=(x, 4 + y, z), texture=wood, scale=1)
        
        for fx in range(-2, 3):
            for fz in range(-2, 3):
                for fy in range(3):
                    if (fx, fz) != (0, 0):
                        Block(position=(x + fx, 8 + fy, z + fz), texture=grass_top, scale=1)

plant_trees()

# Block placement and destruction
def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward(), max_distance=10)
        if hit_info.hit:
            destroy(hit_info.entity)
    
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward(), max_distance=10)
        if hit_info.hit:
            new_pos = hit_info.entity.position + hit_info.normal
            Block(position=new_pos, texture=grass_top, scale=1)

# Sky
sky = Sky(texture='sky_default')

# Lighting
sun = DirectionalLight(parent=scene, direction=(1, 1, 1))

app.run()