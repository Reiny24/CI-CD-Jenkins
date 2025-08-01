#include <stdio.h>
#include <math.h>

int main() {
  int lab = 3;       // Номер лабораторної
  int variant = 1;   // Номер варіанту
  double alpha;      // Вхідне значення
  double z1, z2;     // Результати обчислення

  printf("%d\n", lab);     // Виводимо номер лабораторної
  printf("%d\n", variant); // Виводимо номер варіанту

  scanf("%lf", &alpha);    // Зчитуємо значення alpha з вводу

  // Обчислення згідно з умовою
  z1 = 2 * pow(sin(3 * M_PI - 2 * alpha), 2) * pow(cos(5 * M_PI + 2 * alpha), 2);
  z2 = 0.25 - 0.25 * sin(2.5 * M_PI - 8 * alpha);

  // Виводимо результат у форматі "z1 z2"
  printf("%.6f %.6f\n", z1, z2);

  return 0;
}


///

#include <stdio.h>
#include <math.h>

int main() {
    int lab = 3;       // Номер лабораторної
    int variant = 4;   // Номер варіанту
    double m, n;       // Вхідні значення
    double z1, z2;     // Результати обчислення

    printf("%d\n", lab);     // Виводимо номер лабораторної
    printf("%d\n", variant); // Виводимо номер варіанту

    // Зчитуємо значення m і n з вводу
    scanf("%lf %lf", &m, &n);

    // Обчислення згідно з формулами
    z1 = ((m - 1) * sqrt(m) - (n - 1) * sqrt(n)) / 
         (sqrt(pow(m, 3) * n + n * m + pow(m, 2) - m));
    z2 = (sqrt(m) - sqrt(n)) / m;

    // Виводимо результат у форматі "z1 z2"
    printf("%.6f %.6f\n", z1, z2);

    return 0;
}
