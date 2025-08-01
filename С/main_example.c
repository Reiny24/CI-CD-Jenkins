#include <stdio.h>
void process_string(char *str) {
    "..."
}

int main() {
    char input[100];
    int variant = 4; // Номер варіанту
    printf("%d\n", variant); // Виводимо номер варіанту
    fgets(input, sizeof(input), stdin);  // Зчитуємо вхідний рядок
    process_string(input);
    printf("%s", input);  // Виводимо оброблений рядок
    return 0;
}
