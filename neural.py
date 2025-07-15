def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

qmnist = unpickle("/kaggle/input/qmnist-the-extended-mnist-dataset-120k-images/MNIST-120k")

class TensorBatchDataset(Dataset):
    def __init__(self, images_tensor, labels_tensor):
        self.images = torch.tensor(images_tensor, dtype=torch.float32)
        self.images = self.images.unsqueeze(1)
        self.images /= 255
        self.labels = torch.tensor(labels_tensor, dtype=torch.long).squeeze()

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]
    
    from torch.utils.data import random_split

train_ratio = 0.8
train_size = int(len(dataset)*train_ratio)
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
len(train_dataset), len(test_dataset)

train_dataloader = DataLoader(train_dataset, batch_size=256, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=256, shuffle=False)