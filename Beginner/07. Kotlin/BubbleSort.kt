class BubbleSort {
    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val array = arrayOf(64, 34, 25, 12, 22, 11, 90)
            println("Before Sorted")
            printArray(array)

	    bubbleSort(array)
            println("Sorted Array")
            printArray(array)
        }

        private fun printArray(arr: Array<Int>) {
            for (element in arr) {
                print("$element ")
            }
            println()
        }

        private fun bubbleSort(arr: Array<Int>) {
            for (i in 0 until arr.size - 1) {
                for (j in 0 until arr.size-i-1) {
                    if (arr[j] > arr[j+1]) {
                        val temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
                    }
                }
            }
        }
    }
}
