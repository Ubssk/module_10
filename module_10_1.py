import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write("Какое-то слово №{}\n".format(i))
            time.sleep(0.1)
    print("Завершилась запись в файл {}".format(file_name))

# Однопоточный вариант
start_time = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time = time.time()
print("Время выполнения функций: {} секунд".format(end_time - start_time))

# Многопоточный вариант
start_time = time.time()

threads = []

t1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
threads.append(t1)
t2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
threads.append(t2)
t3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
threads.append(t3)
t4 = threading.Thread(target=write_words, args=(100, "example8.txt"))
threads.append(t4)

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print("Время выполнения потоков: {} секунд".format(end_time - start_time))