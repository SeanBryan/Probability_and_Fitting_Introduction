# ROC Curve

Using a receiver system (for example, a radar) to detect the presence or absence of a target (for example, a distant airplane) in the presence of noise (for example, thermal noise from an amplifier and background noise) inevitably involves a tradeoff between avoiding false positive results from noise yet assuring true positive detections when the target truly is present. After building and operating, or alternately after simulating, a real system and a real target, and after fully exploring this tradeoff, the Receiver Operating Characteristic (ROC) curve is a way to present the results of the study.

True and false positives are both very consequential in any detection system. A false positive is a situation where the target is not present, yet the detector triggers anyway. This is a bad situation since the user will believe that the target is present, and will therefore take an action in response to the target. This action may have undesired side effects, and ultimate is not needed since the target is not present. A low true positive rate is also problematic. A true positive is a situation where the target indeed is present, and the detector does trigger. A low true positive rate is a bad situation, since the user will believe the target is not present, and will therefore not take any action in response to the target. This may also have undesired side effects, since the target may cause harm.

Detection in the presence of noise occurs in a wide range of situations. One example is detecting the presence of adversaries. Another is the detection of weather threats to aircraft. Another is detecting the presence or absense of infectious disease with a test kit. The process of scientific discovery (astronomy, geology, physics, biology, ...) requires reliable detection or absence of signals that indicate new processes in a system under scientific study. Even many sports require rapid and reliable detection of the presence or absence of an opponent.

In this example, we consider a target that generates one unit of power on a receiver if the target is present, and generates zero power on the receiver if the target is not present. The receiver has a signal-to-noise level of 1 (i.e. 0 dB). As the user, we are left to select what threshold we prefer to use. If the value on the detector (which may include signal from the target if it is present, and will definitely include noise) is above our chosen threshold, our detector will trigger. Otherwise it does not trigger.

As we adjust the threshold, we explore this tradeoff between avoiding false positives yet assuring true detections. As the plot below shows, a low threshold yields a high percentage of true positive detections, but also unfortunately has a high false positive rate as well. Higher thresholds avoid false positives, but setting the threshold too high also does not yield true detections. A threshold of 0.5 is a compromise between the two.

![True and False Positive Rates](false_and_true_positive_rates_vs_threshold.png?raw=true)

Plotting the two curves from the previous plot against each other yields the ROC curve shown below. The blue curve below is the traces of the above plot plotted against each other. For comparison, the black line is the performance of a theoretical detector that is not viewing the scene at all, and therefore has no information. This detector would trigger at random, regardless of whether the target is present or not, which means its true positive and false positive rates are identical (yielding the diagonal black line when plotted against each other).

![ROC Curve](roc_curve.png?raw=true)

# Questions

1) Read through the code carefully. Does the operation of the detector make sense? Does the procedure for measuring the true positive and false positive rate make sense? Do you agree that setting the threshold at 0.5 is the "best" compromise in this case? Why or why not?

2) Are you happy with the performance of this system when the signal to noise radio = 1? Why or why not?

3) Re-run the code with a low signal to noise ratio, say 0.1 (i.e. -10 dB). Does the resulting ROC curve make sense? Is it close to the no-information black line?

4) Run the code yet again with a high signal to noise ratio, say 10 (i.e. 10 dB). Does the resulting ROC curve make sense? How does it differ from the nominal and low-SNR cases? What threshold would you choose as the "best" compromise in this case? Why did you choose that value?

5) Are you happy with the performance of this system when the signal to noise radio = 10? Why or why not?
