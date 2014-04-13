package main

import (
    "log"
    "math"
    "strconv"
    "os"
)

func TNumberToIndex(triangle_number int) int {
    return int(math.Ceil(
        (math.Sqrt(8 * float64(triangle_number) + 1) - 1) / 2))
}

func Count1DRectangles(limit int) []int {
    rectangles := make([]int, TNumberToIndex(limit) + 1)
    var i int
    for i = 1; rectangles[i - 1] < limit; i += 1 {
        rectangles[i] = rectangles[i - 1] + i
    }
    return rectangles
}

func GetClosest(num int, rectangles []int, index int) (int, int) {
    smaller_index, larger_index, i := 0, 0, 1
    index_rectange := rectangles[index]
    for ; i < index; i += 1 {
        r := rectangles[i] * index_rectange
        if (r > num) {
            larger_index = i
            break
        } else {
            smaller_index = i
        }
    }
    smaller_distance := int(math.Abs(
        float64(num - rectangles[smaller_index] * index_rectange)))
    larger_distance := int(math.Abs(
        float64(num - rectangles[larger_index] * index_rectange)))
    if smaller_distance < larger_distance {
        return smaller_index * index, smaller_distance
    } else {
        return larger_index * index, larger_distance
    }
}

func main() {
    parsed, _ := strconv.ParseInt(os.Args[1], 10, 32)
    num := int(parsed)
    rectangles := Count1DRectangles(num)
    closest := num
    closest_area := 0
    for i := len(rectangles) - 1; i > 1; i -= 1 {
        area, distance := GetClosest(num, rectangles, i)
        if distance < closest {
            closest = distance
            closest_area = area
        }
    }
    log.Println(closest_area)
}
