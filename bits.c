#include <stdio.h>
#include <stdlib.h>


/* #define MASK 2 */

void basic()
{
    int a = 0xa;
    printf("~a = %d\n", ~a);
    int b = 0x93, c = 0x3d;
    printf("b&c = %d\n", b&c);
    printf("b|c = %d\n", b|c);
    printf("b^c = %d\n", b^c);

}

void mask()
{
    const int MASK = 1;
    int flg0 = 0xfffffffe, flg1 = 0xffffffff;

    /* flg0 &= MASK; */
    printf("0x%08x MASK %d = 0x%08x\n", flg0, MASK, flg0&MASK);
    printf("0x%08x MASK %d = 0x%08x\n", flg1, MASK, flg1&MASK);


}

int main()
{
    mask();

    return 0;
}
