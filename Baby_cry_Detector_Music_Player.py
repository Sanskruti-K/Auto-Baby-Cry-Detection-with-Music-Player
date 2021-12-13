import train_model
import predict_model
import Music_Player
import winsound
from shutil import move
from threading import Thread
import SMS
import time

songs = Music_Player.load_music()
cry_count = 1
silent_count = 1
song = []
flag = 0
songs2 = Music_Player.PriorityQueue()
cry_count = 0
silent_count = 0

# def chk():
#     global cry_count, silent_count
#     while True:
#
#         if cry_count==2 or silent_count==2:
#             # train_model.train_model()
#             print("Training " + " " + str(cry_count) + " " + str(silent_count))
#         else:
#             time.sleep(10)



def Baby_Cry_Detction():
    global cry_count, silent_count, flag, song, songs, songs2


    while True:
        print("Recording Audio ... ")
        label, file = predict_model.predict()

        if label == 1:
            # Play Music
            if songs.isEmpty():
                # songs = songs2
                songs = Music_Player.load_music()
            song = songs.delete()
            print("Baby is Crying")
            SMS.send_sms(" You're baby is crying..  \n Come Soon or Contact Someone at home.", "1010101010")  #valid phone no. should be there.
            print("Playing Song" + song[0])

            winsound.PlaySound("Songs/" + song[0], winsound.SND_FILENAME)

            flag = 1
            if cry_count == 6:
                predict_model.move_files(1)
                cry_count = 1
            move("New.wav", "Baby_Cry" + str(cry_count) + ".wav")

            cry_count += 1

        else:
            if silent_count == 6:
                predict_model.move_files(0)
                silent_count = 1
            move("New.wav", "Silent_" + str(silent_count) + ".wav")

            silent_count += 1
            if flag == 1:
                song[1] += 1
                print(song)
                songs.insert(song[0], song[1])
                flag = 0
            print("Baby is Silent")

status = True
if __name__ == '__main__':
    Thread(target=Baby_Cry_Detction).start()
    # if(status==True):
    #     Thread(target = chk).start()
    #     print("Threading Started")
    #     status=False






