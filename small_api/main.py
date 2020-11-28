from fastapi import FastAPI
from pySOT.surrogate import CubicKernel, LinearKernel, TPSKernel, LinearTail, ConstantTail
from pySOT.surrogate import RBFInterpolant
import pandas as pd
import numpy as np
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data")
async def root():
    class RBF_Surrogate(object):
        def __init__(self, df, metadata, split_factor=0.3,
                     rbf_def={'kernel': 'Cubic', 'tail': 'Linear', 'eta': 1e-06}):
            self.data = df
            self.meta = metadata
            self.surmod_count = len(self.meta['kpis'])
            self.dim = len(self.meta['designParam'])
            self.rbf = rbf_def
            self.split = split_factor
            self.surrogateModels = {}
            self.train_data = {}
            self.test_data = {}
            self._lb_X = np.zeros([1, self.dim])
            self._ub_X = np.zeros([1, self.dim])
            self.create_train_test_split()

        def _get_kernel(self, k=None):
            # Cubic
            if k is None:
                if (self.rbf['kernel'] == 'Cubic'):
                    return TPSKernel()
            # TPSKernel
            if self.rbf['kernel'] == 'TPS':
                return TPSKernel()
            # Linear
            if self.rbf['kernel'] == 'Linear':
                return LinearKernel()
            else:
                if k == 'Cubic':
                    return CubicKernel()
                # TPSKernel
                if k == 'TPS':
                    return TPSKernel()
                # Linear
                if k == 'Linear':
                    return LinearKernel()

            def _get_tail(self, t=None):
                if t is None:

                if (self.rbf['tail'] == 'Linear' or self.rbf['kernel'] is not 'Linear'):
                    return LinearTail(self.dim)
                if (self.rbf['tail'] == 'Constant'):
                    return ConstantTail(self.dim)
                else:
                    if t == 'Linear' or self.rbf['kernel'] is not 'Linear':
                        return LinearTail(self.dim)
                    if t == 'Constant':
                    return ConstantTail(self.dim)


            def create_train_test_split(self):
                for i in range(self.surmod_count):
                    X_train, X_test, y_train, y_test = train_test_split(self.data[self.meta['designParam']].values,
                                                            self.data[self.meta['kpis'][i]].values, random_state=0,
                                                            test_size=self.split)

                    self.train_data[self.meta['kpis'][i]] = {'X': X_train, 'Y': y_train}
                    self.test_data[self.meta['kpis'][i]] = {'X': X_test, 'Y': y_test

            def create_RBFsurrogate(self, surrogateKey, rbf=None):
                # Prepare Boundary Array
                for i in range(self.dim):
                    self._ub_X[0][i] = self.data[self.meta['designParam'][i]].max()
                    self._lb_X[0][i] = self.data[self.meta['designParam'][i]].min()
                if rbf is not None:
                    kernel = self._get_kernel(rbf['kernel'])
                    tail = self._get_tail(rbf['kernel'])
                    eta = rbf['eta']
                else:
                    kernel = self._get_kernel()
                    tail = self._get_tail()
                    eta = self.rbf['eta']
                try:
                    self.surrogateModels[surrogateKey] = RBFInterpolant(dim=self.dim, kernel=kernel, tail=tail, eta=eta,
                                                                        lb=self._lb_X, ub=self._ub_X)
                except KeyError:
                    raise KeyError('Could not find provided key in the meta data')

    def train_surrogate(self, surrogateKey):
        self.surrogateModels[surrogateKey].add_points(self.train_data[surrogateKey]['X'],
                                                      self.train_data[surrogateKey]['Y'])

    def reset_surrogate(self, surrogateKey):

        self.surrogateModels[surrogateKey].reset()

    def predict(self, surrogateKey, x):
        return self.surrogateModels[surrogateKey].predict(x)[0][0]

    def get_determination_coeff(self, surrogateKey, y_test=None, prnt=True):
        if y_test == None:
            y_r2 = self.surrogateModels[surrogateKey].predict(self.test_data[surrogateKey]['X'])
        else:
            y_r2 = y_test
            r = r2_score(self.test_data[surrogateKey]['Y'], y_r2)
        if prnt == True:
            print('R²: {}'.format(r))
        return r

    class Predictor():
        def __init__(self, xlsx_path):
            self.df = pd.read_excel(xlsx_path)
            self.des_names = ['ssl', 'spl', 'wal', 'bil']
            self.min_max = {name: [data_df.min()[name], data_df.max()[name]] for name in self.des_names}
            self.meta = {'designParam': self.des_names, 'kpis': ['hal']}
            self.model = RBF_Surrogate(self.df,
                                   self.meta,
                                   0.0001,
                                   rbf_def={'kernel': 'Cubic', 'tail': 'Linear', 'eta': 1e-06})
            self.designs = {}

        def train_model(self):
            self.model.create_RBFsurrogate('hal')
            self.model.train_surrogate('hal')

        def predict(self, static_input_array):
            for i, design in enumerate(static_input_array):
                X_ = np.full((1000, 4), static_input_array).T  # Only take all values of input
                des_min, des_max = self.min_max[self.des_names[i]]
                X_[i] = np.linspace(des_min, des_max, 1000)
                X_ = X_.T
                self.designs[str(self.des_names[i])] = {
                    'input': list(np.linspace(des_min, des_max, 1000)),
                    'output': [self.model.predict('hal', x) for x in X_]}

    if __name__ == '__main__':
        p = Predictor('data.xlsx')
        p.train_model()
        input_vals = np.array([8.4, 28., 5.3, 0.7])
