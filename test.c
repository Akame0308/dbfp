#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct data{
    char student_id[12];
    unsigned int course_id;
    char course_name[48];
};

int main(void)
{
    struct data test;
    memset(&test,0,sizeof(struct data));
    FILE* f = fopen("data.dat","rb+");
    int tmp =0;
    while(1)
    {
        scanf("%d",&tmp);
        fseek(f,tmp*64,0);
        fread(&test,64,1,f);
        printf("%-12s %04d %-48s\n",test.student_id,test.course_id,test.course_name);
    }
}