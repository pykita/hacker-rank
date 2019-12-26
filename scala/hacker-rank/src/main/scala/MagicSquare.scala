class MagicSquare(square: Array[Array[Int]]) {
    val values = (1 to 9).toSet



    val lines = List(
        List((0,0), (0,1), (0,2)),
        List((1,0), (1,1), (1,2)),
        List((2,0), (2,1), (2,2)),
        List((0,0), (1,0), (2,0)),
        List((0,1), (1,1), (2,1)),
        List((0,2), (1,2), (2,2)),
        List((0,0), (1,1), (2,2)),
        List((2,0), (1,1), (0,2)),
    )

    val meanValue = findMean()

    def isDone(): Boolean = {
        val res = lines.find((x) => meanValue != x.foldLeft(0)((acc, next) => acc + square(next._1)(next._2)))
        res.isEmpty
    }

    def getLineSum(line: List[Tuple2[Int, Int]]): Int = {
        line.foldLeft(0)((acc: Int, next) => acc + square(next._1)(next._2))
    }

    case class Line(val vector: List[Tuple2[Int, Int]], val sum: Int)

    def findNextLine(): Line = {
        val res = lines
            .map((item) => Line(item, getLineSum(item)))
            .sortBy((item: Line) => {
                Math.abs(meanValue - item.sum)
            })
        res(0)
    }

    def proceedNextElement(line: Line): Unit = {
        val stepsNum = meanValue - line.sum



        val possibleCords = line.vector.filter((item: Tuple2[Int, Int]) =>
            values contains square(item._1)(item._2) + stepsNum)
    }

    def findMean(): Int = {
        lines.foldLeft(0)((acc: Int, line) => {
            acc + line.foldLeft(0)((acc: Int, next) => {
                acc + square(next._1)(next._2)
            })
        }) / lines.size
    }
}


object Main {
    def formingMagicSquare(square: Array[Array[Int]]): Int = {
        (new MagicSquare(square)).findMean()
    }

    def testMethod(): Unit = {
        val values = (1 to 9).toSet
        println(values)
    }

    def main(args: Array[String]) = {
//        testMethod()

        val lineOne = Array(9, 3, 1)
        val lineTwo = Array(4, 4, 5)
        val lineThree = Array(6, 3, 2)

        val res = formingMagicSquare(Array(lineOne, lineTwo, lineThree))
        print(s"Hello new $res")
    }
}