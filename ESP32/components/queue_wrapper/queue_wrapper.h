#ifndef QUEUE_WRAPPER_H
#define QUEUE_WRAPPER_H

#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"

// Constants
#define QUEUE_SIZE 5
#define QUEUE_ITEM_SIZE sizeof(char *)

// Extern queue to be used across all tasks
extern QueueHandle_t queue_handle;

void queue_init();
int queue_send(char *msg);
int queue_receive(char **msg_ptr);

#endif // QUEUE_WRAPPER_H