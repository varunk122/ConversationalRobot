
def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    nfft = 200 # Length of each window segment
    fs = 8000 # Sampling frequencies
    noverlap = 120 # Overlap between windows
    nchannels = data.ndim
    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap = noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:,0], nfft, fs, noverlap = noverlap)
    return pxx

# Load a wav file
def get_wav_info(wav_file):
    rate , data = wavfile.read(wav_file)
    return rate, data

def modify_spectogram_shape(sample , noise_factor , add_noise , normalise , shape = (101,198) ):
    a = np.zeros(shape)
    a[: , :sample.shape[1]] = sample
    if(add_noise):
        sample = add_noise(sample , noise_factor)
    if(normalise):
        sample = normalise_spectogram(sample)
    return sample

def add_noise(sample , noise_factor):
    noise = np.random.randn(sample.shape)
    augmented_data = sample + noise_factor * noise
    augmented_data = augmented_data.astype(type(sample[0]))
    return augmented_data

def normalise_spectogram(sample):
    mean = np.mean(sample, axis=0)
    std = np.std(sample, axis=0)
    sample = (sample - mean) / std
    
    return sample
