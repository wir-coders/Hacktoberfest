import kotlin.system.exitProcess

fun main(){
    val r1 = Robot()
    println("Do You want a Robot to make your life easy ? [yes/no] : ")
    val choice= readLine()
    if(choice?.toLowerCase() == "yes"){
        r1.giveName()
        do {
            println(" 1. Set Alarm\n 2. Make Coffee\n 3. Warm Water\n 4. Pack School Bag\n 5. Cook breakfast\n 6. Cook Lunch\n 7. Iron Clothes")
            print(" Choose Any option [1...8] : ")
            val ch = readLine()
            when (ch?.toInt()) {
                1 -> r1.setAlarm()
                2 -> r1.makeCoffee()
                3 -> r1.heatWater()
                4 -> r1.packBag()
                5 -> r1.makeBreakFast()
                6 -> r1.makeLunch()
                7 -> r1.ironClothes()
                8-> exitProcess(1)
                else -> println("Invalid Choice !! Try Again !")
            }
        }while (ch?.toInt()!=8)
    }else{
        print("We will wait when you will want a robot !")
    }

}