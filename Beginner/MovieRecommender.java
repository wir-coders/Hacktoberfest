import java.util.Scanner; //import the Scanner class

public class MovieRecommender {
    
     public static void main(String[] args){
        Scanner in = new Scanner(System.in); //Create Scanner object
        System.out.println("Select a movie genre:");
        System.out.println("1. Romance");
        System.out.println("2. Animation");
        System.out.println("3. Comedy");
        System.out.println("4. Action");
        System.out.println("5. Horror");
        
        String userGenre = in.nextLine(); //Read user input
        if (userGenre == "1" || userGenre.toLowerCase() == "romance"){
            romanceMovies();
        } else if (userGenre == "2" || userGenre.toLowerCase() == "animation"){
            animationMovies();
        } else if (userGenre == "3" || userGenre.toLowerCase() == "comedy"){
            comedyMovies();
        } else if (userGenre == "4" || userGenre.toLowerCase() == "action"){
            actionMovies();
        } else if (userGenre == "5" || userGenre.toLowerCase() == "horror"){
            horrorMovies();
        } else {
            System.out.println("Please enter a valid genre and try again.");
        }
    }
     
    static void romanceMovies(){
        System.out.println("List of recommended romance movies:");
        System.out.println("1. Titanic");
        System.out.println("2. Moulin Rouge");
        System.out.println("3. The Notebook");
        System.out.println("4. Dear John");
        System.out.println("5. A Cinderella Story");
    }
    
    static void animationMovies(){
        System.out.println("List of recommended animation movies:");
        System.out.println("1. My Neighbour Totoro");
        System.out.println("2. The Nightmare Before Christmas");
        System.out.println("3. The Lion King");
        System.out.println("4. Spirited Away");
        System.out.println("5. Wall-E");
    }
    
    static void comedyMovies(){
        System.out.println("List of recommended comedy movies:");
        System.out.println("1. Ghostbusters");
        System.out.println("2. The Hangover");
        System.out.println("3. American Pie");
        System.out.println("4. Central Intelligence");
        System.out.println("5. Home Alone");
    }
    
    static void actionMovies(){
        System.out.println("List of recommended action movies:");
        System.out.println("1. The Terminator");
        System.out.println("2. Lara Croft: Tomb Raider");
        System.out.println("3. Crouching Tiger, Hidden Dragon");
        System.out.println("4. Die Hard");
        System.out.println("5. Pacific Rim");
    }
    
    static void horrorMovies(){
        System.out.println("List of recommended horror movies:");
        System.out.println("1. The Exorcist");
        System.out.println("2. Poltergeist");
        System.out.println("3. The Conjuring");
        System.out.println("4. It");
        System.out.println("5. Let Me In");
    }
    
}