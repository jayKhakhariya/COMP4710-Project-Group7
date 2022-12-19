import time
from prefixspan import PrefixSpan
from transcript_parser.transcript_parser import Parser
import constants
import threading

transcripts = Parser(constants.transcript_en_loc).get_clean_sentences()

our_minsup = 2

# holds the output of prefix-span algorithm on each transcript
ps_frequent_words = []
transcript_id = 1236
stop_thread = False

def run_prefix_span(transcript, transcript_id):
    f = open("output.txt", "a")
    global stop_thread
    start_time = time.time()
    transcript_frequent_words = PrefixSpan(transcript).frequent(our_minsup)
    end_time = time.time()
    f.write(f'Prefix span on transcript {transcript_id} finished, and it took {end_time - start_time}\n')

    stop_thread = True
    # ps_frequent_words.append(transcript_frequent_words)
    f.close()


# print(f'{transcript_id}')
transcripts_not_working = []
if __name__ == '__main__':
    timeout = 2
    for i in range(transcript_id, len(transcripts)):
        # transcripts that have been found bad
        # 75 / 630 / 751 / 890/ 900 / 1062
        # if transcript_id != 75:
        print(f'calculating {transcript_id} and {i}')
        # start = time.time()

        my_thread = threading.Thread(target = run_prefix_span, args=(transcripts[i], transcript_id))
        my_thread.start()
        # process = multiprocessing.Process(target=run_prefix_span, args=(transcripts[i], transcript_id))
        # process.start()
        #
        # while time.time() - start < timeout:
        #     process.join()
        #     if process.is_alive():
        #         time.sleep(0.1)
        #     else:
        #         break
        #
        #
        # if process.is_alive():
        #     print(transcript_id)
        #     transcripts_not_working.append(transcript_id)
        #     process.terminate()

        start = 0
        while not stop_thread and start < timeout:
            time.sleep(0.1)
            start += 1   

        stop_thread = False

        transcript_id += 1
print(transcripts_not_working)