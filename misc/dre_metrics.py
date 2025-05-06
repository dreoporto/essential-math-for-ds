
from sklearn.metrics import confusion_matrix


def print_confusion_matrix(y_true, y_pred):
    """
    print confusion matrix with clear labels for each number
    """
    tn, fp, fn, tp = confusion_matrix(y_true=y_true, y_pred=y_pred).ravel()
    print(f'TP:{tp}\tFN:{fn}')
    print(f'FP:{fp}\tTN:{tn}')
