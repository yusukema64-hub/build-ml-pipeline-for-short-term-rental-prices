name: data_check
conda_env: conda.yml

entry_points:
  main:
    parameters:
      csv:
        description: Fully-qualified name for the CSV file to check
        type: str
      ref:
        description: Fully-qualified name for the reference CSV file
        type: str
      kl_threshold:
        description: Threshold on the KL divergence to detect data drift
        type: float
        default: 0.2
      min_price:
        description: Minimum allowed price
        type: float
        default: 10
      max_price:
        description: Maximum allowed price
        type: float
        default: 350
    command: >-
      python run.py \
        --csv {csv} \
        --ref {ref} \
        --kl_threshold {kl_threshold} \
        --min_price {min_price} \
        --max_price {max_price}
