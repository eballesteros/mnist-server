from math import ceil
import matplotlib.pyplot as plt

DEF_TITLE = 'True: {label}. Predicted: {prediction}'

def show_one(im, label, prediction, title_format=None):
    '''
    '''
    title_format = title_format if title_format else DEF_TITLE

    plt.figure()
    plt.imshow(im)
    plt.axis('off')
    plt.title(title_format.format(label=label, prediction=prediction), fontdict={'size': 16})

def show_multi(ims, labels, predictions, title_format=None, plots_per_row=3):
    '''
    '''
    title_format = title_format if title_format else DEF_TITLE
    
    n_rows = ceil(len(ims)/plots_per_row)
    n_col = plots_per_row if len(ims) > plots_per_row else len(ims)

    fig, axs = plt.subplots(n_rows, n_col)
    for j, (im, label, prediction) in enumerate(zip(ims, labels, predictions)):
        row = j // n_col
        col = j % n_col
        ax = axs[row, col] if n_rows > 1 else axs[col]
        ax.imshow(im)
        ax.set_title(title_format.format(label=label, prediction=prediction))
        ax.axis('off')
        
    # remove remaining axis
    for i in range(j % n_col, n_col):
        row = j // n_col
        col = i % n_col
        ax = axs[row, col] if n_rows > 1 else axs[col]
        ax.axis('off')
    
    
    plt.show()