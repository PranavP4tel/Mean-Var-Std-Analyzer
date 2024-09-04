import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list)
        a = a.reshape(3,3)
        
        calculations = {}
        calculations['mean'] = [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(np.reshape(a,-1))]
        calculations['variance'] = [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(np.reshape(a,-1))]
        calculations['standard deviation'] = [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(np.reshape(a,-1))]
        calculations['max'] = [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(np.reshape(a,-1))]
        calculations['min'] = [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(np.reshape(a,-1))]
        calculations['sum'] = [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(np.reshape(a,-1))]

        return calculations