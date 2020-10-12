import java.util.Scanner;

public class checkPrime{

  public static void main(String[] args){

    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number : ");
    int number = sc.nextInt();

    boolean flag = true;


    if(number==1){
      System.out.println("Number is not prime");
    }
    for(int i=2;i<=Math.sqrt(number);i++){

      if(number%i==0){
          flag =false;
          break;
      }
    }

    if(flag==true){
      System.out.println("Number is Prime");
    }else{
      System.out.println("Number is Not Prime");
    }

  }
}
