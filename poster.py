# !/usr/bin/env python

from gimpfu import *

'''
write the python function to achive filterin
'''

def poster(file1, file2, file3, file4, str1, str2, str3, str4, font1):# args are following soon
       # make a new image
       posterW, posterH = 792, 1008
       posterImage = gimp.Image(posterW, posterH, RGB)
       gimp.Display(posterImage)
       gimp.message("new image created")

       # make the colors
       bColor = gimpcolor.RGB(144, 148, 115)
       fColor = gimpcolor.RGB(254, 166, 85)
       gimp.set_background(bColor)
       gimp.set_foreground(fColor)
       gimp.message("b and f colors made")

       # make background
       backLayer = gimp.Layer(posterImage, "background", posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(backLayer)
       pdb.gimp_drawable_fill(backLayer, 1)
       gimp.message("background made")

       # make Smoke image 1
       image1 = pdb.file_png_load(file1, file1)
       pdb.gimp_image_scale(image1, 1312, 1067)
       pdb.gimp_edit_copy(image1.layers[0])
       layer1 = gimp.Layer(posterImage, "image1", 1512, 1167, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer1)
       floatingLayer1 = pdb.gimp_edit_paste(layer1, False)
       pdb.gimp_floating_sel_anchor(floatingLayer1)
       layer1.translate(-480, -571)
       pdb.gimp_item_transform_rotate(layer1, 3.32, 1, 337.0, 69.0)
       pdb.plug_in_exchange(image1, layer1, 0, 0, 0, 255, 217, 142, 255, 255, 255)
       gimp.message("layer1 made")

       # make Volcano image 2
       image2 = pdb.file_png_load(file2, file2)
       pdb.gimp_image_scale(image2, 792, 792)
       pdb.gimp_image_crop(image2, 792, 411, 0, 378)
       pdb.gimp_edit_copy(image2.layers[0])
       layer2 = gimp.Layer(posterImage, "image2", 792, 792, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer2)
       floatingLayer2 = pdb.gimp_edit_paste(layer2, False)
       pdb.gimp_floating_sel_anchor(floatingLayer2)
       layer2.translate(0, 220)
       gimp.message("layer2 made")
       
       # make Info Panel
       infoLayer = gimp.Layer(posterImage, "infoLayer", posterW, 200, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(infoLayer)
       pdb.gimp_drawable_fill(infoLayer, 0)
       infoLayer.translate(0, 808)
       gimp.message("infoLayer made")
       
       # make Keys image 3
       image3 = pdb.file_png_load(file3, file3)
       pdb.gimp_image_scale(image3, 761, 93)
       pdb.gimp_edit_copy(image3.layers[0])
       layer3 = gimp.Layer(posterImage, "image3", 761, 139, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer3)
       floatingLayer3 = pdb.gimp_edit_paste(layer3, False)
       pdb.gimp_floating_sel_anchor(floatingLayer3)
       layer3.translate(14, 894)
       gimp.message("layer3 made")

       # make trumpet image 4 
       image4 = pdb.file_png_load(file4, file4)
       pdb.gimp_image_scale(image4, 406, 167)
       pdb.gimp_image_crop(image4, 390, 167, 5, 0)
       pdb.gimp_edit_copy(image4.layers[0])
       layer4 = gimp.Layer(posterImage, "image4", 372, 167, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer4)
       floatingLayer4 = pdb.gimp_edit_paste(layer4, False)
       pdb.gimp_floating_sel_anchor(floatingLayer4)
       layer4.translate(235, 528)
       pdb.gimp_item_transform_rotate(layer4, 4.71239, 1, 337.0, 69.0)
       pdb.plug_in_exchange(image4, layer4, 0, 0, 0, 227, 74, 39, 255, 255, 255)
       gimp.message("layer4 made")

       # make title text layer
       textLayer1 = pdb.gimp_text_fontname(posterImage, None, 0, 0, str1, 100, True, 121, PIXELS, font1)
       textLayer1.translate(-70, -100)
       pdb.gimp_text_layer_set_color(textLayer1, '#000000')
       gimp.message("textLayer1 made")
       
       # make slogan text layer
       textLayer2 = pdb.gimp_text_fontname(posterImage, None, 207, 201, str2, 100, True, 62, PIXELS, font1)
       textLayer2.translate(-64, -100)
       pdb.gimp_text_layer_set_color(textLayer2, '#e34a27')
       gimp.message("textLayer2 made")
       textLayer3 = pdb.gimp_text_fontname(posterImage, None, 230, 277, str3, 100, True, 62, PIXELS, font1)
       textLayer3.translate(-70, -100)
       pdb.gimp_text_layer_set_color(textLayer3, '#e34a27')
       gimp.message("textLayer3 made")
       
       # make date text layer
       textLayer4 = pdb.gimp_text_fontname(posterImage, None, 9, 817, str4, 100, True, 65, PIXELS, font1)
       textLayer4.translate(-70, -100)
       pdb.gimp_text_layer_set_color(textLayer4, '#000000')
       gimp.message("textLayer4 made")
       
# end filter

register(
     "python_fu_poster",
     "Poster maker",
     "Poster maker with some interface",
     "ST",
     "@MSCIM2021",
     "2021",
     "Poster Test",
     "",
     [# add input argumenst
         (PF_FILE, "file1", "Choose Image 1 (PNG)", ""),
         (PF_FILE, "file2", "Choose Image 2 (PNG)", ""),
         (PF_FILE, "file3", "Choose Image 3 (PNG)", ""),
         (PF_FILE, "file4", "Choose Image 4 (PNG)", ""),
         (PF_STRING, "str1", "Str1", "CORK JAZZ"),
         (PF_STRING, "str2", "Str2", "JOIN THE"),
         (PF_STRING, "str3", "Str3", "GROOVE"),
         (PF_STRING, "str4", "Str4", "OCTOBER 22 - 25, 2021"),
         (PF_FONT, "font1", "Font1", "Jokerman"),
         
         
     ],
     [],
     poster,
     menu = "<Image>/File/Create/Poster/"
)
 
main()


       
       
       
       
       
       
       
       









       

       

       
