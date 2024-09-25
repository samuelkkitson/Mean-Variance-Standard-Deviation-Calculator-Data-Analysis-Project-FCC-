import numpy as np

np.set_printoptions(precision=15)

def calculate(list):
    if len(list) != 9 or not all(isinstance(item, (int, float)) for item in list):
        raise ValueError("List must contain nine numbers.")
    
    # Reshape the input list into a 3x3 NumPy array
    arr = np.array(list).reshape(3, 3)

    # Calculations
    calculations = {
        'mean': [
            np.mean(arr, axis=0).tolist(),  # Column means
            np.mean(arr, axis=1).tolist(),  # Row means
            np.mean(arr).tolist()             # Overall mean
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),  # Column variances
            np.var(arr, axis=1).tolist(),  # Row variances
            np.var(arr).tolist()             # Overall variance
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(),  # Column std dev
            np.std(arr, axis=1).tolist(),  # Row std dev
            np.std(arr).tolist()             # Overall std dev
        ],
        'max': [
            np.max(arr, axis=0).tolist(),  # Column max values
            np.max(arr, axis=1).tolist(),  # Row max values
            np.max(arr).tolist()             # Overall max
        ],
        'min': [
            np.min(arr, axis=0).tolist(),  # Column min values
            np.min(arr, axis=1).tolist(),  # Row min values
            np.min(arr).tolist()             # Overall min
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(),  # Column sums
            np.sum(arr, axis=1).tolist(),  # Row sums
            np.sum(arr).tolist()             # Overall sum
        ]
    }

    return calculations


