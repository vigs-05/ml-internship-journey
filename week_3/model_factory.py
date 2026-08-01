# FACTORY DESIGN
class RandomForest:
    
    def train(self):
        print("Training Random Forest....!")
        
class LogisticRegression:
    
    def train(self):
        print("Training Logistic Regression...!")

def create_model(model_type):
    if model_type == "rf" :
        return RandomForest()
    elif model_type == "lr" :
        return LogisticRegression()
    else:
        return None
    
model1 = create_model("rf")
model1.train()

model2 = create_model("lr")
model2.train()

model3 = create_model("svm")
