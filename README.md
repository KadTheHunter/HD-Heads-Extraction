# HD Heads Extraction
 Extracted copies of HD Heads, including their cropped versions and a script to extract and crop them yourself.

# Contents
- [/hd-heads/](hd-heads/) contains the extracted textures of the HD Heads in The Shulker Archives. Some folders (`Aheago I`, `Aheago II` and all of `Panthers HD Head Packs`) contain a subfolder `/cropped/`, that contains copies of the textures that have been cropped for use as Emojis or PFPs.
- [/scripts/](scripts/) contains two scripts
  - [PNG Apply](scripts/png-apply.py) is used to append `.png` to all the texture files extracted
  - [HDH Crop](scripts/hdh-crop.py) is an interactive script used to crop the textures of a given folder to the size and area specified. _Requires the Pillow library to run._
- [Guide](Guide.md) contains all the information needed to use the scripts.

# What is this?
HD Heads were custom heads that, prior to Minecraft 1.17, were capable of displaying higher resolution textures than the typical 64x64px skins. This was accomplished by uploading high resolution textures to the _Minecraft: Education Edition_ website, and then creating custom heads that used them in-game. 

While many of the HD Heads created by the community have little or no value (simply being common images, memes and logos), there were several collections that were largely or even entirely made of custom artwork.

While Minecraft 1.17+ prevents the textures from being loaded, mods such as _CustomSkinLoader_ can be used to bypass the restrictions and load them anyway. (Check out my post '[Restoring HD Heads](https://kadthehunter.github.io/ShulkerArchives/guides/restoring-hd-heads/)' for more information!)

I took the collection of HD Heads I've amassed within [The Shulker Archives](https://kadthehunter.github.io/ShulkerArchives/), and carefully extracted all the textures I could. This was done by loading them in a clean Minecraft instance, one box at a time, and saving copies of the files that appeared in `.minecraft/assets/skins/`.

Once I had obtained all the raw files (and sorted them into folders relevant to their in-game boxes), I ran two scripts on them: [PNG Apply](scripts/png-apply.py), which appended `.png` to the end of each file, and then on specific folders I ran [HDH Crop](scripts/hdh-crop.py) which created copies of the textures with the blank space/author credit cropped of, for use as emojis or profile pictures.

I've no idea if anyone will ever find this useful, but I've wanted to save copies of these heads since I first encountered them, so here they are.

# Known Issues/Quirks
There are two major issues/quirks with the current set of images:
1. Some folders do not contain as many textures as there are heads in their in-game Shulker Box counterparts. 
   1. This is because CSL (and/or Minecraft?) caches textures, so if I loaded HD Head 1 in Box A and saved the texture file, and then loaded it again in Box B, it won't create another copy of that heads texture file unless I restarted Minecraft between those boxes. Because of this I only managed to save the texture file in Box As folder.
   2. While this does (inadvertently) prevent duplicates, I do plan to re-extract them in the future with restarts between each box so that the folders are more accurate representations of each collection.
2. One of the boxes (Just Some Heads II) caused major issues when extracting, and as a result none of its heads textures have been saved.
   1. I am still unsure _why_ it causes problems, especially as it's loaded fine prior to now, but I also know it doesn't contain much of anything important and thus isn't of particularly high priority in fixing.