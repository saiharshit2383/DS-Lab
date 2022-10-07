// Insertion Sort Program
#include<stdio.h>
int main(){
    int a[5] = {76, 89, 12, 34, 9}, n = 5, i, j, temp;
    for(i = 1; i < n; i++){
        temp = a[i];
        j = i - 1;
        while(j >= 0 && a[j] > temp){
            a[j + 1] = a[j];   
            j--;
        }
        a[j + 1] = temp;  
        }
    printf("Sorted array:");
    for(i = 0; i < n; i++){
        printf(" %d", a[i]);
    }
}