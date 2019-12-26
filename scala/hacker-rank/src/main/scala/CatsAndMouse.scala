import scala.math.abs

object CatsAndMouse {
  def whoWins(catOnePosition: Int, catTwoPosition: Int, mousePosition: Int) : String = {
    val catOneDistance = abs(catOnePosition - mousePosition)
    val catTwoDistance = abs(catTwoPosition - mousePosition)
    if (catOneDistance < catTwoDistance) {
      return "Cat A"
    } else if (catTwoDistance < catOneDistance) {
      return "Cat B"
    } else {
      return "Mouse C"
    }

  }

  def main(args: Array[String]) : Unit = {
    println("Another class")
  }
}