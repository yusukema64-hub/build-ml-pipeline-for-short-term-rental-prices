name: train_random_forest
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - pip=23.1
  - pip:
      - wandb==0.15.11
      - mlflow==2.8.1
      - pandas==2.0.3
      - numpy==1.25.2
      - scikit-learn==1.3.0
      - matplotlib==3.7.2
