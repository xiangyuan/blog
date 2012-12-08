public: yes
tags: [bash, linux, dwm]
language: en
summary: |
    How to set a random wallpaper from a directory on bash using feh.

Set a Random Wallpaper from Bash
================================

Each time I start my X session, the desktop wallpaper is set in the `.xinitrc`
script. Until now, it was always a single file called `~/.xwallpaper-dwm.jpg`.
But today I wanted to alternate between different wallpapers instead.

The following lines of code choose a random `.jpg` or `.png` file from my
`~/.wallpapers/` directory and set it as wallpaper using `feh`:

.. sourcecode:: bash

    wp_path=/home/danilo/.wallpapers/
    image=$(ls $wp_path | grep -E '(jpg|png)$' | sort -R | tail -1)
    feh --bg-scale $wp_path/$image
