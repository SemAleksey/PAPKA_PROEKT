# «Есть два писателя, которые по очереди в течении определенного времени
# (у каждого разное) пишут в одну книгу. Данная книга очень популярна,
# у неё есть как минимум 3 фаната (читателя), которые ждут не дождутся,
# чтобы прочитать новые записи из неё. Каждый читатель и писатель
# – отдельный поток. Одновременно книгу может читать несколько читателей,
# но писать единовременно может только один писатель.»


import time
import threading


mutex = threading.RLock()
# cond = threading.Condition(mutex)
book = ""


def writer_1():
    global book
    # cond.acquire()
    mutex.acquire()
    book += "Жили были "
    mutex.release()
    # cond.notify_all()
    # cond.release()
    
     
def writer_2():
    global book
    # cond.acquire()
    mutex.acquire()
    book += "дед да баба"
    mutex.release()
    # cond.notify_all()
    # cond.release()
       

def reader_1():
    # cond.acquire()
    # cond.wait()
    mutex.acquire()
    print("Читатель номер 1 читает: %s" % book)
    mutex.release()
    # cond.release()
    

def reader_2():
    # cond.acquire()
    # cond.wait()
    mutex.acquire()
    print("Читатель номер 2 читает: %s" % book)
    mutex.release()
    # cond.release()


def reader_3():
    # cond.acquire()
    # cond.wait()
    mutex.acquire()
    print("Читатель номер 3 читает: %s" % book) 
    mutex.release()
    # cond.release()   


if __name__ == '__main__':
    write1 = threading.Thread(target = writer_1)
    write1.start()    
    print("Первый писатель написал: %s" % book)
    time.sleep(4)
    write2 = threading.Thread(target = writer_2)
    write2.start()
    print("Второй писатель написал: %s" % book)
    time.sleep(3)
    reader1 = threading.Thread(target = reader_1)
    reader1.start()
    reader2 = threading.Thread(target = reader_2)
    reader2.start()
    reader3 = threading.Thread(target = reader_3)
    reader3.start()
    
 

