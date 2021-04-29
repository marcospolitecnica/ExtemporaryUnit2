//****************************************************************************************
//Create a function that receives four integers and return the average of the max and min.
//****************************************************************************************

//including libraries

#include <stdio.h>
#include <string.h>

//start the program

char line[10];
int integer_1;
int integer_2;
int integer_3;
int integer_4;
int average;
int max;
int min;

int main(void){
	printf("Enter first number: \n");
	fgets(line, sizeof(line),stdin);
	sscanf(line, "%d", &integer_1);

	// Tells the user to input first number

	printf("Enter second number: \n");
	fgets(line, sizeof(line),stdin);
	sscanf(line, "%d", &integer_2);

	// Tells the user to input second number

	printf("Enter third number: \n");
	fgets(line, sizeof(line),stdin);
	sscanf(line, "%d", &integer_3);

	// Tells the user to input third number

	printf("Enter final number: \n");
	fgets(line, sizeof(line),stdin);
	sscanf(line, "%d", &integer_4);
  
	// Tells the user to input final number

  {
	  average = (integer_1+integer_2+integer_3+integer_4)/4; //Calculates the average
	  max = integer_4; //Max is the integer 4
	  min = integer_1; //Max is the integer 1

	  printf("Average of the numbers is: %d\n", average); //Prints average
	  printf("Maximum is %d\n", max); //Prints Maximum
	  printf("Min is %d\n", min); //Prints Min
  }
	
	return 0;
}