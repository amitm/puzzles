def print_matrix(matrix)
  matrix.each do |row|
    row.each do |item|
      print "#{item} "
    end
    print "\n"
  end
  print "\n\n"
end

def copy_matrix(matrix)
  copy = Array.new
  matrix.each do |row|
    copy << Array.new(row)
  end
  copy
end

def verified(matrix)
  matrix.each do |row|
    row.each do |item|
      if item == 0
        return false
      end
    end
  end
  true
end

def search(x, y, matrix)
  if x < 0 or x >= matrix.length or y < 0 or y >= matrix[0].length
    return 0
  end
  
  if matrix[x][y] == 3
    return verified(matrix) ? 1 : 0
  end
  
  if matrix[x][y] == 1
    return 0
  end
  
  matrix[x][y] = 1
  
  return search(x + 1, y, copy_matrix(matrix)) +
         search(x - 1, y, copy_matrix(matrix)) +
         search(x, y + 1, copy_matrix(matrix)) +
         search(x, y - 1, copy_matrix(matrix))
end

#spec = [[1, 0, 0, 0],
#    		[0, 0, 0, 0],
#    		[0, 0, 3, 1]]
spec = [[2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 1, 1]]

puts search(0, 1, copy_matrix(spec)) + search(0, 1, copy_matrix(spec))
