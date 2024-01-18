# gallerify

## To run in VSCode:
1.  navigate to gallerify directory
2.  activate the virtual environment by typing:
        
        source [path_to_venv/Scripts/activate]

        source c:/Users/dorot/Documents/Coding_Projects_venvs/gallerify/.venv/Scripts/activate
 
        source c:/Users/amand/dev_venvs/gallerify/.venv/Scripts/activate
3. `cd server`
4. `python ./manage.py runserver`
5. follow link in console
6. add `/draw_group` to browser url



## Front End:
* written in React
* stored in the client folder
* actually nothing's in the front end right now. things are being rendered in the back end.
    * though eventually we want to render this stuff in the fronet end because we can't scale image storage like this.

## Back end:
* written in Python
* Django?!??????
* spotify auth is in `server/server.py` though the name should be changed bc it's confusing
* the bulk of it is in `server/render_gallery.py`
    * `render_gallery.py` has three classes:
        * Gallery
        * AlbumArt
        * Frame
    * Gallery inherits from pygame library's Group class (group of sprites). this lets it inherit properties like :
        * having a surface to draw on and also letting sprites be grouped together. we also have Group.draw, which is the entry point of the app.
    * AlbumArt and Frame inherits from pygame library's Sprite class. 
        * Lets it inherit properties like having sprite dimensions, coordinates, and scale/blit functions (blit superimposes pixels onto the surface)

## For future:
* look into whether we need the pygame library if we're gonna move the rendering from back end to front end 
    * because the function for figuring out the coordinates uses the sprites' coordinates. if we move it, we'll need to work with the html coordinates
* look into rendering an image onto an html page using a url 
    * and also getting the dimensions of that image once it's actually on the screen bc that's what goes into the positioning function
* look into whether html canvas can have fixed dimensions and look into a library that can save html group of elements as a single image (like receiptify)