# Guilherme Narciso Lee boilerplate-daa-fcc
# github: narcisolee
import numpy as np

def calculate(matriceinarray):
    if len(matriceinarray)!=9:
        raise ValueError ("List must contain nine numbers.")
    empty_matrice = np.array(matriceinarray).reshape((3,3))
    output = {
      'mean': [
        np.mean(empty_matrice, axis=0).tolist(), 
        np.mean(empty_matrice, axis=1).tolist(), 
        np.mean(empty_matrice).tolist()],
      'variance': [
        np.var(empty_matrice, axis=0).tolist(), 
        np.var(empty_matrice, axis=1).tolist(), 
        np.var(empty_matrice).tolist()],
      'standard deviation': [
        np.std(empty_matrice, axis=0).tolist(), 
        np.std(empty_matrice, axis=1).tolist(), 
        np.std(empty_matrice).tolist()],
      'max': [
        np.max(empty_matrice, axis=0).tolist(), 
        np.max(empty_matrice, axis=1).tolist(), 
        np.max(empty_matrice).tolist()],
      'min': [
        np.min(empty_matrice, axis=0).tolist(), 
        np.min(empty_matrice, axis=1).tolist(), 
        np.min(empty_matrice).tolist()],
      'sum': [
          np.sum(empty_matrice, axis=0).tolist(), 
          np.sum(empty_matrice, axis=1).tolist(), 
          np.sum(empty_matrice).tolist()]
    }
    return output