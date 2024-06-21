# PNG Apply
Using the PNG Apply script is fairly straightforward:
- Get all the textures and folders into a single folder
  - _They can be sorted into sub-folders; The script will loop through every file in every sub-folder of the root provided._
- Copy that folders address
- Run the PNG Apply script, and paste in the address when prompted to


# HDH Crop
Using the HDH Crop script is a bit more complicated, and requires an understanding of how textures work for Minecraft skins.

First, lets get the script running and pointed to a folder:
- Copy the address of the folder that contains all your textures
- Run the HDH Crop script, and paste in the address when prompted to

Now for the more complicated part:

Skin textures are square images. For default Minecraft skins, the only usable size is 64px by 64px. For HD Heads, the texture can be any size, so long as it maintains the square (1:1 aspect ratio) shape.

The first thing you will be prompted for is the crop size. This should be 1/8th of one side of the texture (e.g a 2,048 x 2,048 texture would require a crop size of 256).

The next two prompts will ask for the X and Y coordinates for the Crop Box. This determines what side of the head the image will be cropped to.

All textures are based on a grid of squares in a 8x8 pattern. The only important squares for this context are the first sixteen in the top two rows.

Each square is linked to a specific part of the head; Top, Bottom, Left, Front, Right, Back. 

The X coordinate starts at 0, and adds 1/8th of the textures side for each of the squares you move over (2nd is 256, 3rd is 512, etc.).

The first rows Y is always 0, and the second rows Y is always 1/8th of the textures side (so a 2,048 x 2,048 texture would be 256), which should also be the number from the previous step (crop size)

Possible coordinates are:

- 1st Layer:
  - Top: S,0
  - Bottom: 2S,0
  - Left 0,S
  - Front: S,S
  - Right: 2S,S
  - Back: 3S,S

- 2nd Layer:
  - Top: 5S,0
  - Bottom: 6S,0
  - Left: 4S,S
  - Front: 5S,S
  - Right: 6S,S
  - Back 7S,S

An easy way to calculate it is to view the grid using zero-based numbering (0-7 instead of 1-8), and multiplying the square number by the square size.

The most common coordinates are 1st Layer Front (S,S) and 2nd Layer Front (5S,S).

To identify whether it's a 1st or 2nd layer, have a look at the whole texture; If it's left aligned then it's 1st layer, and if it's right aligned then it's 2nd layer.

Use the coordinates above and the Crop Size (1/8th of the textures side) to select the face for cropping.

Once entered, the script will loop through all images in all folders of the specified directory, creating a new sub-folder labeled `cropped` containing the cropped copies.

Due to the range of image sizes and coordinate locations, I recommend running the script one folder at a time.
