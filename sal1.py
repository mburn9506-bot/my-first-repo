# from datasets import load_dataset

# dataset = load_dataset('lukebarousse/data_jobs')
# print(type(dataset))
# print(type(dataset['train']))
from datasets import load_dataset
import pandas as pd

dataset = load_dataset("lukebarousse/data_jobs")
train_ds = dataset["train"]

# Check that this is a Dataset
print(type(train_ds))

# Convert to pandas
df = train_ds.to_pandas()

# Inspect
print(df.head())

