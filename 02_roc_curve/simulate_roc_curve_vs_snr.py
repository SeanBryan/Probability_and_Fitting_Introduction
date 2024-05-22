import numpy as np
import matplotlib.pyplot as pl

def simulate_detection_experiment(threshold=0.1,SNR=10,target_present=True,verbose=False):
    '''
    define a function that simulates a detector viewing a scene where:
        - the signal = 1 if the target is truly present, 0 if not
        - the threshold is a user input
        - the SNR is a user input
        - whether the target is present is a user input
    '''
    
    # if the target truly is there
    if target_present:
        # generate a unit power signal
        sig = 1.0
    else:
        # otherwise there is no signal
        sig = 0.0

    # generate gaussian noise and add it to the signel
    # to yield the total value observed at the detector
    detector_value = sig + np.random.randn()/SNR

    # if the value observed at the detector is above the threshold
    if detector_value > threshold:
        # trigger the detector
        triggered = True
    else:
        # otherwise the detector is not triggered
        triggered = False
    
    # if the user wants to print out intermediate information
    if verbose:
        # print out intermediate information
        if target_present:
            print('target is present')
        else:
            print('target is not present')

        print('threshold = '+str(threshold))
        print('value observed at detector = '+str(detector_value))

        if triggered:
            print('detector triggered')
        else:
            print('detector did not trigger')
    
    # return the output
    return triggered

# choose the signal to noise ratio (linear units)
SNR = 1

# as a demonstration, perform a few experiments
# where the threshold is 0.5
# and the target is truly there
print('=========================================')
print('Performing demonstration experiments:')
for count in range(5):
    print('Experiment #'+str(count+1))
    simulate_detection_experiment(threshold=0.5,SNR=SNR,target_present=True,verbose=True)
    print(' ')
    print(' ')
print('=========================================')


# now consider a broad range of possible thresholds
thresholds = np.arange(-5,5,0.1)
# choose the number of times to repeat the experiment
Nexperiments = 10000

# measure the true positive rate
# and the false positive rate
true_positive_count = np.zeros_like(thresholds)
false_positive_count = np.zeros_like(thresholds)
# at each threshold
for i in range(len(thresholds)):
    # for each repeat of the detection experiment
    for j in range(Nexperiments):
        # simulate a detector viewing a scene where the target truly is there
        triggered = simulate_detection_experiment(threshold=thresholds[i],SNR=SNR,target_present=True)
        # if the detector triggered
        if triggered:
            # then we have a true positive
            # count this
            true_positive_count[i] += 1
        
        # simulate a detector viewing a scene where the target truly is not there
        triggered = simulate_detection_experiment(threshold=thresholds[i],SNR=SNR,target_present=False)
        # if the detector triggered
        if triggered:
            # then we have a false positive
            # count this
            false_positive_count[i] += 1
        
# plot the ROC curve
pl.ion()
pl.figure()
pl.plot(false_positive_count/Nexperiments, true_positive_count/Nexperiments, '*-',label='SNR = '+str(10*np.log10(SNR))+' dB')
pl.plot([0,1],[0,1],'k-',label='No-Information Line')
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.grid('on')
pl.legend()
pl.title('ROC Curve for Threshold Detector with Gaussian Noise')
# save the figure
# pl.savefig('roc_curve.png',dpi=600)

# plot the false positive and true positive rates vs threshold
pl.figure()
pl.plot(thresholds,false_positive_count/Nexperiments,'*-',label='False Positive Rate')
pl.plot(thresholds,true_positive_count/Nexperiments,'*-',label='True Positive Rate')
pl.xlabel('Threshold [arb]')
pl.ylabel('[rate]')
pl.title('False and True Positive Rates vs Threshold, SNR = '+str(10*np.log10(SNR))+' dB')
pl.grid('on')
pl.legend()
# save the figure
# pl.savefig('false_and_true_positive_rates_vs_threshold.png',dpi=600)