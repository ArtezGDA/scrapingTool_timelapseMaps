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