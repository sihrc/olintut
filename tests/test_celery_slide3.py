from olintut.celery_slide3 import magic_celery_task


if __name__ == "__main__":
    task_result_1 = magic_celery_task.delay()
    print(f"Launched magic_celery_task 1")
    task_result_2 = magic_celery_task.delay()
    print(f"Launched magic_celery_task 2")

    print(f"magic number 1 {task_result_1.get()}")  # blocking call
    print(f"magic number 2 {task_result_2.get()}")  # blocking call
