# Session 1, Introduction to machine learning and deep learning

Day 1, 09:00–10:30. Slides: [`01_Intro_to_DeepLearning.pdf`](../../slides/01_Intro_to_DeepLearning.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`01_01_BasicML_intro.ipynb`](01_01_BasicML_intro.ipynb) | Linear regression, classification and k-means in scikit-learn; loss functions as the common thread. | < 1 min, CPU |
| [`01_02_GradientDescent_and_StochasticGradientDescent.ipynb`](01_02_GradientDescent_and_StochasticGradientDescent.ipynb) | GD and SGD written from scratch in NumPy on `SGD_data.txt`; mini-batches, momentum, learning rates. | < 1 min, CPU |
| [`01_03_Double_Descent.ipynb`](01_03_Double_Descent.ipynb) | Reproduces double descent on a controlled synthetic problem. | ~2 min, CPU |
| [`01_04_Gentle_DNN.ipynb`](01_04_Gentle_DNN.ipynb) | First deep network end to end in TensorFlow/Keras: regression and classification. | ~3 min, CPU |
| [`01_05_PyTorch_intro.ipynb`](01_05_PyTorch_intro.ipynb) | The same two tasks in PyTorch, so both frameworks are familiar. | ~3 min, CPU |
| [`01_06_Genz_Approximation_and_Loss_Functions.ipynb`](01_06_Genz_Approximation_and_Loss_Functions.ipynb) | Genz test functions: approximation quality, choice of loss, and the curse of dimensionality. **Warm-up exercise.** | ~3 min, CPU |

Suggested order: `01_01` → `01_02` → `01_04` → `01_03` → `01_05` → `01_06`.
