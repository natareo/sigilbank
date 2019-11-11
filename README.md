# sigilbank

Prefabricated Azimuth sigils, ready for inclusion in other projects.

After `git clone`ing this repo, `cd` into it and run:

    npm install urbit-sigil-js
    npm install upper-case

Then create sigils using:

    python sigilbank.py --pixelsize 128
    node out.js

and visit `localhost:8080` to generate SVGs in `working/`.

    python svg2png.py

to convert SVGs in `svg/128` to PNGs.  (I.e., you need to copy from `working/` to `svg/$SIZE` first.  Sizes can be anything appropriate, but are numeric.)

Or just use the sigils in `svg/` and `png/`.  You can link directly or download them.
