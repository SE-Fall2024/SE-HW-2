'''Rand.py'''
import subprocess

def random_array(arr):
    '''Random Array Function'''
    for i,_in in enumerate(arr):  # Iterate over the index directly
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout.decode('utf-8').strip())  # Ensure conversion to int
    return arr
