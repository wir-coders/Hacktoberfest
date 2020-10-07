/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hackToberfest;

import java.util.Scanner;

/**
 *
 * @author KIIT
 */
public class hactoberfest {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
         for ( int i=1;i<=n;i++){
            for(int j=1;j<=10;j++){
                int a =i*j;
                System.out.print(a+" ");
            }
            System.out.println();
        }
         for ( int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
                
                System.out.print("*"+" ");
            }
            System.out.println();
         }
    }
    
}
