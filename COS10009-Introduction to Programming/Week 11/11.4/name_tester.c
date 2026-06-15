#include <stdio.h>
#include <string.h>
#include "terminal_user_input.h"

#define LOOP_COUNT 60


void print_silly_name(my_string name)
{
    int index;
    
    printf(" %s is a", name.str);
    
    for(index = 0; index < LOOP_COUNT; index++) 
    {
        printf(" silly");
    }
    
    printf(" name!\n");
}

int main()
{
    my_string name;
    
    name = read_string("What is your name? ");

    printf("\nYour name");

   
    if (strcmp(name.str, "Ms.Tram") == 0)
    {
        printf(" is an AWESOME name!\n");
    } 
    else 
    {
   
        print_silly_name(name);
    }

    return 0;
}