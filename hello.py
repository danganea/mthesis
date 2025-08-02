import h5py
import numpy as np

def _recursively_load(h5_obj):
    """
    Recursively loads HDF5 groups and datasets into a nested dictionary.
    """
    data_dict = {}
    for key, item in h5_obj.items():
        if isinstance(item, h5py.Dataset):
            # Load dataset value. [()] reads the entire dataset into memory.
            data_dict[key] = item[()]
        elif isinstance(item, h5py.Group):
            # If it's a group, recurse.
            data_dict[key] = _recursively_load(item)
    return data_dict

def load_hdf5_to_dict(file_path):
    """
    Loads an HDF5 file into a nested Python dictionary.

    Args:
        file_path (str): The path to the HDF5 file.

    Returns:
        dict: A dictionary containing the HDF5 file's data.
    """
    with h5py.File(file_path, 'r') as hf:
        return _recursively_load(hf)

def main():
    # file_path = 'resources/test/TrackedNuclei.mat'
    # data = load_hdf5_to_dict(file_path)

    base_path = 'resources/test/'
    file_path = base_path + 'matrices_E1-PEchopBB1only.mat'

    data = load_hdf5_to_dict(file_path)

    # f = h5py.File(file_path, 'r')
    #
    # print("Ok")
    #
    # f.close()

    print("DOne")


if __name__ == "__main__":
    main()
