
from sklearn.metrics import (confusion_matrix, f1_score, precision_score,
                             recall_score)


def print_confusion_matrix(y_true, y_pred):
    """
    print confusion matrix with clear labels for each number
    """
    tn, fp, fn, tp = confusion_matrix(y_true=y_true, y_pred=y_pred).ravel()
    print(f'TP:{tp}\tFN:{fn}')
    print(f'FP:{fp}\tTN:{tn}')

def print_classification_metrics(y_true, y_pred):
    """
    print F1 score, Precision and Recall
    """
    score = f1_score(y_true=y_true, y_pred=y_pred)
    print(f'F1 score:\t{score:0.4}')

    p_score = precision_score(y_true=y_true, y_pred=y_pred)
    print(f'Precision:\t{p_score:0.4f}')

    r_score = recall_score(y_true=y_true, y_pred=y_pred)
    print(f'Recall:\t\t{r_score:0.4f}')
    