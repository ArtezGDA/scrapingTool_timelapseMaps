# scraping images from a video by using Processing

### How to:
- Download processing
- Add library video
- Replace AAA.mov by your own video file(name)
- example: "firstvideo.mov"
- Press the play button
- You can find the images in a folder in the processing folder

### [Code (link to Processing file)](https://github.com/ArtezGDA/scrapingTool_timelapseMaps/blob/master/example_code/Processing%20file%20images_from_movie/images_from_movie.pde) 

import processing.video.*;
Movie mov;
int newFrame = 0;
void setup() {
 size(640, 360);
 background(0);
 mov = new Movie(this, "AAA.mov");  
 mov.play();
}
void movieEvent(Movie m) {
 m.read();
}
void draw() {
 background(0);
 image(mov, 0, 0, width, height);
 if(frameCount % 48 == 1)
 {
   saveFrame("frames/####.png");
 }
}