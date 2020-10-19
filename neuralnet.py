class NeuralNet:
    def __init__(self):
        pass
    
    def activation_function(z):
        denominator = 1 + np.exp(-z)
        return 1/denominator

    def neurons1(x_val, neuron_num):
        N = len(x_val[0])
        weights = np.random.randn(N, neuron_num)
        bias = np.random.randn(x_val.shape[0], neuron_num)
        return activation_function(np.dot(x_val, weights) + bias)
    
    def create_layers(x, neuron, layer):
        layers = []
        for i in range(layer):
            lay = neurons1(x, neuron)
            layers.append(lay)
        return layers

    def final_output(x, neuron, layer):
        out1 = create_layers(x = xx, neuron = 3, layer = 100)[-1]
        n1 = out1.shape[-1]
        weights = np.random.randn(n1, 1)
        bias = np.random.randn(1, 1)
        if activation_function(np.dot(out1, weights) + bias)[0][0] > 0.5:
            return 1
        else:
            return -1
        
    def train_model(inp, out):
        Y = np.array([1,-1, 1,1,-1,-1,1,-1,1,1])
        count = 0
        pred1 = np.zeros(10)
        error = np.array(Y) == np.array(pred1)
        state = True
        while state:
            inputs = [np.array([[8,1]]), np.array([[2,7]]), np.array([[5,0]]), np.array([[12,6]]), np.array([[15,10]]), 
              np.array([[-5,-9]]), np.array([[2,-10]]), np.array([[-12,-1]]), np.array([[-7,6]]), np.array([[-5,4]])]
            for i in range(len(inputs)):
                f0 = final_output(x = inputs[i], neuron = 3, layer = 100)
                pred1[i] = f0
            error = np.array(Y) == np.array(pred1)
            count += 1
            if False not in error:
                state = False
        return pred1
    
    def score(self):
        pass
    
    def predict(self):
        pass