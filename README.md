# Python GIMP Poster

This is a Python script that generates a poster using the GIMP image editor. The poster contains a random quote and a background image.

## Installation

1. Install GIMP on your computer.
2. Clone this repository to your local machine.
3. Install the required Python packages by running `pip install -r requirements.txt`.

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the script by executing `python poster.py`.
3. The poster will be generated and saved in the `output/` directory.

## About the Project

After researching existing jazz posters, I found that many posters used simple imagery with block colours and instrument silhouettes.
I decided to create a poster with these elements. I wanted the central theme of the poster to be energetic, so I chose a volcano to be the focus of the poster,
incorporating instruments to drive the musical theme. I found a colour palette synonymous with jazz that also suited my theme. 
I chose my slogan as it was short but conveyed a reason to go to the Jazz Festival.

###Design Principles:

  •  Symmetrical Balance: 

I designed the poster with symmetry, having the volcano centred and the trumpet running through the middle like lava. All text has also been centred.

  •  Alignment:

I aligned the text to lead the eye from the title of the main event through to the Date of the event, getting interest first then giving event details after.

  •  Unity:

I chose a font that reminded me of what I had seen in many of the examples I found and used it throughout while changing its size and colour for each element.

  •  Emphasis:

With the colour palette I chose, there were several dark, muted colours and a red and orange that were brighter and more vibrant.
I was able to draw attention to the instruments with this contrast in colours. 
I also emphasised the title by making the text more prominent than the rest and having black font on a light background.


To create the smoke layer I had to rotate the layer using gimp_item_transform_rotate and I exchanged the colour black to the desired colour using plug_in_exchange.

To create the info layer I created a new layer and filled it with the foreground colour.

I rotated the trumpet layer using gimp_item_transform_rotate and I exchanged the colour black to the desired colour using plug_in_exchange.

after creating the text layer, I changed the colour using gimp_text_layer_set_color.
