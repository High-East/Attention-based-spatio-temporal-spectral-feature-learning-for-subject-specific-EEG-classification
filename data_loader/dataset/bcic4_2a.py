import torch
from torch.utils.data import Dataset


class BCIC4_2A(Dataset):
    def __init__(self, options, phase):
        self.options = options
        self.load_data(phase)

    def load_data(self, phase):
        self.X = torch.load(f"./data_loader/dataset/bcic4-2a/{phase}/S{self.options.subject:02}_X.pt")
        self.y = torch.load(f"./data_loader/dataset/bcic4-2a/{phase}/S{self.options.subject:02}_y.pt")

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        sample = [self.X[idx], self.y[idx]]
        return sample
