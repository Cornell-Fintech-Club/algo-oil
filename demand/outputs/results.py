import pandas as pd 

pred_df = pd.read_csv("demand/outputs/pred.csv", header = None)
pred_df = pred_df.transpose()


with open("demand/outputs/loss.csv", 'r') as file:
    loss_values = [float(line.strip()) for line in file]


pred_df.columns = loss_values
print(pred_df)
pred_df.to_csv("demand/outputs/modelresults_by_loss.csv")

best_loss = min(loss_values)
best_loss_df = pred_df[best_loss]
best_loss_df.to_csv("demand/outputs/best_loss_data.csv")
