from os import walk
import pygame

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list


def import_folder_with_scale(path, scale):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), (scale))
			surface_list.append(image_surf)

	return surface_list


def animate_loop(animation, frame_index, animation_speed):
        
	# Loop over frame index 
	frame_index += animation_speed
	if frame_index >= len(animation):
		frame_index = 0

	# Return the animation frame
	return animation[int(frame_index)], frame_index
