import torch
import numpy as np


def main():
    """Main function"""
    v = torch.tensor([1, 2, 3])
    print(v)
    print(v[1])
    print(v.dtype)

    f = torch.FloatTensor([1, 2, 3, 4])
    print(f)
    print(f.dtype)
    print(f.size())

    # Rearranges 2 rows 2 columns
    f.view(2, 2)
    print(f.view(2, 2))
    print(f.view(2, -1))

    # Convert numpy array to torch, and vice versa
    a = np.array([1, 2, 3, 4, 5])
    tensor_cnv = torch.from_numpy(a)
    print(tensor_cnv)
    print(tensor_cnv.type())
    print(tensor_cnv.numpy())


if __name__ == "__main__":
    main()
