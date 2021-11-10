import time
import keyboard # pip install keyboard

class Drone:    
    
    def __init__(self):
        pass

    # Hareket fonksiyonları
    def go_forward(self):
        print("Drone ileri gidiyor")
        # time.sleep(0.25)

    def go_right(self):
        print("Drone sağa gidiyor")
        # time.sleep(0.25)
    
    def go_left(self):
        print("Drone sola gidiyor")
        # time.sleep(0.25)

    def lock(self):
        i = 0
        while i < 12:
            if i == 0:
                print("Kilitlenme Başladı")
                time.sleep(1)
                i += 1
            elif i == 11:
                print("Kilitlenme Bitti")
                i += 1
            else:
                print(i)
                time.sleep(1)
                i += 1

    # Kontrol fonksiyonu (kontroller numaralandırıldı)
    def control(self, command):
        if command == 1:
            self.go_forward()
        elif command == 2:
            self.go_right()
        elif command == 3:
            self.go_left()
        elif command == 4:
            self.lock()
        else:
            print("Geçersiz komut")

    # Başlatma fonksiyonu (numaralandırılan kontroller çağırıldı)
    def start(self):
        while True:
            if not(keyboard.is_pressed("right")) and not(keyboard.is_pressed("left")) and not(keyboard.is_pressed("k")):
                Drone().control(1)
            if keyboard.is_pressed("right"):
                Drone().control(2)
            if keyboard.is_pressed("left"):
                Drone().control(3)
            if keyboard.is_pressed("k"):
                Drone().control(4)
            if keyboard.is_pressed("esc"): # Uygulama kapatma kontrolü eklendi
                break

Drone().start()
