#include "example.h"

int sum_list(int arr[], unsigned int length) {
  int sum = 0;

  for (unsigned int i = 0; i < length; i++)
    sum += arr[i];

  return sum;
}
