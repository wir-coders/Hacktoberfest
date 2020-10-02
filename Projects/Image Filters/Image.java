import image.Pixel;
import image.SimplePicture;
import java.awt.Color;

/**
 * Simple class used to represent an image.
 *
 * Internally, it stores the image data as a 2D array of Color objects where
 * each element in the array represents one pixel in the given image object.
 */
public class Image {

    // DO NOT CHANGE
    public static Image dummy = new Image(new Color[][]{{Color.white}});

    // Member variable used to store the pixels of the Image object
    private Color[][] pixels;

    // Member variables used to store the width and height of the Image object
    private int width;
    private int height;

    /**
     * Constructor that creates a new Image object from the image file specified by
     * the given path.
     */
    public Image(String path) {
        // Use SimplePicture to parse file and convert Pixel object
        // to Color object for this Image object
        SimplePicture pic = new SimplePicture(path);
        Pixel[] pixelsToLoad = pic.getPixels();
        this.width = pic.getWidth();
        this.height = pic.getHeight();
        this.pixels = new Color[this.height][this.width];
        for (int row = 0; row < this.height; row++) {
            for (int col = 0; col < this.width; col++) {
                Pixel p = pixelsToLoad[row * width + col];
                this.pixels[row][col] = new Color(p.getRed(), p.getGreen(), p.getBlue());
            }
        }
    }

    /**
     * Constructor that creates a new Image object from the given pixels.
     */
    public Image(Color[][] pixelsToLoad) {
        // Make a copy of the pixels array to avoid mutating this Image object
        this.width = pixelsToLoad[0].length;
        this.height = pixelsToLoad.length;
        this.pixels = new Color[this.height][this.width];
        for (int row = 0; row < this.height; row++) {
            for (int col = 0; col < this.width; col++) {
                this.pixels[row][col] = pixelsToLoad[row][col];
            }
        }
    }

    /**
     * Gets the distance between two colors
     */
    public static double colorDistance(Color color1, Color color2) {
        int redDistance = color1.getRed()-color2.getRed();
        int greenDistance = color1.getGreen()-color2.getGreen();
        int blueDistance = color1.getBlue()-color2.getBlue();
        int totalDistance = redDistance * redDistance +
            greenDistance * greenDistance +
            blueDistance * blueDistance;
        return totalDistance / 1000.0;
    }

    /**
     * Visualizes this Image object in an interactive window.
     */
    public void explore() {
        SimplePicture picToExplore = new SimplePicture(this.width, this.height);
        for (int row = 0; row < this.height; row++) {
            for (int col = 0; col < this.width; col++) {
                picToExplore.setBasicPixel(col, row, this.pixels[row][col].getRGB());
            }
        }
        picToExplore.explore();
    }

    /**
     * Returns the width of this Image object.
     */
    public int getWidth() {
        return this.width;
    }

    /**
     * Returns the height of this Image object.
     */
    public int getHeight() {
        return this.height;
    }

    /**
     * Returns a copy of the pixels of this Image object.
     */
    public Color[][] getPixels2D() {
        Color[][] copy = new Color[this.height][this.width];
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                copy[row][col] = this.pixels[row][col];
            }
        }
        return copy;
    }

    /**
     * Returns a String representation of this Image object
     */
    @Override
    public String toString() {
        String pixelRef = this.pixels.toString();
        String p = pixelRef.substring(pixelRef.indexOf("@"));
        return "Image[width=" + this.width + ", height=" + this.height + ", pixels=" + p + "]";
    }

    /**
     * A Canvas Constructor that creates a new Image object
     * that is a canvas of the given color with the given dimensions.
     */
    public Image(int widthIn, int heightIn, Color color) {
        

          this.width= widthIn;
          this.height=heightIn;
          this.pixels= new Color[heightIn][widthIn];
          for(int row=0;row<this.height;row++){
            for(int col=0;col<this.width;col++){
              this.pixels[row][col]= color;
            }
          }
    }
    /**crops an image */
    public Image crop(int topLeftX, int topLeftY, int bottomRightX, int bottomRightY) {

        int ht=bottomRightY-topLeftY;
        int wt=bottomRightX-topLeftX;


        Color[][] pixels = this.getPixels2D();
        Color[][] cropped = new Color[ht][wt];
        int row2=topLeftY;
        for(int row=0;row<ht && row2<=bottomRightY-1;row++,row2++){
          int col2=topLeftX;
          for(int col=0;col<wt && col2<=bottomRightX-1;col++,col2++){
            cropped[row][col]= pixels[row2][col2];
          }
        }
        return new Image(cropped);
    }
    /** Overlays Images */
    public Image overlay(Image bg, int topLeftX, int topLeftY) {
      Color[][] arr = this.getPixels2D();
      Color[][] bcg= bg.getPixels2D();
      Color[][] overlayed= new Color[bg.getHeight()][bg.getWidth()];
      int ht=topLeftY;
      int wt=topLeftX;
      for(int row1=0;row1<bg.getHeight();row1++){
        for(int col1=0;col1<bg.getWidth();col1++){
          overlayed[row1][col1]=bcg[row1][col1];
        }
      }
      int tly= topLeftY;
      for(int row=0;tly<topLeftY+this.getHeight();row++,tly++){
        int tlx=topLeftX;
        for(int col=0;tlx<topLeftX+this.getWidth();col++,tlx++){
          overlayed[tly][tlx]= arr[row][col];
        }
      }

        return new Image(overlayed);
    }
    /** chroma keying */
    public Image chromakey(Image bg, Color key, double threshold) {
        Color[][] chromakeyed= this.getPixels2D();
        Color[][] bcground= bg.getPixels2D();
        for(int row=0;row<bg.getHeight();row++){
          for(int col=0;col<bg.getWidth();col++){
            if(colorDistance(chromakeyed[row][col],key)<threshold){
              chromakeyed[row][col]=bcground[row][col];
            }
          }
        }
        return new Image(chromakeyed);
    }
    // flips image horizontally
    public Image flipHorizontal() {
      Color[][] flipped= this.getPixels2D();
      Color[][] arr = this.getPixels2D();
        for(int row=0;row<this.getHeight();row++){
          for(int col=0;col<this.getWidth();col++){
            flipped[row][col]=arr[this.getHeight()-row-1][col];
          }
        }
        return new Image(flipped);
    }
}
