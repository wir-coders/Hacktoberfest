import java.awt.Color;

public class ImageTester {

    // ------------------------------------------------------------------------
    // Tests
    // ------------------------------------------------------------------------

    public static void testCanvas() {
        // Create a blue canvas with width 5 and height 10
        Image canvas1 = new Image(5, 10, Color.blue);

        // Verify the result is a 10x5 blue canvas
        //canvas1.explore();

        //test case2
        Image canvas2 = new Image(1,1,Color.red);
        // Verify the result is a 1x1 red canvas
        canvas2.explore();

        //test case 3
        Image cavas3 = new Image(1,15,Color.black);
        // Verify the result is a 15x1 black canvas
        //canvas3.explore();
    }

    public static void testCrop() {
        // Create a 4x4 2D array
        Color[][] test1 = { { Color.black, Color.black, Color.red, Color.red }, // row0
                { Color.black, Color.black, Color.red, Color.red }, // row1
                { Color.black, Color.black, Color.red, Color.red }, // row2
                { Color.black, Color.black, Color.black, Color.black } // row3
        };

        // Create an image from the array and crop the bottom right corner
        Image img1 = new Image(test1);
        Image cropped1 = img1.crop(2, 0, 4, 3);

        // Visualize the cropped picture
        //cropped1.explore();

        Image img = new Image("images/pixel-heart.png");
        Image cropped2 = img.crop(100, 100, 500, 500);

        //cropped2.explore();

        //test 2
        Color[][] test2={
          {Color.red, Color.black, Color.red, Color.red},   // row0
          {Color.blue, Color.blue, Color.red, Color.red},   // row1
          {Color.blue, Color.blue, Color.blue, Color.blue},   // row2
          {Color.red, Color.red, Color.red, Color.red}, //row3
          {Color.red, Color.red, Color.red, Color.red} //row 4
        };
        Image img2 = new Image(test2);
        Image result2= img2.crop(0,0,1,1);
        //result2.explore();

        Color[][] test3={
          {Color.blue, Color.blue, Color.blue, Color.red},   // row0
          {Color.blue, Color.blue, Color.blue, Color.red},   // row1
          {Color.blue, Color.blue, Color.blue, Color.blue},   // row2
          {Color.red, Color.blue, Color.blue, Color.red}, //row3
          {Color.black, Color.black, Color.black, Color.black}, //row 4
          {Color.black, Color.black, Color.black, Color.black} //row 5
        };
        Image img3 = new Image(test3);
        Image result3= img3.crop(1,2,3,4);
        result3.explore();
    }

    public static void testOverlay() {
        // Create a 4x4 2D array
        Color[][] bgTest1 = {
            { Color.black, Color.black, Color.black, Color.black }, // row0
            { Color.black, Color.black, Color.black, Color.black }, // row1
            { Color.black, Color.black, Color.black, Color.black }, // row2
            { Color.black, Color.black, Color.black, Color.black } // row3
        };

        // Create a 3x2 2D array
        Color[][] fgTest1 = { { Color.red, Color.red }, { Color.red, Color.red }, { Color.red, Color.red } };

        // Create an image from the array and crop the bottom right corner
        Image bgImg1 = new Image(bgTest1);
        Image fgImg1 = new Image(fgTest1);
        Image overlayed1 = fgImg1.overlay(bgImg1, 1, 1);

        // Visualize the cropped picture
        overlayed1.explore();

        // Adding two more test cases
          Color[][] test1_2 = {{new Color(0, 0, 0)}};
          Color[][] test1_1={
            {Color.blue, Color.blue, Color.blue, Color.red},   // row0
            {Color.blue, Color.blue, Color.blue, Color.red},   // row1
            {Color.blue, Color.blue, Color.blue, Color.blue},   // row2
            {Color.red, Color.blue, Color.blue, Color.red}, //row3
            {Color.black, Color.black, Color.black, Color.black}, //row 4
            {Color.black, Color.black, Color.black, Color.black} //row 5
          };
          Image img3 = new Image(test1_1);
          Image img2= new Image(test1_2);
          Image overlayed2= img2.overlay(img3,2,3);
          // Visualize the cropped picture
          overlayed2.explore();

          //test 3
          Color[][] test2_1 = {{new Color(0, 0, 0)}};
          Color[][] test2_2 = {{new Color(255, 255, 255)}};
          Image img4 = new Image(test2_1);
          Image img5= new Image(test2_2);
          Image overlayed3= img5.overlay(img4,0,0);
          // Visualize the cropped picture
          overlayed3.explore();

    }

    public static void testChromakey() {
        // Create a 4x4 2D array
        Color[][] bgTest1 = {
            { Color.red, Color.red, Color.red, Color.red }, // row0
            { Color.red, Color.red, Color.red, Color.red }, // row1
            { Color.red, Color.red, Color.red, Color.red }, // row2
            { Color.red, Color.red, Color.red, Color.red } // row3
        };

        // Create a 3x2 2D array
        Color[][] fgTest1 = {
            { Color.green, Color.green, Color.black, Color.black }, // row0
            { Color.green, Color.green, Color.black, Color.black }, // row1
            { Color.green, Color.green, Color.black, Color.black }, // row2
            { Color.green, Color.green, Color.black, Color.black } // row3
        };

        // Create an image from the array and crop the bottom right corner
        Image bgImg1 = new Image(bgTest1);
        Image fgImg1 = new Image(fgTest1);
        Image chromakeyed1 = fgImg1.chromakey(bgImg1, Color.green, 1);

        // Visualize the cropped picture
        //chromakeyed1.explore();

        //test 2
        Color[][] test1_1 = {{new Color(0, 0, 0)}};
        Image img2 = new Image(test1_1);
        Color[][] test1_2 = {{new Color(255, 255, 255)}};
        Image img3 = new Image(test1_2);
        Image chromakeyed2=img2.chromakey(img3,Color.black,1);
        // Visualize the cropped picture
        //chromakeyed2.explore();
        // Create a 4x4 2D array
        Color[][] bgTest3 = {
            { Color.red, Color.red, Color.red, Color.red }, // row0
            { Color.red, Color.red, Color.red, Color.red }, // row1
            { Color.red, Color.red, Color.red, Color.red }, // row2
            { Color.red, Color.red, Color.red, Color.red } // row3
        };

        // Create a 3x2 2D array
        Color[][] fgTest3 = {
            { Color.black, Color.black, Color.black, Color.black }, // row0
            { Color.black, Color.green, Color.green, Color.black }, // row1
            { Color.black, Color.green, Color.green, Color.black }, // row2
            { Color.black, Color.black, Color.black, Color.black } // row3
        };
        Image bgImg3 = new Image(bgTest3);
        Image fgImg3 = new Image(fgTest3);
        Image chromakeyed3 = fgImg3.chromakey(bgImg3, Color.black, 1);
        chromakeyed3.explore();
    }

    public static void testFlipHorizontal() {
        // Create 4x4 2D array
        Color[][] test1 = { { Color.black, Color.black, Color.black, Color.black }, // row0
                { Color.black, Color.black, Color.black, Color.black }, // row1
                { Color.red, Color.red, Color.red, Color.red }, // row2
                { Color.red, Color.red, Color.red, Color.red } // row3
        };

        // First visualize the original image
        Image img1 = new Image(test1);
        //img1.explore();

        // Flip the image and visualize the result
        Image flippedImg1 = img1.flipHorizontal();
        //flippedImg1.explore();

        //test 2
        Color[][] test1_1 = {{new Color(0, 0, 0)}};
        Image img2 = new Image(test1_1);
        Image flippedImg2 = img2.flipHorizontal();
        //flippedImg2.explore();
        Color[][] test3 = { { Color.red, Color.black, Color.black, Color.green }, // row0
                { Color.black, Color.black, Color.black, Color.black }, // row1
                { Color.black, Color.black, Color.black, Color.black }, // row2
                { Color.green, Color.black, Color.black, Color.red } // row3
              };
        Image img3 = new Image(test3);
        Image flippedImg3 = img3.flipHorizontal();
        flippedImg3.explore();

    }

    // ------------------------------------------------------------------------
    // Main Method
    // ------------------------------------------------------------------------

    public static void main(String[] args) {
        // You may want to uncomment one test at a time
        // NOTE: testCanvas will error unless the canvas constructor is implemented
        // please implement the canvas constructor before uncommenting that line.

        // testCanvas();
        //testCrop();
        // testOverlay();
         //testChromakey();
         //testFlipHorizontal();


        Color[][] bg= {
            { Color.black, Color.black, Color.black, Color.black }, // row0
            { Color.black, Color.black, Color.black, Color.black }, // row1
            { Color.black, Color.black, Color.black, Color.black }, // row2
            { Color.black, Color.black, Color.black, Color.black }, // row3
            { Color.black, Color.black, Color.black, Color.black }, // row4
            { Color.black, Color.black, Color.black, Color.black }, // row5
            { Color.black, Color.black, Color.black, Color.black }, // row6
            { Color.black, Color.black, Color.black, Color.black } // row7
        };
        Color[][] c1 = {
            { Color.blue, Color.blue }, // row0
            { Color.blue, Color.blue }, // row1
            { Color.red, Color.red}, // row2
            { Color.blue, Color.blue} // row3
        };
        Color[][] c2 = {
            { Color.red, Color.red }, // row0
            { Color.blue, Color.blue }, // row1
            { Color.red, Color.red}, // row2
            { Color.red, Color.red} // row3
        };
        Color[][] c3 = {
            { Color.green, Color.green }, // row0
            {Color.white, Color.white }, // row1
            { Color.green, Color.green}, // row2
            { Color.green, Color.green} // row3
        };
        Color[][] c4 = {
            { Color.white, Color.white }, // row0
            { Color.green, Color.green }, // row1
            { Color.white, Color.white}, // row2
            { Color.white, Color.white} // row3
        };
        Image bg1 = new Image(bg);
        Image img1 = new Image(c1);
        Image img2 = new Image(c2);
        Image img3 = new Image(c3);
        Image img4 = new Image(c4);
        Image flippedImg2 = img2.flipHorizontal();
        Image flippedImg3 = img3.flipHorizontal();
        Image overlayed1 = img1.overlay(bg1, 0, 0);
        Image overlayed2 = flippedImg2.overlay(overlayed1, 2, 0);
        Image overlayed3 = flippedImg3.overlay(overlayed2, 0, 4);
        Image overlayed4 = img4.overlay(overlayed3, 2, 4);
        Image cropped= overlayed4.crop(1, 2, 3, 6);
        //cropped.explore();

    }
}
