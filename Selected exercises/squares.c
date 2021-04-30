//*************************************************************************************
//Create a program that receibes an integer and prints all squares from 1 to n (n<100).
//*************************************************************************************


//Include libraries

#include <stdio.h>
#include <math.h>

//Start the program

int main(){ //integer of the program
    char line[100]; //char for line
    int i = 0; //integer of i is 0
    int n = 0; //integer of n is 0

    printf("Enter number until 100: \n"); //Tells the user to input the number
    fgets(line, sizeof(line), stdin);//Gets the input that the user entered
    sscanf(line, "%d", &n);//scans the input

    if (n > 100) { //If n is more than 100
        printf("The maximum is 100, dummy\n"); //Tells the user the incorrect input and exits the program
    } else if (n < 1) { //else if n is less than 1
        printf("The minimum is 1, dummy\n"); //Tells the use the incorrect input and exits the program
    } else { //Else
        printf("All squares from 1 to %d are: \n", n); // Print the squares from 
        for (i = 1; i <= n; ++i) { //this for loop
            printf("%f\n", sqrt(i));//Prints the squares
        }
    }

    return 0;//exit the program
}
