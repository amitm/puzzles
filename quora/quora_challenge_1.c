#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#import <math.h>

int verified_count = 0;

/**
 * create_matrix takes the number or rows and columns
 * to represent the cooling duct. Instead of using integers.
 * We are using chars to get the most compact set of data
 * Since all we need is 2 bits to represent the combinations
 */ 
char *create_matrix(int rows, int columns) {
  int size = rows * columns;
  // mutiply the size of char by 4 because we need 2 bits 
  int num_elements = ceil(1.0 * size / (sizeof(char) * 4));
  char *matrix = (char *)malloc(num_elements * sizeof(char));
  memset(matrix, 0, num_elements);
  // set the unused bits to 1
  matrix[num_elements - 1] = (~0 << (num_elements - size / (sizeof(char) * 4))) ^ ~0;
  
  return matrix;
}

char get_element(char *matrix, int rows, int columns, int row, int column) {
  int index = (row * columns + column) / (sizeof(char) * 4);
  int offset = (row * columns + column) % (sizeof(char) * 4);
  return 3 & (matrix[index] >> (8 * sizeof(char) - 2 * (1 + offset)));
}

void set_element(char *matrix, int rows, int columns, int row, int column, char element) {
  if (row < 0 || row >= rows || column < 0 || column >= columns) { return; }
  int index = (row * columns + column) / (sizeof(char) * 4);
  int offset = (row * columns + column) % (sizeof(char) * 4);
  matrix[index] = matrix[index] | (element << (8 * sizeof(char) - 2 * (1 + offset)));
}

void print_matrix(char *matrix, int rows, int columns) {
  int i, j;
  for (i = 0; i < rows; i += 1) {
    for (j = 0; j < columns; j += 1) {
      printf("%d ", get_element(matrix, rows, columns, i, j));
    }
    printf("\n");
  }
  printf("\n");
}

int verified(char *matrix, int rows, int columns) {
  int num_elements = ceil(1.0 * rows * columns / (sizeof(char) * 4));
  int i = 0;
  char mask = ~0;
  for (i = 0; i < num_elements; i += 1) { 
    if ((matrix[i] ^ mask) != 0) {
      return 0;
    }
  }
  verified_count += 1;
  printf("%d\n", verified_count);
  return 1;
}

int search(char *matrix, int rows, int columns, int row, int column) {
  char *left, *right, *top, *bottom;
  int num_elements = ceil(1.0 * rows * columns / (sizeof(char) * 4));
  
  if (row < 0 || row >= rows || column < 0 || column >= columns) {
    return 0;
  }
  
  print_matrix(matrix, rows, columns);
  
  char element = get_element(matrix, rows, columns, row, column);
  if (element == 2) {
    set_element(matrix, rows, columns, row, column, 3);
    return verified(matrix, rows, columns);
  }
  
  if (element == 3) {
    printf("--- FAIL ----\n");
    return 0;
  }
  
  set_element(matrix, rows, columns, row, column, 3);
  
  left = create_matrix(rows, columns);
  memcpy(left, matrix, num_elements);
  right = create_matrix(rows, columns);
  memcpy(right, matrix, num_elements);
  bottom = create_matrix(rows, columns);
  memcpy(bottom, matrix, num_elements);
  top = create_matrix(rows, columns);
  memcpy(top, matrix, num_elements);

  set_element(right, rows, columns, row + 1, column, 1);
  set_element(left, rows, columns, row - 1, column, 1);
  set_element(bottom, rows, columns, row, column + 1, 1);
  set_element(top, rows, columns, row, column - 1, 1);
  
  int total = search(left, rows, columns, row - 1, column) +
              search(right, rows, columns, row + 1, column) +
              search(top, rows, columns, row, column - 1) +
              search(bottom, rows, columns, row, column + 1);
  

  free(left);
  free(right);
  free(top);
  free(bottom);
  return total;
}



int main(int argc, char *argv[]) {
  int rows = 8; 
  int columns = 7; //4;
  char *matrix = create_matrix(rows, columns);
  
  /*
  set_element(matrix, rows, columns, 0, 0, 1);
  set_element(matrix, rows, columns, 0, 1, 0);
  set_element(matrix, rows, columns, 0, 2, 0);
  set_element(matrix, rows, columns, 0, 3, 0);
  
  set_element(matrix, rows, columns, 1, 0, 0);
  set_element(matrix, rows, columns, 1, 1, 0);
  set_element(matrix, rows, columns, 1, 2, 0);
  set_element(matrix, rows, columns, 1, 3, 0);
  
  set_element(matrix, rows, columns, 2, 0, 0);
  set_element(matrix, rows, columns, 2, 1, 0);
  set_element(matrix, rows, columns, 2, 2, 2);
  set_element(matrix, rows, columns, 2, 3, 3);
  */
  
  set_element(matrix, rows, columns, 0, 0, 1);
  set_element(matrix, rows, columns, 0, 1, 0);
  set_element(matrix, rows, columns, 0, 2, 0);
  set_element(matrix, rows, columns, 0, 3, 0);
  set_element(matrix, rows, columns, 0, 4, 0);
  set_element(matrix, rows, columns, 0, 5, 0);
  set_element(matrix, rows, columns, 0, 6, 0);
  
  set_element(matrix, rows, columns, 1, 0, 0);
  set_element(matrix, rows, columns, 1, 1, 0);
  set_element(matrix, rows, columns, 1, 2, 0);
  set_element(matrix, rows, columns, 1, 3, 0);
  set_element(matrix, rows, columns, 1, 4, 0);
  set_element(matrix, rows, columns, 1, 5, 0);
  set_element(matrix, rows, columns, 1, 6, 0);
  
  set_element(matrix, rows, columns, 2, 0, 0);
  set_element(matrix, rows, columns, 2, 1, 0);
  set_element(matrix, rows, columns, 2, 2, 0);
  set_element(matrix, rows, columns, 2, 3, 0);
  set_element(matrix, rows, columns, 2, 4, 0);
  set_element(matrix, rows, columns, 2, 5, 0);
  set_element(matrix, rows, columns, 2, 6, 0);
  
  set_element(matrix, rows, columns, 3, 0, 0);
  set_element(matrix, rows, columns, 3, 1, 0);
  set_element(matrix, rows, columns, 3, 2, 0);
  set_element(matrix, rows, columns, 3, 3, 0);
  set_element(matrix, rows, columns, 3, 4, 0);
  set_element(matrix, rows, columns, 3, 5, 0);
  set_element(matrix, rows, columns, 3, 6, 0);
  
  set_element(matrix, rows, columns, 4, 0, 0);
  set_element(matrix, rows, columns, 4, 1, 0);
  set_element(matrix, rows, columns, 4, 2, 0);
  set_element(matrix, rows, columns, 4, 3, 0);
  set_element(matrix, rows, columns, 4, 4, 0);
  set_element(matrix, rows, columns, 4, 5, 0);
  set_element(matrix, rows, columns, 4, 6, 0);
  
  set_element(matrix, rows, columns, 5, 0, 0);
  set_element(matrix, rows, columns, 5, 1, 0);
  set_element(matrix, rows, columns, 5, 2, 0);
  set_element(matrix, rows, columns, 5, 3, 0);
  set_element(matrix, rows, columns, 5, 4, 0);
  set_element(matrix, rows, columns, 5, 5, 0);
  set_element(matrix, rows, columns, 5, 6, 0);
  
  set_element(matrix, rows, columns, 6, 0, 0);
  set_element(matrix, rows, columns, 6, 1, 0);
  set_element(matrix, rows, columns, 6, 2, 0);
  set_element(matrix, rows, columns, 6, 3, 0);
  set_element(matrix, rows, columns, 6, 4, 0);
  set_element(matrix, rows, columns, 6, 5, 0);
  set_element(matrix, rows, columns, 6, 6, 0);
  
  set_element(matrix, rows, columns, 7, 0, 2);
  set_element(matrix, rows, columns, 7, 1, 0);
  set_element(matrix, rows, columns, 7, 2, 0);
  set_element(matrix, rows, columns, 7, 3, 0);
  set_element(matrix, rows, columns, 7, 4, 0);
  set_element(matrix, rows, columns, 7, 5, 3);
  set_element(matrix, rows, columns, 7, 6, 3);
  
  print_matrix(matrix, rows, columns);
  
  printf("%d\n", search(matrix, rows, columns, 0, 0));
  return 0;
}