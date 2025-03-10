# Fatigue Life Predictor
This library offers SUS316 Fatigue Life Prediction via LSTM and Contextual Attention mechanism.

![image](https://github.com/user-attachments/assets/afe22725-0309-41ee-8ca3-7afa976ccda4)

Low-cycle fatigue (LCF) data involve complex temporal interactions in a strain cycle series, which hinders accurate fatigue life prediction. Current studies lack reliable methods for fatigue life prediction using only initial-cycle data while simultaneously capturing both temporal dependencies and localized features. This study introduces a novel deep-learning-based prediction model designed for LCF data. The proposed approach combines long short-term memory (LSTM) and convolutional neural network (CNN) architectures with an attention mechanism to effectively capture the temporal and localized characteristics of stress-strain data from acquisition through a series of cycle strain-controlled tests. Among the models tested, the LSTM-Contextual attention model demonstrated superior performance (R2=0.99), outperforming the baseline LSTM and CNN models with higher R² values and improved statistical metrics. The analysis of attention weights further revealed the model’s ability to focus on critical timesteps associated with fatigue damage, highlighting its effectiveness in learning key features from LCF data. This study underscores the potential of deep-learning-based methods for accurate fatigue life prediction in LCF applications. This study provides a foundation for future research to extend these approaches to diverse materials with varying fatigue conditions and advanced models capable of incorporating non-linear fatigue mechanisms.

![image](https://github.com/user-attachments/assets/2701336a-5c58-46d9-8862-c9b90b9ced7c)

Contact: saekomi5@korea.ac.kr
