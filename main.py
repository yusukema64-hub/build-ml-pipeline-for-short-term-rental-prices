name: basic_cleaning
conda_env: conda.yml

entry_points:
  main:
    parameters:
      input_artifact:
        description: Fully-qualified name for the input artifact
        type: str
      output_name:
        description: Name for the output artifact
        type: str
      output_type:
        description: Type for the output artifact
        type: str
      output_description:
        description: Description for the output artifact
        type: str
      min_price:
        description: Minimum nightly rental price to include in the dataset
        type: float
        default: 10
      max_price:
        description: Maximum nightly rental price to include in the dataset
        type: float
        default: 350
    command: >-
      python run.py \
        --input_artifact {input_artifact} \
        --output_name {output_name} \
        --output_type {output_type} \
        --output_description {output_description} \
        --min_price {min_price} \
        --max_price {max_price}
