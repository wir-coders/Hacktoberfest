import java.util.*;

class Board
{
  int[][] board = new int[3][3];

  Board()
  {
    for(int i=0;i<3;i++)
    {
      for(int j=0;j<3;j++)
      {
        board[i][j]=0;
      }
    }
  }

  public int set(int index,int val)
  {
    board[index/3][index%3]=val;
    return 0;
  }
  public int get(int index)
  {
    return board[index/3][index%3];
  }
  public boolean isFull()
  {
    int i,j;
    for(i=0;i<9;i++)
    {
        if(board[i/3][i%3]==0)
        {
          break;
        }
    }
    if(i==9)
    {
      return true;
    } 
    return false;
  }
  public boolean win(int last)
  {
    int row = last/3;
    int col = last%3;
    int trow=1,tcol=1,tdiag1=1,tdiag2=1;
    for(int i=0;i<3;i++)
    {
      if(board[row][i]!=board[row][col])
      {
        trow=0;
      }
      if(board[i][col]!=board[row][col])
      {
        tcol=0;
      }
      if(board[i][i]!=board[row][col]&&row==col)
      {
        tdiag1=0;
      }
      if(board[i][2-i]!=board[row][col]&&row==2-col)
      {
        tdiag2=0;
      }
    }
    int sum=trow+tcol;
    if(row==col)
    {
      sum+=tdiag1;
    }
    if(row==2-col)
    {
      sum+=tdiag2;
    }
    return sum>0;
  }

  public int optimal()
  {
    int a=1,optimal=0,max=-1,sum=0;
    int arr[] = new int[9];
    for(int i=0;i<9;i++)
    {
      arr[i]=9;
      if(this.get(i)==0)
      {
        this.set(i,a);
        arr[i]=this.minimax(-a,i);
        if(arr[i]>max)
        {
          max=arr[i];
        }
        this.set(i,0);
      }
    }
    Vector<Integer> idx = new Vector<Integer>();
    for(int i=0;i<9;i++)
    {
      if(arr[i]==max)
      {
        idx.add(i);
      }
    }
    int index = (int)(Math.random()*idx.size());
    optimal = (idx.get(index)).intValue();
    return optimal;
  }

  public int minimax(int a,int last)
  {
    if(this.win(last))
    {
      return board[last/3][last%3];
    }
    else if(this.isFull())
    {
      return 0;
    }
    int max=-1,min=1;
    for(int i=0;i<9;i++)
    {
      if(this.get(i)==0)
      {
        this.set(i,a);
        int k=this.minimax(-a,i);
        if(k>max&&a>0)
        {
          max=k;
        }
        if(k<min&&a<0)
        {
          min=k;
        }
        this.set(i,0);
      }
    }
    if(a>0)
    {
      return max;
    }
    return min;
  }

  public void print()
  {
    for(int i=0;i<3;i++)
    {
      for(int j=0;j<3;j++)
      {
        if(board[i][j]==0)
        System.out.print("_"+(i*3+j+1)+"_ ");
        else if(board[i][j]==-1)
        System.out.print("( ) ");
        else if(board[i][j]==1)
        System.out.print("| | ");
      }
      System.out.println();
    }
    System.out.println("\n\n");
  }
}

class Main 
{
  public static void main(String args[])
  {
    int t=0;
    Scanner sc = new Scanner(System.in);
    while(t==0)
    {
      System.out.println("1.Start 1st");
      System.out.println("2.Start 2nd");
      System.out.println("3.Exit");
      int ch = sc.nextInt();
      switch(ch)
      {
        case 1 : {
          start(1);
          break;
        }
        case 2 : {
          start(2);
          break;
        }
        case 3 : {
          t=1;
          break;
        }
        default : {
          System.out.println("Enter valid choice!!");
        }
      }
    }
  }

  public static void start(int starts) 
  {
    Scanner sc = new Scanner(System.in);
    Board b = new Board();
    System.out.println();
    while(true)
    {
      clearScreen();
      b.print();
      if(starts==2)
      {
        int optimal = b.optimal();
        b.set(optimal,1);
        clearScreen();
        b.print();
        if(b.win(optimal))
        {
          System.out.println("Computer won");
          break;
        }
      }
      if(b.isFull())
      {
        System.out.println("Tie");
        break;
      }
      while(true)
      {
        System.out.println("Enter index");
        int a = sc.nextInt();
        if(b.get(a-1)==0)
        {
          b.set(a-1,-1);
          clearScreen();
          b.print();
          if(b.win(a-1))
          {
            System.out.println("You won");
            break;
          }
          break;
        }
        else
        {
          clearScreen();
          b.print();
          System.out.println("Try Again");
        }
      }
      if(b.isFull())
      {
        System.out.println("Tie");
        break;
      }
      if(starts==1)
      {
        int optimal = b.optimal();
        b.set(optimal,1);
        clearScreen();
        b.print();
        if(b.win(optimal))
        {
          System.out.println("Computer won");
          break;
        }
      }
      if(b.isFull())
      {
        System.out.println("Tie");
        break;
      }
    }
  }  
    public static void clearScreen() 
    {  
      System.out.print("\033[H\033[2J");  
      System.out.flush();  
    }  
}