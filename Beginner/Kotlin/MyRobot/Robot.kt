import java.lang.Exception

class Robot() {
    val dayList = listOf("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    var day:String?= "0"
    var bookList = mutableListOf<String>("English","Maths","Computer","Data Structure","Cryptography","Python","Fun with Kotlin")

    fun giveName(){
      print("Name your Robot : ")
      val name = readLine()
      println()
        println("I am $name ,What can i do for you?")
    }

   fun setAlarm(){
       print("Enter time [hr:min pm/am] : ")
       val time = readLine()
       println()
       println(" 1. Sunday\n 2. Monday\n 3. Tuesday\n 4. Wednesday\n 5.Thursday\n 6. Friday\n 7. Saturday")
       print("Choose your day : ")
        day = readLine()
       println("Alarm has been set to $time ,${dayList[day?.toInt()!!-1]}")
   }
  fun makeCoffee(){
      var sugar : String?
      print("How do you like your coffee (Black/With Milk) :")
      val coffee= readLine()
      print("How much sugar you’ll take [1...5 spoon] :")
      sugar = readLine()
      if(sugar?.toInt()!! > 5){
          println("More than 5 spoon of sugar is harmful for your health ! want this[yes/No] ? ")
          val choice = readLine()
          if(choice?.toLowerCase() == "yes"){
              println("Your ${coffee?.toLowerCase()} is ready with $sugar spoon of sugar, Please have it !")
          }else{
              print("How much sugar you’ll take [1...5 spoon] :")
              sugar = readLine()
              println("Your ${coffee?.toLowerCase()} is ready with $sugar spoon of sugar, Please have it !")
          }
      }else{
          println("Your ${coffee?.toLowerCase()} is ready with $sugar spoon of sugar, Please have it !")
      }

  }

    fun heatWater(){
        print("Temperature you like for your bathing water (in Fahrenheit) : ")
        val temp = readLine()
        if(temp?.toInt()!! <= 112){
            println("warm water is ready for you to take bath !")
        }else{
            println("warning : High Temperature !!")
            heatWater()
        }
        println(" 1. Sunday\n 2. Monday\n 3. Tuesday\n 4. Wednesday\n 5.Thursday\n 6. Friday\n 7. Saturday")
        print("Choose your day for not taking bath : ")
        day = readLine()
        println("You should take bath daily. Do you rally want not to take bath on ${dayList[day?.toInt()!!]} [yes/no] :")
        val choice = readLine()
        if(choice?.toLowerCase() == "yes"){
            println("Ok! I will not warm water on ${dayList[day?.toInt()!!-1]} as you will not take bath.")
        }else{
            println("It's nice to hear that you will take bath daily. ")

        }
    }

    fun packBag(){
        println(" 1. Monday\n 2. Tuesday\n 3. Wednesday\n 4.Thursday\n 5. Friday\n 6. Saturday")
        print("Tell me the day so that i can pack your bag accordingly : ")
        day = readLine()
        when(day?.toInt()){
            0 -> println("hahah.. It's sunday mam ! it's holiday")
            1->  println(" Books in Bag are : ${bookList[0]},${bookList[2]},${bookList[4]},${bookList[5]},${bookList[6]}")
            2->  println(" Books in Bag are : ${bookList[1]},${bookList[3]},${bookList[5]},${bookList[6]},${bookList[0]}")
            3->  println(" Books in Bag are : ${bookList[0]},${bookList[1]},${bookList[2]},${bookList[3]},${bookList[4]}")
            4->  println(" Books in Bag are : ${bookList[3]},${bookList[4]},${bookList[6]},${bookList[1]}}")
            5->  println(" Books in Bag are : ${bookList[0]},${bookList[2]},${bookList[4]},${bookList[5]},${bookList[6]}")
            6->  println(" Books in Bag are : ${bookList[4]},${bookList[6]},${bookList[1]}")
        }

    }
    fun makeBreakFast(){
        val breakFasts = mutableListOf<String>("Bread with peanut butter","Poha","Upma","Bread Omlet","Sandwich")
        println("Toady is ${breakFasts.random()} in breakfast !")
    }
    fun makeLunch(){
        val lunch = mutableListOf<String>("Dal, rice, veg curry, salad","rice, fish curry, salad","chapatis, chicken, salad","Aloo Parathe, chutney","rice, egg curry")
        println("Today is ${lunch.random()} in lunch !")
    }

    fun ironClothes(){
        var choose:String? ="0"
        val clothes = mutableListOf<String>("Jeans & Shirt","Jeans & top","Frock","Gown","hot pant & top","Jump Suit")
        println(" 1. Jeans & Shirt\n 2. Jeans & top\n 3. Frock\n 4. Gown\n 5. hot pant & top\n 6. Jump Suit")
        print("Choose Any : ")
        try{
        choose = readLine()
            println("${clothes[choose?.toInt()!!-1]} is ironed and ready !")
        }catch (e:Exception) {
           // println("${clothes[choose?.toInt()!!]} is ironed and ready !")
        }
    }



}