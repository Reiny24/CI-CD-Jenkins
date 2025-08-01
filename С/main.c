#include <stdio.h>
void process_string(char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (i % 2 != 0) { // Even index -> lowercase
            if (str[i] >= 'A' && str[i] <= 'Z') str[i] += 32;
        } else { // Odd index -> uppercase
            if (str[i] >= 'a' && str[i] <= 'z') str[i] -= 32;
        }
    }
}

int main() {
    char input[100];
    int lab = 1; // Номер лабораторної
    int variant = 5; // Номер варіанту
    printf("%d\n", lab); // Виводимо номер лабораторної
    printf("%d\n", variant); // Виводимо номер варіанту
    fgets(input, sizeof(input), stdin);  // Read input
    process_string(input);
    printf("%s", input);  // Output only the transformed string
    fgets(input, sizeof(input), stdin);  // Read input
    return 0;
}