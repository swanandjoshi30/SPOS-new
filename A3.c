#include<jni.h>
#include<stdio.h>
#include "A3.h"

JNIEXPORT jint JNICALL Java_A3_add(JNIEnv *env,jobject obj,jint a,jint b){
	jint result = a+b;
	printf("\n%d + %d = %d\n",a,b,result);
	return result;
}

JNIEXPORT jint JNICALL Java_A3_sub(JNIEnv *env, jobject obj, jint a, jint b) {
    jint result = a - b;
    printf("\n%d - %d = %d\n", a, b, result);
    return result; // Return the result
}

JNIEXPORT jint JNICALL Java_A3_mult(JNIEnv *env, jobject obj, jint a, jint b) {
    jint result = a * b;
    printf("\n%d * %d = %d\n", a, b, result);
    return result; // Return the result
}

JNIEXPORT jint JNICALL Java_A3_div(JNIEnv *env, jobject obj, jint a, jint b) {
    if (b == 0) {
        printf("Error: Division by zero.\n");
        return 0; // Return 0 or handle error appropriately
    }
    jint result = a / b;
    printf("\n%d / %d = %d\n", a, b, result);
    return result; // Return the result
}