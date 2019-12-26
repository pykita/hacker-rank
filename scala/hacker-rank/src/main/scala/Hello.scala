package example

object Main {
    def getMoneySpent(keyboards: Array[Int], drives: Array[Int], b: Int): Int = {
        var result = -1

        for(keyboardPrice <- keyboards) {
            for(drivePrice <- drives) {
                val currentDeal = keyboardPrice + drivePrice
                if(currentDeal > result && currentDeal <= b)
                    result = currentDeal
            }
        }

        result
    }

    def main(args: Array[String]) {
        // val stdin = scala.io.StdIn

        // val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

        // val bnm = stdin.readLine.split(" ")

        val b = 10//bnm(0).trim.toInt

        // val n = bnm(1).trim.toInt

        // val m = bnm(2).trim.toInt

        val keyboards = Array(3, 1) //)stdin.readLine.split(" ").map(_.trim.toInt)

        val drives = Array(5, 2, 8) //stdin.readLine.split(" ").map(_.trim.toInt)
        /*
         * The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
         */

        val moneySpent = getMoneySpent(keyboards, drives, b)

        Console.println(moneySpent)

        // printWriter.close()
    }
}
