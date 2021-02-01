import numpy as np
import iso
from joblib import Parallel, delayed

hw = np.array([bin(i).count('1') for i in range(256)])

#1round分書き戻してHWをとる
def mk_labels_twov(key, round9, round10):
    
    out = round10 ^ key
    out = np.array([iso.new_base(iso.iso_map_inv, v) for v in out])
    out = iso.inv_s_box[out]
    out = np.array([iso.new_base(iso.iso_map, v) for v in out])
    out = out ^ round9

    return hw[out]


    

def calc_corr(w, hs):
    return np.array([np.corrcoef([w, hs[key]])[0][1] for key in range(256)])


def calc_corr_time(w, hs, i):
    return np.array([np.corrcoef([w[:i+1], hs[key,:i+1]])[0][1] for key in range(256)])

def main():
    
    base = ""
    wave_size = 
    data_size = 
    
    wave = np.fromfile(base + '/wavename', np.uint8)
    wave = wave.reshape(-1,wave_size)
    print(wave.shape)
    wave = wave[:data_size,:]
    
    with open('./csv/rounddata1') as f:
        data1 = f.readlines()
    data1 = np.array(data1,dtype=int)
    data1 = data[:data_size]
    
    with open('./csv/rounddata1') as f:
        data2 = f.readlines()
    data2 = np.array(data2,dtype=int)
    data2 = data2[:data_size]

    
    hs = np.array(Parallel(n_jobs=64, verbose=5)([delayed(mk_labels_twov)(key, data1, data2) for key in range(256)]))
    
    out = np.array(Parallel(n_jobs=64, verbose=5)([delayed(calc_corr)(w, hs) for w in wave.T]))
    np.save('./csv/corr_0123_mask', out)
    

    #時間方向にとる場合
    '''
    wave = wave.T
    wave = wave[849]
    out = np.array(Parallel(n_jobs=128, verbose=5)([delayed(calc_corr_time)(wave, hs, i) for i in range(400000)]))
    np.save('corr_0122_time', out)
    '''
    #for key in range(256):
    #    print('key:', key)
    #    for w in wave.T:
    #        print(np.corrcoef([w, mk_labels(key, round9)])[0][1])

if __name__ == '__main__':
    main()
