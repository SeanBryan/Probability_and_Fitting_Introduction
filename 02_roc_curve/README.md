# ROC Curve

Using a receiver system (for example. a radar) to detect the presence or absence of a target (for example, a distant airplane) in the presence of noise (for example, thermal noise from an amplifier and background noise) inevitably involves a tradeoff between avoiding false positive results from noise yet assuring true positive detections when the target truly is present. After building and operating, or alternately after simulating, a real system and a real target, and after fully exploring this tradeoff, the Receiver Operating Characteristic (ROC) curve is a way to present the results of the study.

In this example, we consider a target that generates one unit of power on a receiver if the target is present, and generates zero power on the receiver if the target is not present. The receiver has a signal-to-noise level of 1 (i.e. 0 dB). As the user, we are left to select what threshold we prefer to use. If the value on the detector (which may include signal from the target if it is present, and will definitely include noise) is above our chosen threshold, our detector will trigger. Otherwise it does not trigger.

As we adjust the threshold, we explore this tradeoff between avoiding false positives yet assuring true detections. As the plot below shows, a low threshold yields a high percentage of true positive detections, but also unfortunately has a high false positive rate as well. Higher thresholds avoid false positives, but setting the threshold too high also does not yield true detections. A threshold of 0.5 is a compromise between the two.

![True and False Positive Rates](false_and_true_positive_rates_vs_threshold.png?raw=true)

Plotting the two curves from the previous plot against each other yields the ROC curve shown below. The blue curve below is the traces of the above plot plotted against each other. For comparison, the black line is the performance of a theoretical detector that is not viewing the scene at all, and therefore has no information. This detector would trigger at random, regardless of whether the target is present or not, which means its true positive and false positive rates are identical (yielding the diagonal black line when plotted against each other).

![ROC Curve](roc_curve.png?raw=true)

# Questions

1) Read through the code carefully. Does the operation of the detector make sense? Does the procedure for measuring the true positive and false positive rate make sense? Do you agree that setting the threshold at 0.5 is the "best" compromise in this case? Why or why not?

2) Re-run the code with a low signal to noise ratio, say 0.1 (i.e. -10 dB). Does the resulting ROC curve make sense? Is it close to the no-information black line?

3) Run the code yet again with a high signal to noise ratio, say 10 (i.e. 10 dB). Does the resulting ROC curve make sense? How does it differ from the nominal and low-SNR cases?
