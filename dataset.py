import os
import csv
from torch.utils.data import Dataset

class LimerickDataset(Dataset):
  def __init__(self, path="limericks.txt"):
    super().__init__()

    self.limericks = []
    self.EOT = "<|endoftext|>"

    with open(path) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter="\n")
      limerick, skip_count = [], 0
      for row in csv_reader:
        if len(row) == 0:
          limerick.append(self.EOT)
          self.limericks.append("\n".join(limerick))
          limerick, skip_count = [], 0
        elif skip_count < 2:
          skip_count += 1
        else:
          limerick.append(" ".join(row))

  def __len__(self):
    return len(self.limericks)

  def __getitem__(self, item):
    return self.limericks[item]
