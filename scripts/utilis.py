import os
import pygame

def import_folder(path):
	surface_list = []

	for _,__,img_files in os.walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list


def import_folder_with_scale(path, scale):
	surface_list = []

	for _,__,img_files in os.walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), (scale))
			surface_list.append(image_surf)

	return surface_list


def get_all_folder_names(directory, name):

	folders = []

	fu = [f.path for f in os.scandir(directory) if f.is_dir()]
	for i in range(len(fu)):
		temp = fu[i].partition(name + "/")[2]
		folders.append(temp)
	
	return folders

def get_all_folder_animations(directory, name):

	folders = get_all_folder_names(directory, name)
	animations = dict.fromkeys(folders, [])

	return animations


def animate_loop(animation, frame_index, animation_speed):
        
	# Loop over frame index 
	frame_index += animation_speed
	if frame_index >= len(animation):
		frame_index = 0

	# Return the animation frame
	return animation[int(frame_index)], frame_index
